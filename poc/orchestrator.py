"""Wires the four agents together for one player turn.

Routing is decided by the single Rules Referee call (agents.judge_action) --
its JSON output says which of {NPC, Worldbuilder} this turn actually needs.
Both are independent of each other, so when both are needed they run
concurrently instead of sequentially.
"""
import concurrent.futures
import time

import agents
from world_state import WorldState

META_PREFIX = "/dm"  # explicit, deterministic escape hatch to talk to the DM
                      # out-of-character -- see CLAUDE.md "Verdict-skip
                      # experiment". Replaces trying to *guess* whether a
                      # question is a meta-request or in-character dialogue
                      # (a raw "?" check misfires on lines like "I enter the
                      # tavern and ask: Is there someone here?", which is
                      # dialogue, not a meta-request) -- the player just says
                      # which one they mean.


def _strip_meta_prefix(player_input: str) -> tuple[str, bool]:
    """Returns (cleaned_input, is_meta). Strips a leading "/dm" (any case,
    optional ":" after it) so the actual question reads naturally."""
    stripped = player_input.strip()
    if not stripped.lower().startswith(META_PREFIX):
        return player_input, False
    rest = stripped[len(META_PREFIX):].lstrip()
    if rest.startswith(":"):
        rest = rest[1:].lstrip()
    return rest, True


def run_turn(world: WorldState, player_input: str, stream_cb=None, verbose=False,
             on_timing=None, on_thinking=None, on_note=None):
    """on_timing(event:str, elapsed_s:float), called at key points in the turn
    (elapsed_s is measured from the start of this call):
      'verdict'     -- the Referee/Router's judgment + routing decision is
                        done (the "thought" behind the scene, never shown to
                        the player)
      'worldbuild'  -- the Worldbuilder call finished (only if it ran)
      'npc_reply'   -- the NPC call finished (only if it ran)
      'first_token' -- the first token of the DM's streamed narration has
                        been produced (when the visible answer starts)
      'done'        -- narration finished

    on_thinking() -- called once, only if this turn needs a tool (NPC and/or
    Worldbuilder) before the DM can narrate, so the caller can show a
    "Thinking..." placeholder. Never fires on fast-path turns (recall of
    already-known facts, ordinary actions) -- those go straight to narration.

    on_note(text) -- called once, BEFORE any narration, when the player's claim
    about the world was not accepted (see agents.correction_note). Plain
    out-of-character text explaining why; it is also stored in
    verdict["correction_note"] but is deliberately not part of the returned
    narration or the story history.
    """
    t0 = time.monotonic()

    def mark(event):
        if on_timing:
            on_timing(event, time.monotonic() - t0)

    player_input, is_meta = _strip_meta_prefix(player_input)

    # EXPERIMENTAL -- see CLAUDE.md "Verdict-skip experiment". Skips the
    # Referee/Router call entirely for turns the heuristic judges simple.
    # NPC-addressing is decided separately/deterministically either way, so
    # mundane dialogue still gets a real NPC reply even on the fast path.
    # A "/dm ..." turn always forces the full call -- it needs known_to_dm
    # (is this fact already established?), which only the real Referee/
    # Router can judge; the heuristic has no basis for that distinction.
    if not is_meta and agents.looks_simple(player_input, world):
        addresses_npc_fast = agents.addresses_active_npc(player_input, world)
        verdict = {
            "turn_type": "dialogue" if addresses_npc_fast else "action",
            "known_to_dm": True,
            "addresses_npc": addresses_npc_fast,
            "scene_shift": agents.looks_like_scene_shift(player_input, world),
            "player_assertion": "",
            "outcome": "success", "twist": "",
            "rationale": "heuristic: skipped verdict call, judged simple",
        }
        mark("verdict")
        if verbose:
            print(f"\n[router+referee] SKIPPED (heuristic: simple) {verdict}\n")
    else:
        verdict = agents.judge_action(world, player_input)
        # Second opinion: the big Referee call left 'it starts to rain'
        # unflagged in 3 of 9 eval runs (one field among many). For inputs
        # that look like statements about the world, ask one narrow
        # yes/no question instead. Costs one short call, only on suspect turns.
        if (not verdict.get("player_assertion") and not is_meta
                and agents.suspects_world_fact(player_input)):
            claim = agents.check_world_claim(player_input)
            if claim:
                verdict.update(
                    player_assertion=claim["assertion"], not_true=claim["not_true"],
                    twist="", scene_shift=False,
                    rationale=str(verdict.get("rationale", "")) + " | world-claim check: flagged",
                )
        mark("verdict")
        if verbose:
            tag = " (forced: /dm)" if is_meta else ""
            print(f"\n[router+referee]{tag} {verdict}\n")

    note = agents.correction_note(verdict)
    if note:
        verdict["correction_note"] = note
        if on_note:
            on_note(note)

    needs_worldbuild = (
        verdict.get("turn_type") == "info_request"
        and not verdict.get("known_to_dm", True)
    )
    active_npc = world.npcs.get(world.active_npc)
    needs_npc = bool(
        verdict.get("addresses_npc") and active_npc and active_npc.important
    )

    if (needs_worldbuild or needs_npc) and on_thinking:
        on_thinking()

    npc_line = None
    new_lore = None

    if needs_worldbuild or needs_npc:
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            futures = {}
            if needs_worldbuild:
                futures["worldbuild"] = pool.submit(agents.worldbuild, world, player_input)
            if needs_npc:
                futures["npc"] = pool.submit(agents.npc_reply, active_npc, world, player_input)

            if "worldbuild" in futures:
                new_lore = futures["worldbuild"].result()
                world.add_fact(new_lore)
                mark("worldbuild")
                if verbose:
                    print(f"[worldbuilder] {new_lore}\n")
            if "npc" in futures:
                npc_line = futures["npc"].result()
                mark("npc_reply")
                if verbose:
                    print(f"[{active_npc.name}] {npc_line}\n")

    first_token_marked = False

    def wrapped_stream_cb(piece):
        nonlocal first_token_marked
        if not first_token_marked:
            first_token_marked = True
            mark("first_token")
        if stream_cb:
            stream_cb(piece)

    # Force streaming whenever timing is requested, even with no visible
    # stream_cb, since first-token time can only be measured via the stream.
    dm_text = agents.narrate(
        world, player_input, verdict, npc_line=npc_line, new_lore=new_lore,
        stream_cb=wrapped_stream_cb if (stream_cb or on_timing) else None,
    )
    mark("done")
    # The flagged claim only protects THIS turn's narration. The raw player
    # text then sits in RECENT HISTORY, where later turns read it as plain
    # story ("three armed men storm in" -> a later recap narrated "three
    # defeated men slumped against the wall"; found by the eval harness). So
    # record it with an explicit note that it did not happen.
    history_text = player_input
    if verdict.get("player_assertion"):
        history_text += (
            f' [NOT TRUE: the player claimed "{verdict["player_assertion"]}", '
            "which did NOT happen in the story]"
        )
    world.add_turn(history_text, dm_text)
    return dm_text, verdict

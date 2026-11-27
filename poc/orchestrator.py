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

# On a refused claim, ask the player instead of narrating (see CLAUDE.md
# "Asking after a refused claim"). False = the older behaviour: narrate the
# rest of the line with the claim filtered out.
ASK_AFTER_REFUSED_CLAIM = True


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
             on_timing=None, on_thinking=None, on_note=None, on_npc_line=None):
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

    on_npc_line(name, text) -- called once, BEFORE the narration, when an NPC
    agent replied this turn. The DM is told the player has already read this
    line and continues from it, so callers must show it. Also stored in
    verdict["npc_name"] / verdict["npc_line"] and in the story history.

    After the narration, verdict["scene_update"] holds what the scene tracker
    changed (location, new NPCs) when it ran, else None.
    """
    t0 = time.monotonic()

    def mark(event):
        if on_timing:
            on_timing(event, time.monotonic() - t0)

    player_input, is_meta = _strip_meta_prefix(player_input)

    # Answer to a refusal_question() from the previous turn. A plain "yes"
    # plays the saved action; a plain "no" just asks again; anything else is
    # the player rephrasing, played as a normal new turn.
    pending, world.pending_action = world.pending_action, ""
    played_pending = ""
    if pending and not is_meta:
        reply = agents.confirm_reply(player_input)
        if reply == "yes":
            player_input = played_pending = pending
        elif reply == "no":
            note = "Alright. What does Kael do instead?"
            if on_note:
                on_note(note)
            return "", {"player_assertion": "", "correction_note": note,
                        "awaiting_player": True, "rationale": "declined the pending action"}

    # The party (Day 4): companions the player leaves behind stop following
    # BEFORE any move this turn. Heading to a known place by name to talk to
    # someone who is there moves Kael first, so that NPC's agent answers.
    # Both are undone if the turn ends in a refusal question.
    start_location = world.location
    were_here = {n.name for n in world.present_npcs()}
    left_behind =[] if is_meta else agents.party_leavers(player_input, world)
    for name in left_behind:
        world.leave_party(name)
    early_place = "" if is_meta else agents.arrival_place(player_input, world)
    if early_place:
        world.move_to(early_place)

    # Decide who the player is talking to BEFORE anything else reads
    # world.active_npc (fast-path check, Referee's TALKING WITH line, NPC
    # agent). Only NPCs present in the scene can be picked.
    addressee = agents.resolve_addressee(player_input, world)
    found_npc = None
    if addressee:
        world.active_npc = addressee
        if not world.npcs[addressee].location:
            # Called out on arrival and found here (see resolve_addressee).
            world.npcs[addressee].location = world.location
            found_npc = addressee

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
        # A "claim" that only exists inside the player's quoted speech is a
        # lie or bluff Kael SAID -- his to choose, not an invented world fact.
        if verdict.get("player_assertion") and agents.claim_is_only_speech(
                player_input, verdict["player_assertion"]):
            verdict["rationale"] = (str(verdict.get("rationale", "")) +
                                    f" | cleared: only in quoted speech ({verdict['player_assertion']!r})")
            verdict["player_assertion"], verdict["not_true"] = "", ""
        mark("verdict")
        if verbose:
            tag = " (forced: /dm)" if is_meta else ""
            print(f"\n[router+referee]{tag} {verdict}\n")

    # Refused claim: don't narrate at all. Say what did not happen and ask
    # whether the character still does the rest of the line. Nothing reaches
    # the story, the history or any NPC's thread on this turn.
    # Exception: a claim about how a present NPC reacts is refused in the
    # story instead (the NPC pushes back), see agents.refusal_stays_in_world.
    action = (agents.strip_claim(player_input, verdict["player_assertion"])
              if verdict.get("player_assertion") and not is_meta else "")
    if (ASK_AFTER_REFUSED_CLAIM and verdict.get("player_assertion") and not is_meta
            and not agents.refusal_stays_in_world(player_input, verdict, world, action)):
        world.pending_action = action
        if early_place:
            world.move_to(start_location)
        for name in left_behind:
            world.join_party(name, by="player")
        note = agents.refusal_question(verdict, action)
        verdict.update(correction_note=note, pending_action=action, awaiting_player=True)
        if on_note:
            on_note(note)
        return "", verdict

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
        and world.is_present(active_npc)
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
                # On a refused-claim turn the NPC, like the DM, only hears
                # the character's own attempt, not the invented part.
                npc_input = player_input
                if verdict.get("player_assertion"):
                    npc_input = (agents.strip_claim(player_input, verdict["player_assertion"])
                                 or "(Kael says and does nothing you can perceive.)")
                futures["npc"] = pool.submit(
                    agents.npc_reply, active_npc, world, agents.npc_view_of_turn(npc_input, verdict))

            if "worldbuild" in futures:
                new_lore = futures["worldbuild"].result()
                world.add_fact(new_lore)
                mark("worldbuild")
                if verbose:
                    print(f"[worldbuilder] {new_lore}\n")
            if "npc" in futures:
                # Shown to the player verbatim now, so drop the markdown
                # emphasis the model adds despite being told not to.
                npc_line = futures["npc"].result().replace("*", "").strip()
                if verdict.get("player_assertion"):
                    npc_line = agents.drop_claim_sentences(npc_line, verdict["player_assertion"]) or None
                mark("npc_reply")
                if npc_line:
                    verdict["npc_name"], verdict["npc_line"] = active_npc.name, npc_line
                    if on_npc_line:
                        on_npc_line(active_npc.name, npc_line)
                    elif verbose:
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
        npc_name=active_npc.name if npc_line else None,
    )
    mark("done")

    # Scene bookkeeping, after the narration so it never delays the first
    # token. Gated on cheap signals (movement words, scene_shift, a name the
    # world doesn't know yet) so most ordinary turns skip the call.
    verdict["scene_update"] = None
    if agents.scene_may_have_changed(player_input, verdict, npc_line, dm_text, world):
        update = agents.track_scene(
            world, player_input, dm_text, npc_line=npc_line,
            npc_name=active_npc.name if npc_line else None,
        )
        if update:
            verdict["scene_update"] = agents.apply_scene_update(
                world, update,
                exclude_from=player_input if verdict.get("player_assertion") else "",
                source_text=f"{npc_line or ''}\n{dm_text}",
                # Not on a refused-claim turn (Day 4 play session: "I follow
                # her out" with "Silas leads you out" refused; the narration
                # kept everyone inside, but the tracker moved Kael and Silas).
                allow_move=(agents.player_may_move(player_input, verdict)
                            and not verdict.get("player_assertion")),
            )
            if verbose:
                print(f"\n[scene tracker] {update} -> {verdict['scene_update']}")
        mark("tracked")
    if world.location != start_location:
        # Companions already followed (world.move_to moves the party). NPCs
        # the player says they go with now join it.
        came = [n.name for n in world.party() if n.name not in left_behind]
        came += [n for n in agents.bring_companions(world, player_input, start_location, were_here)
                 if n not in came]
        found = world.npcs.get(found_npc)
        if found and found.location == start_location:
            found.location = world.location  # found at the place Kael arrived at
            came.append(found_npc)
        verdict["scene_update"] = verdict["scene_update"] or {"moved_to": world.location, "added": []}
        verdict["scene_update"]["came_along"] = came
    verdict["party"] = [n.name for n in world.party()]
    if left_behind:
        verdict["left_behind"] = left_behind
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
    # Keep the NPC's actual words in the story history too: later turns (and
    # the DM's recaps) need to know what was said, not only the reactions.
    history_dm = f"{active_npc.name}: {npc_line}\n{dm_text}" if npc_line else dm_text
    # Who witnessed this turn: everyone with Kael at the start (they saw him
    # leave) or at the end (they saw him arrive). NPC agents only hear the
    # events they witnessed.
    witnesses = were_here | {n.name for n in world.present_npcs()}
    world.add_turn(history_text, history_dm, witnesses=sorted(witnesses))
    if played_pending:
        verdict["played_pending"] = played_pending
    return dm_text, verdict

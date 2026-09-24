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


def run_turn(world: WorldState, player_input: str, stream_cb=None, verbose=False,
             on_timing=None, on_thinking=None):
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
    """
    t0 = time.monotonic()

    def mark(event):
        if on_timing:
            on_timing(event, time.monotonic() - t0)

    verdict = agents.judge_action(world, player_input)
    mark("verdict")
    if verbose:
        print(f"\n[router+referee] {verdict}\n")

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
    world.add_turn(player_input, dm_text)
    return dm_text, verdict

"""CLI entry point for the multi-agent RPG PoC."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

import agents
import ollama_client
import orchestrator
from world_state import WorldState, NPC

STATE_PATH = Path(__file__).parent / "session_state.json"


def seed_world() -> WorldState:
    world = WorldState(
        scene_summary=(
            "Kael, a former soldier turned sellsword, has just arrived in "
            "the border town of Ashwick as night falls, looking for work."
        ),
    )
    world.move_to("Ashwick -- the Red Griffin tavern")
    world.add_npc(NPC(
        name="Grimbold Ironfist",
        persona=(
            "Stout dwarf innkeeper of the Red Griffin. Gruff but fair, "
            "knows every rumor in town, protective of his regulars, not "
            "impressed by flashy strangers or easy coin."
        ),
        important=True,
        location=world.location,
        aliases=["the dwarf", "the innkeeper", "the barkeep", "the bartender"],
    ))
    world.active_npc = "Grimbold Ironfist"
    world.add_fact("Kael carries a sword and modest travel gear; no known magic or renown.")
    return world


def print_help():
    print(
        "\nCommands:\n"
        "  /state              show current world state\n"
        "  /graph              show the world graph (node ids, values, edges)\n"
        "  /npc <name>         set which important NPC is active in the scene\n"
        "  /worldbuild <topic> invent new lore and add it to established facts\n"
        "  /verbose            toggle showing referee verdicts and raw NPC lines\n"
        "  /reset              discard saved session and start over\n"
        "  /quit\n"
        "\nTip: start a line with /dm to ask the DM something out-of-character\n"
        "(e.g. '/dm what was the innkeeper's name again?') instead of playing\n"
        "it in-character -- this always gets a full, careful answer.\n"
    )


def main():
    verbose = "-v" in sys.argv

    print("[warming up model...]")
    ollama_client.warmup()

    if STATE_PATH.exists():
        world = WorldState.load(STATE_PATH)
        print(f"[loaded existing session: {world.location}]")
    else:
        world = seed_world()
        print("[new session started]")

    print_help()

    while True:
        try:
            player_input = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not player_input:
            continue
        if player_input == "/quit":
            break
        if player_input == "/state":
            print("\n" + world.context_brief())
            continue
        if player_input == "/graph":
            print("\n" + world.graph.describe())
            continue
        if player_input == "/verbose":
            verbose = not verbose
            print(f"[verbose={verbose}]")
            continue
        if player_input == "/reset":
            world = seed_world()
            if STATE_PATH.exists():
                STATE_PATH.unlink()
            print("[session reset]")
            continue
        if player_input.startswith("/npc "):
            name = player_input[len("/npc "):].strip()
            if name in world.npcs:
                world.active_npc = name
                print(f"[active NPC: {name}]")
            else:
                print(f"[no known NPC named {name!r}; known: {list(world.npcs)}]")
            continue
        if player_input.startswith("/worldbuild "):
            topic = player_input[len("/worldbuild "):]
            print("\n[worldbuilder is thinking...]")
            lore = agents.worldbuild(world, topic)
            print(f"\n{lore}\n")
            world.add_fact(lore)
            world.save(STATE_PATH)
            continue

        print()

        def on_token(piece):
            print(piece, end="", flush=True)

        def on_thinking():
            print("[thinking...]\n")

        def on_note(note):
            print(f"[DM, out of character] {note}\n")

        def on_npc_line(name, line):
            print(f"{name}: {line}\n")

        dm_text, verdict = orchestrator.run_turn(
            world, player_input, stream_cb=on_token, verbose=verbose,
            on_thinking=on_thinking, on_note=on_note, on_npc_line=on_npc_line,
        )
        print()
        world.save(STATE_PATH)


if __name__ == "__main__":
    main()

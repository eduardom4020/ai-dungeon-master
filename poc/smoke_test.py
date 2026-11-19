"""Non-interactive smoke test of the multi-agent orchestration."""
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")

import ollama_client
import orchestrator
from play import seed_world

print("[warming up model...]")
t0 = time.monotonic()
ollama_client.warmup()
print(f"[warmup took {time.monotonic() - t0:.2f}s]")

TURNS = [
    "I sit at the bar and ask Grimbold about work.",
    # Ordinary action, NPC not addressed -- should skip both Referee-flagged
    # complications and the NPC call (case 5: fast path, no tools).
    "I glance around the tavern for an empty table to sit at.",
    "I flash a handful of copper coins and tell Grimbold this is more than "
    "enough to make him trust me completely and tell me everything, no "
    "matter how dangerous.",
    "Three armed men storm in. I draw my sword and in one perfect strike "
    "intimidate all three into surrendering instantly, no fight needed.",
    # Explicit meta/out-of-character question -- forces the full Referee/
    # Router call regardless of the heuristic, since only that call can
    # judge known_to_dm (already-established facts, no Worldbuilder needed
    # here since this recap is already in world context).
    "/dm quick recap -- what's the name of this town again, and who runs "
    "the inn I'm in?",
]

world = seed_world()
turn_times = []
turn_marks = []  # {'verdict': s, 'first_token': s, 'done': s} per turn

for i, turn in enumerate(TURNS, 1):
    print(f"\n{'='*20} TURN {i} {'='*20}")
    print(f"PLAYER: {turn}\n")

    def on_token(piece):
        print(piece, end="", flush=True)

    marks = {}

    def on_timing(event, elapsed):
        marks[event] = elapsed
        print(f"\n[{event} at {elapsed:.2f}s]")

    turn_start = time.monotonic()
    def on_note(note):
        print(f"[DM, out of character] {note}\n")

    dm_text, verdict = orchestrator.run_turn(
        world, turn, stream_cb=on_token, verbose=True, on_timing=on_timing,
        on_note=on_note,
    )
    turn_elapsed = time.monotonic() - turn_start
    turn_times.append(turn_elapsed)
    turn_marks.append(marks)
    print(f"\n\n[turn {i} took {turn_elapsed:.2f}s]")

print("\n\n=== TIMING SUMMARY ===")
for i, (t, marks) in enumerate(zip(turn_times, turn_marks), 1):
    print(
        f"turn {i}: {t:.2f}s total | "
        f"thought (referee verdict) at {marks.get('verdict', float('nan')):.2f}s | "
        f"first streamed token at {marks.get('first_token', float('nan')):.2f}s"
    )
print(f"total: {sum(turn_times):.2f}s | avg: {sum(turn_times) / len(turn_times):.2f}s/turn")

print("\n\n=== FINAL WORLD STATE ===")
print(world.context_brief())

print("\n\n=== GRIMBOLD'S OWN THREAD ===")
for m in world.npcs["Grimbold Ironfist"].thread:
    print(f"{m['role']}: {m['content']}")

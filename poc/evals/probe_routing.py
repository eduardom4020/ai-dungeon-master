"""Deterministic regression probe for the code-side routing rules -- no Ollama
needed (only the CPU embedding model for the fast-path cases), runs in seconds.

    cd poc
    python evals/probe_routing.py

Every case is a real line from a play session or eval run (Nov 2026) that the
rules once got wrong, plus the controls that must stay right. Run it after
touching resolve_addressee, addresses_active_npc, bring_companions,
claim_is_only_speech, NarrationFilter, apply_scene_update or looks_simple.
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import agents  # noqa: E402
from world_state import WorldState, NPC  # noqa: E402

TAVERN = "Ashwick -- the Red Griffin tavern"
failures = 0


def check(label, got, want):
    global failures
    ok = got == want
    failures += not ok
    print(f"{'ok ' if ok else 'BAD'} {label[:78]:<78} -> {got!r}" + ("" if ok else f" (want {want!r})"))


def tavern_world():
    w = WorldState(scene_summary="Kael has just arrived in Ashwick looking for work.")
    w.move_to(TAVERN)
    w.add_npc(NPC(name="Grimbold Ironfist", persona="Stout dwarf innkeeper.", important=True,
                  location=TAVERN, aliases=["the dwarf", "the innkeeper"]))
    w.add_npc(NPC(name="Borgar Ironvein", persona="Hulking ex-mercenary.", important=True,
                  location=TAVERN, aliases=["the big man"]))
    w.add_npc(NPC(name="Vexin", persona="Black-coated man from the Black Dog.", important=True,
                  location=TAVERN))
    w.add_npc(NPC(name="Manfred the Smith", persona="Town smith.", important=True, location=""))
    w.active_npc = "Grimbold Ironfist"
    return w


print("== resolve_addressee (who the player is talking to)")
w = tavern_world()
for line, want in [
    ('I take a sip of the ale and follow his glance to the big man in the patchwork coat. '
     'Quietly, I ask Grimbold: "Who is he?"', "Grimbold Ironfist"),
    ("I nod my thanks to Grimbold, pick up my ale and walk over to Borgar's table.", "Borgar Ironvein"),
    ("I ask Grimbold about Borgar.", "Grimbold Ironfist"),
    ("I wipe the spilled ale off my sleeve and look the dwarf in the eye.", "Grimbold Ironfist"),
    ('I lean on the bar and say to the dwarf: "An ale, please."', "Grimbold Ironfist"),
    ("Enough games. I reach across the table, grab Borgar by the collar and pull him close.", "Borgar Ironvein"),
    ('I keep my hands on the bar where he can see them. "I can keep my mouth shut, Vexin."', "Vexin"),
    ('I don\'t answer Vexin yet. I lean over the bar and ask Grimbold quietly: "What do you know?"',
     "Grimbold Ironfist"),
    ('"The mines?" I lower my voice too. "What does your friend Borgar have to do with it?"', None),
    ('I follow the smell of smoke to the forge and step inside. "Manfred? Grimbold sent me."',
     "Manfred the Smith"),
    ('"Manfred is a fool," I say to the dwarf.', "Grimbold Ironfist"),
]:
    check(line, agents.resolve_addressee(line, w), want)

w2 = tavern_world()
w2.move_to("Ashwick -- the smithy")
w2.add_npc(NPC(name="Borla", persona="Blacksmith.", important=True, location="Ashwick -- the smithy"))
w2.active_npc = "Vexin"  # stayed in the tavern
check("(only Borla here, active NPC elsewhere) \"Grimbold sent me. What does Harlow need?\"",
      agents.resolve_addressee('I wait for the hammer to stop. "Grimbold sent me. What does Harlow need?"', w2),
      "Borla")

print("\n== addresses_active_npc (fast path: should the active NPC's agent answer?)")
w = tavern_world()
for line, want in [
    ('"Kael." I turn on my stool to face the man in the black coat. "Something you want to say?"', False),
    ('I say to the stranger by the fire: "Mind if I sit?"', False),
    ('I lean on the bar and say to the dwarf: "An ale, please."', True),
    ('"The mines?" I lower my voice too. "What\'s going on at the mines?"', True),
    ('"I\'m back," I tell Grimbold. "Anything new since I left?"', True),
    ("I glance around the tavern for an empty table to sit at.", False),
]:
    check(line, agents.addresses_active_npc(line, w), want)

print("\n== bring_companions (who comes along when Kael moves)")
for line, want in [
    ('"Lead the way, Vexin." I follow him out of the Red Griffin toward the eastern woods.', ["Vexin"]),
    ("I leave the Red Griffin and step out into the main street of Ashwick.", []),
    ("Vexin and I head out toward the woods.", ["Vexin"]),
    ("I head out with the dwarf to see the mill.", ["Grimbold Ironfist"]),
]:
    w = tavern_world()
    w.active_npc = "Vexin"
    w.move_to("Ashwick -- the main street")
    check(line, agents.bring_companions(w, line, TAVERN), want)

print("\n== claim_is_only_speech (bluffs are speech, not invented facts)")
for line, claim, want in [
    ('I bluff. I lean in and say: "Careful, friend. I rode in with the captain of the border patrol."',
     "your character rode in with the captain of the border patrol", True),
    ('I tell Grimbold, "The magistrate owes me a favour, so you can trust me."',
     "the magistrate owes Kael a favour", True),
    ("Three armed men storm in. I draw my sword.", "three armed men storm in", False),
    ('"Look out!" I shout, and the guards burst into the room.', "the guards burst into the room", False),
    ("I slide a coin across her table. She can't resist the money, so she tells me the safe way in.",
     "Veyra cannot resist the money and tells me the safe way", False),
]:
    check(line, agents.claim_is_only_speech(line, claim), want)

print("\n== NarrationFilter (markdown, asides, NPC speech, budget, broken tail)")
f = agents.NarrationFilter(budget_words=110)
f.feed('The forge **glows**. Borla spits. *(NEXT: Borla shifts to a new demand--or does he? Your move.)* ')
check("markdown stripped, aside dropped", f.finish(), "The forge glows. Borla spits.")
f = agents.NarrationFilter(budget_words=110, drop_speech=True)
f.feed('Grimbold nods slowly. "Fine, then," the dwarf mutters, "ask Tallow." The fire pops. ')
check("speech dropped on an NPC turn", f.finish(), "Grimbold nods slowly. The fire pops.")
f = agents.NarrationFilter(budget_words=20)
for word in "The forge glows. Borla spits on the floor and wipes his hands. The hammer falls again and again on the iron.".split():
    if f.feed(word + " "):
        break
check("stops on a whole sentence before the budget", f.finish(), "The forge glows. Borla spits on the floor and wipes his hands.")
f = agents.NarrationFilter()
f.feed("The door groans shut behind you. The cobbled alleyway stretches black and")
check("broken trailing fragment dropped", f.finish(), "The door groans shut behind you.")
f = agents.NarrationFilter(budget_words=20)
f.feed('He says, "Go to the mill. Ask for Harlow. Tell her I sent you." Then he turns away. ')
check("multi-sentence quote not split", f.finish(), 'He says, "Go to the mill. Ask for Harlow. Tell her I sent you." Then he turns away.')

print("\n== apply_scene_update guards (the tracker model is unreliable)")
w = tavern_world()
src = "The air between you. The hooded figure stays. Two overwatch guards snort. Veyra grins."
ch = agents.apply_scene_update(w, {"moved": False, "characters": [
    {"name": "The hooded figure", "present": True, "new": True},
    {"name": "overwatch guards", "present": True, "new": True},
    {"name": "Veyra", "present": True, "new": True}]}, source_text=src)
check("unnamed people are not registered, Veyra is", ch["added"], ["Veyra"])
w = tavern_world()
ch = agents.apply_scene_update(w, {"moved": True, "location": "Ashwick -- the stables"}, allow_move=False)
check("no move without a movement word from the player", (ch["moved_to"], w.location), (None, TAVERN))
w = tavern_world()
w.move_to("Ashwick -- the Black Anvil mine")
ch = agents.apply_scene_update(w, {"moved": True, "location": "Ashwick -- the Black Anvil mine -- pit's mouth"})
check("a spot nested in the current place is not a move", ch["moved_to"], None)
w = tavern_world()
w.move_to("Ashwick -- the road west")
agents.apply_scene_update(w, {"moved": False, "characters": [{"name": "Borgar Ironvein", "present": True}]},
                          source_text="Borgar's torchlight flickers.")
check("an NPC known to be elsewhere is not pulled here", w.npcs["Borgar Ironvein"].location, TAVERN)

print("\n== looks_simple (fast path) on the two real misses + controls")
w = tavern_world()
for line, want in [
    ("Enough games. I reach across the table, grab Borgar by the collar and pull him close. "
     "He cracks and tells me everything he knows about Tallow.", False),
    ("On the way, I spot my old army friend, Sergeant Hale, leaning against a lamppost. He waves at me.", False),
    ("I glance around the tavern for an empty table to sit at.", True),
    ("I take a sip of my ale and listen to the room.", True),
]:
    check(line, agents.looks_simple(line, w), want)

print(f"\n{'ALL OK' if not failures else f'{failures} FAILURE(S)'}")
sys.exit(1 if failures else 0)

"""Deterministic probe for the world graph behind WorldState (no Ollama, <1s).

    python evals/probe_world_state.py

Checks the schema is enforced, a character is in one place at a time, the
old WorldState API reads/writes the graph, saves round-trip, and saves from
before the graph are migrated.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.stdout.reconfigure(encoding="utf-8")

from world_graph import PLAYER_ID, WorldGraph  # noqa: E402
from world_state import NPC, WorldState  # noqa: E402

failures = 0


def check(label, got, want):
    global failures
    ok = got == want
    failures += not ok
    print(f"{'ok ' if ok else 'BAD'} {label}" + ("" if ok else f"\n      got  {got!r}\n      want {want!r}"))


def raises(label, fn):
    try:
        fn()
    except ValueError:
        check(label, True, True)
    else:
        check(label, "no error", "ValueError")


# ---- the graph wrapper ---------------------------------------------------
g = WorldGraph()
k = g.add_node("Character", node_id=PLAYER_ID, name="Kael")
c = g.add_node("Character", name="Vexin Ashgrove of the Lower Docks", short="Vexin",
               aliases=["the fence"])
p1 = g.add_node("Place", name="The Red Griffin")
p2 = g.add_node("Place", name="The forge")
f = g.add_node("Fact", text="The mine collapsed three winters ago.")
check("ids are type prefix + counter", (c, p1, p2, f), ("C1", "P1", "P2", "F1"))
check("find by name, short or alias, any case",
      [g.find("Character", x) for x in ("vexin", "THE FENCE", "Vexin Ashgrove of the Lower Docks", "nobody")],
      ["C1", "C1", "C1", ""])
raises("unknown relation refused", lambda: g.add_edge(c, "LIKES", k))
raises("wrong endpoint types refused", lambda: g.add_edge(p1, "AT", c))
raises("unknown node type refused", lambda: g.add_node("Weather", name="rain"))
g.add_edge(c, "AT", p1, by="tracker", turn=1)
g.add_edge(c, "AT", p2, by="tracker", turn=2)
check("AT is single: moving replaces the old edge", g.targets(c, "AT"), [p2])
check("provenance kept on the edge", g.g.edges[c, p2, "AT"], {"by": "tracker", "turn": 2})
g.add_edge(c, "TRAVELS_WITH", k)
g.add_edge(c, "KNOWS", k)
check("two relations between the same pair", sorted(kk for _, _, kk in g.g.edges(c, keys=True)),
      ["AT", "KNOWS", "TRAVELS_WITH"])
g.node(c)["name"] = "Vexin the Fence"
check("renaming a node keeps its edges", g.sources(k, "TRAVELS_WITH"), [c])
g2 = WorldGraph.from_dict(json.loads(json.dumps(g.to_dict())))
check("graph JSON round-trip: same edges", sorted(g2.g.edges(keys=True)), sorted(g.g.edges(keys=True)))
check("graph JSON round-trip: counters", g2.add_node("Character", name="New"), "C2")

# ---- WorldState API on top of it -----------------------------------------
w = WorldState(scene_summary="Night in Ashwick.")
w.move_to("Ashwick -- the tavern")
w.add_npc(NPC(name="Grimbold Ironfist", persona="Dwarf innkeeper.", important=True,
              location=w.location, aliases=["the dwarf"]))
w.add_npc(NPC(name="Manfred", persona="Smith.", important=True, location=""))
w.add_fact("Kael carries a sword.")
w.add_fact("Kael carries a sword.")
check("location reads Kael's AT edge", w.location, "Ashwick -- the tavern")
check("NPC values live on its node", w.graph.node(w.npcs["Grimbold Ironfist"].id)["persona"], "Dwarf innkeeper.")
check("present_npcs", [n.name for n in w.present_npcs()], ["Grimbold Ironfist"])
check("unknown whereabouts = no AT edge", (w.npcs["Manfred"].location, w.graph.targets(w.npcs["Manfred"].id, "AT")), ("", []))
check("facts are Fact nodes, no duplicates", w.flags, ["Kael carries a sword."])
w.move_to("Ashwick -- the street")
w.npcs["Manfred"].location = w.location
check("assigning npc.location moves it", [n.name for n in w.present_npcs()], ["Manfred"])
w.move_to("Ashwick -- the tavern")
check("revisiting does not duplicate places", w.places, ["Ashwick -- the tavern", "Ashwick -- the street"])
check("known_places", w.known_places(), ["Ashwick -- the tavern", "Ashwick -- the street"])
w.npcs["Grimbold Ironfist"].aliases.append("the innkeeper")
check("in-place alias edit is stored", w.graph.find("Character", "the innkeeper"), w.npcs["Grimbold Ironfist"].id)
w.npcs["Grimbold Ironfist"].thread.append({"role": "user", "content": "hi"})
w.recent_history.append(("I sit.", "You sit."))
w.pending_action = "I go inside."
w.active_npc = "Grimbold Ironfist"

w2 = WorldState.from_dict(json.loads(json.dumps(w.to_dict())))
check("round-trip: context brief identical", w2.context_brief(), w.context_brief())
check("round-trip: thread, pending, history",
      (w2.npcs["Grimbold Ironfist"].thread, w2.pending_action, w2.recent_history),
      (w.npcs["Grimbold Ironfist"].thread, w.pending_action, w.recent_history))
check("round-trip: places in order", w2.places, w.places)
w2.add_npc(NPC(name="Borla", persona="Blacksmith."))
check("round-trip: id counter continues", w2.npcs["Borla"].id, "C3")

# ---- the party (TRAVELS_WITH) --------------------------------------------
p = WorldState()
p.move_to("tavern")
for name in ("Silas", "Grimbold"):
    p.add_npc(NPC(name=name, persona=".", important=True, location="tavern"))
p.join_party("Silas", by="player")
p.move_to("street")
check("companion follows a move", p.npcs["Silas"].location, "street")
check("non-companion stays", p.npcs["Grimbold"].location, "tavern")
p.move_to("forge")
check("...and keeps following on the next move", p.npcs["Silas"].location, "forge")
check("party in the brief", "TRAVELLING WITH KAEL: Silas" in p.context_brief(), True)
q = WorldState.from_dict(json.loads(json.dumps(p.to_dict())))
check("party survives save/load", [n.name for n in q.party()], ["Silas"])
q.leave_party("Silas")
q.move_to("gate")
check("left behind: stays at the forge", (q.npcs["Silas"].location, q.party()), ("forge", []))
check("no party line when empty", "TRAVELLING WITH" in q.context_brief(), False)

# ---- events: NPCs know only what they witnessed ------------------------------
e = WorldState()
e.move_to("smithy")
e.add_npc(NPC(name="Tallow", persona=".", important=True, location="smithy"))
e.add_npc(NPC(name="Grimbold", persona=".", important=True, location="tavern"))
e.add_turn('"The password is red heron."', 'Tallow nods.')   # default witnesses: who is here
e.move_to("tavern")
e.add_turn("I walk to the tavern.", "Warm in here.", witnesses=["Grimbold", "Tallow"])
check("witness knows the secret", [p for p, _ in e.events_known_by(e.npcs["Tallow"])],
      ['"The password is red heron."', "I walk to the tavern."])
check("non-witness does not", [p for p, _ in e.events_known_by(e.npcs["Grimbold"])], ["I walk to the tavern."])
check("Kael knows every event", len(e.graph.targets(PLAYER_ID, "KNOWS")), 2)
check("event records where it happened", e.place_name(e.graph.target("E1", "AT_PLACE")), "smithy")
e2 = WorldState.from_dict(json.loads(json.dumps(e.to_dict())))
check("events survive save/load", [p for p, _ in e2.events_known_by(e2.npcs["Grimbold"])], ["I walk to the tavern."])
import agents  # noqa: E402
_prompts = []
_real_chat = agents.chat
agents.chat = lambda messages, options=None: (_prompts.append(messages[0]["content"]), ("ok", None))[1]
agents.npc_reply(e.npcs["Grimbold"], e, "What is the password?")
agents.npc_reply(e.npcs["Tallow"], e, "What is the password?")
agents.chat = _real_chat
check("NPC prompt: non-witness Grimbold doesn't get the secret", "red heron" in _prompts[0], False)
check("NPC prompt: witness Tallow does", "red heron" in _prompts[1], True)
pre = e.to_dict()
pre["graph"]["data"]["nodes"] = [n for n in pre["graph"]["data"]["nodes"] if n.get("type") != "Event"]
pre["graph"]["data"]["edges"] = [x for x in pre["graph"]["data"]["edges"]
                                 if not (str(x["source"]).startswith("E") or str(x["target"]).startswith("E"))]
e3 = WorldState.from_dict(pre)
check("graph save from before events: history known by all",
      len(e3.events_known_by(e3.npcs["Grimbold"])), 2)

# ---- clock, timeline log, DM brief (Day 4) ----------------------------------
t = WorldState(scene_summary="Kael looks for work.")
check("default clock", t.clock_text(), "Year 200, 14th of Frostmonth, evening")
t.advance_clock("night")
check("later today", t.clock_text(), "Year 200, 14th of Frostmonth, night")
t.advance_clock("dawn")
check("earlier part -> next day", t.clock_text(), "Year 200, 15th of Frostmonth, dawn")
t.advance_clock("", False)
check("one step on", t.clock["part"], "morning")
t.clock = {"year": "Year 200", "month": "Frostmonth", "day": 21, "part": "late night"}
t.advance_clock("", False)
check("late night + hours -> dawn next day", t.clock_text(), "Year 200, 22nd of Frostmonth, dawn")
t.clock = dict(t.clock, day=14, part="evening")
t.move_to("Ashwick -- Borin's farm")
t.add_npc(NPC(name="Borin", persona="Old trapper.", important=True, location=t.location))
t.add_npc(NPC(name="Grimbold", persona="Innkeeper.", important=True, location="Ashwick -- the tavern"))
t.join_party("Borin")
agents.log_turn(t, action="I follow Borin north along the hunter's path.", npc_name="Borin",
                npc_line='Borin spits. "Fine. But you walk behind."', start_location=t.location,
                were_here={"Borin"}, left_behind=[], party_before=set(), scene_update={},
                narration="They set off.")
t.move_to("Blackpine Ridge -- the ridge's edge")
agents.log_turn(t, action="We climb until dawn.", npc_name="", npc_line="",
                start_location="Ashwick -- Borin's farm", were_here={"Borin"}, left_behind=[],
                party_before={"Borin"}, scene_update={"situation": "a cold ridge top with wolf tracks"},
                narration="")
tl = t.timeline()
check("every line has the full date and place", all(re.match(r"\d+\. \[Year 200, \d+\w\w of Frostmonth, [a-z ]+ \| .+\] ", x) for x in tl), True)
check("timeline lines", [x.split("] ", 1)[1] for x in tl], [
    'Kael (in the player\'s words): "I follow Borin north along the hunter\'s path."',
    'Borin: Borin spits. "Fine. But you walk behind."',
    "Borin joined Kael and travel with him now.",
    'Kael (in the player\'s words): "We climb until dawn."',
    "Kael and Borin left for Blackpine Ridge -- the ridge's edge.",
    "Time passed: it is now dawn.",
    "Kael and Borin arrived. The place: a cold ridge top with wolf tracks.",
])
check("arrival stamped with the new place and new time", tl[-1].split("] ")[0],
      "7. [Year 200, 15th of Frostmonth, dawn | Blackpine Ridge -- the ridge's edge")
check("Grimbold witnessed none of it", t.timeline(viewer=t.npcs["Grimbold"]), [])
check("Borin witnessed all of it", len(t.timeline(viewer=t.npcs["Borin"])), 7)
b = t.dm_brief()
check("brief: current scene is the last block", b.rsplit("\n", 6)[0].count("CURRENT SCENE"), 0)
check("brief: order", [b.index(k) for k in ("STORY PREMISE", "TIMELINE", "CURRENT SCENE")],
      sorted(b.index(k) for k in ("STORY PREMISE", "TIMELINE", "CURRENT SCENE")))
check("scene block", t.scene_block().splitlines()[:3], [
    "Place: Blackpine Ridge -- the ridge's edge",
    "Time: Year 200, 15th of Frostmonth, dawn",
    "Here: Kael; Borin (travelling with Kael): Old trapper."])
t2 = WorldState.from_dict(json.loads(json.dumps(t.to_dict())))
check("clock and timeline survive save/load", (t2.clock_text(), t2.timeline()), (t.clock_text(), tl))
check("exchanges and log lines stay separate", t.events_known_by(t.npcs["Borin"]), [])

# ---- old saves -------------------------------------------------------------
legacy = {
    "location": "Ashwick -- the smithy", "scene_summary": "Old save.",
    "npcs": {
        "Grimbold Ironfist": {"name": "Grimbold Ironfist", "persona": "Dwarf.", "important": True,
                              "known_facts": [], "thread": [{"role": "user", "content": "x"}],
                              "location": "Ashwick -- the tavern", "aliases": ["the dwarf"]},
        "Borla": {"name": "Borla", "persona": "Smith.", "important": True,
                  "known_facts": [], "thread": []},  # pre-location save
    },
    "flags": ["Fact one.", "Fact two."], "active_npc": "Borla",
    "recent_history": [["I go in.", "You go in."]],
    "places": ["Ashwick -- the tavern", "Ashwick -- the smithy"], "pending_action": "",
}
m = WorldState.from_dict(legacy)
check("legacy: location", m.location, "Ashwick -- the smithy")
check("legacy: places in order", m.places, ["Ashwick -- the tavern", "Ashwick -- the smithy"])
check("legacy: NPC locations", {n: x.location for n, x in m.npcs.items()},
      {"Grimbold Ironfist": "Ashwick -- the tavern", "Borla": "Ashwick -- the smithy"})
check("legacy: facts", m.flags, ["Fact one.", "Fact two."])
check("legacy: thread kept", m.npcs["Grimbold Ironfist"].thread, [{"role": "user", "content": "x"}])
check("legacy: history tuples", m.recent_history, [("I go in.", "You go in.")])

print("\nALL OK" if not failures else f"\n{failures} FAILED")
sys.exit(1 if failures else 0)

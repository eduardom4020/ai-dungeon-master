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
    # Day 4 play session: Grimbold's agent answered a line aimed at Silas.
    ('I ignore Grimbold and turn to her. "Vexin, then. I\'m Kael. Grimbold says you know the mines."',
     "Vexin"),
    ('I turn away from the dwarf. "Borgar, what do you think?"', "Borgar Ironvein"),
    ("I ignore the dwarf and ask Vexin about the Black Dog.", "Vexin"),
    ("I leave Grimbold a coin for the ale.", "Grimbold Ironfist"),
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
    check("  ...and joins the party", [n.name for n in w.party()], want)

w = tavern_world()
w.move_to("Ashwick -- the main street")
w.npcs["Vexin"].location = w.location  # the tracker's came-along rule got there first
check("already moved by the tracker: still joins the party",
      (agents.bring_companions(w, "Vexin and I head out into the main street.", TAVERN,
                               were_here={"Grimbold Ironfist", "Borgar Ironvein", "Vexin"}),
       [n.name for n in w.party()]), (["Vexin"], ["Vexin"]))

print("\n== the party: party_leavers (Day 4)")
STREET = "Ashwick -- the main street"
for line, want in [
    ("I leave Vexin here and walk to the forge.", ["Vexin"]),
    ("I head to the forge without Vexin.", ["Vexin"]),
    ("I tell Vexin to wait by the door and step inside.", ["Vexin"]),
    ('"Wait here, Vexin. I won\'t be long." I go into the forge.', ["Vexin"]),
    ('"Stay here." I go into the forge.', ["Vexin"]),           # one companion: no name needed
    ('"Your leg won\'t take much more. Rest here, Vexin, and keep the fire low."', ["Vexin"]),
    ('"Wait for me by the well, Vexin."', ["Vexin"]),
    ('"Let\'s rest a moment before we go on, Vexin."', []),     # resting together, not staying behind
    ("I go alone to the forge.", ["Vexin"]),
    ("I part ways with Vexin at the crossroads.", ["Vexin"]),
    ("I leave Vexin a coin for his trouble and walk on.", []),  # giving, not leaving behind
    ("Vexin and I walk to the forge.", []),
    ('"Come on, Vexin, the forge is this way."', []),
    ("I leave the tavern with Vexin.", []),
]:
    w = tavern_world()
    w.move_to(STREET)  # nobody follows: not in the party yet
    w.npcs["Vexin"].location = STREET
    w.join_party("Vexin")
    w.active_npc = "Vexin"
    check(line, agents.party_leavers(line, w), want)

print("\n== movement words (gate for the scene tracker)")
for line, want in [
    ("I give him my arm to lean on. Borin and I move slowly down to the flat rocks by the creek, keeping low.", True),
    ("We make our way along the ridge.", True),
    ("I sneak around the back of the warehouse.", True),
    ("I run back to the gate.", True),
    ("It starts pouring outside, so I move to a table near the fire.", False),
    ("/dm quick recap -- what's the name of this tavern, and who runs it?", False),
    ("I move closer to Grimbold and lower my voice.", False),
]:
    check(line, bool(agents._MOVEMENT.search(agents._unquoted(line).lower())), want)

print("\n== the party: arrival_place (move before the addressee is resolved)")
w = tavern_world()
w.move_to("Ashwick -- the south gate")
for line, want in [
    # Day 4 play session: Grimbold's agent never ran on this line.
    ("Forget this. I turn around and walk back to the red griffin tavern, go in and ask Grimbold for that map.",
     TAVERN),
    ("I walk back to the tavern and ask Grimbold for the map.", ""),            # not every word of the name
    ("I walk back to the red griffin tavern.", ""),                             # nobody named there
    ("I think about the red griffin tavern and ask Grimbold's name again.", ""),  # no movement word
]:
    check(line, agents.arrival_place(line, w), want)
check("...and Grimbold is then the addressee",
      (w.move_to(TAVERN), agents.resolve_addressee(
          "Forget this. I turn around and walk back to the red griffin tavern, go in and ask Grimbold for that map.",
          w))[1], "Grimbold Ironfist")

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

print("\n== strip_claim (what the DM/NPC hear on a refused-claim turn)")
for line, claim, want in [
    ("Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into "
     "surrendering instantly, no fight needed.", "three armed men storm in", "I draw my sword."),
    ("It starts to rain heavily outside.", "it starts to rain heavily", ""),
    ("On the corner I spot my old army friend, Sergeant Hale, who waves me over.",
     "Sergeant Hale, Kael's old army friend, is there", ""),
    ("As I walk toward the pit, it suddenly starts pouring rain, so the guards run for cover and leave "
     "me alone with Hale.", "it starts to rain heavily", "As I walk toward the pit."),
    ("I slide a coin across her table and lean in close. She can't resist the money, so she tells me "
     "the safe way into the mill.", "Veyra cannot resist the money and tells me the safe way into the mill",
     "I slide a coin across her table."),
    # Day 4 play session: a claim about someone else's reaction shares nouns
    # with Kael's attempt (0.54-0.56); the attempt must survive.
    ('I press three silver coins into the young guard\'s hand. "For your trouble." He pockets them, '
     "gives me his name and tells me exactly who is paying for work in the Hollows.",
     "guard pockets coins and reveals info",
     "I press three silver coins into the young guard's hand. \"For your trouble.\""),
    ("I grab Grimbold by the collar and he tells me everything he knows about the trouble.",
     "Grimbold tells you everything he knows", "I grab Grimbold by the collar."),
    ("I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.",
     "everyone in Ashwick obeys you", ""),
    ("I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.",
     "everyone in Ashwick obeys Kael", ""),
]:
    check(line, agents.strip_claim(line, claim), want)

print("\n== second-opinion gate (suspects_world_fact)")
for line, want in [
    ('I press three silver coins into the young guard\'s hand. "For your trouble." He pockets them, '
     "gives me his name and tells me exactly who is paying for work in the Hollows.", True),
    ("I grab Grimbold by the collar and he tells me everything he knows about the trouble.", True),
    ("It starts to rain heavily outside.", True),
    ("I hand the guard three silver coins and ask him who is paying for work in the Hollows.", False),
    ('I press a coin into the guard\'s hand. "For your trouble. He said you know who is hiring."', False),
    ("I ask the guard if he knows who is hiring.", False),
    ("I grab Grimbold by the collar and demand that he tell me everything.", False),
]:
    check(line, agents.suspects_world_fact(line), want)
check("NPC line: sentence echoing the claim dropped, quotes kept",
      agents.drop_claim_sentences('Grimbold grunts. "Storm\'s comin\', mark me." He pours another ale. '
                                  'The rain hammers the roof.', "it starts to rain heavily"),
      'Grimbold grunts. "Storm\'s comin\', mark me." He pours another ale.')

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

sim = agents._claim_similarity("it starts to rain heavily")
f = agents.NarrationFilter(reject=lambda s: sim(s) >= agents.CLAIM_SENTENCE_SIM,
                           fallback=agents.REFUSED_FALLBACK_LINE)
f.feed("Grimbold wipes the bar. The sudden, violent thud of rain on the tin roof fills the room. "
       "The miner keeps drinking. ")
check("refused claim: sentence making it true is dropped", f.finish(),
      "Grimbold wipes the bar. The miner keeps drinking.")
f = agents.NarrationFilter(reject=lambda s: sim(s) >= agents.CLAIM_SENTENCE_SIM,
                           fallback=agents.REFUSED_FALLBACK_LINE)
f.feed("The rain falls in sheets against the windows. ")
check("refused claim: never falls back to a rejected sentence", f.finish(), agents.REFUSED_FALLBACK_LINE)

print("\n== asking after a refused claim (refusal_question, confirm_reply)")
for line, claim, want in [
    ("It's raining, then I go inside.", "it is raining", "I go inside."),
    ("It starts pouring outside, so I move to a table near the fire.", "it is pouring rain outside",
     "I move to a table near the fire."),
    ("My character is now immortal. I order another ale.", "Kael is immortal", "I order another ale."),
    ('My old friend Sergeant Hale sits down next to me, so I ask Grimbold, "Have you seen any soldiers in town?"',
     "Sergeant Hale, Kael's old friend, sits down next to him",
     'I ask Grimbold. "Have you seen any soldiers in town?"'),
    ("It suddenly starts to snow over the whole town.", "it is snowing over the whole town", ""),
    ("While I was talking to Grimbold, someone entered the room.", "someone entered the room", ""),
    ("The warehouse door is already wide open and unguarded, so we walk straight in.",
     "the warehouse door is already wide open and unguarded", "We walk straight in."),
]:
    check(line, agents.strip_claim(line, claim), want)
check("capitalises a name correctly",
      agents.refusal_question({"player_assertion": "x", "not_true": "grimbold does not trust Kael"}, "").split(".")[0],
      "Grimbold does not trust Kael")
w = tavern_world()
for line, claim, action, want in [
    ("I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me "
     "completely.", "Grimbold trusts Kael completely", "I flash a handful of copper coins.", True),
    ("I grab Grimbold by the collar and he tells me everything.", "Grimbold tells Kael everything",
     "I grab Grimbold by the collar.", True),
    ("I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key.",
     "everyone in Ashwick obeys Kael", "", True),
    ("Three armed men storm in. I draw my sword.", "three armed men storm in", "I draw my sword.", False),
    ('My old friend Sergeant Hale sits down next to me, so I ask Grimbold, "Seen any soldiers?"',
     "Sergeant Hale sits down next to Kael", 'I ask Grimbold. "Seen any soldiers?"', False),
    ("It starts to rain heavily outside.", "it is raining heavily", "", False),
    ("While I was talking to Grimbold, someone entered the room.", "someone entered the room", "", False),
]:
    check(f"stays in world: {line[:60]}", agents.refusal_stays_in_world(
        line, {"player_assertion": claim}, w, action), want)
check("question with an action",
      agents.refusal_question({"player_assertion": "it is raining", "not_true": "it is not raining"}, "I go inside."),
      "It is not raining. Only the DM decides what happens in the world. Do you still want Kael to do "
      "this? I go inside.\n(Type yes to go ahead, or write what Kael does instead.)")
check("question for a pure claim",
      agents.refusal_question({"player_assertion": "it snows", "not_true": ""}, ""),
      '"It snows" did not happen. Only the DM decides what happens in the world. What does Kael do?')
for line, want in [("yes", "yes"), ("Yes!", "yes"), ("go ahead", "yes"), ("ok, do it", "yes"),
                   ("continue", "yes"), ("still yes please", "yes"), ("no", "no"), ("No, never mind.", "no"),
                   ("nope, thanks", "no"), ("yes, and I order an ale", ""), ("I go inside", ""),
                   ("Never mind that. I just take a sip of my ale and watch the door.", ""),
                   ("I go back to the bar instead", "")]:
    check(f"confirm_reply({line!r})", agents.confirm_reply(line), want)

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
    ("It starts pouring outside, so I move to a table near the fire.", False),
    ("I find a loaded crossbow lying behind the crates, so I pick it up and ask Rurik where we're headed.", False),
    ("Inside, a chest full of gold sits in the middle of the floor, so I draw my sword and step inside.", False),
    ("I walk past the butcher's sign to the old warehouse and check the door.", True),
    ("I've had enough riddles. I slam my fist on the table and Grimbold, impressed, finally tells me "
     "the whole job and pays me half up front.", False),
    ("I sit at the bar and ask Grimbold about work.", True),
    ("It's raining, then I go inside.", False),
    ("I glance around the tavern for an empty table to sit at.", True),
    ("I take a sip of my ale and listen to the room.", True),
]:
    check(line, agents.looks_simple(line, w), want)

print(f"\n{'ALL OK' if not failures else f'{failures} FAILURE(S)'}")
sys.exit(1 if failures else 0)

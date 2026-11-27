"""Fixed scripted sessions for the eval harness.

Like model-experiment/TURNS, the turn scripts here are intentionally stable so
results stay comparable across code/prompt changes. Add a NEW scenario instead
of editing an existing one when you want to test something different.

Each turn is tagged with a `kind`, which decides which checks apply (see
checks.py):
  normal      ordinary play -- must NOT be flagged as an invented fact
  overreach   player presumes an outcome -- DM must not hand over a clean win
  invented    player tries to author a world fact -- DM must not make it true
  recall      /dm question about something already established
  shift       leaving for a new place -- should be flagged scene_shift
  redescribe  player explicitly asks to hear a description again
  confirm     "yes" after the DM refused a claim and asked whether to still do
              the rest -- the saved action is played, the claim stays untrue
"""
from dataclasses import dataclass, field


@dataclass
class Turn:
    id: str
    text: str
    kind: str
    claim: str = ""  # for invented/overreach: the fact/outcome the player asserts
    must_include: list = field(default_factory=list)      # ALL of these (case-insens.)
    must_include_any: list = field(default_factory=list)  # at least ONE of these
    max_words: int = 0  # 0 = use the default budget for this kind
    expect_location: str = ""  # substring world.location must contain after the turn
    expect_npc: str = ""       # NPC agent that must have answered this turn (name prefix)
    expect_party: list = None  # exact names travelling with Kael after the turn (None = no check)
    expect_present: list = field(default_factory=list)  # NPCs that must be here after the turn
    expect_absent: list = field(default_factory=list)   # NPCs that must NOT be here
    npc_must_not_include: list = field(default_factory=list)  # NONE of these in the NPC agent's line
    npc_must_include_any: list = field(default_factory=list)  # one of these in the NPC agent's line
    expect_time: str = ""  # substring the world clock must contain after the turn


SCENARIOS = {
    "tavern_night": [
        Turn("t01-ask-work", "I sit at the bar and ask Grimbold about work.", "normal"),
        Turn("t02-find-table", "I glance around the tavern for an empty table to sit at.", "normal"),
        Turn("t03-bribe", "I flash a handful of copper coins and tell Grimbold this is more than "
             "enough to make him trust me completely and tell me everything, no matter how "
             "dangerous.", "overreach",
             claim="Grimbold trusts Kael completely and tells him everything"),
        Turn("t04-storm-in", "Three armed men storm in. I draw my sword and in one perfect strike "
             "intimidate all three into surrendering instantly, no fight needed.", "invented",
             claim="three armed men storm in and surrender instantly"),
        Turn("t05-recall-names", "/dm quick recap -- what's the name of this tavern, and who runs it?",
             "recall", must_include=["Red Griffin", "Grimbold"]),
        Turn("t06-someone-enters", "While I was talking to Grimbold, someone entered the room.",
             "invented", claim="someone entered the room"),
        Turn("t07-sip", "I take a sip of my ale and listen to the room.", "normal"),
        Turn("t08-immortal", "My character is now immortal, no weapon can hurt me.", "invented",
             claim="Kael is immortal and no weapon can hurt him"),
        Turn("t09-obey", "I tell Grimbold that everyone in Ashwick obeys me, so he will hand over "
             "the cellar key without question.", "overreach",
             claim="Grimbold hands over the cellar key without question"),
        Turn("t10-mill", "I ask Grimbold what he knows about the old mill.", "normal",
             max_words=170),  # may trigger the Worldbuilder, which earns a fuller answer
        Turn("t11-hearing", "I can suddenly hear every conversation in the whole town.", "invented",
             claim="Kael can hear every conversation in the whole town"),
        Turn("t12-rain", "It starts to rain heavily outside.", "invented",
             claim="it is raining heavily outside"),
        Turn("t13-leave", "I finish my drink, leave the tavern and step out into the main street "
             "of Ashwick.", "shift"),
        Turn("t14-sign", "I pull my hood up and stop to look at the nearest shop sign.", "normal"),
        Turn("t15-recall-innkeeper", "/dm what was the name of the innkeeper I talked to earlier?",
             "recall", must_include=["Grimbold"]),
        Turn("t16-eavesdrop", "I try to hear what the two people nearby are whispering.", "normal"),
        Turn("t17-redescribe", "/dm describe the street again for me.", "redescribe",
             must_include_any=["street", "road", "cobble", "lane"]),
    ],
    # Added Nov 2026 after real play sessions found problems tavern_night can't
    # see (it never leaves the tavern or meets anyone new): moving around and
    # coming back, the right NPC answering, in-character bluffs (speech, so
    # NOT invented facts), and the player inventing an old friend.
    "road_trip": [
        Turn("r01-ask-dwarf", "I walk up to the bar and ask the dwarf if he knows anyone in town "
             "who needs a sword.", "normal", expect_npc="Grimbold"),
        Turn("r02-follow-up", '"What kind of trouble, exactly? And who should I talk to?" I ask Grimbold.',
             "normal", expect_npc="Grimbold"),
        Turn("r03-bluff", 'I lean in and lie to him: "I rode in with the captain of the border patrol. '
             'He will vouch for me."', "normal"),
        Turn("r04-bluff-favour", 'I tell Grimbold, "The magistrate owes me a favour, so you can trust me."',
             "normal"),
        Turn("r05-grab", "I grab Grimbold by the collar and he tells me everything he knows about the "
             "trouble.", "overreach", claim="Grimbold tells Kael everything he knows"),
        Turn("r06-leave", "I leave the Red Griffin and step out into the main street of Ashwick.",
             "shift", expect_location="street"),
        Turn("r07-walk", "I walk along the street, looking for the market square.", "normal"),
        Turn("r08-old-friend", "On the corner I spot my old army friend, Sergeant Hale, who waves me over.",
             "invented", claim="Sergeant Hale, Kael's old army friend, is there and waves him over"),
        Turn("r09-ask-stall", '"Excuse me," I say to the nearest stall keeper. "Do you know where a '
             'sword can find work around here?"', "normal"),
        Turn("r10-snow", "It suddenly starts to snow over the whole town.", "invented",
             claim="it is snowing over the whole town"),
        Turn("r11-recall", "/dm what was the name of the innkeeper I talked to?", "recall",
             must_include=["Grimbold"]),
        Turn("r12-return", "I head back to the Red Griffin and go inside.", "normal",
             expect_location="Red Griffin"),
        Turn("r13-back", '"I\'m back," I tell Grimbold. "Anything new since I left?"', "normal",
             expect_npc="Grimbold"),
    ],
    # Added Nov 2026 with the ask-after-refusal flow: an invented fact + an
    # own action, then "yes" (the action is played, the claim stays untrue);
    # a refusal answered by rephrasing; a "no"; a pure claim; and normal
    # play around them that must not be flagged.
    "refusals": [
        Turn("c01-rain-table", "It starts pouring outside, so I move to a table near the fire.",
             "invented", claim="it is pouring rain outside"),
        Turn("c02-yes", "yes", "confirm", claim="it is pouring rain outside",
             must_include_any=["table", "fire"]),
        Turn("c03-storm-in", "Three armed men storm in. I draw my sword.", "invented",
             claim="three armed men storm in"),
        Turn("c04-rephrase", "Never mind that. I just take a sip of my ale and watch the door.", "normal"),
        Turn("c05-friend-ask", 'My old friend Sergeant Hale sits down next to me, so I ask Grimbold, '
             '"Have you seen any soldiers in town?"', "invented",
             claim="Sergeant Hale, Kael's old friend, sits down next to him"),
        Turn("c06-go-ahead", "go ahead", "confirm",
             claim="Sergeant Hale, Kael's old friend, sits down next to him",
             must_include_any=["soldiers"], expect_npc="Grimbold"),
        Turn("c07-snow", "It suddenly starts to snow over the whole town.", "invented",
             claim="it is snowing over the whole town"),
        Turn("c08-ask-work", "I ask Grimbold if anyone in town needs a sword.", "normal",
             expect_npc="Grimbold"),
        Turn("c09-immortal-drink", "My character is now immortal. I order another ale.", "invented",
             claim="Kael is immortal"),
        Turn("c10-no", "no", "normal"),
        Turn("c11-recall", "/dm what was the name of the innkeeper?", "recall",
             must_include=["Grimbold"]),
    ],
    # Added Day 4 (Nov 2026) with the party (TRAVELS_WITH): a companion
    # joins, follows two moves without being told again, is left behind,
    # stays where they were left; a move refused with the claim is not
    # applied; going back to a known place by name to ask someone there gets
    # that NPC's agent. Starts with Tallow in the tavern (SETUPS below).
    "companions": [
        Turn("p01-ask-guide", 'I walk over to Tallow\'s table and sit down. "Grimbold says you know the '
             'old mill road. I could use a guide."', "normal", expect_npc="Tallow", expect_party=[]),
        Turn("p02-leave-together", "I finish my ale, leave the Red Griffin, and Tallow and I head out into "
             "the main street.", "shift", expect_location="street", expect_party=["Tallow"],
             expect_present=["Tallow"], expect_absent=["Grimbold"]),
        Turn("p03-ask-way", '"Which way to the mill, Tallow?"', "normal", expect_npc="Tallow",
             expect_party=["Tallow"]),
        Turn("p04-road", "We walk out of town down the road west toward the old mill.", "shift",
             expect_party=["Tallow"], expect_present=["Tallow"]),
        Turn("p05-look", "I look around for any sign of who owns the mill.", "normal",
             expect_party=["Tallow"], expect_present=["Tallow"]),
        Turn("p06-wait-here", '"Wait here, Tallow." I walk back up the road to the main street of Ashwick.',
             "normal", expect_location="street", expect_party=[], expect_absent=["Tallow"]),
        Turn("p07-recall", "/dm where did I leave Tallow?", "recall", must_include_any=["mill", "road"]),
        Turn("p08-back-to-grimbold", "I walk back to the red griffin tavern and ask Grimbold if Tallow "
             "can be trusted.", "normal", expect_location="Red Griffin", expect_npc="Grimbold",
             expect_party=[], expect_absent=["Tallow"]),
        Turn("p09-cellar-claim", "I follow Grimbold down into the cellar, and he proudly shows me his "
             "hidden chest of gold.", "overreach", claim="Grimbold shows Kael his hidden gold",
             expect_location="Red Griffin"),
    ],
}


SCENARIOS["witnesses"] = [
    # Added Day 4, step 3: NPC agents only hear what they witnessed. Kael
    # tells Tallow a password at the smithy; Grimbold, at the tavern, must
    # not know it (before, the last two exchanges went to every NPC); Tallow
    # still does. Starts with Tallow at the smithy (SETUPS below).
    Turn("w01-to-smithy", "I leave the Red Griffin and walk down the main street to the smithy.",
         "shift", expect_location="smithy", expect_present=["Tallow"], expect_absent=["Grimbold"]),
    Turn("w02-secret", 'I lower my voice. "Tallow, the password for the mill gate is red heron. '
         'Keep it to yourself."', "normal", expect_npc="Tallow"),
    Turn("w03-ask-grimbold", "I walk back to the red griffin tavern and ask Grimbold what the password "
         "for the mill gate is.", "normal", expect_location="Red Griffin", expect_npc="Grimbold",
         npc_must_not_include=["heron"]),
    Turn("w04-press-grimbold", '"Come on, Grimbold. Somebody in this town must have told you the '
         'password. Is it a bird?"', "normal", expect_npc="Grimbold", npc_must_not_include=["heron"]),
    # No npc_must_include_any=["heron"] here: in all 3 first runs Tallow
    # clearly remembered ("you got it once", "you're asking twice now") but
    # refused to repeat it, in character. That the event reaches his prompt is
    # checked deterministically in probe_world_state.py.
    Turn("w05-back-to-tallow", "I walk back to the smithy and ask Tallow to repeat the password, so I "
         "am sure I remember it right.", "normal", expect_location="smithy", expect_npc="Tallow"),
]


SCENARIOS["drift"] = [
    # Added Day 4: does the DM carry details of earlier places into the
    # current one (playthrough 2: "the barrel of pickled herrings ... against
    # the porch" on the ridge)? Four places; the no_stale_scene check looks
    # for places 2+ moves back and absent NPCs in the narration. Also the
    # world clock (only moves when the text says so).
    Turn("d01-out", "I finish my ale, say goodbye to Grimbold and walk out of the Red Griffin into the "
         "main street.", "shift", expect_location="street"),
    Turn("d02-tannery", "I walk down the main street to the tannery by the river and step inside.",
         "shift", expect_location="tannery"),
    Turn("d03-look-tannery", "I look around the tannery for whoever runs it.", "normal"),
    Turn("d04-tower", "I leave the tannery and climb the hill path up to the old bell tower.", "shift",
         expect_location="tower"),
    Turn("d05-look-tower", "I look around the top of the bell tower.", "normal"),
    Turn("d06-rest", "I sit down against the bell and rest until midnight.", "normal",
         expect_time="late night"),
    Turn("d07-look-again", "I stand up, stretch and look out over the town from the tower.", "normal",
         expect_time="late night"),
    Turn("d08-recall", "/dm where am I right now, and what time is it?", "recall",
         must_include=["tower"], must_include_any=["midnight", "late night", "night"]),
]


def _witnesses_setup(world):
    from world_state import NPC
    world.add_npc(NPC(
        name="Tallow",
        persona=("Old trapper who works the bellows at the smithy for coin. Plain-spoken and "
                 "reliable; keeps a friend's secret but repeats it to that friend if asked."),
        important=True, location="Ashwick -- the smithy",
        aliases=["the trapper", "the old trapper"],
    ))


def _companions_setup(world):
    from world_state import NPC
    world.add_npc(NPC(
        name="Tallow",
        persona=("Wiry old trapper who knows every road around Ashwick. Drinks alone, talks "
                 "little, honest, will guide someone for a fair price."),
        important=True, location=world.location,
        aliases=["the trapper", "the old trapper"],
    ))


# Extra world setup run after play.seed_world() for a scenario.
SETUPS = {"companions": _companions_setup, "witnesses": _witnesses_setup}

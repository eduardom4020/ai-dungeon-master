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
}

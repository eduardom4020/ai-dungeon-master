"""The four agent roles: Rules Referee (also the turn Router), DM/Narrator,
NPC, Worldbuilder.

Generation params (temperature/top_p/...) below are placeholder defaults --
intentionally not tuned yet. Revisit once we're testing against real play
sessions, per the plan to defer that tuning until it's needed.
"""
import json
import re
import urllib.error

import torch
from sentence_transformers import SentenceTransformer, util

from ollama_client import chat
from world_state import WorldState, NPC

RULES_OPTIONS = {"temperature": 0.3, "top_p": 0.9}
DM_OPTIONS = {"temperature": 0.85, "top_p": 0.95}
NPC_OPTIONS = {"temperature": 0.8, "top_p": 0.95}
WORLDBUILD_OPTIONS = {"temperature": 0.9, "top_p": 0.95}

RULES_SYSTEM = """You are the Rules Referee and turn Router for a simple \
homebrew tabletop RPG. There are no dice and no numeric stats -- your \
judgment IS the resolution mechanic. The player never sees your output \
directly; you decide what actually happens AND which helper agents are \
needed this turn, then a separate narrator describes it all to the player.

PART 1 -- ROUTE the turn:
- "info_request": the player is asking a question or requesting a recap, \
  not declaring an action (e.g. "what did he say his name was?", "what does \
  the square look like?").
- "dialogue": the player is directly speaking to / engaging an NPC.
- "action": the player is declaring/attempting to do something, including \
  ordinary actions (sitting, walking, looking around) and risky ones.
A turn can be both "dialogue" and involve risk (e.g. a bribe) -- in that \
case, set turn_type="dialogue" AND still judge outcome/twist normally; \
addresses_npc will route it to the NPC agent regardless.

- known_to_dm: only meaningful when turn_type=="info_request". True if the \
  WORLD CONTEXT you were given already contains the answer. False if it's \
  something new that would need to be invented.
- addresses_npc: true if the player is directly speaking to or engaging the \
  NPC named under TALKING WITH in the world context, this specific turn -- \
  not just because an NPC happens to be present in the scene. False if \
  there is no TALKING WITH line.
- scene_shift: true if this turn moves to a meaningfully new or different \
  environment worth describing at length -- arriving somewhere for the \
  first time, stepping out into a space that contrasts sharply with where \
  the player just was (e.g. leaving a tavern into a crowded city street), \
  or another notable change in the physical scene itself. False for an \
  ordinary continuation of the current scene, and almost always false \
  during dialogue or a simple back-and-forth exchange -- those should stay \
  tight, not scenic.

PART 2 -- JUDGE the action (same as always). Do not grant an action just \
because it was declared confidently, dramatically, or as an assumed fact. \
Weigh:
- Plausibility given the character's established abilities and gear (no \
  magic, feats, or knowledge that hasn't been established).
- Whether NPCs have their own will, goals, and resistance -- they do not \
  simply comply, trust, or surrender because the player asserts it.
- Whether the action would trivialize tension the story is building. \
  Prefer partial success or a complication over a flat, clean success when \
  the player is overreaching, presuming an outcome instead of attempting \
  one, or trying to skip past conflict that should matter.
- Genuinely reasonable, well-set-up actions should still succeed -- you are \
  not here to punish the player, only to stop free wins.
- For a pure info_request with nothing being contested, outcome is simply \
  "success" and twist is empty.

PART 3 -- PLAYER AUTHORITY. The player controls ONLY their own character: \
what that character attempts to do, says, thinks, and perceives through \
ordinary senses. The player does NOT decide facts about the world; only the \
DM does. These are invented facts, not actions: other characters or \
creatures arriving, leaving, attacking, surrendering, or reacting in a \
specific way; events (a storm, a fire, a collapse, an ambush); objects or \
places appearing; the character gaining powers, immunity, knowledge, senses, \
or items that are not already established; what an NPC feels or decides. \
When the player asserts one of these, do NOT treat it as true: put a short \
phrase naming it in "player_assertion", and judge only the legitimate \
remainder (the character's own attempt). If nothing legitimate remains, \
outcome is "failure". Examples of invented facts: "three armed men storm \
in", "someone entered the room while I was talking", "my character is now \
immortal", "I can suddenly hear everything beyond my senses", "I can hear every \
conversation in the whole town", "it starts to rain heavily", "the guard \
falls asleep", "I spot an old friend of mine waiting by the road" (a \
character the DM never introduced), "I grab him and he tells me everything \
he knows" (the grab is an attempt; his reaction is invented). Weather, \
noise, light, and any change to the surroundings \
are the DM's to decide, never the player's. Also, never copy the asserted \
fact into "twist" -- the twist must not make the invented fact true. NOT \
invented facts: "I draw my sword", "I shout at the \
guard", "I try to hear what they're whispering", and ANYTHING the \
character says out loud, including lies, bluffs, boasts and threats (\
'I tell him: "I rode in with the captain of the border patrol"', '"The \
guards are right behind me," I bluff'): the words are the player's to \
choose, they do not become true by being said, and whether anyone \
believes them is for the NPCs to decide. Exceptions, leave \
player_assertion empty: (a) the DM's most recent narration in RECENT \
HISTORY explicitly invited the player to decide that detail, or (b) it is \
trivial scene dressing that cannot change the flow of events (e.g. picking \
an empty seat in a tavern that already has tables). When unsure, ask: could \
this change what happens next in the story? If yes, it is an invented fact.

Respond with ONLY a JSON object, no other text, matching exactly:
{"player_assertion": "a short phrase naming any world fact the player tried to invent (see PART 3), or empty string if none",
 "not_true": "if player_assertion is set: one short lower-case clause saying plainly what did NOT happen, e.g. 'no men came into the room' or 'your character did not become immortal' or 'it is not raining'; otherwise empty string",
 "turn_type": "info_request" | "dialogue" | "action",
 "known_to_dm": true | false,
 "addresses_npc": true | false,
 "scene_shift": true | false,
 "outcome": "success" | "partial" | "complication" | "failure",
 "twist": "a bare mechanical note on WHAT changes, under 12 words, no dialogue, no quotes, no character voice -- e.g. 'a guard notices' or 'the rope frays' or 'he demands proof first', or empty string if none",
 "rationale": "one short sentence of internal reasoning, never shown to the player"}
"""

DM_SYSTEM = """You are the Dungeon Master (DM) for a simple, homebrew tabletop \
RPG. There is no rigid mechanical system -- you narrate. A separate Rules \
Referee has already decided the outcome of the player's action; you will be \
given that RULING and must narrate consistently with it. Never resolve the \
action as more successful than the ruling allows, and never contradict it.

1. NARRATIVE QUALITY: Vivid, sensory prose. Concrete detail, not generic \
   fantasy filler. Distinct NPC voices and motives.
2. COHESION: Stay consistent with the world context, established facts, and \
   recent history you are given. Never contradict them. Only characters \
   listed under CHARACTERS HERE (or unnamed people in the scene) can speak \
   or act this turn; characters listed as NOT here cannot.
3. CONCISION: be brief by default. Most turns -- and almost all dialogue -- \
   are TIGHT: 2-4 sentences, one short paragraph, roughly 60-100 words, \
   covering only what changed because of the player's action. End on a \
   clear situation or choice point, not a wall of exposition. You may write \
   more ONLY when one of these is true: (a) pacing is FULL SCENE (a \
   genuinely new or dramatically different environment), or (b) this turn \
   is the FIRST time the story introduces something that matters -- a new \
   place, a new important character, or a key object or clue. Give that \
   new thing a fuller description (at most 5 sentences), and still \
   end on a clear situation or choice point. This is permission to spend \
   more of the reader's attention where it earns it, not a license to \
   ramble.
3b. NEVER RE-DESCRIBE: the player has already read everything in RECENT \
   HISTORY and the world context. Do not repeat the room, the weather, an \
   NPC's appearance, or any detail that has already been described -- refer \
   to it in passing only if it matters to what happens now. Spend your \
   words only on what is new this turn. The only exception is when the \
   player explicitly asks you to describe or recap something again (e.g. \
   "describe the room again", "/dm recap"); then do so.
4. Never play the player character's actions, thoughts, or dialogue for \
   them. Only describe the world's and NPCs' response, then hand control \
   back.
5. If given an NPC's in-character line, treat it as dialogue that already \
   happened -- continue the scene from it (reactions, follow-up, what \
   happens next). Do NOT quote it, restate it, or paraphrase it back; the \
   player already read it. Do not re-describe the same beat twice.
6. The RULING's "twist" is a bare fact about what changes, not dialogue --\
   translate it into scene action/detail yourself, in your own words, once.
7. If given NEWLY ESTABLISHED LORE, that's reference material, not prose to \
   read aloud -- weave its content into the scene naturally, once, in your \
   own words, the way a DM would reveal it through description or an NPC's \
   knowledge. Do not quote or recite it like a document -- except when the \
   player is reading something written (a letter, a note, a sign): then \
   quote the words that matter, plainly.
8. PLAYER AUTHORITY: only the DM decides what is true in the world. The \
   player only controls what their own character attempts, says, and \
   thinks. If the user message contains a PLAYER OVERSTEP note, the player \
   tried to declare something about the world (an arrival, an event, a \
   reaction, a new power) -- that did NOT happen. Do not narrate it as fact, \
   do not have NPCs react to it, and do not scold the player or mention \
   rules. Stay in the fiction: describe only the character's own attempt \
   (e.g. they look toward the door, they reach for a sword), let the world \
   carry on exactly as it was, and end on a clear choice point. Never \
   "yes, and" an invented fact into existence. Apply the same rule even \
   when there is no OVERSTEP note, if the player's message plainly declares \
   such a fact (e.g. "it starts to rain", "someone walks in"). A lie or \
   bluff the character SPEAKS is just speech: the NPCs react to hearing it \
   (believe it, doubt it, call the bluff); it does not become true.
9. TONE: keep the world grounded. Ashwick is an ordinary frontier town; \
   tension comes from people, money, danger and ordinary detail (smoke, \
   mud, tired faces). Do not add magic or anything uncanny on your own -- \
   no glowing substances, living or breathing walls, curses, omens, strange \
   lights in the sky, voices with no source -- unless it is already in the \
   ESTABLISHED FACTS. Most turns need no ominous hint at all.
10. Plain text only: no asterisks, no markdown, no notes or asides to the \
   player in parentheses.
"""

NPC_SYSTEM_TEMPLATE = """You are role-playing a single NPC named {name} in a \
homebrew RPG. Persona: {persona}

Where you are right now: {location}. Also here: {others}.

Other people in this story (stay consistent with who they are, e.g. their \
name and whether they are a man or a woman):
{people}

Facts you have already told the player, and must stay consistent with: \
{known_facts}

What just happened, for context (the player's character is Kael):
{recent}

Rules:
- Speak and act ONLY as {name}. 1-3 sentences: dialogue plus minimal \
  physical beats. Never narrate the wider scene, other characters, or the \
  player character.
- When Kael asks you something, answer out loud: say what you know, or \
  refuse, dodge, or name a price -- but say it in words, in character.
- You have your own goals and will. Do not comply, trust, or over-share \
  just because the player is confident or persuasive -- react the way this \
  specific character actually would.
- React only to what the player's character actually says or does in front \
  of you. If the player claims something happened in the world (someone \
  arrived, an event occurred) or tells you what you feel or decide, you \
  have not perceived it: do not play along.
- Plain text only: spoken words in double quotes; actions in the third \
  person with your name ("{name} wipes the bar."), never "I" outside the \
  quotes. No asterisks and no other markdown.
- Do not break character or mention being an AI.
"""

WORLDBUILD_SYSTEM = """You are a worldbuilding assistant for a homebrew \
fantasy RPG campaign. Given a short request and the facts already \
established, write 80-150 words of new lore that fits seamlessly with \
what exists and does not contradict it. Write it as reference material for \
the DM: plain, concrete facts (who, what, where, how much), not story prose \
read aloud to players and not riddles. If the request is about what \
something says or contains (a letter, a sign, a map), give its exact \
content in plain words first. Keep it grounded: prefer human explanations \
(debts, feuds, smugglers, accidents) and add magic or the supernatural only \
if the established facts already include it. Plain text only, no markdown.
"""

TRACKER_SYSTEM = """You keep the bookkeeping for a text roleplaying game. \
You read what happened in ONE turn and report, as JSON, where the player's \
character (Kael) is now and which NAMED characters appeared. Use only what \
the PLAYER, NPC LINE and NARRATION texts actually say; never invent.

Return ONLY a JSON object, matching exactly:
{"moved": true | false,
 "location": "where Kael is at the END of this turn",
 "characters": [{"name": "...", "present": true | false}, \
{"name": "...", "present": true | false, "new": true, "persona": "...", "aliases": ["..."]}]}

- moved: true only if Kael physically left the place in CURRENT LOCATION \
for a different building, street, or area (walked out of a building, \
arrived at another site, is now out on the streets). Moving around within \
the same place is NOT moving: crossing a room, sitting at another table, \
walking up to someone, going up to a gate or toward a pit at the same site. \
Talking is never moving.
- location: if moved is false, copy CURRENT LOCATION exactly. If moved is \
true and Kael went back to one of KNOWN PLACES, copy that name exactly; \
otherwise give a short new name in the same style, e.g. \
"Ashwick -- the main street".
- characters: every character with a PROPER NAME (e.g. "Borgar", \
"Captain Mira") who speaks, acts, or is mentioned in the NPC LINE or \
NARRATION this turn. Never Kael. Never unnamed people ("a guard", "the \
patrons").
  - name: their name as written, in its fullest form.
  - present: true if they are physically in the same place as Kael at the \
end of the turn -- including anyone who leaves WITH Kael (leads the way, \
walks out with him, is followed by him); false if they were only \
mentioned, or stayed behind when Kael left.
  - For characters already in KNOWN CHARACTERS give only name and present.
  - For anyone NOT in KNOWN CHARACTERS also give "new": true, a "persona" \
(one short sentence on who they are and how they behave, from the text \
only) and "aliases" (up to 3 short ways the player might refer to them \
without the name, from the text, e.g. "the dwarf", "the big man"; [] if \
none).
"""


# EXPERIMENTAL -- see CLAUDE.md "Verdict-skip experiment". Zero-model-call
# gate to decide whether a turn is simple/self-contained enough to skip the
# Referee/Router call entirely. A sentence-embedding few-shot classifier
# judges RISK/CONTENT only -- it generalizes to paraphrased overreach that
# plain keyword/TF-IDF matching provably misses (tested this session:
# TF-IDF scored 0.000 similarity and misclassified "I casually mention that
# people generally just do what I say" as simple; embeddings correctly
# caught it at 0.233). Still imperfect on very low-confidence cases, which
# is why anything below CONFIDENCE_THRESHOLD falls through to the real
# Referee call rather than trusting a coin-flip match -- this only ever
# saves time, never adds capability, so ambiguity should always lose.
#
# Whether the turn addresses the active NPC is a SEPARATE, always-computed
# deterministic check (addresses_active_npc) -- it decides whether the NPC
# agent gets consulted, not whether the Referee gets skipped. Mundane
# dialogue ("I ask the innkeeper about work") should still skip the Referee
# and still get a real NPC reply; only risky/overreaching content (bribes,
# threats, demands for compliance) should force the full judgment call,
# regardless of whether it's aimed at an NPC or not.
_FIRST_PERSON = re.compile(r"\b(i|i'm|i'll|i've|me|my|mine|we|our|us)\b")
_WORLD_FACT_MARKERS = re.compile(
    r"\b(suddenly|all of a sudden|out of nowhere|meanwhile|instantly|"
    r"while i was|storms? in|bursts? in|walks? in|rushes? in|"
    r"starts? to (rain|snow|pour|storm)|(starts?|begins?) (raining|snowing|pouring|storming)|"
    r"i can now|i now (have|can|am))\b"
)
_QUESTION_STARTERS = ("what", "who", "where", "when", "why", "how", "tell me", "recap")
# Someone other than the player's character is the subject of a clause
# ("... pull him close. He cracks and tells me everything", "and the guard
# lets me pass"): the player is deciding what another character does. Found
# in a real play session, where both of these took the fast path and came
# true. Run on lower-cased text with quoted speech removed.
_CLAUSE_START = r"(?:^|[.!?;:]\s+|,\s*|\b(?:and|then|so|but)\s+)"
_OTHER_SUBJECT = re.compile(
    _CLAUSE_START
    # "it"/"there" added Nov 2026: "It starts pouring outside, so I move to a
    # table" took the fast path 3/3 and the rain came true.
    + r"(?:(?:he|she|they|it|it's|there|there's|someone|somebody|everyone|everybody|nobody)\s+[a-z]+"
    r"|(?:the|his|her|their)\s+[a-z]+\s+(?:[a-z]+(?:s|ed)|ran|fell|gave|told|came|went|left)\b)"
)
_QUOTED = re.compile(r'"[^"]*"?|“[^”]*”?')
# Words that make the player's line about engaging a specific person, used to
# pick WHICH present NPC they mean when several are named.
_ADDRESS_CUE = re.compile(
    r"\b(?:ask|asks|asking|say|says|saying|tell|tells|telling|turn(?:s|ing)?(?: back)? to|"
    r"whisper(?:s|ing)?(?: to)?|shout(?:s|ing)?(?: at| to)?|call(?:s|ing)?(?: out)?(?: to)?|"
    r"greet(?:s|ing)?|talk(?:s|ing)? to|speak(?:s|ing)? to|question|reply to|answer|"
    r"approach(?:es)?|walk(?:s)? (?:over|up) to|go(?:es)? (?:over|up) to|head(?:s)? over to|"
    r"sit(?:s)? (?:down )?(?:with|across from|next to|beside)|join|"
    r"lean(?:s)?(?: in)? (?:toward|towards|closer to)|nod(?:s)? to|wave(?:s)? to|"
    r"face|faces|facing|grab(?:s)?|push(?:es)?|shove(?:s)?)\b"
)
# Leaving or arriving somewhere: one of the cheap signals that the scene
# tracker should look at this turn (see scene_may_have_changed).
_MOVEMENT = re.compile(
    r"\b(?:leave|leaves|leaving|left|exit|exits|head|heads|heading|go|goes|going|"
    r"walk|walks|walking|enter|enters|step|steps|arrive|arrives|follow|follows|"
    r"travel|ride|rides|climb|climbs|descend|descends|return|returns|cross|crosses)\b"
)
_EMBED_MODEL_NAME = "all-MiniLM-L6-v2"
# Minimum (mean-simple-sim - mean-complex-sim) margin to call it SIMPLE.
# Small on purpose: these are averages over a small example pool, so raw
# scores sit in the 0.1-0.4 range, not the near-1.0 range a single close
# match would give. Untuned placeholder, like the temperature/top_p dicts
# above -- tested this session against a 15-case probe set. 0.025 sits in
# the gap between "Everyone here just naturally does whatever I ask of
# them" (margin +0.022, must stay COMPLEX -- this is the adversarial case
# that motivated switching to mean-of-class similarity in the first place)
# and "I sit at the bar and ask Grimbold about work" (margin +0.029, a
# legitimate SIMPLE fast-path win worth keeping).
CONFIDENCE_THRESHOLD = 0.025

_SIMPLE_EXAMPLES = [
    # ordinary physical actions -- varied settings, deliberately not tied
    # to any one scene's vocabulary
    "I pick up the fallen apple from the ground.",
    "I entered the room and looked around.",
    "I glance around the tavern for an empty table to sit at.",
    "I stretch my legs and yawn.",
    "I walk over to the hearth to warm my hands.",
    "I take a sip of my drink.",
    "I lean back in my chair.",
    "I look up at the ceiling beams.",
    "I set my pack down on the floor.",
    "I quietly hum a tune while waiting.",
    "I brush the dust off my cloak.",
    "I take a seat by the window.",
    "I close the door behind me.",
    "I light a candle on the table.",
    "I pull my hood up against the rain.",
    "I tie my boots before setting off.",
    "I pick up my sword and sheath it.",
    "I sit down by the campfire.",
    # mundane, low-stakes dialogue -- content carries no risk, even though
    # it's addressed to someone; varied speakers/settings
    "I said hi to her as she passed by.",
    "I ask the innkeeper about work.",
    "I ask him what's on the menu tonight.",
    "I say hello to the bartender.",
    "I ask her how her day has been.",
    "I greet the merchant at his stall.",
    "I nod politely to the passing guard.",
    "I ask the blacksmith how business has been.",
    "I comment on the weather to the farmer nearby.",
]
_COMPLEX_EXAMPLES = [
    # combat / physical risk
    "I draw my sword and in one perfect strike intimidate all three into surrendering instantly.",
    "I attack the bandit.",
    "I challenge the champion to a duel.",
    "I climb over the castle wall under cover of darkness.",
    # persuasion / social manipulation / overreach
    "I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely.",
    "I try to convince the guard to let me pass.",
    "I threaten the merchant unless he lowers his price.",
    "Everyone here just naturally listens to whatever I tell them.",
    "People around here tend to trust me the moment they meet me.",
    "I want him to tell me a secret.",
    "Reveal yourself!",
    "I demand the knight surrender his sword.",
    "I try to seduce the noblewoman into giving me the key.",
    "I bribe the guard to look the other way.",
    "I interrogate the prisoner for information.",
    # deception / stealth / risky skill actions
    "I attempt to pick the lock on the door.",
    "I sneak past the guards without being seen.",
    "I lie to the captain about who I really am.",
    "I pickpocket the merchant's purse without him noticing.",
    "I cast a spell to charm the wizard.",
    # player inventing facts about the world (only the DM decides these):
    # arrivals, events, environment, NPC reactions, new powers or items
    "A group of soldiers marches into the market square.",
    "Meanwhile, a hooded figure slips through the door behind me.",
    "Suddenly a dragon lands on the castle tower.",
    "While I was speaking, a messenger rushed into the hall.",
    "A storm rolls in and floods the street.",
    "The torches go out and the whole dungeon goes dark.",
    "The innkeeper gets angry and throws everyone out.",
    "I am now invulnerable and cannot be hurt by any weapon.",
    "My eyes glow and I can see through walls.",
    "I discover a secret passage behind the bookshelf.",
    "Out of nowhere, a thief steals the merchant's gold.",
    "The ground shakes and the wall collapses.",
    "Another traveler comes in from the road and joins the group.",
    "Somebody else wanders into the shop while we talk.",
    "I suddenly gain the ability to understand every language.",
    "Snow begins to fall over the whole village.",
    "A patrol shows up and surrounds the camp.",
    # real misses from a play session (paraphrased, not copied, so the
    # examples don't overfit to that one scene): the player decides how an
    # NPC reacts, or brings in a character the DM never introduced
    "I shove the smuggler against the wall and he spills every secret he has.",
    "I run into an old friend of mine from the army at the market.",
    "My cousin is waiting for me at the gate and lets me in.",
]

# Fast-path scene-shift detection: the DM_SYSTEM/RULES_SYSTEM "pacing"
# signal (full description vs tight) normally comes from judge_action(),
# but fast-path turns skip that call entirely -- without a check here,
# arriving somewhere new (usually low-risk, so fast-path-eligible) would
# always get hardcoded scene_shift=False and never the fuller treatment.
# Purely cosmetic/pacing, not a safety check like looks_simple(), so no
# confidence threshold: a false negative here just means a slightly
# tighter description than ideal, never a wrong or unsafe answer.
_SCENE_SHIFT_EXAMPLES = [
    "I step outside into the city for the first time.",
    "I open the door and walk into the grand hall.",
    "I leave the tavern and head out onto the street.",
    "I climb the last steps and emerge onto the mountain summit.",
    "I push through the crowd and enter the marketplace.",
    "I cross the bridge into the old quarter of the city.",
    "I walk through the gates into the castle courtyard.",
    "I descend into the dungeon for the first time.",
    "I step off the boat onto the docks.",
    "I ride over the hill and see the valley spread out below.",
]

# Ordinary actions that happen OUTDOORS or in public spaces. Only used as the
# "not a shift" side of looks_like_scene_shift(): the plain simple examples
# are mostly indoor, so street-level actions ("look at the shop sign") looked
# closer to the scene-shift examples than to them and got flagged as scene
# changes -- the eval harness showed that turn running 200-290 words.
_NON_SHIFT_EXAMPLES = [
    "I walk a little way along the road.",
    "I stop at a market stall to look at the wares.",
    "I sit on a bench by the well.",
    "I look at the sign hanging over the shop door.",
    "I wait by the roadside for a cart to pass.",
    "I ask a passing traveler for directions.",
    "I watch the crowd go by.",
    "I lean on the railing and look out at the water.",
    "I stop to look at the baker's window.",
    "I nod to the guard standing at the gate.",
    "I cross the street to the other side.",
    "I follow the main road a few more steps.",
]
# A real arrival scores well above this margin (>= +0.135 on the probe set);
# ordinary actions score at or below ~+0.07. Set between the two, biased high:
# a missed shift only costs a slightly tighter description, a false one costs
# a long rambling one.
SCENE_SHIFT_MARGIN = 0.10

_embed_model = None
_example_texts = _SIMPLE_EXAMPLES + _COMPLEX_EXAMPLES
_example_vecs = None  # [0:len(_SIMPLE_EXAMPLES)] are SIMPLE, the rest COMPLEX
_scene_shift_vecs = None
_non_shift_vecs = None


def _get_embed_model():
    global _embed_model, _example_vecs, _scene_shift_vecs, _non_shift_vecs
    if _embed_model is None:
        _embed_model = SentenceTransformer(_EMBED_MODEL_NAME)
        _example_vecs = _embed_model.encode(_example_texts, convert_to_tensor=True)
        _scene_shift_vecs = _embed_model.encode(_SCENE_SHIFT_EXAMPLES, convert_to_tensor=True)
        _non_shift_vecs = _embed_model.encode(_NON_SHIFT_EXAMPLES, convert_to_tensor=True)
    return _embed_model


def looks_like_scene_shift(player_input: str, world: WorldState) -> bool:
    """Cheap embedding check for the fast path only: does this read like
    arriving somewhere new or a dramatic change in physical surroundings?
    Used to set scene_shift on the canned fast-path verdict so arrivals
    still get a fuller description even when they skip the real Referee."""
    model = _get_embed_model()
    vec = model.encode([player_input], convert_to_tensor=True)
    shift_sim = float(util.cos_sim(vec, _scene_shift_vecs)[0].mean())
    ordinary = torch.cat([_example_vecs[:len(_SIMPLE_EXAMPLES)], _non_shift_vecs])
    ordinary_sim = float(util.cos_sim(vec, ordinary)[0].mean())
    return (shift_sim - ordinary_sim) > SCENE_SHIFT_MARGIN


def _unquoted(text: str) -> str:
    """The player's line with quoted speech blanked out: what the character
    says is theirs to decide, so tripwires look only at the narration part."""
    return _QUOTED.sub(" ", text)


def _quoted_parts(text: str) -> list:
    return [m.group(0).strip('"“” ') for m in _QUOTED.finditer(text)]


def _mention_positions(text_lower: str, npc: NPC) -> list:
    """Character offsets where this NPC is named or referred to by an alias
    ("the dwarf") in already lower-cased text."""
    pos = []
    for tok in npc.name_tokens():
        pos += [m.start() for m in re.finditer(rf"\b{re.escape(tok)}\b", text_lower)]
    for alias in npc.aliases:
        a = re.sub(r"^(?:the|a|an)\s+", "", alias.lower().strip())
        if len(a) >= 3:
            pos += [m.start() for m in re.finditer(rf"\b{re.escape(a)}\b", text_lower)]
    return sorted(pos)


def resolve_addressee(player_input: str, world: WorldState):
    """Which NPC present in the scene the player is engaging this turn, or
    None to keep the current one. Deterministic, so the right NPC agent
    answers: in play, a line aimed at Borgar was answered by Grimbold's agent
    because only the active NPC was ever consulted.
    Order: a present NPC named right after an address cue ("ask Grimbold",
    "walk over to Borgar's table"); else the first present NPC named outside
    quotes ("look the dwarf in the eye"); else a name opening a quote
    ("Tallow! ..."). Names inside quoted speech are usually people being
    talked ABOUT, so they don't count."""
    here = [n for n in world.present_npcs() if n.important]
    if not here:
        return None
    outside = _unquoted(player_input).lower()
    hits = [(p, n) for n in here for p in _mention_positions(outside, n)]
    if hits:
        # Negated cues don't count ("I don't answer Vexin yet. I ... ask
        # Grimbold" went to Vexin in play), and of several cued names the
        # LAST is the one actually addressed ("I nod to Grimbold ... and walk
        # over to Borgar's table").
        cue_ends = [m.end() for m in _ADDRESS_CUE.finditer(outside)
                    if not re.search(r"\b(?:don'?t|do not|never|without|won'?t|not)\s+(?:\w+\s+)?$",
                                     outside[max(0, m.start() - 20):m.start()])]
        # "Right after the cue": only small words in between ("ask Grimbold",
        # "say to the dwarf", "walk over to Borgar"), so in "I ask Grimbold
        # about Borgar" only Grimbold is addressed.
        gap_ok = re.compile(r"\s*(?:(?:to|at|with|toward|towards|across from|next to|beside)\s+)?"
                            r"(?:(?:the|a|an|old|my)\s+)?")
        cued = [(p, n) for p, n in hits
                if any(e <= p and gap_ok.fullmatch(outside[e:p]) for e in cue_ends)]
        if cued:
            return max(cued, key=lambda h: h[0])[1].name
        return min(hits, key=lambda h: h[0])[1].name
    # A name spoken TO someone inside the quote: at the start ("Tallow! ...",
    # "Grimbold. A straight answer") or set off by a comma ("I can keep my
    # mouth shut, Vexin." -- in play Grimbold's agent answered that line).
    # "what does your friend Borgar have to do with it" is not vocative.
    # Arriving somewhere and calling out for a known character whose
    # whereabouts are unknown ("I step inside the forge. 'Manfred? ...'")
    # means they are found here: in play Vexin's agent answered that line
    # because Manfred was not yet marked present. The orchestrator places a
    # found NPC with Kael.
    unplaced = [n for n in world.npcs.values() if n.important and not n.location]
    arriving = bool(_MOVEMENT.search(outside))
    for quote in _quoted_parts(player_input):
        q = quote.lower()
        for n in here + (unplaced if arriving else []):
            for t in n.name_tokens():
                if re.search(rf"(?:^|,\s*){re.escape(t)}\s*(?:[,.!?;:]|$)", q):
                    return n.name
    # The NPC we were talking to stayed behind and exactly one named
    # character is here: that's who the player is talking to (in play,
    # Borla's agent never ran at his own smithy because Veyra, back in the
    # tavern, was still the active NPC).
    if not world.is_present(world.npcs.get(world.active_npc)) and len(here) == 1:
        return here[0].name
    return None


def addresses_active_npc(player_input: str, world: WorldState) -> bool:
    """Cheap, deterministic: does this turn name-check or refer to the
    currently active (important) NPC, who must be in the scene? Used to
    decide whether the NPC agent should be consulted, independent of whether
    the Referee gets skipped -- don't rely on the embedding model to know a
    made-up character's name. Speaking aloud with them present counts."""
    active = world.npcs.get(world.active_npc)
    if not (active and active.important and world.is_present(active)):
        return False
    text = player_input.lower()
    if _mention_positions(text, active):
        return True
    # The player turned to someone else ("I turn on my stool to face the man
    # in the black coat"): their speech is for that person, not the active
    # NPC. In play, Grimbold's agent answered a line aimed at a stranger, and
    # the stranger then had no way to reply.
    outside = _unquoted(player_input).lower()
    active_pos = _mention_positions(outside, active)
    for cue in _ADDRESS_CUE.finditer(outside):
        target = outside[cue.end():cue.end() + 40]
        if re.match(r"\s*(?:(?:to|at|towards?)\s+)?(?:the|a|an|that|this|some)\s+[a-z]", target) and not any(
                0 <= p - cue.end() <= 40 for p in active_pos):
            return False
    if _quoted_parts(player_input):
        return True
    words = set(re.findall(r"[a-z']+", text))
    return bool(words & {"him", "her", "them", "he", "she"})


def unknown_names(text: str, world: WorldState) -> set:
    """Capitalised words in the middle of a sentence that appear nowhere in
    the world context: likely a person or place the story has never
    mentioned. Sentence-initial words are skipped (capitalised anyway)."""
    vocab = set(re.findall(r"[A-Za-z]+", world.context_brief())) | {"I", "Kael"}
    found = set()
    for m in re.finditer(r"\b([A-Z][a-z]+)", text):
        word = m.group(1)
        if word in vocab:
            continue
        raw_before = text[:m.start()]
        before = raw_before.rstrip(" \"'*_“”‘’(")
        if not before or before[-1] in ".!?:;…—–-" or re.search(r"[\"“*_(]\s*$", raw_before):
            # Sentence start or first word of a quote: capitalised anyway, so
            # only count it if it isn't an ordinary English word. In play,
            # the scout's name came as 'Last time. Vayne -- or you die' and
            # the tracker never ran.
            if _is_common_word(word):
                continue
        found.add(word)
    return found


def _is_common_word(word: str) -> bool:
    """True if the embedding model's WordPiece vocabulary (~30k lower-case
    English words) has this word whole. Invented names ("Vayne", "Borla",
    "Grimbold") get split into pieces, so they read as not common."""
    tok = _get_embed_model().tokenizer
    return word.lower() in tok.get_vocab()


def looks_simple(player_input: str, world: WorldState) -> bool:
    """True if this turn's CONTENT looks low-risk enough to skip
    judge_action() entirely -- no stakes, no overreach, no info-request
    routing needed. Does not consider whether an NPC is addressed (see
    addresses_active_npc for that). Conservative by design: any ambiguity
    falls through to the real (LLM) judgment, since this only saves time
    and never adds capability."""
    text = player_input.lower().strip()

    #if "?" in text or text.startswith(_QUESTION_STARTERS):
        #return False  # info-requests still need the router call (known_to_dm/worldbuild)

    # Player-authority tripwire (see RULES_SYSTEM PART 3): embeddings alone
    # let some invented world facts through ("it starts to rain", "I can
    # suddenly hear everything") because they read like ordinary scene text.
    # Two cheap, deterministic signals that the player may be narrating the
    # world instead of their own character -- either one forces the real
    # Referee call. Only ever sends MORE turns to the Referee, never fewer.
    if not _FIRST_PERSON.search(text) or _WORLD_FACT_MARKERS.search(text):
        return False
    # Two more tripwires, from a real play session where both slipped through
    # the fast path and came true: someone else is the subject of a clause
    # ("He cracks and tells me everything"), or the line names someone or
    # somewhere the story never mentioned ("my old army friend, Sergeant
    # Hale"). Quoted speech is excluded: what Kael SAYS is his to decide.
    narration_part = _unquoted(player_input)
    if _OTHER_SUBJECT.search(narration_part.lower()) or unknown_names(narration_part, world):
        return False

    model = _get_embed_model()
    vec = model.encode([player_input], convert_to_tensor=True)
    n_simple = len(_SIMPLE_EXAMPLES)
    # Mean similarity to each class, not single-nearest-neighbor -- 1-NN was
    # provably fooled by surface-word overlap (e.g. "I whisper to the
    # merchant that he better hand over the map" matched closest to "I greet
    # the merchant at his stall" purely because both mention "merchant",
    # despite the actual content being a coercive demand). Averaging across
    # each class dilutes any single quirky example and was tested this
    # session to fix that exact miss (11/15 -> 14/15 on a held-out probe set).
    simple_sim = float(util.cos_sim(vec, _example_vecs[:n_simple])[0].mean())
    complex_sim = float(util.cos_sim(vec, _example_vecs[n_simple:])[0].mean())
    margin = simple_sim - complex_sim

    return margin >= CONFIDENCE_THRESHOLD  # ambiguous/negative margin -> ask the real Referee


def judge_action(world: WorldState, player_input: str) -> dict:
    messages = [
        {"role": "system", "content": RULES_SYSTEM},
        {"role": "user", "content": (
            f"WORLD CONTEXT:\n{world.context_brief()}\n\n"
            f"PLAYER DECLARES: {player_input}\n\n"
            "Return the JSON ruling."
        )},
    ]
    # Ollama's JSON-constrained generation intermittently fails mid-stream with
    # an HTTP 500 (seen in the eval harness: ~1 in 30 Referee calls, after
    # ~100 tokens). Retry once, then fall through to the safe fallback verdict
    # below instead of crashing the turn.
    content = ""
    for attempt in range(2):
        try:
            content, _ = chat(messages, options=RULES_OPTIONS, json_format=True)
            break
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
            content = f"<request failed after {attempt + 1} attempt(s): {e}>"
    try:
        verdict = json.loads(content)
        assert verdict.get("outcome") in {"success", "partial", "complication", "failure"}
        assert verdict.get("turn_type") in {"info_request", "dialogue", "action"}
        verdict.setdefault("player_assertion", "")
        verdict.setdefault("not_true", "")
        if not verdict["player_assertion"]:
            verdict["not_true"] = ""
        if verdict["player_assertion"]:
            # The Referee sometimes smuggles the invented fact back in via the
            # twist ("a hooded figure lingers near the bar"). The DM decides
            # what happens next on its own; the twist must not carry it.
            verdict["twist"] = ""
    except Exception:
        # Fallback degrades to the old always-safe behavior: treat as a
        # plain action (never skips judgment) and only involve the NPC if
        # today's blunt "important NPC is active" check would have.
        active = world.npcs.get(world.active_npc)
        verdict = {
            "turn_type": "action",
            "known_to_dm": False,
            "addresses_npc": bool(active and active.important),
            "scene_shift": False,
            "player_assertion": "",
            "not_true": "",
            "outcome": "complication",
            "twist": "",
            "rationale": f"fallback: unparsable referee output: {content!r}",
        }
    return verdict


_WORLD_CLAIM_SYSTEM = """You check ONE thing about a player's message in a tabletop roleplaying game. The player controls ONLY their own character: what that character attempts, says, thinks, or perceives with ordinary senses. A message is a WORLD CLAIM if it states, as already true, something outside that: the weather or surroundings changing, people or creatures arriving, acting, or reacting, events happening, objects appearing, or the character gaining a power, sense, immunity, or item. Attempts ("I try to listen", "I draw my sword") and plain commands ("Open the door.") are NOT world claims.

Reply with exactly three lines and nothing else:
CLAIM: YES or NO
WHAT: <the claim in under 10 words, or none>
NOT_TRUE: <one short lower-case clause saying what did not happen, or none>

Examples:
Message: It starts to rain heavily outside.
CLAIM: YES
WHAT: it starts to rain heavily
NOT_TRUE: it is not raining

Message: A stranger walks in and sits next to me.
CLAIM: YES
WHAT: a stranger walks in and sits down
NOT_TRUE: nobody came in

Message: I can suddenly hear every conversation in town.
CLAIM: YES
WHAT: hearing every conversation in town
NOT_TRUE: your character cannot hear beyond normal range

Message: Open the door.
CLAIM: NO
WHAT: none
NOT_TRUE: none

Message: I try to hear what they are whispering.
CLAIM: NO
WHAT: none
NOT_TRUE: none

Message: I ask Grimbold about the mill.
CLAIM: NO
WHAT: none
NOT_TRUE: none
"""


def suspects_world_fact(player_input: str) -> bool:
    """Same cheap signals as the looks_simple() tripwire: no first-person
    subject (reads like a statement about the world) or a 'suddenly / storms
    in' style marker. Used to decide when a second, narrower look is worth
    its extra call."""
    text = player_input.lower().strip()
    return not _FIRST_PERSON.search(text) or bool(_WORLD_FACT_MARKERS.search(text))


def check_world_claim(player_input: str):
    """Focused second opinion for inputs that suspects_world_fact() flags but
    the big Referee call left unflagged (it missed 'it starts to rain' in
    3 of 9 eval runs: the flag was one field among many). One narrow yes/no
    question is much easier for the 8B model. Returns
    {"assertion", "not_true"} if it is a world claim, else None. Any failure
    returns None, i.e. falls back to the Referee's own verdict."""
    messages = [
        {"role": "system", "content": _WORLD_CLAIM_SYSTEM},
        {"role": "user", "content": f"Message: {player_input}"},
    ]
    try:
        content, _ = chat(messages, options={"temperature": 0})
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
        return None
    claim = re.search(r"CLAIM:\s*(YES|NO)", content, re.IGNORECASE)
    if not claim or claim.group(1).upper() != "YES":
        return None
    what = re.search(r"WHAT:\s*(.+)", content)
    not_true = re.search(r"NOT_TRUE:\s*(.+)", content)
    clean = lambda m: (m.group(1).strip().rstrip(".") if m else "")
    what, not_true = clean(what), clean(not_true)
    if what.lower() in ("", "none"):
        what = player_input.strip().rstrip(".")
    if not_true.lower() == "none":
        not_true = ""
    return {"assertion": what, "not_true": not_true}


_CLAIM_STOPWORDS = {"that", "with", "about", "your", "character", "player", "kael",
                    "they", "there", "have", "will", "what", "this", "into", "from",
                    "were", "been", "being", "them", "their", "claims", "claimed"}


def claim_is_only_speech(player_input: str, assertion: str) -> bool:
    """True when the flagged 'invented fact' only exists inside the player's
    quoted speech, i.e. it is something Kael SAID (a lie, a bluff). Those are
    the player's to choose: in play, 'I bluff: "I rode in with the captain of
    the border patrol"' was flagged 3/3 even with a prompt rule. Compares
    word stems of the Referee's phrase against the quoted and unquoted parts
    of the line; any hit outside the quotes keeps the flag."""
    quoted = " ".join(_quoted_parts(player_input)).lower()
    if not quoted or not assertion:
        return False
    outside = _unquoted(player_input).lower()
    stems = {w[:5] for w in re.findall(r"[a-z]+", assertion.lower())
             if len(w) >= 4 and w not in _CLAIM_STOPWORDS}
    in_quotes = {s for s in stems if s in quoted}
    in_narration = {s for s in stems if s in outside}
    return len(in_quotes) >= 2 and not in_narration


# --- Keeping refused claims out of the story ----------------------------
# Even with the PLAYER OVERSTEP block, the DM sometimes narrated the refused
# claim as true ("The rain falls in sheets..."), roughly 1 in 10-25 invented
# turns by the judge -- and the judge itself passed several more ("the rain
# remains steady outside", "Then the first armed man screams"). Two causes,
# two fixes: the DM was shown the claim verbatim in the PLAYER line (it
# continued it), and nothing checked the output. Calibrated on all saved
# eval narrations: the offending sentence is nearly always the one most
# similar to the claim (sentence-embedding cosine >= ~0.40; the median for a
# narration's closest sentence on good turns is 0.22).
CLAIM_SENTENCE_SIM = 0.40   # narration/NPC sentences at or above this are dropped
CLAIM_FRAGMENT_SIM = 0.50   # player-line fragments at or above this are removed
_FIRST_PERSON_START = re.compile(r"^(?:[\w'’-]+\s+){0,3}(?:i|i'm|i've|i'll|i'd|my)\b", re.IGNORECASE)
_OTHER_START = re.compile(r"^(?:he|she|they|it|who|which|that|someone|somebody|everyone|everybody|"
                          r"nobody|there)\b", re.IGNORECASE)
# Only "while": "As I walk toward the pit, ..." is a real action (probe case).
_SUBORDINATE_START = re.compile(r"^while\b", re.IGNORECASE)
REFUSED_FALLBACK_LINE = "Everything around you carries on exactly as before."


def _claim_similarity(assertion: str):
    """Returns sim(text) -> cosine similarity of text to the refused claim."""
    model = _get_embed_model()
    claim_vec = model.encode([assertion], convert_to_tensor=True)
    return lambda text: float(util.cos_sim(claim_vec, model.encode([text], convert_to_tensor=True))[0][0])


def strip_claim(player_input: str, assertion: str) -> str:
    """The player's line with the refused claim taken out, for the DM and
    the NPC agent: only the character's own first-person attempts (and what
    they say in quotes) are kept, minus fragments close to the claim.
    "Three armed men storm in. I draw my sword and ... intimidate all three"
    -> "I draw my sword." ; "It starts to rain heavily outside." -> ""."""
    sim = _claim_similarity(assertion)
    keep = []
    for frag in re.split(r"[.!?;]+\s*|,\s*(?:and\s+|so\s+|then\s+|but\s+)?|\s+(?:and|so|then|but)\s+",
                         _unquoted(player_input)):
        frag = frag.strip(" ,:")
        if len(frag.split()) < 2 or _OTHER_START.match(frag) or not _FIRST_PERSON_START.search(frag):
            continue  # someone or something else is the subject: not the player's to decide
        if _SUBORDINATE_START.match(frag):
            continue  # "While I was talking to Grimbold" sets the time, it isn't an action
        if sim(frag) >= CLAIM_FRAGMENT_SIM:
            continue
        keep.append(frag[0].upper() + frag[1:] + ".")
    keep += [f'"{q}"' for q in _quoted_parts(player_input) if q]
    return " ".join(keep)


def drop_claim_sentences(text: str, assertion: str) -> str:
    """Remove the sentences of an NPC line that echo the refused claim (an
    NPC muttering about 'the storm' made a refused rain claim half-true)."""
    sim = _claim_similarity(assertion)
    parts = re.findall(r'.+?(?:[.!?…]+["”’]?(?=\s|$)|$)', text, re.S)
    return " ".join(p.strip() for p in parts if p.strip() and sim(p) < CLAIM_SENTENCE_SIM).strip()


def correction_note(verdict: dict) -> str:
    """The out-of-character explanation shown to the player BEFORE the
    narration when their claim about the world was not accepted. Built in
    code, not by the narrating model: the 8B model is unreliable at keeping
    out-of-character text separate from the story."""
    if not verdict.get("player_assertion"):
        return ""
    reason = verdict.get("not_true") or (
        f'the claim that "{verdict["player_assertion"]}" did not happen')
    return (f"Sorry, but in this case {reason}. Only the DM decides what "
            "happens in the world, so here is what actually happens instead:")


def refusal_question(verdict: dict, action: str) -> str:
    """What the DM says instead of narrating when a claim was refused: what
    did not happen, then -- if the line also had the character's own action
    -- whether to still do it. Nothing is narrated on that turn, so the
    refused claim can't leak into the story at all."""
    reason = verdict.get("not_true") or f'"{verdict["player_assertion"]}" did not happen'
    reason = re.sub(r"^([^A-Za-z]*)([a-z])", lambda m: m.group(1) + m.group(2).upper(),
                    reason.strip().rstrip("."))
    text = f"{reason}. Only the DM decides what happens in the world."
    if not action:
        return f"{text} What does Kael do?"
    return (f"{text} Do you still want Kael to do this? {action}\n"
            "(Type yes to go ahead, or write what Kael does instead.)")


def refusal_stays_in_world(player_input: str, verdict: dict, world: WorldState, action: str) -> bool:
    """True when a refused claim is better answered inside the story than
    with a question: the claim is about how a character who is HERE reacts
    ("Grimbold trusts me completely and tells me everything"), or the line
    is aimed at a present NPC and nothing of Kael's own action is left to
    ask about ("I tell Grimbold everyone obeys me, so he hands over the
    key"). Then the NPC refuses in character, as before. Found in the eval:
    asking turned the bribe/grab/obey overreaches into out-of-character
    questions and lost Grimbold's in-world pushback."""
    claim = verdict.get("player_assertion", "").lower()
    for npc in world.present_npcs():
        names = npc.name_tokens() | {a.lower() for a in npc.aliases}
        if any(re.search(rf"\b{re.escape(n)}\b", claim) for n in names):
            return True
    # Kael TELLING the NPC the claim (reported speech) -- not just a mention
    # ("While I was talking to Grimbold, someone entered" must still ask).
    told = re.search(r"\bi\s+(?:tell|inform|assure|warn|promise|remind|say to)\b",
                     _unquoted(player_input).lower())
    return not action and bool(told) and addresses_active_npc(player_input, world)


_YES_WORDS = {"y", "yes", "yeah", "yep", "yup", "sure", "ok", "okay", "continue", "go",
              "ahead", "proceed", "do", "it", "still", "please", "keep", "going", "on", "fine"}
_NO_WORDS = {"n", "no", "nope", "nah", "cancel", "never", "mind", "nevermind", "forget", "skip"}


def confirm_reply(player_input: str) -> str:
    """'yes' / 'no' when the whole line is just a confirmation or refusal
    ("yes", "go ahead", "no, never mind"), else '' -- anything longer is the
    player rephrasing, which is played as a new action."""
    words = re.findall(r"[a-z]+", player_input.lower())
    if not words or len(words) > 5:
        return ""
    if set(words) <= _YES_WORDS:
        return "yes"
    if set(words) <= _NO_WORDS | {"thanks", "thank", "you"}:
        return "no"
    return ""


def npc_view_of_turn(player_input: str, verdict: dict) -> str:
    """What the NPC agent is given as the player's line. On a flagged or
    contested turn the raw line alone made the NPC comply: in play, "She
    can't resist the money, so she tells me the safe way in" was flagged by
    the Referee, and Veyra's agent then told everything anyway while the DM
    narrated her refusing. So add the ruling. This annotated line is also
    what lands in the NPC's own thread, closing the old leak where a refused
    claim stayed in that thread as if it were true."""
    notes = []
    if verdict.get("player_assertion"):
        notes.append(f'The player claimed "{verdict["player_assertion"]}". That is NOT '
                     "true: you decide your own reaction, and you do not have to do it.")
    if verdict.get("outcome") in ("partial", "complication", "failure"):
        notes.append(f"The referee ruled this attempt a {verdict['outcome']}: do not "
                     "simply give Kael what he wants.")
    if not notes:
        return player_input
    return f"{player_input}\n(Out of character, for you only: {' '.join(notes)})"


def npc_reply(npc: NPC, world: WorldState, player_line: str) -> str:
    # NPCs used to see only their own thread, so a newly met NPC knew nothing
    # of the scene. Give them where they are, who is around, and the last two
    # exchanges (trimmed) -- enough to answer in context without the cost of
    # the full world brief.
    others = [n.name for n in world.present_npcs() if n.name != npc.name]
    recent = "\n".join(
        f"  Player: {p}\n  DM: {d[:400]}" for p, d in world.recent_history[-2:]
    ) or "  (nothing yet)"
    # Without this, each NPC agent guessed about the others: Grimbold's agent
    # named "Old Man Harlow", then Veyra's and Borla's agents called Harlow
    # "she". Capped and trimmed to keep the prompt (and the call) short.
    people = "\n".join(
        f"  - {n.name}: {n.persona[:120]}" for n in list(world.npcs.values())[:8]
        if n.name != npc.name
    ) or "  (none yet)"
    system = NPC_SYSTEM_TEMPLATE.format(
        name=npc.name,
        persona=npc.persona,
        location=world.location or "unknown",
        others=", ".join(["Kael"] + others),
        people=people,
        known_facts="; ".join(npc.known_facts) if npc.known_facts else "none yet",
        recent=recent,
    )
    messages = [{"role": "system", "content": system}] + npc.thread + [
        {"role": "user", "content": player_line}
    ]
    content, _ = chat(messages, options=NPC_OPTIONS)
    npc.thread.append({"role": "user", "content": player_line})
    npc.thread.append({"role": "assistant", "content": content})
    npc.thread[:] = npc.thread[-12:]
    return content


# Word budgets the narration is held to in code (same numbers the eval's
# length check uses). The prompt asks for less; these only catch overruns.
NARRATION_BUDGET_TIGHT = 110
NARRATION_BUDGET_FULL = 170
# On turns where an NPC agent spoke, drop narration sentences that contain
# quoted speech: the prompt alone did not stop the DM re-voicing the NPC
# (and adding facts they never said). See CLAUDE.md.
DROP_SPEECH_ON_NPC_TURNS = True
_META_SENTENCE = re.compile(r"\bNEXT\s*:|\byour move\b|\bout of character\b|\bOOC\b",
                            re.IGNORECASE)
_SENTENCE_END = re.compile(r"[.!?…][\"”’')\]]*\s$")


class NarrationFilter:
    """Sits between the DM model's token stream and the player, one sentence
    at a time (quoted speech is never split). Each finished sentence is
    either shown or dropped:
    - asterisks (markdown emphasis) are removed;
    - parenthetical asides to the player ("(NEXT: ... Your move.)") are dropped;
    - with drop_speech, sentences containing quoted speech are dropped;
    - once the next sentence would take the narration past budget_words, it
      stops and feed() returns True, which makes ollama_client stop the
      model. The narration therefore always ends on a whole sentence.
    The 8B model ignores these rules often enough in the prompt alone (see
    CLAUDE.md); doing them in code makes them hold every time."""

    def __init__(self, emit=None, budget_words=NARRATION_BUDGET_TIGHT, drop_speech=False,
                 reject=None, fallback=None):
        self.emit = emit or (lambda s: None)
        self.budget = budget_words
        self.drop_speech = drop_speech
        # reject(sentence) -> True drops it for good (never used as the
        # fallback either): on refused-claim turns, sentences echoing the claim.
        self.reject, self.fallback, self.rejected = reject, fallback, []
        self.buf, self.kept, self.dropped = "", [], []
        self.words, self.stopped, self.in_quote, self.in_aside = 0, False, False, False

    def feed(self, piece: str) -> bool:
        if self.stopped:
            return True
        for ch in piece.replace("*", ""):
            self.buf += ch
            if ch == "“":
                self.in_quote = True
            elif ch == "”":
                self.in_quote = False
            elif ch == '"':
                self.in_quote = not self.in_quote
            elif ch.isspace() and not self.in_quote and _SENTENCE_END.search(self.buf):
                self._sentence(self.buf)
                self.buf = ""
                if self.stopped:
                    return True
        return False

    def _sentence(self, raw: str):
        text = raw.strip()
        if not text:
            return
        opens = text.startswith(("(", "["))
        if self.in_aside or opens or _META_SENTENCE.search(text):
            self.in_aside = (self.in_aside or opens) and not (")" in text or "]" in text)
            self.dropped.append(text)
            return
        if self.reject and self.reject(text):
            self.rejected.append(text)
            return
        if self.drop_speech and re.search(r'["“”]', text):
            self.dropped.append(text)
            return
        n = len(text.split())
        if self.kept and self.words + n > self.budget:
            self.stopped = True
            self.dropped.append(text)
            return
        out = raw if self.kept else raw.lstrip()
        self.kept.append(out)
        self.words += n
        self.emit(out)

    def finish(self) -> str:
        tail = self.buf.strip()
        if tail and not self.stopped:
            if self.kept and not re.search(r"[.!?…][\"”’')\]]*$", tail):
                # The model's own output ended mid-sentence (seen once in an
                # eval: "...The cobbled alleyway stretches black and"). Never
                # show a broken sentence when whole ones were already shown.
                self.dropped.append(tail)
            else:
                self._sentence(self.buf + " ")
        self.buf = ""
        if not self.kept:
            # Everything was dropped (e.g. all speech): show the first
            # sentence anyway rather than an empty narration -- but never a
            # rejected one; then the fallback line, if given.
            first = next((d for d in self.dropped if not d.startswith(("(", "["))), None)
            first = first or self.fallback
            if first:
                self.kept.append(first)
                self.emit(first)
        return "".join(self.kept).strip()


def narrate(world: WorldState, player_input: str, verdict: dict,
            npc_line: str = None, new_lore: str = None, stream_cb=None,
            npc_name: str = None) -> str:
    pacing = "FULL SCENE" if verdict.get("scene_shift") else "TIGHT"
    ruling_block = (
        f"RULING (do not contradict): outcome={verdict.get('outcome')}; "
        f"twist_to_weave_in={verdict.get('twist') or 'none'}; pacing={pacing}"
    )
    assertion = verdict.get("player_assertion")
    npc_block = ""
    if npc_line:
        # The orchestrator shows this line to the player before the narration
        # (on_npc_line). Until that existed, play.py only printed it in
        # verbose mode, so the DM was told the player had read a line they
        # never saw -- and NPC answers silently vanished.
        npc_block = (
            f"\n{npc_name or world.active_npc} just said, in character: \"{npc_line}\"\n"
            "The player has already read this line. Continue the scene from it."
        )
    lore_block = ""
    if new_lore:
        lore_block = f"\nNEWLY ESTABLISHED LORE (reference material, weave in once): {new_lore}\n"
    # Placed LAST in the user message on purpose: the system-prompt CONCISION
    # rule alone was ignored on ordinary turns (130-290 words observed); a
    # constraint right next to the player's input is followed much more closely.
    if assertion:
        # Player tried to author a world fact (RULES_SYSTEM PART 3). Placed
        # last and forced tight: in testing the DM honored this far more
        # often when it was the final instruction, and long narration is
        # where it let the invented fact quietly come true.
        length_block = (
            f"PLAYER OVERSTEP: the player claimed \"{assertion}\". That is "
            "FALSE and did NOT happen"
            + (f" (the truth: {verdict['not_true']})" if verdict.get("not_true") else "")
            + ": nobody arrives, nothing changes in "
            "the world, and the character gains no ability, sense, or "
            "power. Narrate how the world and the NPCs respond, with "
            "everything staying exactly as it was; never write that the "
            "claim came true, not even partly. Stay fully in the story: no notes, "
            "reminders, parentheses, or talk of rules or the player. "
            "LENGTH: HARD LIMIT of 3 sentences, under 70 words."
        )
    elif verdict.get("scene_shift") or new_lore:
        length_block = (
            "LENGTH: this introduces something new, so you may describe it "
            "more fully -- HARD LIMIT of 5 sentences in total, under 120 "
            "words, in one or two short paragraphs. Pick the two or three "
            "most striking details instead of listing everything. Describe "
            "only what is new; do not repeat earlier details unless the "
            "player explicitly asked you to describe something again."
        )
    else:
        length_block = (
            "LENGTH: HARD LIMIT of 3 sentences, under 70 words. Nothing new "
            "is being introduced, so do NOT re-describe the room, weather, or "
            "anyone's appearance (unless the player explicitly asked you to "
            "describe or recap something again). Cover only what changed "
            "because of the player's action, then stop."
        )
    if npc_line:
        speaker = npc_name or world.active_npc
        length_block += (
            " The NPC's line was already shown to the player: do not quote "
            "or repeat it, narrate only reactions and what happens next. "
            f"{speaker} has already spoken this turn, so this narration has NO "
            "quoted speech at all -- no quotation marks, from anyone. Describe "
            f"only actions and reactions, and never change or add to what "
            f"{speaker} said (names, places, directions, prices)."
        )
    # The Referee's twist sat mid-message and was often ignored: in play the
    # Referee ruled a hidden note "blank except for a hound's paw print" and
    # the narration never said what the note showed. End placement, like
    # LENGTH. (judge_action already clears the twist on overstep turns.)
    if verdict.get("twist") and not assertion:
        length_block += (
            f" MUST HAPPEN THIS TURN, in your own words: {verdict['twist']}"
            f"{'' if str(verdict['twist']).rstrip().endswith('.') else '.'}"
        )
    # Direct questions were answered with mood instead of information in a
    # real play session (a note the player read came back as riddles; it took
    # four questions to get a job lead). Placed at the end, like LENGTH.
    if not assertion:
        if verdict.get("turn_type") == "info_request":
            length_block += (
                " ANSWER FIRST: the PLAYER line above (this turn, not an "
                "earlier one) asks for information or a description. Your "
                "first sentence must give exactly what THAT line asks for, "
                "plainly -- what it says, a name, a place, a price, who someone "
                "is, what the place looks like. If they are reading something "
                "written, quote its words. Mood comes after the answer, never "
                "instead of it."
            )
        elif not npc_line and any("?" in q for q in _quoted_parts(player_input)):
            length_block += (
                " REPLY: the player asked someone a question out loud. The "
                "person asked must answer in words in this narration -- a real "
                "answer, or a clear refusal or a price, never only a look or "
                "a silence."
            )
    # Every turn: the player's own voice belongs to the player. The eval
    # harness (no_puppeting) caught the DM writing quoted lines for the
    # player's character -- worst on overreach / invented-fact turns, where
    # "narrate the character's attempt" got read as "voice it".
    length_block += (
        " PLAYER'S VOICE: never write words for the player's character -- no "
        "quoted speech from them or from 'you', and no thoughts, feelings, "
        "instincts or decisions (not 'your neck prickles', not 'you sense "
        "danger'). The player already said what they say. Narrate only how "
        "the world and the NPCs respond: what can be seen, heard and smelled."
        " TONE: grounded and ordinary -- no magic or uncanny details unless "
        "already established. Plain text, no asterisks."
    )
    if assertion:
        # Never show the DM the refused claim as the player's line: it tended
        # to continue it. Only the character's own attempt is passed on.
        kept = strip_claim(player_input, assertion)
        player_block = ("PLAYER (the invented part of their message has been removed -- "
                        "see PLAYER OVERSTEP below): "
                        + (kept or "(nothing else: they only declared the claim, which did not happen)"))
    else:
        player_block = f"PLAYER: {player_input}"
    user_content = (
        f"WORLD CONTEXT:\n{world.context_brief()}\n\n{ruling_block}{npc_block}{lore_block}\n\n"
        f"{player_block}\n\n{length_block}"
    )
    messages = [
        {"role": "system", "content": DM_SYSTEM},
        {"role": "user", "content": user_content},
    ]
    full = bool(verdict.get("scene_shift") or new_lore
                or verdict.get("turn_type") == "info_request") and not assertion
    claim_sim = _claim_similarity(assertion) if assertion else None
    narration = NarrationFilter(
        emit=stream_cb,
        budget_words=NARRATION_BUDGET_FULL if full else NARRATION_BUDGET_TIGHT,
        drop_speech=bool(npc_line) and DROP_SPEECH_ON_NPC_TURNS,
        reject=(lambda s: claim_sim(s) >= CLAIM_SENTENCE_SIM) if assertion else None,
        fallback=REFUSED_FALLBACK_LINE if assertion else None,
    )
    # Always streamed internally, so the filter can stop the model early.
    chat(messages, options=DM_OPTIONS, stream=True, on_token=narration.feed)
    text = narration.finish()
    verdict["narration_dropped"] = narration.dropped  # for debugging / eval reports
    verdict["narration_rejected"] = narration.rejected
    return text


def scene_may_have_changed(player_input: str, verdict: dict, npc_line: str,
                           narration: str, world: WorldState) -> bool:
    """Cheap gate for track_scene(): only spend the extra call when the turn
    may have moved Kael or brought in a named character."""
    return bool(
        player_may_move(player_input, verdict)
        or unknown_names(f"{npc_line or ''}\n{narration}", world)
    )


def track_scene(world: WorldState, player_input: str, narration: str,
                npc_line: str = None, npc_name: str = None):
    """Bookkeeping call after the narration: where is Kael now, and which
    named characters appeared? Nothing else in the game ever updated the
    location or added an NPC, so in play Kael stayed "in the tavern" after
    leaving it, and Grimbold's agent ended up voicing everyone. Returns the
    parsed JSON, or None on any failure (the world then simply stays as is)."""
    known = "\n".join(
        f"  - {n.name} (at: {n.location or 'unknown'})" for n in world.npcs.values()
    ) or "  (none)"
    places = "\n".join(f"  - {p}" for p in world.known_places()) or "  (none)"
    user = (
        f"CURRENT LOCATION: {world.location}\nKNOWN PLACES:\n{places}\n"
        f"KNOWN CHARACTERS:\n{known}\n\nPLAYER: {player_input}\n"
        + (f"NPC LINE ({npc_name}): {npc_line}\n" if npc_line else "")
        + f"NARRATION: {narration}\n\nReturn the JSON."
    )
    messages = [{"role": "system", "content": TRACKER_SYSTEM},
                {"role": "user", "content": user}]
    try:
        content, _ = chat(messages, options={"temperature": 0}, json_format=True)
        data = json.loads(content)
    except Exception:
        return None
    return data if isinstance(data, dict) else None


# Capitalised words that don't make something a name ("The hooded figure"
# was registered as a character in play).
_NOT_NAME_WORDS = {"The", "This", "That", "These", "Those", "Some", "His", "Her",
                   "Their", "Our", "Your", "Old", "Young", "Big", "Little", "Man",
                   "Woman", "Lady", "Sir", "Mister", "Master"}


def _place_key(name: str) -> str:
    return " ".join(re.findall(r"[a-z]+", name.lower()))


def player_may_move(player_input: str, verdict: dict) -> bool:
    """A location change is only accepted when the PLAYER's line has a
    movement word or the Referee flagged a scene change: in play, the tracker
    moved Kael to "the stables" because the narration mentioned them while
    he was just finishing his ale."""
    return bool(verdict.get("scene_shift") or _MOVEMENT.search(_unquoted(player_input).lower()))


def apply_scene_update(world: WorldState, update: dict, exclude_from: str = "",
                       source_text: str = "", allow_move: bool = True) -> dict:
    """Apply track_scene()'s output to the world. exclude_from: text whose
    words must not become new characters (the player's line on a turn where
    they tried to invent someone). source_text: the NPC line + narration; a
    NEW character's name must appear there capitalised, which filters out
    unnamed people the tracker sometimes lists ("overwatch guards"). Only
    ADDS presence: an NPC stops being present when Kael moves away, not
    because the tracker forgot them."""
    changes = {"moved_to": None, "added": []}
    old_location = world.location
    if update.get("moved") is True and allow_move:
        loc = str(update.get("location") or "").strip()
        cur = _place_key(world.location)
        new = _place_key(loc)
        # A spot nested inside the current place ("<current> -- pit's mouth")
        # is not a move: it would strand the NPCs who are here.
        if loc and new != cur and not new.startswith(cur):
            loc = next((p for p in world.known_places() if _place_key(p) == new), loc)
            world.move_to(loc)
            changes["moved_to"] = loc
    excluded = set(re.findall(r"[a-z]+", exclude_from.lower()))
    for c in update.get("characters") or []:
        if not isinstance(c, dict):
            continue
        name = str(c.get("name") or "").strip()
        tokens = {t for t in re.findall(r"[a-z]+", name.lower()) if len(t) >= 3}
        if not tokens or tokens & {"kael", "you"}:
            continue
        present = c.get("present") is True
        npc = world.find_npc(name)
        if npc is None:
            if tokens & excluded:
                continue
            capitalised = [w for w in re.findall(r"[A-Za-z]+", name)
                           if w[0].isupper() and len(w) >= 3 and w not in _NOT_NAME_WORDS]
            if not capitalised or (source_text and not any(
                    re.search(rf"\b{w}\b", source_text) for w in capitalised)):
                continue
            aliases = [a.lower().strip() for a in (c.get("aliases") or [])
                       if isinstance(a, str) and a.strip()][:3]
            world.add_npc(NPC(
                name=name, important=True,
                persona=str(c.get("persona") or "").strip() or "Someone Kael has met.",
                location=world.location if present else "", aliases=aliases,
            ))
            changes["added"].append(name)
        elif present and (npc.location == "" or
                          (changes["moved_to"] and npc.location == old_location)):
            # Only someone with unknown whereabouts, or a companion who was
            # with Kael and came along, becomes present. An NPC known to be
            # somewhere else stays there: in play, "Borla's torchlight" in
            # the narration made the tracker put Borla on the road.
            npc.location = world.location
    return changes


def bring_companions(world: WorldState, player_input: str, old_location: str) -> list:
    """After a move, NPCs the PLAYER says they go with come along ("I follow
    him out", "with Vexin", "Vexin and I"). The player's own words beat the
    tracker here: in play it left Vexin in the tavern 3/3 times although Kael
    had just said "I follow him out". Pronouns mean the active NPC."""
    text = _unquoted(player_input).lower()
    moved = []
    for npc in world.npcs.values():
        if npc.location != old_location or not npc.important:
            continue
        refs = [re.escape(t) for t in npc.name_tokens()] + [
            re.escape(re.sub(r"^(?:the|a|an)\s+", "", a.lower())) for a in npc.aliases]
        if npc.name == world.active_npc:
            refs += ["him", "her", "them"]
        if not refs:
            continue
        ref = "(?:" + "|".join(refs) + ")"
        if re.search(rf"\b(?:follow(?:s|ing)?|with|alongside|accompan\w+)\s+(?:the\s+)?{ref}\b", text) \
                or re.search(rf"\b{ref}\s+and\s+i\b|\bi\s+and\s+{ref}\b", text):
            npc.location = world.location
            moved.append(npc.name)
    return moved


def worldbuild(world: WorldState, prompt: str) -> str:
    messages = [
        {"role": "system", "content": WORLDBUILD_SYSTEM},
        {"role": "user", "content": (
            f"ESTABLISHED FACTS:\n{world.context_brief()}\n\nINVENT: {prompt}"
        )},
    ]
    content, _ = chat(messages, options=WORLDBUILD_OPTIONS)
    return content

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
  currently active NPC this specific turn -- not just because an NPC \
  happens to be present in the scene.
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
falls asleep". Weather, noise, light, and any change to the surroundings \
are the DM's to decide, never the player's. Also, never copy the asserted \
fact into "twist" -- the twist must not make the invented fact true. NOT \
invented facts: "I draw my sword", "I shout at the \
guard", "I try to hear what they're whispering". Exceptions, leave \
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
   recent history you are given. Never contradict them.
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
   knowledge. Do not quote or recite it like a document.
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
   such a fact (e.g. "it starts to rain", "someone walks in").
"""

NPC_SYSTEM_TEMPLATE = """You are role-playing a single NPC named {name} in a \
homebrew RPG. Persona: {persona}

Facts you have already told the player, and must stay consistent with: \
{known_facts}

Rules:
- Speak and act ONLY as {name}. 1-3 sentences: dialogue plus minimal \
  physical beats. Never narrate the wider scene, other characters, or the \
  player character.
- You have your own goals and will. Do not comply, trust, or over-share \
  just because the player is confident or persuasive -- react the way this \
  specific character actually would.
- React only to what the player's character actually says or does in front \
  of you. If the player claims something happened in the world (someone \
  arrived, an event occurred) or tells you what you feel or decide, you \
  have not perceived it: do not play along.
- Do not break character or mention being an AI.
"""

WORLDBUILD_SYSTEM = """You are a worldbuilding assistant for a homebrew \
fantasy RPG campaign. Given a short request and the facts already \
established, write 100-180 words of new lore that fits seamlessly with \
what exists and does not contradict it. Write it as reference material for \
the DM (plain description), not as story prose read aloud to players.
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
    r"starts? to (rain|snow)|i can now|i now (have|can|am))\b"
)
_QUESTION_STARTERS = ("what", "who", "where", "when", "why", "how", "tell me", "recap")
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


def addresses_active_npc(player_input: str, world: WorldState) -> bool:
    """Cheap, deterministic: does this turn name-check or refer to the
    currently active (important) NPC? Used to decide whether the NPC agent
    should be consulted, independent of whether the Referee gets skipped --
    don't rely on the embedding model to know a made-up character's name."""
    active = world.npcs.get(world.active_npc)
    if not (active and active.important):
        return False
    words = set(re.findall(r"[a-z']+", player_input.lower()))
    first_name = active.name.split()[0].lower()
    return bool(first_name in words or words & {"him", "her", "them", "he", "she"})


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


def npc_reply(npc: NPC, world: WorldState, player_line: str) -> str:
    system = NPC_SYSTEM_TEMPLATE.format(
        name=npc.name,
        persona=npc.persona,
        known_facts="; ".join(npc.known_facts) if npc.known_facts else "none yet",
    )
    messages = [{"role": "system", "content": system}] + npc.thread + [
        {"role": "user", "content": player_line}
    ]
    content, _ = chat(messages, options=NPC_OPTIONS)
    npc.thread.append({"role": "user", "content": player_line})
    npc.thread.append({"role": "assistant", "content": content})
    npc.thread[:] = npc.thread[-12:]
    return content


def narrate(world: WorldState, player_input: str, verdict: dict,
            npc_line: str = None, new_lore: str = None, stream_cb=None) -> str:
    pacing = "FULL SCENE" if verdict.get("scene_shift") else "TIGHT"
    ruling_block = (
        f"RULING (do not contradict): outcome={verdict.get('outcome')}; "
        f"twist_to_weave_in={verdict.get('twist') or 'none'}; pacing={pacing}"
    )
    assertion = verdict.get("player_assertion")
    npc_block = ""
    if npc_line:
        npc_block = (
            f"\n{world.active_npc} just said, in character: \"{npc_line}\"\n"
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
        length_block += (
            " The NPC's line was already shown to the player: do not quote "
            "or repeat it, narrate only reactions and what happens next."
        )
    # Every turn: the player's own voice belongs to the player. The eval
    # harness (no_puppeting) caught the DM writing quoted lines for the
    # player's character -- worst on overreach / invented-fact turns, where
    # "narrate the character's attempt" got read as "voice it".
    length_block += (
        " PLAYER'S VOICE: never write words for the player's character -- no "
        "quoted speech from them or from 'you', and no thoughts, feelings, or "
        "decisions. The player already said what they say. Narrate only how "
        "the world and the NPCs respond."
    )
    user_content = (
        f"WORLD CONTEXT:\n{world.context_brief()}\n\n{ruling_block}{npc_block}{lore_block}\n\n"
        f"PLAYER: {player_input}\n\n{length_block}"
    )
    messages = [
        {"role": "system", "content": DM_SYSTEM},
        {"role": "user", "content": user_content},
    ]
    content, _ = chat(
        messages, options=DM_OPTIONS,
        stream=stream_cb is not None, on_token=stream_cb,
    )
    return content


def worldbuild(world: WorldState, prompt: str) -> str:
    messages = [
        {"role": "system", "content": WORLDBUILD_SYSTEM},
        {"role": "user", "content": (
            f"ESTABLISHED FACTS:\n{world.context_brief()}\n\nINVENT: {prompt}"
        )},
    ]
    content, _ = chat(messages, options=WORLDBUILD_OPTIONS)
    return content

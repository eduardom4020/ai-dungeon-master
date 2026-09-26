"""The four agent roles: Rules Referee (also the turn Router), DM/Narrator,
NPC, Worldbuilder.

Generation params (temperature/top_p/...) below are placeholder defaults --
intentionally not tuned yet. Revisit once we're testing against real play
sessions, per the plan to defer that tuning until it's needed.
"""
import json
import re

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

Respond with ONLY a JSON object, no other text, matching exactly:
{"turn_type": "info_request" | "dialogue" | "action",
 "known_to_dm": true | false,
 "addresses_npc": true | false,
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
3. CONCISION: 120-220 words. End on a clear situation or choice point, not \
   a wall of exposition.
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
_QUESTION_STARTERS = ("what", "who", "where", "when", "why", "how", "tell me", "recap")
_EMBED_MODEL_NAME = "all-MiniLM-L6-v2"
CONFIDENCE_THRESHOLD = 0.45  # untuned placeholder, like the temperature/top_p dicts above

_SIMPLE_EXAMPLES = [
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
    # mundane, low-stakes dialogue -- content carries no risk, even though
    # it's addressed to someone
    "I ask the innkeeper about work.",
    "I ask him what's on the menu tonight.",
    "I say hello to the bartender.",
    "I ask her how her day has been.",
]
_COMPLEX_EXAMPLES = [
    "I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely.",
    "I draw my sword and in one perfect strike intimidate all three into surrendering instantly.",
    "I try to convince the guard to let me pass.",
    "I attack the bandit.",
    "I attempt to pick the lock on the door.",
    "I threaten the merchant unless he lowers his price.",
    "Everyone here just naturally listens to whatever I tell them.",
    "People around here tend to trust me the moment they meet me.",
    "I sneak past the guards without being seen.",
]

_embed_model = None
_example_texts = _SIMPLE_EXAMPLES + _COMPLEX_EXAMPLES
_example_labels = ["SIMPLE"] * len(_SIMPLE_EXAMPLES) + ["COMPLEX"] * len(_COMPLEX_EXAMPLES)
_example_vecs = None


def _get_embed_model():
    global _embed_model, _example_vecs
    if _embed_model is None:
        _embed_model = SentenceTransformer(_EMBED_MODEL_NAME)
        _example_vecs = _embed_model.encode(_example_texts, convert_to_tensor=True)
    return _embed_model


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

    if "?" in text or text.startswith(_QUESTION_STARTERS):
        return False  # info-requests still need the router call (known_to_dm/worldbuild)

    model = _get_embed_model()
    vec = model.encode([player_input], convert_to_tensor=True)
    sims = util.cos_sim(vec, _example_vecs)[0]
    best_idx = int(sims.argmax())
    best_sim = float(sims[best_idx])

    if best_sim < CONFIDENCE_THRESHOLD:
        return False  # not confident enough either way -- ask the real Referee
    return _example_labels[best_idx] == "SIMPLE"


def judge_action(world: WorldState, player_input: str) -> dict:
    messages = [
        {"role": "system", "content": RULES_SYSTEM},
        {"role": "user", "content": (
            f"WORLD CONTEXT:\n{world.context_brief()}\n\n"
            f"PLAYER DECLARES: {player_input}\n\n"
            "Return the JSON ruling."
        )},
    ]
    content, _ = chat(messages, options=RULES_OPTIONS, json_format=True)
    try:
        verdict = json.loads(content)
        assert verdict.get("outcome") in {"success", "partial", "complication", "failure"}
        assert verdict.get("turn_type") in {"info_request", "dialogue", "action"}
    except Exception:
        # Fallback degrades to the old always-safe behavior: treat as a
        # plain action (never skips judgment) and only involve the NPC if
        # today's blunt "important NPC is active" check would have.
        active = world.npcs.get(world.active_npc)
        verdict = {
            "turn_type": "action",
            "known_to_dm": False,
            "addresses_npc": bool(active and active.important),
            "outcome": "complication",
            "twist": "",
            "rationale": f"fallback: unparsable referee output: {content!r}",
        }
    return verdict


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
    ruling_block = (
        f"RULING (do not contradict): outcome={verdict.get('outcome')}; "
        f"twist_to_weave_in={verdict.get('twist') or 'none'}"
    )
    npc_block = ""
    if npc_line:
        npc_block = (
            f"\n{world.active_npc} just said, in character: \"{npc_line}\"\n"
            "Weave this into your narration naturally."
        )
    lore_block = ""
    if new_lore:
        lore_block = f"\nNEWLY ESTABLISHED LORE (reference material, weave in once): {new_lore}\n"
    user_content = (
        f"WORLD CONTEXT:\n{world.context_brief()}\n\n{ruling_block}{npc_block}{lore_block}\n\n"
        f"PLAYER: {player_input}"
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

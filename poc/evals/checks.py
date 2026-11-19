"""Per-turn checks. Deterministic where possible, local-LLM judge where not.

Every check returns {"name", "passed", "detail", "judged"} so the report can
tell hard (deterministic) results apart from judged (noisy, 8B-model) ones.
"""
import json
import re

from ollama_client import chat

# Word budgets. The DM's own prompt asks for <70 words on TIGHT turns and
# <150 on fuller ones; the budgets leave slack so only real overruns fail.
TIGHT_BUDGET = 110
FULL_BUDGET = 170

# Internal scaffolding that must never reach the player.
_META_LEAK = re.compile(
    r"OVERSTEP|\bRULING\b|referee|rationale|player_assertion|outcome\s*=|"
    r"pacing\s*=|\(OPTIONS|reminder:|^\s*---\s*$|as an AI",
    re.IGNORECASE | re.MULTILINE,
)

_JUDGE_SYSTEM = (
    "You are a strict evaluator of a tabletop roleplaying game's narration. "
    "The player character is Kael. Grimbold is the innkeeper (an NPC). You are "
    "given what the player declared and what the Dungeon Master narrated. "
    "Judge only what the narration literally says. First write one short "
    "sentence of reasoning quoting the relevant words, THEN answer yes or no. "
    'Reply with ONLY a JSON object, with keys in this order: '
    '{"reason": "<one short sentence>", "answer": "yes" | "no"}'
)

# Each question is phrased so that "yes" means the BAD thing happened.
_QUESTIONS = {
    "folded": (
        'The player declared: "{text}". The player wanted this outcome: '
        '"{claim}". Does the narration show that outcome actually happening '
        "(the NPCs trust, comply, surrender, or hand things over as the player "
        "wanted), without the NPC refusing or holding back? Answer yes if the "
        "player mostly got what they wanted. Answer no if the NPC refuses, "
        "resists, demands more, or the outcome does not happen."
    ),
    "became_true": (
        'The player claimed this as a fact: "{claim}". Does the narration '
        "present that claim as really happening or being true in the story "
        "(someone really arrives, the power or sense is really gained, the "
        "event really occurs)? Answer yes if the narration treats the claim as "
        "real, even partly. Answer no if the narration shows it not happening, "
        "says nothing changed, or ignores it."
    ),
    "puppeting": (
        "Does the narration put words in Kael's mouth, or state what Kael "
        "thinks, emotionally feels, or decides? Examples of yes: a quoted line "
        "spoken by Kael or by 'you' ('I'll take any job,' Kael says; "
        "'Rain?' you say), 'Kael decides to...', 'he feels hope'. Examples of "
        "NO: physical gestures and reflexes (gripping a hilt, breath "
        "catching, fists clenching, looking around, stepping back), and "
        "anything an NPC or the world says or does. Answer yes only if Kael "
        "speaks, or the narration states his thoughts, emotions, or decisions."
    ),
}


def judge(kind: str, turn, narration: str) -> dict:
    question = _QUESTIONS[kind].format(text=turn.text, claim=turn.claim)
    messages = [
        {"role": "system", "content": _JUDGE_SYSTEM},
        {"role": "user", "content": (
            f"PLAYER DECLARED: {turn.text}\n\nNARRATION:\n{narration}\n\n"
            f"QUESTION: {question}"
        )},
    ]
    content, _ = chat(messages, options={"temperature": 0}, json_format=True)
    try:
        out = json.loads(content)
        ans = str(out.get("answer", "")).strip().lower()
        if ans not in ("yes", "no"):
            raise ValueError(ans)
        return {"answer": ans == "yes", "reason": str(out.get("reason", ""))}
    except Exception:
        return {"answer": None, "reason": f"unparsable judge output: {content!r}"}


def _check(name, passed, detail="", judged=False):
    return {"name": name, "passed": passed, "detail": detail, "judged": judged}


def _judged(name, kind, turn, narration, want_answer, use_judge):
    """Passes when the judge's answer equals want_answer. Skipped (None) when
    the judge is disabled or returned garbage, so it doesn't count either way."""
    if not use_judge:
        return None
    j = judge(kind, turn, narration)
    if j["answer"] is None:
        return _check(name, None, j["reason"], judged=True)
    return _check(name, j["answer"] == want_answer, j["reason"], judged=True)


def run_checks(turn, narration: str, verdict: dict, use_judge: bool = True) -> list:
    results = []
    words = len(narration.split())
    flagged = bool(verdict.get("player_assertion"))
    outcome = verdict.get("outcome")

    # --- every turn -------------------------------------------------------
    full = turn.kind in ("shift", "redescribe", "recall") or verdict.get("scene_shift")
    budget = turn.max_words or (FULL_BUDGET if full else TIGHT_BUDGET)
    results.append(_check("length", words <= budget, f"{words} words (budget {budget})"))
    leak = _META_LEAK.search(narration)
    results.append(_check("no_meta_leak", leak is None,
                          f"leaked: {leak.group(0)!r}" if leak else ""))

    # --- by kind ----------------------------------------------------------
    if turn.kind == "normal":
        results.append(_check("not_flagged", not flagged,
                              f"false positive: {verdict.get('player_assertion')!r}" if flagged else ""))
        results.append(_check("no_stray_note", not verdict.get("correction_note"),
                              f"unexpected note: {verdict.get('correction_note')!r}"))
    elif turn.kind == "overreach":
        # The Referee may also flag a presumption as an invented fact; either
        # counts as "did not hand over a clean success".
        results.append(_check("not_clean_success", outcome != "success" or flagged,
                              f"outcome={outcome}, flagged={flagged}"))
        results.append(_judged("held_the_line", "folded", turn, narration, False, use_judge))
    elif turn.kind == "invented":
        results.append(_check("flagged", flagged, f"player_assertion={verdict.get('player_assertion')!r}"))
        # The player must be told, out of character and before the narration,
        # why their claim wasn't accepted (verdict["correction_note"]).
        note = verdict.get("correction_note") or ""
        results.append(_check("explained", bool(note) and len(note.split()) <= 45,
                              f"note={note!r}" if note else "no correction note"))
        results.append(_judged("not_made_true", "became_true", turn, narration, False, use_judge))
    elif turn.kind == "shift":
        results.append(_check("scene_shift_flagged", bool(verdict.get("scene_shift")),
                              f"scene_shift={verdict.get('scene_shift')}"))

    if turn.kind in ("recall", "redescribe"):
        low = narration.lower()
        missing = [k for k in turn.must_include if k.lower() not in low]
        ok = not missing
        detail = f"missing: {missing}" if missing else ""
        if turn.must_include_any:
            hit = any(k.lower() in low for k in turn.must_include_any)
            ok = ok and hit
            detail = (detail + " " if detail else "") + (
                "" if hit else f"none of {turn.must_include_any} present")
        results.append(_check("recall", ok, detail))

    if turn.kind in ("normal", "overreach", "invented"):
        results.append(_judged("no_puppeting", "puppeting", turn, narration, False, use_judge))

    return [r for r in results if r is not None]

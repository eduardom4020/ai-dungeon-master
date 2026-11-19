"""Eval harness for the multi-agent DM.

Replays a fixed scripted session N times against the live pipeline and scores
it: narration length, overreach resistance, refusal of invented world facts,
recall of established facts, scene-shift flagging, leaks of internal text,
false positives on legitimate play, and latency.

    cd poc
    python evals/run_eval.py                     # 2 runs of tavern_night
    python evals/run_eval.py --runs 5 --label after-brevity
    python evals/run_eval.py --no-judge          # deterministic checks only (faster)
    python evals/run_eval.py --only t03,t04      # a subset of turns (ids or prefixes)
    python evals/run_eval.py --compare evals/results/a.json evals/results/b.json

Results go to evals/results/<timestamp>_<label>.{json,md}.

Scores from the "judged" checks come from the same 8B local model that plays
the DM, so treat them as a noisy signal: compare runs against each other
rather than reading any single number as ground truth.
"""
import argparse
import json
import statistics
import sys
import time
import urllib.error
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
POC_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(POC_DIR))
sys.path.insert(0, str(Path(__file__).resolve().parent))

RESULTS_DIR = Path(__file__).resolve().parent / "results"


def run_scenario(turns, use_judge, run_idx, total_runs):
    import checks
    import orchestrator
    from play import seed_world

    world = seed_world()
    out = []
    for turn in turns:
        marks = {}
        t0 = time.monotonic()
        retries = 0
        while True:
            try:
                narration, verdict = orchestrator.run_turn(
                    world, turn.text, on_timing=lambda ev, el: marks.__setitem__(ev, el)
                )
                break
            except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
                # Transient Ollama failure (the DM/NPC calls aren't wrapped like
                # the Referee's). Retry the turn rather than losing the run.
                retries += 1
                print(f"  ! {turn.id}: {e} -- retry {retries}", flush=True)
                if retries > 2:
                    raise
                marks.clear()
        elapsed = time.monotonic() - t0
        verdict["_location"] = world.location
        verdict["_present"] = [n.name for n in world.present_npcs()]
        results = checks.run_checks(turn, narration, verdict, use_judge=use_judge)
        fails = [r["name"] for r in results if r["passed"] is False]
        print(f"  run {run_idx}/{total_runs} {turn.id:<22} {len(narration.split()):>4}w "
              f"{elapsed:>5.1f}s  {'FAIL: ' + ', '.join(fails) if fails else 'ok'}", flush=True)
        out.append({
            "id": turn.id, "kind": turn.kind, "player": turn.text,
            "narration": narration, "words": len(narration.split()),
            "verdict": verdict, "elapsed_s": round(elapsed, 2),
            "first_token_s": round(marks.get("first_token", float("nan")), 2),
            "fast_path": str(verdict.get("rationale", "")).startswith("heuristic"),
            "retries": retries,
            "referee_fallback": str(verdict.get("rationale", "")).startswith("fallback"),
            "checks": results,
        })
    return out


def summarize(runs):
    """Aggregate per-check pass rates (skipping None = judge unavailable)."""
    by_check, by_kind_words, lat, ftok = {}, {}, [], []
    fast, total = 0, 0
    for run in runs:
        for t in run:
            total += 1
            fast += t["fast_path"]
            lat.append(t["elapsed_s"])
            ftok.append(t["first_token_s"])
            by_kind_words.setdefault(t["kind"], []).append(t["words"])
            for c in t["checks"]:
                if c["passed"] is None:
                    continue
                d = by_check.setdefault(c["name"], {"pass": 0, "n": 0, "judged": c["judged"]})
                d["n"] += 1
                d["pass"] += bool(c["passed"])
    return {
        "checks": {k: {**v, "rate": round(v["pass"] / v["n"], 3)} for k, v in sorted(by_check.items())},
        "words_by_kind": {k: {"mean": round(statistics.mean(v), 1), "max": max(v)}
                          for k, v in sorted(by_kind_words.items())},
        "latency_mean_s": round(statistics.mean(lat), 2),
        "first_token_mean_s": round(statistics.mean(x for x in ftok if x == x), 2),
        "fast_path_rate": round(fast / total, 3) if total else 0,
        "turns": total,
    }


def write_report(path_md, meta, runs, summary):
    L = [f"# Eval report: {meta['label']}", "",
         f"- scenario: `{meta['scenario']}`  |  runs: {meta['runs']}  |  judge: {meta['judge']}",
         f"- model: `{meta['model']}`  |  git: `{meta['git']}`  |  {meta['timestamp']}", "",
         "## Check pass rates", "",
         "| check | pass | rate | type |", "|---|---|---|---|"]
    for name, d in summary["checks"].items():
        L.append(f"| {name} | {d['pass']}/{d['n']} | {d['rate']:.0%} | "
                 f"{'judged' if d['judged'] else 'deterministic'} |")
    L += ["", "## Narration length (words)", "", "| turn kind | mean | max |", "|---|---|---|"]
    for k, d in summary["words_by_kind"].items():
        L.append(f"| {k} | {d['mean']} | {d['max']} |")
    L += ["", f"Latency: {summary['latency_mean_s']}s/turn mean, first token "
          f"{summary['first_token_mean_s']}s. Fast path used on {summary['fast_path_rate']:.0%} of turns.",
          "", "## Failures", ""]
    any_fail = False
    for ri, run in enumerate(runs, 1):
        for t in run:
            fails = [c for c in t["checks"] if c["passed"] is False]
            if not fails:
                continue
            any_fail = True
            L.append(f"### run {ri} / {t['id']} ({t['kind']})")
            L.append(f"**Player:** {t['player']}")
            for c in fails:
                L.append(f"- **{c['name']}**{' (judged)' if c['judged'] else ''}: {c['detail']}")
            L.append(f"\n> {t['narration'].replace(chr(10), chr(10) + '> ')}\n")
    if not any_fail:
        L.append("None.")
    L += ["", "## Full transcripts", ""]
    for ri, run in enumerate(runs, 1):
        L.append(f"### Run {ri}")
        for t in run:
            v = t["verdict"]
            L.append(f"**[{t['id']}] Player:** {t['player']}  ")
            L.append(f"*verdict: outcome={v.get('outcome')}, scene_shift={v.get('scene_shift')}, "
                     f"player_assertion={v.get('player_assertion')!r}, fast_path={t['fast_path']}, "
                     f"{t['words']}w, {t['elapsed_s']}s*\n")
            if v.get("npc_line"):
                L.append(f"**{v.get('npc_name')}:** {v['npc_line']}\n")
            L.append(f"> {t['narration'].replace(chr(10), chr(10) + '> ')}\n")
    Path(path_md).write_text("\n".join(L), encoding="utf-8")


def compare(a_path, b_path):
    a, b = (json.loads(Path(p).read_text(encoding="utf-8")) for p in (a_path, b_path))
    print(f"A: {a['meta']['label']} ({a['meta']['git']})   B: {b['meta']['label']} ({b['meta']['git']})\n")
    print(f"{'check':<22}{'A':>10}{'B':>10}{'delta':>9}")
    for name in sorted(set(a["summary"]["checks"]) | set(b["summary"]["checks"])):
        ra = a["summary"]["checks"].get(name, {}).get("rate")
        rb = b["summary"]["checks"].get(name, {}).get("rate")
        f = lambda x: "-" if x is None else f"{x:.0%}"
        d = "" if ra is None or rb is None else f"{(rb - ra) * 100:+.0f}pt"
        print(f"{name:<22}{f(ra):>10}{f(rb):>10}{d:>9}")
    print(f"\n{'mean words/kind':<22}{'A':>10}{'B':>10}")
    for k in sorted(set(a["summary"]["words_by_kind"]) | set(b["summary"]["words_by_kind"])):
        ma = a["summary"]["words_by_kind"].get(k, {}).get("mean", "-")
        mb = b["summary"]["words_by_kind"].get(k, {}).get("mean", "-")
        print(f"{k:<22}{ma:>10}{mb:>10}")
    print(f"\nlatency/turn: A {a['summary']['latency_mean_s']}s  B {b['summary']['latency_mean_s']}s")


def rejudge(path):
    """Re-run only the checks (incl. the judge) over stored narrations. Lets a
    change to checks.py be applied to old runs, so before/after results are
    scored by the SAME checks without replaying the game."""
    import checks
    from scenarios import SCENARIOS

    src = Path(path)
    data = json.loads(src.read_text(encoding="utf-8"))
    turns = {t.id: t for t in SCENARIOS[data["meta"]["scenario"]]}
    use_judge = data["meta"].get("judge") != "off"
    for run in data["runs"]:
        for t in run:
            t["checks"] = checks.run_checks(turns[t["id"]], t["narration"], t["verdict"], use_judge)
    summary = summarize(data["runs"])
    meta = {**data["meta"], "label": data["meta"]["label"] + "-rejudged",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")}
    out = src.with_name(src.stem + "-rejudged.json")
    out.write_text(json.dumps({"meta": meta, "summary": summary, "runs": data["runs"]},
                              indent=2, default=str), encoding="utf-8")
    write_report(out.with_suffix(".md"), meta, data["runs"], summary)
    print(f"rejudged -> {out}")
    for name, d in summary["checks"].items():
        print(f"  {name:<22}{d['pass']:>3}/{d['n']:<3}{d['rate']:>6.0%}")


def _git_rev():
    import subprocess
    try:
        rev = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True,
                             text=True, cwd=POC_DIR).stdout.strip()
        dirty = subprocess.run(["git", "status", "--porcelain", "--", "."], capture_output=True,
                               text=True, cwd=POC_DIR).stdout.strip()
        return rev + ("+dirty" if dirty else "")
    except Exception:
        return "unknown"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--scenario", default="tavern_night")
    ap.add_argument("--runs", type=int, default=2)
    ap.add_argument("--label", default="run")
    ap.add_argument("--no-judge", action="store_true")
    ap.add_argument("--only", help="comma-separated turn ids or id prefixes (e.g. t03,t04)")
    ap.add_argument("--compare", nargs=2, metavar=("A.json", "B.json"))
    ap.add_argument("--rejudge", metavar="RESULT.json",
                    help="re-score the stored narrations/verdicts of a previous result with the "
                         "current checks.py (no game replay); writes a new result file")
    args = ap.parse_args()

    if args.compare:
        return compare(*args.compare)
    if args.rejudge:
        return rejudge(args.rejudge)

    from scenarios import SCENARIOS
    import ollama_client

    turns = SCENARIOS[args.scenario]
    if args.only:
        wanted = tuple(args.only.split(","))
        turns = [t for t in turns if t.id.startswith(wanted)]
        if not turns:
            sys.exit(f"--only matched no turns in {args.scenario}")

    print("[warming up model...]", flush=True)
    ollama_client.warmup()

    RESULTS_DIR.mkdir(exist_ok=True)
    stem = f"{datetime.now():%Y%m%d-%H%M%S}_{args.label}"
    meta = {"label": args.label, "scenario": args.scenario, "runs": args.runs,
            "judge": "off" if args.no_judge else "on", "model": ollama_client.DEFAULT_MODEL,
            "git": _git_rev(), "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "turn_ids": [t.id for t in turns]}

    def save(runs, partial):
        # Written after every completed run, so a crash or Ctrl-C keeps the
        # runs that already finished (a full run takes many minutes).
        summary = summarize(runs)
        m = {**meta, "runs": len(runs), "partial": partial}
        (RESULTS_DIR / f"{stem}.json").write_text(
            json.dumps({"meta": m, "summary": summary, "runs": runs}, indent=2, default=str),
            encoding="utf-8")
        write_report(RESULTS_DIR / f"{stem}.md", m, runs, summary)
        return summary

    runs = []
    try:
        for i in range(1, args.runs + 1):
            runs.append(run_scenario(turns, not args.no_judge, i, args.runs))
            save(runs, partial=i < args.runs)
    except BaseException:
        if runs:
            save(runs, partial=True)
            print(f"\n[aborted after {len(runs)} complete run(s); partial results saved]")
        raise
    summary = save(runs, partial=False)

    print(f"\n=== {args.label}: {args.runs} run(s) of {args.scenario} ===")
    for name, d in summary["checks"].items():
        print(f"  {name:<22}{d['pass']:>3}/{d['n']:<3}{d['rate']:>6.0%}  "
              f"{'(judged)' if d['judged'] else ''}")
    print(f"  words/kind: " + ", ".join(f"{k} {v['mean']}" for k, v in summary['words_by_kind'].items()))
    print(f"  latency {summary['latency_mean_s']}s/turn | fast path {summary['fast_path_rate']:.0%}")
    print(f"\nreport: {RESULTS_DIR / (stem + '.md')}")


if __name__ == "__main__":
    main()

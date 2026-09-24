"""
Side-by-side DM-narrative test harness for candidate Ollama models.
Runs the same fixed 5-turn scene through each model and records
transcripts + latency/throughput, for manual comparison.
"""
import json
import sys
import time
import urllib.request
from pathlib import Path

OLLAMA_URL = "http://localhost:11434/api/chat"
HERE = Path(__file__).parent

MODELS = [
    ("mistral-nemo", "mistral-nemo:12b-instruct-2407-q4_K_M"),
    ("gemma2-9b", "gemma2:9b"),
    ("stheno-8b", "fluffy/l3-8b-stheno-v3.2:latest"),
    ("mistral-nemo-q3", "mistral-nemo:12b-instruct-2407-q3_K_M"),
    ("ministral-3-8b", "ministral-3:8b-instruct-2512-q4_K_M"),
]

SYSTEM_PROMPT = (HERE / "dm_system_prompt.txt").read_text(encoding="utf-8")

# Fixed scripted player turns. Turn 3 and 4 are deliberate "overreach" probes
# (bribery demanding instant trust; guaranteed one-shot intimidation of three
# armed men) to see whether the model pushes back instead of complying.
# Turn 5 probes memory/cohesion by asking it to recall facts from turn 2.
TURNS = [
    "I am Kael, a former soldier turned sellsword, arriving at the gates of "
    "the border town of Ashwick as the sun sets. I've heard there's work "
    "here. I head to the nearest tavern.",

    "I ask the innkeeper about any rumors of missing people or strange "
    "happenings nearby.",

    "I flash a handful of copper coins and tell the innkeeper this is more "
    "than enough to make him tell me everything he knows, no matter how "
    "dangerous, and to trust me completely as if we were old friends.",

    "Suddenly three armed men burst into the tavern looking for trouble. I "
    "draw my sword and, in one perfect strike, intimidate all three into "
    "surrendering instantly without a fight.",

    "Before we continue -- what was the innkeeper's name again, and what "
    "did he tell me about the rumors?",
]


def call_ollama(model_tag, messages):
    payload = json.dumps({
        "model": model_tag,
        "messages": messages,
        "stream": False,
    }).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"}
    )
    start = time.monotonic()
    with urllib.request.urlopen(req, timeout=600) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    wall_s = time.monotonic() - start

    content = body["message"]["content"]
    eval_count = body.get("eval_count", 0)
    eval_ns = body.get("eval_duration", 0)
    tok_per_s = (eval_count / (eval_ns / 1e9)) if eval_ns else float("nan")
    total_ns = body.get("total_duration", 0)

    return content, {
        "wall_s": round(wall_s, 2),
        "total_duration_s": round(total_ns / 1e9, 2),
        "output_tokens": eval_count,
        "tokens_per_s": round(tok_per_s, 1),
    }


def run_model(label, model_tag):
    print(f"\n=== {label} ({model_tag}) ===")
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    transcript_lines = [f"# DM test transcript -- {label} (`{model_tag}`)\n"]
    metrics_rows = []

    for i, turn in enumerate(TURNS, 1):
        messages.append({"role": "user", "content": turn})
        print(f"  turn {i}/{len(TURNS)}...", end="", flush=True)
        content, metrics = call_ollama(model_tag, messages)
        messages.append({"role": "assistant", "content": content})
        print(f" {metrics['wall_s']}s, {metrics['tokens_per_s']} tok/s")

        transcript_lines.append(f"\n## Turn {i}\n\n**Player:** {turn}\n")
        transcript_lines.append(f"\n**DM ({label}):**\n\n{content}\n")
        transcript_lines.append(
            f"\n*[{metrics['wall_s']}s wall | {metrics['output_tokens']} "
            f"tokens | {metrics['tokens_per_s']} tok/s]*\n"
        )
        metrics_rows.append((i, metrics))

    out_path = HERE / f"transcript_{label}.md"
    out_path.write_text("\n".join(transcript_lines), encoding="utf-8")
    print(f"  -> saved {out_path.name}")
    return metrics_rows


def main():
    requested = set(sys.argv[1:])
    models = [m for m in MODELS if not requested or m[0] in requested]

    summary = {}
    for label, model_tag in models:
        try:
            summary[label] = run_model(label, model_tag)
        except Exception as e:
            print(f"  !! failed for {label}: {e}")
            summary[label] = None

    print("\n\n=== SUMMARY (avg tok/s, avg latency) ===")
    for label, rows in summary.items():
        if not rows:
            print(f"{label}: FAILED")
            continue
        avg_lat = sum(m["wall_s"] for _, m in rows) / len(rows)
        avg_tps = sum(m["tokens_per_s"] for _, m in rows) / len(rows)
        print(f"{label}: avg {avg_lat:.2f}s/turn, avg {avg_tps:.1f} tok/s")


if __name__ == "__main__":
    main()

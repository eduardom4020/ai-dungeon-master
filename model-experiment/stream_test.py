"""Verify token-by-token streaming works against the selected model."""
import json
import time
import urllib.request

MODEL = "ministral-3:8b-instruct-2512-q4_K_M"
OLLAMA_URL = "http://localhost:11434/api/chat"

payload = json.dumps({
    "model": MODEL,
    "messages": [
        {"role": "system", "content": "You are a terse narrator."},
        {"role": "user", "content": "Describe a tavern door opening, in 2 sentences."},
    ],
    "stream": True,
}).encode("utf-8")

req = urllib.request.Request(
    OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"}
)

print("Requesting with stream=True...\n")
start = time.monotonic()
first_chunk_t = None
chunk_count = 0
full_text = []

with urllib.request.urlopen(req, timeout=120) as resp:
    for raw_line in resp:
        if not raw_line.strip():
            continue
        t = time.monotonic() - start
        chunk = json.loads(raw_line.decode("utf-8"))
        piece = chunk.get("message", {}).get("content", "")
        done = chunk.get("done", False)

        if first_chunk_t is None and piece:
            first_chunk_t = t

        chunk_count += 1
        full_text.append(piece)
        print(f"  [t={t:5.2f}s] chunk#{chunk_count:<3} done={done!s:<5} piece={piece!r}")

        if done:
            total_t = t
            break

print("\n--- summary ---")
print(f"time to first token: {first_chunk_t:.2f}s")
print(f"total chunks received: {chunk_count}")
print(f"total time: {total_t:.2f}s")
print(f"assembled text: {''.join(full_text)!r}")

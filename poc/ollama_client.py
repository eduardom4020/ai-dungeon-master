"""Thin shared wrapper around the local Ollama chat API."""
import json
import urllib.request

OLLAMA_URL = "http://localhost:11434/api/chat"
DEFAULT_MODEL = "ministral-3:8b-instruct-2512-q4_K_M"


def chat(messages, model=DEFAULT_MODEL, stream=False, options=None,
         json_format=False, on_token=None, keep_alive=-1):
    """Call the Ollama chat endpoint.

    options: dict of generation params (temperature, top_k, top_p, ...) --
        left to the caller so each agent role can carry its own tuning.
    json_format: request strict JSON output (Ollama's `format: "json"`).
    on_token: callback(piece:str) invoked per chunk when stream=True.

    keep_alive: how long Ollama keeps the model loaded in VRAM after this
        call. -1 means indefinitely -- fine here since every agent role
        shares the same DEFAULT_MODEL, so there's no other model competing
        for that VRAM.

    Returns (content:str, metadata:dict).
    """
    payload = {
        "model": model,
        "messages": messages,
        "stream": stream,
        "keep_alive": keep_alive,
    }
    if options:
        payload["options"] = options
    if json_format:
        payload["format"] = "json"

    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )

    if not stream:
        with urllib.request.urlopen(req, timeout=600) as resp:
            body = json.loads(resp.read().decode("utf-8"))
        return body["message"]["content"], body

    content_parts = []
    meta = {}
    with urllib.request.urlopen(req, timeout=600) as resp:
        for raw_line in resp:
            if not raw_line.strip():
                continue
            chunk = json.loads(raw_line.decode("utf-8"))
            piece = chunk.get("message", {}).get("content", "")
            if piece:
                content_parts.append(piece)
                if on_token:
                    on_token(piece)
            if chunk.get("done"):
                meta = chunk
    return "".join(content_parts), meta


def warmup(model=DEFAULT_MODEL):
    """Fire a trivial request so Ollama loads the model into VRAM now,
    instead of on the player's first real turn (a ~10s+ cold-load delay
    measured in model-experiment/stream_test.py)."""
    chat([{"role": "user", "content": "hi"}], model=model)

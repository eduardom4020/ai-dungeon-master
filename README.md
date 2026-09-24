# AI Dungeon Master

A multi-agent AI system that plays the Dungeon Master for a tabletop RPG (D&D-style), running entirely on local hardware via [Ollama](https://ollama.com) — no paid APIs, no cloud LLMs.

## Purpose

Most "AI DM" experiments lean on tight game mechanics (dice, stat blocks, combat resolvers) because that's easy to make deterministic. This project deliberately does the opposite: a very simple, homebrew RPG system with no dice and no numeric stats, where the focus is storytelling and roleplay. The interesting problem isn't rules simulation, it's building a DM that:

- Writes narrative prose worth reading (voice, atmosphere, distinct NPCs).
- Stays cohesive — remembers what it already established and doesn't contradict itself.
- Pushes back. A good DM doesn't hand the player a clean win just because they declared one confidently. NPCs have their own will; overreach gets a complication, not free compliance.
- Responds with reasonable latency on consumer hardware (this was built and tuned against an 8GB-VRAM laptop GPU).

Interface is a CLI text adventure — no UI work, all the effort goes into the agent architecture and prompting.

## How it's built

**Multi-agent orchestration**, not a single do-everything prompt:

| Agent | Role |
|---|---|
| Rules Referee | Silent judge. Given the world state and the player's declared action, returns a strict JSON verdict (`success` / `partial` / `complication` / `failure` + a short twist). The player never sees this directly. |
| NPC | A persistent, in-character persona per important NPC, with its own conversation thread and known facts. |
| DM / Narrator | Turns the Referee's verdict (and the NPC's line, if any) into prose. Never plays the player character's own actions or dialogue. |
| Worldbuilder | On-demand agent that invents new lore consistent with what's already established. |

All four agents read from one shared `WorldState` (location, scene summary, NPCs, established facts, recent history) instead of relying on raw chat history — that shared state, not the chat log, is what keeps the story cohesive across independent model calls.

## Repo layout

```
model-experiment/   Scripts + transcripts used to pick the local LLM (see below)
  results/           Full transcripts from that comparison, one per model
poc/                 The actual multi-agent implementation (the game)
posts/               LinkedIn "building in public" write-ups documenting the project
```

## Model selection

Before writing any agent code, five local models (7B–12B, quantized to fit 8GB VRAM) were run through the same fixed 5-turn scripted scene — including two deliberate "overreach" probes (a bribe demanding instant trust; a claimed guaranteed win against three armed men) — to see which ones actually resist player overreach instead of just complying. `ministral-3:8b-instruct-2512-q4_K_M` won on narrative quality, cohesion, and non-sycophancy, at good latency. Full methodology and results are in [model-experiment/](model-experiment/) and written up in [posts/01-choosing-the-model.md](posts/01-choosing-the-model.md).

## Running it

See [CLAUDE.md](CLAUDE.md) for exact commands (running the PoC, re-running model experiments, drafting posts). Short version: `python poc/play.py` for the interactive CLI game, once Ollama is running locally with the picked model pulled.

## Status

Working PoC: shared world state, all four agents wired together, verified via a scripted smoke test that overreach probes get pushed back on and NPC memory persists. Known open issue: DM responses in the live pipeline sometimes run longer than the prompt's 120–220 word target — see [CLAUDE.md](CLAUDE.md) for context.

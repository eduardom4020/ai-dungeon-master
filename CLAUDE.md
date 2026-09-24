# CLAUDE.md

Working notes for AI agent sessions in this repo. Read [README.md](README.md) first for what/why; this file is how.

## Environment

- Local LLMs run via Ollama, REST API at `http://localhost:11434/api/chat`. Check it's up with `ollama list` before assuming any script will work.
- Picked model: `ministral-3:8b-instruct-2512-q4_K_M` (set as `DEFAULT_MODEL` in `poc/ollama_client.py`). If it's missing locally, `ollama pull ministral-3:8b-instruct-2512-q4_K_M`.
- Hardware this was tuned against: 8GB VRAM laptop GPU. Keep that in mind before suggesting bigger/unquantized models — they won't fit.
- No paid APIs anywhere in this project. Don't introduce one without the user explicitly asking.

## Running the PoC

```bash
cd poc
python play.py          # interactive CLI game
python play.py -v       # same, with verbose mode (shows router/Referee JSON, NPC lines, worldbuilder output)
python smoke_test.py    # non-interactive, 5 scripted turns, no typing needed
```

`play.py` persists to `poc/session_state.json`. In-game commands: `/state`, `/npc <name>`, `/worldbuild <topic>`, `/verbose`, `/reset`, `/quit`.

Windows note: both entry scripts call `sys.stdout.reconfigure(encoding="utf-8")` at the top — needed because the models emit curly quotes/em-dashes that mojibake on the default Windows console encoding. Keep that line if you add new entry-point scripts that print model output directly.

## Working on the multi-agent pipeline (`poc/`)

- `world_state.py` — shared state (the cohesion mechanism). If cohesion/memory issues show up, look here first, not at chat history — agents intentionally don't share raw chat history, they share this.
- `agents.py` — all four system prompts + the generation-param dicts (`RULES_OPTIONS`, `DM_OPTIONS`, `NPC_OPTIONS`, `WORLDBUILD_OPTIONS`). **Those option dicts are explicitly untuned placeholders** — the user deferred temperature/top_p/top_k tuning until real play sessions expose an actual problem. Don't tune them speculatively; only touch them if asked or if you're fixing a concretely observed failure.
- `orchestrator.py` — **real agentic routing, not a fixed pipeline.** One combined Rules Referee + Router call (`agents.judge_action`) runs every turn and decides, via its JSON (`turn_type`, `known_to_dm`, `addresses_npc`, plus the usual `outcome`/`twist`), which of {NPC, Worldbuilder} this specific turn actually needs — not "NPC runs whenever an important NPC happens to be in the scene" like the old fixed sequence. When both are needed they run **concurrently** via `concurrent.futures.ThreadPoolExecutor` (validated empirically this session: ~1.4x speedup on this hardware for 2 concurrent Ollama calls against the same loaded model — see git history / conversation for the raw numbers). Fast-path turns (already-known recall, ordinary actions) skip both tools entirely and the DM streams immediately after the one router call. The DM always narrates last, after whatever's needed has resolved — it's the one genuine data dependency in the pipeline (it needs the verdict and, if present, the NPC line/new lore, as context).
- `orchestrator.run_turn()`'s `on_thinking` callback fires once, only on turns that need a tool call, so the CLI can show a `[thinking...]` placeholder instead of the player staring at nothing. Fast-path turns never trigger it.
- Worldbuilding can now happen **automatically** (Referee/Router flags `turn_type="info_request"` + `known_to_dm=False`), not only via the manual `/worldbuild` command — this was the first slice of genuine agentic tool-selection in the project, closing the gap where the DM previously had no way to invoke a "tool" on its own judgment.

**Known open issue (unresolved, not currently being worked unless asked):** DM narration in the live pipeline sometimes runs longer than the `DM_SYSTEM` prompt's stated 120–220 word target (seen up to ~280-400 words). Already tightened once (see `RULES_SYSTEM`'s `twist` field and `DM_SYSTEM` rules 5–6, which fixed a worse duplication bug where the Referee's twist and the DM's narration told the same beat 2–3 times). If asked to continue on this, it's a prompt-strength problem, not a sampling-parameter one — don't reach for temperature/top_p first.

## Re-running the model experiment (`model-experiment/`)

This produced the model choice documented in `posts/01-choosing-the-model.md` and shouldn't normally need re-running. If asked to test a new candidate model:

```bash
cd model-experiment
python dm_test.py                      # runs every model in MODELS
python dm_test.py ministral-3-8b       # runs just one label (matches MODELS tuples)
```

- Add new candidates to the `MODELS` list in `dm_test.py` (label, ollama tag).
- The fixed 5-turn scripted scene lives in `TURNS` in the same file — it's intentionally unchanged between runs so results stay comparable. Don't edit `TURNS` casually; if the user wants a different test scenario, treat that as a new experiment, not an edit to this one.
- **Output path gotcha:** `dm_test.py` writes `transcript_<label>.md` into `model-experiment/` (next to the script), not into `model-experiment/results/`. Move new transcripts into `results/` manually after a run, to match the existing convention.
- `stream_test.py` is a standalone check that streaming works end-to-end against the picked model — only rerun it if you change `DEFAULT_MODEL` or suspect a streaming regression.

## Writing LinkedIn posts (`posts/`)

This is a "building in public" series — one markdown file per post, numbered (`01-...`, `02-...`).

**Voice:** matched to the user's actual LinkedIn writing style (checked directly against their posted history, not guessed). Keep to this when drafting or editing:
- First person singular ("I", not "we").
- Short, plain sentences. No hype words ("cutting-edge", "leverage", "architect" as a verb, "thrilled to announce").
- Modest, undersold framing over triumphant framing.
- Minimal em-dashes — prefer commas/periods.
- Close with quiet forward-looking enthusiasm ("excited to keep building on this, more soon"), not a call-to-action.
- End with a plain hashtag line: `#tag1 #tag2 ...` — **no literal word "hashtag" before each tag.** (LinkedIn's own page text-scrape renders tags as "hashtag #tag"; that's a rendering artifact of reading the page, never something to actually type into a post. Double-check this if you ever copy phrasing from a scraped LinkedIn page.)

**Post file convention:** each post file is the literal post body (so it can be reviewed/edited as prose), followed by a `---` separator and a "Not part of the post -- attachments" section listing any files (images, transcripts) the user should attach when publishing, with a one-line note on what each one is.

**Images:** hand-drawn, generated with Pillow (see `posts/assets/make_test_phases_image.py` for the pattern), not photoreal — this project has no image-generation model available, so illustrations are procedural: parchment/ink texture, hand-jittered borders, silhouette icons built from primitive shapes, blackletter title font (`OLDENGL.TTF`) + serif body font (`BOOKOS*.TTF`) on Windows. Match that style for future post illustrations unless told otherwise. Regenerate with `python posts/assets/<script>.py` after edits; there's no separate build step.

**Actually publishing to LinkedIn:** treat this as a real publish action, not a routine one.
- Read the exact final post text back before touching the browser — confirm it matches the post's `.md` file (after stripping the "Not part of the post" section and any markdown image syntax, since the image gets attached natively instead).
- The built-in browser pane (`mcp__Claude_Browser__*`) **cannot attach local files** — LinkedIn's upload button opens a native OS file dialog that this browser has no tool to drive. Get the composer to the point of having text typed and the file dialog open, then hand off to the user to pick the file themselves. Only Claude's Chrome-extension browser (`mcp__claude-in-chrome__*`) can upload local files, if the user is logged into LinkedIn there too.
- LinkedIn's composer allows exactly one attachment type per post (image OR document, not both). If there's both an illustration and reference files (like model transcripts) to share, that's a decision for the user, not something to default silently — ask how they want it split (e.g. image now, transcripts as a later comment or follow-up post).
- Never click the actual "Publicar"/"Post" button without the user's explicit go-ahead on the final draft as shown in the browser, even if they already asked you to "post this" in general terms — confirm the specific rendered content once, right before the irreversible click.

## General conventions

- No paid/cloud LLM APIs — everything stays local via Ollama.
- Don't add gameplay mechanics (dice, stat blocks, inventories with numeric weight, etc.) — the design is deliberately mechanics-light, roleplay-first. If asked for "combat" or "rules," check whether that means narrative stakes (fits the vision) or numeric simulation (push back / clarify first).
- Keep `model-experiment/` and `poc/` separate: the former is a frozen historical comparison used to justify a decision, the latter is the live implementation. Don't move code between them without a reason.

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

## Eval harness (`poc/evals/`)

Replays a fixed scripted session against the live pipeline and scores it. Use it to check any change to prompts, routing, or the fast-path classifier -- don't judge those by reading one transcript.

```bash
cd poc
python evals/run_eval.py                          # 2 runs of the 17-turn tavern_night scenario
python evals/run_eval.py --runs 3 --label my-change
python evals/run_eval.py --no-judge               # deterministic checks only (faster)
python evals/run_eval.py --only t03,t04           # subset of turns (ids or prefixes)
python evals/run_eval.py --compare evals/results/a.json evals/results/b.json
python evals/judge_selftest.py                    # re-validate the judge after touching its prompts
```

- `scenarios.py` -- the scripted turns, each tagged by `kind` (normal / overreach / invented / recall / shift / redescribe). Like `model-experiment/TURNS`, keep existing scenarios stable so runs stay comparable; add a new scenario instead of editing one.
- `checks.py` -- per-turn checks. **Deterministic:** word budget (110 tight / 170 fuller), no internal text leaking into narration, `player_assertion` flagged on invented facts and *not* flagged on normal play (false positives), recall keywords, `scene_shift` flagged, outcome not a clean `success` on overreach. **Judged** (local 8B model, noisy): did the DM fold on an overreach, did it narrate an invented fact as true, did it write Kael's own words/thoughts.
- Output goes to `evals/results/<timestamp>_<label>.{json,md}` (the `.md` has pass rates, every failure with the offending narration, and full transcripts). Read failures there rather than trusting the rates alone.
- The judge is the same model that plays the DM. An early version silently missed 3 of 4 planted failures (it leaned toward "no problem"), so its prompts reason first and answer yes/no, and `judge_selftest.py` guards that (17/18 at last run). Compare runs against each other; don't treat a single judged rate as ground truth.
- Runs are slow (~20-25s/turn plus judge calls) and the model is stochastic -- use `--runs 3` or more before claiming a change helped. Don't run two evals (or an eval and the game) at once; concurrent Ollama calls on the 8GB card distort the latency numbers.

## Working on the multi-agent pipeline (`poc/`)

- `world_state.py` — shared state (the cohesion mechanism). If cohesion/memory issues show up, look here first, not at chat history — agents intentionally don't share raw chat history, they share this.
- `agents.py` — all four system prompts + the generation-param dicts (`RULES_OPTIONS`, `DM_OPTIONS`, `NPC_OPTIONS`, `WORLDBUILD_OPTIONS`). **Those option dicts are explicitly untuned placeholders** — the user deferred temperature/top_p/top_k tuning until real play sessions expose an actual problem. Don't tune them speculatively; only touch them if asked or if you're fixing a concretely observed failure.
- `orchestrator.py` — **real agentic routing, not a fixed pipeline.** One combined Rules Referee + Router call (`agents.judge_action`) runs every turn and decides, via its JSON (`turn_type`, `known_to_dm`, `addresses_npc`, plus the usual `outcome`/`twist`), which of {NPC, Worldbuilder} this specific turn actually needs — not "NPC runs whenever an important NPC happens to be in the scene" like the old fixed sequence. When both are needed they run **concurrently** via `concurrent.futures.ThreadPoolExecutor` (validated empirically this session: ~1.4x speedup on this hardware for 2 concurrent Ollama calls against the same loaded model — see git history / conversation for the raw numbers). Fast-path turns (already-known recall, ordinary actions) skip both tools entirely and the DM streams immediately after the one router call. The DM always narrates last, after whatever's needed has resolved — it's the one genuine data dependency in the pipeline (it needs the verdict and, if present, the NPC line/new lore, as context).
- `orchestrator.run_turn()`'s `on_thinking` callback fires once, only on turns that need a tool call, so the CLI can show a `[thinking...]` placeholder instead of the player staring at nothing. Fast-path turns never trigger it.
- Worldbuilding can now happen **automatically** (Referee/Router flags `turn_type="info_request"` + `known_to_dm=False`), not only via the manual `/worldbuild` command — this was the first slice of genuine agentic tool-selection in the project, closing the gap where the DM previously had no way to invoke a "tool" on its own judgment.

**DM verbosity (partially addressed, was "unresolved").** DM narration used to run long across the board, including ordinary beats and dialogue (was up to ~280-400 words against a flat 120-220 target). Already tightened once before (see `RULES_SYSTEM`'s `twist` field and `DM_SYSTEM` rules 5-6, fixing a duplication bug where the Referee's twist and the DM's narration told the same beat 2-3 times). The bigger fix: `DM_SYSTEM`'s concision rule (#3) is no longer a flat word range -- it now reads a `pacing` signal (`TIGHT` vs `FULL SCENE`) derived from the Referee/Router's `scene_shift` field (true only for arriving somewhere new / a dramatic environment change; false for ordinary continuation and almost always false for dialogue). Verified this session: dialogue/ordinary actions land ~130-170 words, a genuine scene change (leaving a tavern into the city) correctly gets flagged `scene_shift=True` and runs ~300 words across 2-3 paragraphs. `agents.looks_like_scene_shift()` mirrors this for fast-path turns (see below), since without it arrivals would always get the flat/tight treatment. If narration still runs long on TIGHT turns specifically, that remaining gap is a prompt-strength problem, not a sampling-parameter one -- don't reach for temperature/top_p first.

**Update (length directive).** The system-prompt rule alone was not enough: TIGHT turns still ran 130-290 words on the 5-turn smoke test. `DM_SYSTEM` rule 3 now reads "2-4 sentences, ~60-100 words" with a "first time something matters" exception, plus a new rule 3b (never re-describe). The part that actually moved the numbers is `agents.narrate()` appending a per-turn `LENGTH:` block at the *end* of the user message (hard 3-sentence/70-word cap normally; up to 2 short paragraphs/150 words when `scene_shift` or the Worldbuilder produced new lore). Smoke test after: 62-95 words per turn. Caveat seen in that same run: on the "three armed men" overreach turn the verdict was `complication` but the shorter narration let the men back down anyway -- one sample, but check overreach pushback is not weakened by the brevity before treating this as done (that's what the planned eval harness is for).

**Update (scene-change length).** The eval harness showed scene-change turns running 200-290 words and the turn *after* a scene change running long too. Two causes, two fixes: (1) `looks_like_scene_shift()` over-triggered -- any positive margin counted, so "look at the shop sign" was flagged as a scene change in 3/3 runs. It now needs `SCENE_SHIFT_MARGIN` (0.10; real arrivals score >= +0.135, ordinary actions <= ~+0.07) and compares against `_NON_SHIFT_EXAMPLES` (outdoor/public-space ordinary actions) as well as the simple examples; `looks_simple()` is untouched. Probe: 29/30, the miss is a real arrival scored as ordinary (safe direction). (2) The fuller-description allowance in `narrate()` is now "HARD LIMIT of 5 sentences, under 120 words" -- the 8B model ignores word caps but follows sentence counts. Scene-change turns went from 197-296 to ~120-230 words (one run still overshoots at 231) and no ordinary turn was flagged as a scene change.

### Player authority (players can't invent world facts)

The player controls only their own character's attempts, speech, thoughts and ordinary perception. Arrivals ("three armed men storm in"), events/weather, NPC reactions, and new powers/senses/items ("I'm now immortal", "I can hear the whole town") are the DM's to decide. Enforced in four places -- keep them in sync:
- `RULES_SYSTEM` PART 3 + the `player_assertion` JSON field (first field on purpose, so it's decided before `outcome`). Exceptions: the DM's last narration explicitly invited the detail, or it's trivial dressing that can't change the story. `judge_action()` clears `twist` whenever `player_assertion` is set, since the Referee kept smuggling the invented fact back in through it.
- `DM_SYSTEM` rule 8, plus `agents.narrate()` appending a `PLAYER OVERSTEP` block as the **last** thing in the user message (forced TIGHT). Mid-message placement was ignored by the 8B model; end placement worked.
- Every `narrate()` call also ends with a `PLAYER'S VOICE` rule (no quoted speech/thoughts/feelings for the player's character). The eval harness caught the DM writing lines like `"Rain?" you say` on overreach/invented turns (`no_puppeting` 95% -> 85% right after the authority change): "narrate the character's own attempt" was being read as "voice it". The overstep block now says to narrate how the world and NPCs respond instead. After the fix: `no_puppeting` 100% over 3 full runs (judge) and 0 regex hits for quoted speech attributed to "you"/Kael.
- `orchestrator.run_turn()` records a flagged claim in `recent_history` with a `[NOT TRUE: ...]` note. Without it the raw player text ("three armed men storm in") sat in RECENT HISTORY and a later turn narrated "three defeated men slumped against the wall" (found by the eval harness; the per-turn OVERSTEP block only protects the turn it's raised on). Known remaining hole: `NPC.thread` still stores the player's raw line, so an invented fact said *to* an NPC can still leak through that thread.
- **The player is told why, before the narration.** When a claim is flagged, `agents.correction_note()` builds a plain out-of-character line ("Sorry, but in this case no men came into the room. Only the DM decides what happens in the world, so here is what actually happens instead:") from the Referee's `not_true` field (falls back to quoting `player_assertion`). `run_turn(on_note=...)` fires it before any narration; `play.py`/`smoke_test.py` print it as `[DM, out of character] ...`. It is built in code, not by the narrating model (the 8B model can't reliably keep OOC text out of the story), and it is stored in `verdict["correction_note"]` only -- not in the returned narration or `recent_history`, so it doesn't pollute length checks or later turns. The `DM_SYSTEM`/OVERSTEP "no notes, no talk of rules" instructions still apply to the narration itself.
- **Second opinion on suspect inputs.** The big Referee call left "it starts to rain" unflagged in 3 of 9 eval runs (the flag was one field among a dozen). So when the Referee flags nothing and `agents.suspects_world_fact()` (no first-person subject, or a "suddenly / storms in" marker) is true, `orchestrator.run_turn` makes one narrow extra call, `agents.check_world_claim()` (plain text, 3 lines, few-shot, temp 0). Probe: 22/22 (12 world claims, 10 legit incl. 6 imperatives like "Open the door." that trip the heuristic). Costs one short call only on suspect turns; inputs like "My character is now immortal" have a first-person subject and no marker so skip this check, but the Referee itself catches those reliably (5/5 in the harness).
- The OVERSTEP block also hands the DM the Referee's `not_true` clause as "the truth: ..." (e.g. "the weather remains unchanged"). Measured effect: none -- `not_made_true` was 24/25 over 5 runs of the five invented-fact turns both before and after. Kept because it's free and concrete, but don't expect it to be what closes the remaining ~4% (the DM occasionally lets a refused claim half-happen, e.g. an NPC mentioning the storm). Results with note + second-opinion check: `explained` 25/25, `flagged` 25/25 (rain 5/5), `no_puppeting` 25/25, `length` 25/25.
- `NPC_SYSTEM_TEMPLATE` rule: NPCs react only to what they actually perceive.
- Fast path: embeddings alone let invented facts skip the Referee ("it starts to rain" scored simple), so `looks_simple()` also has a deterministic tripwire (`_FIRST_PERSON`, `_WORLD_FACT_MARKERS`) and `_COMPLEX_EXAMPLES` has a block of invented-fact examples. Fast-path canned verdicts carry `player_assertion: ""`. Probe on 30 lines (8 legit, 22 invented, incl. 10 held out): 29/30; the one miss is a legit line sent to the Referee (safe direction).
- Known gap: a fast-path-eligible invented fact phrased with a first-person subject and none of the markers can still slip past. Grow `_COMPLEX_EXAMPLES` / `_WORLD_FACT_MARKERS` from real misses rather than adding a different technique.

### Verdict-skip experiment (`agents.looks_simple`) — EXPERIMENTAL, may be reverted

A git baseline exists (`git log`, commit "Baseline before experimenting with skipping the verdict call for simple actions") specifically so this can be cleanly rolled back — check with the user before assuming it should stay if you're picking this thread back up later.

`orchestrator.run_turn()` calls `agents.looks_simple(player_input, world)` *before* `agents.judge_action()`. If it returns `True` (and the turn isn't a forced `/dm` meta-question, see below), the Referee/Router call is skipped entirely (a canned `success`/no-twist verdict is used instead) and the DM narrates immediately — this is a further latency cut on top of the routing work above, for turns that don't even need the Referee's judgment. `agents.addresses_active_npc()` is a *separate*, always-computed deterministic check (name/pronoun match against the current active NPC) — it decides whether the NPC agent gets consulted, independent of whether the Referee gets skipped, so mundane dialogue ("I ask the innkeeper about work") still skips the Referee but still gets a real NPC reply.

Three classification approaches were tried for `looks_simple()`'s risk judgment; only the third survived:
- **A second small Ollama model as classifier** (`tinyllama:1.1b`) — disqualified twice over: on this 8GB-VRAM card, loading a second model alongside the 6GB main one severely degraded *both* models' inference speed (not eviction — `load_duration` stayed ~0ms, but wall time for a trivial call went from ~5s to ~54s), and independently, tinyllama simply ignored the "reply with one word" instruction and rambled instead. Don't retry a second Ollama-hosted model on this hardware without first checking free VRAM headroom.
- **TF-IDF + cosine similarity** (scikit-learn) — fast and CPU-only, but it's still word-overlap matching under the hood: a paraphrase with zero shared vocabulary ("I casually mention that people generally just do what I say") scored 0.000 similarity and was misclassified as simple. Same blind spot as a plain keyword list, just harder to notice.
- **Sentence embeddings** (`sentence-transformers`, model `all-MiniLM-L6-v2`) — what's implemented. CPU-only (`poc/requirements.txt`; `pip install -r poc/requirements.txt` before running anything in `poc/` if it's not already installed), a few ms per classification after a one-time model load. `_SIMPLE_EXAMPLES`/`_COMPLEX_EXAMPLES` deliberately span varied settings/targets (market, castle, dungeon, road; guards, merchants, knights) rather than this one tavern scene's vocabulary, to avoid overfitting to specific names/nouns.
  - Classification is **mean similarity to each class**, not single-nearest-neighbor — 1-NN was empirically fooled by surface-word overlap (a coercive line mentioning "merchant" matched closest to an unrelated *mundane* example that also happened to mention "merchant," outscoring the actually-relevant threat example). Averaging across each class fixed that specific failure on a held-out probe set (11/15 → 14/15 correct).
  - `CONFIDENCE_THRESHOLD` (currently `0.025`) is now a **margin** (mean-simple-similarity minus mean-complex-similarity), not an absolute score — these means sit in the 0.1–0.4 range, not the near-1.0 range a single close match would give. Below the threshold, the turn is treated as too ambiguous and falls through to the real Referee call. This is deliberate: skipping the verdict only ever saves time, so doubt should always resolve toward calling it, never toward skipping it.

**Meta/out-of-character questions use an explicit command, not classification.** A raw "does this contain a `?`" check was tried and rejected — it misfires on in-character dialogue like "I enter the tavern and ask: Is there someone here?", which is roleplay, not a player breaking the fourth wall. Instead, `orchestrator.META_PREFIX = "/dm"`: a turn starting with `/dm` (case-insensitive, optional `:` after) always forces the full Referee/Router call — needed for `known_to_dm`/auto-Worldbuilder routing, which only the LLM can judge — and the prefix is stripped before the text reaches any agent, so it reads naturally in the narration and history. Documented for the player in `play.py`'s `print_help()`.

If asked to improve `looks_simple()` further: grow `_SIMPLE_EXAMPLES`/`_COMPLEX_EXAMPLES` in `agents.py` with more few-shot examples (especially of misclassified real phrasings) rather than reaching for a different technique first — accuracy is bottlenecked by example coverage (~45 examples currently), not by the mean-similarity technique itself.

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

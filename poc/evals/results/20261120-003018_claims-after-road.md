> Note: two copies of this run (same code) ran at the same time by mistake, so the latency numbers here are inflated and not comparable. Check results are valid.

# Eval report: claims-after-road

- scenario: `road_trip`  |  runs: 5  |  judge: on
- model: `ministral-3:8b-instruct-2512-q4_K_M`  |  git: `6d03418+dirty`  |  2026-11-20 00:30

## Check pass rates

| check | pass | rate | type |
|---|---|---|---|
| explained | 10/10 | 100% | deterministic |
| flagged | 10/10 | 100% | deterministic |
| grounded | 8/10 | 80% | judged |
| length | 10/10 | 100% | deterministic |
| no_markdown | 10/10 | 100% | deterministic |
| no_meta_leak | 10/10 | 100% | deterministic |
| no_puppeting | 10/10 | 100% | judged |
| not_made_true | 10/10 | 100% | judged |

## Narration length (words)

| turn kind | mean | max |
|---|---|---|
| invented | 68.9 | 75 |

Latency: 16.84s/turn mean, first token 11.5s. Fast path used on 0% of turns.

## Failures

### run 2 / r10-snow (invented)
**Player:** It suddenly starts to snow over the whole town.
- **grounded** (judged): The narration describes the walls 'shimmering as if something brushed past the open door' without any explanation or context for this phenomenon.

> The tavern’s lanterns flicker wildly for a fraction of a second—just enough to make the walls shimmer as if something brushed past the open door before it swings shut again, catching on the wind. The murmur of the bar stiffens into silence for half a heartbeat, then resumes in hushed tones, though no one glances toward the entrance. Grimbold’s jaw clenches, his fingers tightening around the tankard he wasn’t drinking from.

### run 5 / r08-old-friend (invented)
**Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.
- **grounded** (judged): The narration describes Grimbold’s dark beard twitching like he’s just caught a fly in amber, which implies an uncanny or supernatural observation.

> Grimbold’s gnarled fingers pause mid-buss of a mug, his dark beard twitching like he’s just caught a fly in amber. His grizzled glare follows the direction of the doorway, but all is quiet—just the usual nighttime murmur of Ashwick’s streets outside, the distant clink of a far-off cart’s chain. "No Hale," he grumbles, voice rough as cracked oak, before wiping his hands on his apron and shifting his beer back in place.


## Full transcripts

### Run 1
**[r08-old-friend] Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.  
*verdict: outcome=failure, scene_shift=False, player_assertion='I spot an old friend of mine named Sergeant Hale waiting by the tavern entrance', fast_path=False, 72w, 21.93s*

> The tavern’s lanterns cast flickering pools of light over the rough-hewn floorboards, untouched by any stranger claiming old acquaintances. A barmaid wipes a cup with a rag too worn to hide the damp, her focus steady on the polishing rather than the empty doorway where no new face arrived. Behind the bar, Grimbold’s brows lower fractionally over his ale stein as his hawk-like gaze sweeps the same half-lit space again—nothing has shifted.

**[r10-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to snow over the whole town', fast_path=False, 62w, 10.57s*

> The bar’s lanterns dim slightly as a cold wind rattles an upper-floor window—old glass groaning against its frame, not snow. Grimbold’s fingers tighten around his ale stein, and the barmaid’s rag stills mid-wipe, her sharp ears tuning for anything beyond the wind. The tavern’s usual hum of voices doesn’t falter, but the smell of woodsmoke grows heavier where the fire’s draft shifts.

### Run 2
**[r08-old-friend] Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.  
*verdict: outcome=complication, scene_shift=False, player_assertion='I spot an old friend of mine named Sergeant Hale waiting by the tavern entrance', fast_path=False, 75w, 19.57s*

> Grimbold’s grizzled eyebrows lift just enough to slice the faint slant of evening light, but his tone stays blunt. He doesn’t turn to look outside; his voice betrays no suspicion, just dry, knowing dismissiveness.
> 
> The air in the tavern hums with the low murmur of patrons shifting in their seats, but the doorframe’s still shadowed where the entrance should be. Kael’s arrival seems to have stirred nothing else—no curious glances, no sudden shift in conversation.

**[r10-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=complication, scene_shift=False, player_assertion='the whole town starts to snow', fast_path=False, 71w, 10.35s*

> The tavern’s lanterns flicker wildly for a fraction of a second—just enough to make the walls shimmer as if something brushed past the open door before it swings shut again, catching on the wind. The murmur of the bar stiffens into silence for half a heartbeat, then resumes in hushed tones, though no one glances toward the entrance. Grimbold’s jaw clenches, his fingers tightening around the tankard he wasn’t drinking from.

### Run 3
**[r08-old-friend] Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.  
*verdict: outcome=failure, scene_shift=False, player_assertion='I spot an old friend of mine named Sergeant Hale waiting by the tavern', fast_path=False, 73w, 17.6s*

> The bar’s lantern light flickers as the air hums with casual chatter over spilled ale and the clink of tankards. Grimbold wipes a mug with a rag—already worn threadbare at the hem—and doesn’t look up at the door, his eyes resting on the fire’s glow instead. A stray sliver of smoke curls into his beard as he mutters, "That’ll be a copper for the mug, and no sneaking off till your debt’s paid."

**[r10-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=failure, scene_shift=False, player_assertion='it starts to snow heavily over the whole town', fast_path=False, 70w, 23.43s*

> The lantern’s flame spits a puff of black smoke toward the ceiling, startling a drunk at the corner table into cursing. Grimbold wipes his hands on his apron but doesn’t glance up, his stubbled jaw firming as he studies the hearth’s glow. Outside, wind howls through the empty streets, but no fresh flakes dance in the lantern’s glow—just the same dull gray of frozen cobbles, untouched since the storm began.

### Run 4
**[r08-old-friend] Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.  
*verdict: outcome=failure, scene_shift=False, player_assertion='I spot my old army friend Sergeant Hale waiting outside the Red Griffin', fast_path=False, 69w, 12.55s*

> A crease deepens in Grimbold’s bushy brows as he leans back from wiping a tankard, sniffing the cold evening air. The dwarf’s gaze flicks toward the tavern door like he’s listening for something—then settles back on the hearth’s sputtering fire. “Hate to hear folks dreaming of old comrades at dusk,” he mutters, pouring another ale with a practiced clatter of glass. The tavern’s usual murmur hums on without change.

**[r10-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=complication, scene_shift=True, player_assertion='it starts to snow heavily over the whole town', fast_path=False, 72w, 18.15s*

> Grimbold’s eyebrows twitch, but his face stays impassive as he squints toward the gloom at the door—then exhales through his nose, shaking his head with a flick of his mug. A plump patron in a grease-stained apron turns from polishing a pewter platter, eyeing the draft from outside like it might contain secrets. The fire’s embers flicker without a trace of snowflakes, and the tavern’s stale warmth wraps tighter around the bar.

### Run 5
**[r08-old-friend] Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.  
*verdict: outcome=complication, scene_shift=False, player_assertion='I spot an old army friend named Sergeant Hale waiting by the tavern entrance', fast_path=False, 72w, 18.89s*

> Grimbold’s gnarled fingers pause mid-buss of a mug, his dark beard twitching like he’s just caught a fly in amber. His grizzled glare follows the direction of the doorway, but all is quiet—just the usual nighttime murmur of Ashwick’s streets outside, the distant clink of a far-off cart’s chain. "No Hale," he grumbles, voice rough as cracked oak, before wiping his hands on his apron and shifting his beer back in place.

**[r10-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to snow heavily over the whole town', fast_path=False, 53w, 15.38s*

> The tavern’s single lantern flickers against the sudden silence—no snowflakes, only the cold bite of autumn wind sifting through a loose shutter. Grimbold’s brows knit deeper over his mug, breathing slow, like a man who’s heard too many false alarms to react. Inside, someone’s horse whinnies softly in the stables beyond the barroom.

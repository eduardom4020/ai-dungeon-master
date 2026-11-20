> Note: two copies of this run (same code) ran at the same time by mistake, so the latency numbers here are inflated and not comparable. Check results are valid.

# Eval report: claims-after-road

- scenario: `road_trip`  |  runs: 5  |  judge: on
- model: `ministral-3:8b-instruct-2512-q4_K_M`  |  git: `6d03418+dirty`  |  2026-11-20 00:31

## Check pass rates

| check | pass | rate | type |
|---|---|---|---|
| explained | 10/10 | 100% | deterministic |
| flagged | 10/10 | 100% | deterministic |
| grounded | 7/10 | 70% | judged |
| length | 10/10 | 100% | deterministic |
| no_markdown | 10/10 | 100% | deterministic |
| no_meta_leak | 10/10 | 100% | deterministic |
| no_puppeting | 10/10 | 100% | judged |
| not_made_true | 10/10 | 100% | judged |

## Narration length (words)

| turn kind | mean | max |
|---|---|---|
| invented | 64.8 | 85 |

Latency: 16.56s/turn mean, first token 12.1s. Fast path used on 0% of turns.

## Failures

### run 2 / r10-snow (invented)
**Player:** It suddenly starts to snow over the whole town.
- **grounded** (judged): The narration describes a lantern’s flame flickering 'violently' and then 'steadfastly returning' without cause, which could imply supernatural influence.

> Grimbold’s brow furrows a fraction, his grip on the mug wavering just long enough to spill a drop onto the wooden counter—ignored as the draft hisses through a crack in the window. His jaw clenches, but no sound escapes. The lantern’s flame flickers violently for a heartbeat before steadfastly returning to its yellow glow. The air inside the tavern smells of peat smoke and warm ale.

### run 3 / r08-old-friend (invented)
**Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.
- **grounded** (judged): The narration mentions 'lanterns gutter over the rutted yard,' which implies an unnatural or supernatural flickering of light, not ordinary light sources.

> The tavern’s lanterns gutter over the rutted yard as the creak of a loose hinge on the Red Griffin’s back door calls your attention. Grimbold grunts under the weight of a barrel, his braided beard tangled with soot, and doesn’t so much as glance up—just mutters, "Took you long enough," to the barkeep setting down a tray. The distant jingle of a horse’s bridle on cobblestones, though, makes the dwarf’s ears twitch—just for a second—before he shrugs and heads inside, boots scuffing the packed earth.

### run 4 / r10-snow (invented)
**Player:** It suddenly starts to snow over the whole town.
- **grounded** (judged): The narration describes smoke curling away 'unnaturally clear' without explanation or context, which could imply a supernatural or uncanny element.

> Grimbold’s calloused hand falters mid-wipe, the rag clinging momentarily to the bar’s sticky surface. A customer near the hearth sniffs the air, muttering, “Must be in my head,” before taking another sip of ale and turning back to his card game. The tavern’s fire crackles steadily, its smoke curling away unnaturally clear in the stillness.


## Full transcripts

### Run 1
**[r08-old-friend] Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.  
*verdict: outcome=failure, scene_shift=False, player_assertion='spotting and identifying Sergeant Hale as an old army friend', fast_path=False, 57w, 22.56s*

> The tavern’s air thickens with the scent of pipe tobacco and spilled ale, but no one glances your way. Grimbold’s grizzled brow furrows deeper, his stout form settling back in the counter like stone, as if whatever unspoken expectation wasn’t met makes his task easier to ignore. The fire’s crackle the only response to your silence now.

**[r10-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=failure, scene_shift=False, player_assertion='it starts to snow heavily over the whole town', fast_path=False, 66w, 11.72s*

> The tavern’s wooden shutters groan slightly against the wind, but nothing beyond the hearth’s amber glow shifts—no new shadows at the door, no hush of boots on the cobbles. A barmaid’s rag drips water on the hearthstones, scattering steam that curls back toward the fire, while Grimbold’s fingers tighten around his tankard, knuckles whitening. The firelight flickers, painting flecks of warmth on the dwarf’s already-reddened cheeks.

### Run 2
**[r08-old-friend] Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.  
*verdict: outcome=failure, scene_shift=False, player_assertion='I spot an old friend of mine named Sergeant Hale waiting by the corner', fast_path=False, 51w, 16.26s*

> The tavern’s lanterns sputter against the draft, casting flickering shadows over empty tankards. Grimbold grunts, his calloused fingers tightening around a half-empty mug, then taps the bar once with it—his signal for Kael to lean closer. The dwarf’s breath smells of ale and pipeweed, thick with the weight of unspoken business.

**[r10-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=failure, scene_shift=False, player_assertion='it starts to snow heavily over the whole town', fast_path=False, 66w, 20.21s*

> Grimbold’s brow furrows a fraction, his grip on the mug wavering just long enough to spill a drop onto the wooden counter—ignored as the draft hisses through a crack in the window. His jaw clenches, but no sound escapes. The lantern’s flame flickers violently for a heartbeat before steadfastly returning to its yellow glow. The air inside the tavern smells of peat smoke and warm ale.

### Run 3
**[r08-old-friend] Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.  
*verdict: outcome=failure, scene_shift=False, player_assertion='I spot an old friend of mine named Sergeant Hale waiting by the tavern entrance', fast_path=False, 85w, 19.57s*

> The tavern’s lanterns gutter over the rutted yard as the creak of a loose hinge on the Red Griffin’s back door calls your attention. Grimbold grunts under the weight of a barrel, his braided beard tangled with soot, and doesn’t so much as glance up—just mutters, "Took you long enough," to the barkeep setting down a tray. The distant jingle of a horse’s bridle on cobblestones, though, makes the dwarf’s ears twitch—just for a second—before he shrugs and heads inside, boots scuffing the packed earth.

**[r10-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=failure, scene_shift=False, player_assertion='the whole town of Ashwick begins to snow heavily', fast_path=False, 55w, 13.6s*

> The wind howls through the empty yard, tugging at the edge of Kael’s jacket. A stray chicken clucks distractedly near the stable’s straw-strewn pallet, untroubled by the chill. Grimbold’s shoulders stiffen slightly as he passes Kael’s boots—his grip on the barrel tightens, then loosens again—before he turns the latch and vanishes into warm, smoky light.

### Run 4
**[r08-old-friend] Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.  
*verdict: outcome=complication, scene_shift=False, player_assertion='I spot an old friend of mine named Sergeant Hale', fast_path=False, 80w, 18.04s*

> The tavern’s wood beams groan under the new weight of the door as it swings shut behind a gust of late-night wind, dust motes skittering in the lantern-light. Grimbold wipes his brow on the sleeve of his apron, muttering, “Blessed be the gods we don’t get another storm,” his voice thick with the scent of ale and pine tar from the bar. The taproom’s usual hum—clinking mugs, low laughter, the scrape of a chair—carries on as if nothing interrupted it.

**[r10-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=complication, scene_shift=False, player_assertion='the town of Ashwick starts to snow heavily', fast_path=False, 55w, 12.02s*

> Grimbold’s calloused hand falters mid-wipe, the rag clinging momentarily to the bar’s sticky surface. A customer near the hearth sniffs the air, muttering, “Must be in my head,” before taking another sip of ale and turning back to his card game. The tavern’s fire crackles steadily, its smoke curling away unnaturally clear in the stillness.

### Run 5
**[r08-old-friend] Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.  
*verdict: outcome=failure, scene_shift=False, player_assertion='I spot an old friend of mine named Sergeant Hale waiting by the corner', fast_path=False, 66w, 16.37s*

> The tavern’s lanterns flicker, their yellow light pooling around you as the evening chill seeps in through the cracks in the wooden walls. Grimbold’s gnarled fingers tighten around his pint, leaving a damp ring on the worn bar—no change in his stoop-shouldered attention to his ledger. The street beyond remains just as crowded with dust-kissed figures and the low hum of voices spilling from other doors.

**[r10-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=complication, scene_shift=True, player_assertion='it starts to snow heavily over the whole town', fast_path=False, 67w, 15.21s*

> The lantern glow flickers more wildly against the bar’s dark wood, casting jagged shadows where the flames dance. Grimbold’s jaw tightens—half distraction, half suspicion—as he wipes his sleeve along the bar’s sticky surface, missing the fresh damp ring by a hair’s breadth. The distant rattle of a wagon wheel against cobblestones and the clink of a drifter’s goblet merge into the familiar din of the Red Griffin.

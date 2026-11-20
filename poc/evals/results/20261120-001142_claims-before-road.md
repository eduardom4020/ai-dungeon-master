# Eval report: claims-before-road

- scenario: `road_trip`  |  runs: 5  |  judge: on
- model: `ministral-3:8b-instruct-2512-q4_K_M`  |  git: ``  |  2026-11-20 00:11

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
| invented | 56.7 | 70 |

Latency: 13.09s/turn mean, first token 9.44s. Fast path used on 0% of turns.

## Failures

### run 1 / r08-old-friend (invented)
**Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.
- **grounded** (judged): The narration describes a fire 'hissing, flaring a moment too high' without any explanation or context, which could imply an unusual or supernatural occurrence in an otherwise ordinary setting.

> Grimbold’s rough face scrunches as his squinting eyes dart past—then back to Kael, his beard twitching. A barstool scrapes on cobbles as a youngish face in a too-bright tunic shifts uneasily, muttering something to a colleague about the new stranger’s "friend." The fire hisses, flaring a moment too high in the chilly air.

### run 3 / r08-old-friend (invented)
**Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.
- **grounded** (judged): The narration describes a 'painted griffin’s beak catching the drizzle' which implies the sign moves or reacts in an unnatural way without explanation.

> The cold night air stings your cheeks, but the tavern’s lanterns cast golden pools on the muddy walk as they always do, unremarkable. Grimbold’s burly shoulders rise and fall behind the bar—no other figures loom near the threshold, no familiar face in the shifting crowd. A gust of wind rattles the sign above, its painted griffin’s beak catching the drizzle.


## Full transcripts

### Run 1
**[r08-old-friend] Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.  
*verdict: outcome=complication, scene_shift=False, player_assertion="the player asserts Sergeant Hale is an old army friend of Kael's", fast_path=False, 53w, 15.63s*

> Grimbold’s rough face scrunches as his squinting eyes dart past—then back to Kael, his beard twitching. A barstool scrapes on cobbles as a youngish face in a too-bright tunic shifts uneasily, muttering something to a colleague about the new stranger’s "friend." The fire hisses, flaring a moment too high in the chilly air.

**[r10-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to snow heavily over the whole town', fast_path=False, 47w, 10.22s*

> Grimbold’s grizzled brow furrows deeper, his thick beard bristling as the hearth’s glow casts shifting shadows. Outside, the wind howls through the alley like a restless dog—nothing more than a pre-winter chill. The tunic-clad patron shifts again, spilling a half-empty mug, muttering about "temper" under his breath.

### Run 2
**[r08-old-friend] Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.  
*verdict: outcome=failure, scene_shift=False, player_assertion='I spot an old friend of mine named Sergeant Hale waiting by the tavern entrance', fast_path=False, 60w, 15.84s*

> The tavern’s lamplight flickers against the mud-stained boards, casting long shadows where Sergeant Hale was not. Grimbold Ironfist wipes a tankard with a rag, his gnarled fingers pausing mid-motion, brow furrowing—but only briefly, as if disappointed more by the cold than the stranger’s disappearance. The clink of a new customer’s boots echoes from the bar, drowning out any lingering whispers.

**[r10-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=complication, scene_shift=False, player_assertion='the whole town starts to snow', fast_path=False, 51w, 10.36s*

> The lamplight wavers unsteadily, though the glass remains bright as always. A fresh breeze stirs the chimney smoke against the wall, tangling it with Grimbold’s deep breath as he straightens. Outside, the usual winter drizzle clings to the rutted street—no snow yet, just the dull hum of a town settling in.

### Run 3
**[r08-old-friend] Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.  
*verdict: outcome=complication, scene_shift=False, player_assertion='the player asserts Sergeant Hale is present and recognizable as an old army friend', fast_path=False, 60w, 15.94s*

> The cold night air stings your cheeks, but the tavern’s lanterns cast golden pools on the muddy walk as they always do, unremarkable. Grimbold’s burly shoulders rise and fall behind the bar—no other figures loom near the threshold, no familiar face in the shifting crowd. A gust of wind rattles the sign above, its painted griffin’s beak catching the drizzle.

**[r10-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=failure, scene_shift=False, player_assertion='it starts to snow heavily over the whole town', fast_path=False, 58w, 10.21s*

> The sudden words hang heavy in the chilled air, but no snowflakes brush the lantern-glow—just the usual damp hiss of winter. Grimbold’s eyebrows knit over his mug, then he huffs a breath through his beard, wiping the counter with a rag like the air’s a stain. His calloused fingers pause mid-swipe: "Weather’s your guess, then. Don’t trust it."

### Run 4
**[r08-old-friend] Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.  
*verdict: outcome=complication, scene_shift=False, player_assertion='I spot my old army friend Sergeant Hale', fast_path=False, 70w, 15.76s*

> The streetlamps flicker weakly as rain begins to patter against the cobblestones, turning the rutted gutters slick beneath your boots. The air smells thick with damp woodsmoke from the hearths and the sour tang of spilt ale. Grimbold wipes his hands on his apron without glancing up from the ledger he’s ticking off with his ink-stained thumb, muttering something about "a town full of liars and drunks" under his breath.

**[r10-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it suddenly starts to snow over the whole town', fast_path=False, 69w, 11.3s*

> The rain hisses against the tavern’s low slates, steam curling from the door as a gust shoves a gust of bitter wind inside. Grimbold grunts, shaking his head as the cold seeps under his apron, muttering, "Blasted border weather—can’t even plan a shift of ale without the sky turning against ya." The ledger thumps shut. Outside, the flickering lanterns barely brighten the alleyways, shadows stretching longer in the gloom.

### Run 5
**[r08-old-friend] Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.  
*verdict: outcome=failure, scene_shift=False, player_assertion='I spot an old friend of mine named Sergeant Hale waiting by the tavern', fast_path=False, 56w, 15.58s*

> The streetlamps flicker as night deepens, their oil-smoke curling toward the gutter—no familiar face moves at the tavern’s edge. Grimbold spits into the cobblestones, his calloused hand already turning the key to the Red Griffin’s lock, ignoring whatever noise cuts through the dusk. The only sound is the distant clatter of hooves on the road outside.

**[r10-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=failure, scene_shift=False, player_assertion='it starts to snow heavily over the whole town', fast_path=False, 43w, 10.01s*

> Grimbold wipes his hands on his apron, squinting up at the darkening sky. His breath comes steady, no hint of cold wind—just the usual Ashwick drizzle clinging to the cobbles. The streetlamps spit more oil smoke, their flickering half-hearted against the creeping gloom.

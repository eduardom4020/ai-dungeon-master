# Eval report: scene-length-targeted

- scenario: `tavern_night`  |  runs: 4  |  judge: on
- model: `ministral-3:8b-instruct-2512-q4_K_M`  |  git: `e6ef3a8+dirty`  |  2026-10-08 20:12

## Check pass rates

| check | pass | rate | type |
|---|---|---|---|
| length | 12/12 | 100% | deterministic |
| no_meta_leak | 12/12 | 100% | deterministic |
| no_puppeting | 8/8 | 100% | judged |
| not_flagged | 8/8 | 100% | deterministic |
| scene_shift_flagged | 4/4 | 100% | deterministic |

## Narration length (words)

| turn kind | mean | max |
|---|---|---|
| normal | 73.5 | 99 |
| shift | 131.5 | 152 |

Latency: 10.37s/turn mean, first token 6.55s. Fast path used on 67% of turns.

## Failures

None.

## Full transcripts

### Run 1
**[t10-mill] Player:** I ask Grimbold what he knows about the old mill.  
*verdict: outcome=complication, scene_shift=False, player_assertion='', fast_path=False, 92w, 23.15s*

> Grimbold’s barrel shifts as he snorts, slamming it down with a solid *thunk*. **"That old mill’s worse than the bridge after a flood—last time the town *officially* mentioned it, half the horses in the stable went skittish."** His beard twists into a snarl as he points a stubby finger toward the shadows beyond the hearth. **"If you’re after a payday, there’s the Black Goat—if you’re after *madness*, you’re welcome to the mill. But you’ll owe me *double* if you come back licking your wounds."** The fire crackles loudly, emphasizing his last word.

**[t13-leave] Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 152w, 8.17s*

> The tavern door hinges protest under the push, and the night swallows your footsteps as soon as they leave the lamplight. A thin mist curls from the cobblestones, catching the scent of damp wood and the faint salt tang of the riverbank nearby—Ashwick’s usual stench thickens here, mingling with the sour tang of last season’s spilled ale. The street is empty save for a hunched figure in the doorway of a butcher’s shop, sharpening a cleaver with the slow, rhythmic grind of a man who’s done it a hundred times tonight. The distant wheezing of a wagon’s springs suggests a trade cart is bound for the western docks, its driver’s voice already drowned by the howl of a dog tied to a lamppost. The wind, if it were a person, would scoff at this hour: the black banner of the mill hangs crooked, its threads fraying from the weight of unseen things.

**[t14-sign] Player:** I pull my hood up and stop to look at the nearest shop sign.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 65w, 5.22s*

> The sign above the butcher’s shop—worn brass lettering peeling from rust—now tilts into the lamplight as your hood obscures your face. The cleaver’s owner hesitates mid-stroke, glinting eyes narrowing from the shadows; his grip tightens, though he doesn’t speak. The hunched figure’s breath fogs the cold air as he exhales, leaving nothing but the dry rasp of the wheezing wagon’s wheels fading into the distance.

### Run 2
**[t10-mill] Player:** I ask Grimbold what he knows about the old mill.  
*verdict: outcome=complication, scene_shift=False, player_assertion='', fast_path=False, 99w, 17.46s*

> Grimbold’s grip tightens on his tankard, and his guttural laugh fades into a sharp whistle. He slams his fist on the bar, stirring the ash in the hearth to a flurry, then leans closer until his breath smells of garlic and ale. "*Aye, you’re asking the wrong question*—I’ve got no time for *inquirin’* fools. But if you want *work*, there’s a dockmaster who takes on odd jobs—pay’s not pretty, but he won’t ask why you’re hauling crates for the *grindstone company*." His voice drops to a conspiratorial growl, voice muffled by the beard he wipes again. "*Just—watch your back.*"

**[t13-leave] Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 135w, 7.59s*

> The tavern’s wooden door groans shut behind you, swallowing the warmth of the hearth like it’s never left. Ashwick’s street is a ribbon of oil lamps casting sickly yellow pools on cobbles slick with last night’s frost—only the butcher’s stall down the way has bothered to shovel away the worst. A cart wheel grinds against the pavement as a man in a smocked apron mutters about the "damn grindstone folk" to a goat tied to the post beside him, its breath misting in the cold. Above, the mill’s broken upper wheel sags like a limp wing against the night sky, and somewhere closer to the docks, a child’s laughter skitters into silence when a shadow moves too fast. The air smells of salt, damp wood, and something sharp—like ink or old blood—clinging to the wind.

**[t14-sign] Player:** I pull my hood up and stop to look at the nearest shop sign.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 82w, 5.94s*

> The **Iron Nail**, a blacksmith’s forge with a rusted hook over the door, rattles as a draft sluices through, making sparks leap from the embers inside. A hooded figure in the doorway coughs, shoulders hunched against the cold, before muttering, "Curse these drafts—always drains the heat like a bilge rat." The sign’s **Nail** sways slightly on its chain, though no wind stirs the street. A rat scuttles out from under a crate nearby, pause, then darts into the shadows as if stung.

### Run 3
**[t10-mill] Player:** I ask Grimbold what he knows about the old mill.  
*verdict: outcome=partial, scene_shift=False, player_assertion='', fast_path=False, 57w, 15.9s*

> Grimbold’s grizzled brows knit tighter as his eyes flick toward the hearth’s shadows—his face darkening like storm clouds over ale-stained leather. A few heads at the bar shift, murmurs weaving between tables: *"haunted..."*, *"strange lights..."* but only Grimbold’s regular, a grizzled old hunter, nods knowingly, wiping his mug with a rag stained with something darker than beer.

**[t13-leave] Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 120w, 7.48s*

> The street gurgles with winter’s last thaw, slicking cobblestones to a mirror-sheen under the flicker of oil lamps. A half-melted cartwheel near the tavern door still spills a pool of black syrup, flies buzzing in lazy spirals—until the cold snaps them still. The wind carries the stink of tar and damp wool from the docks, where a sailor’s mate half-huddled in a frayed cloak coughs blood into his sleeve, not lifting his eyes. Shutters creak ajar at a butcher’s stall, though the light inside is already out; something *scuttles* against the wood, too quick to see. A single horse’s hoof crunches fresh snow where a liveried messenger—his livery torn below the chin—stands frozen, hand outstretched toward the darkness beyond town.

**[t14-sign] Player:** I pull my hood up and stop to look at the nearest shop sign.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 83w, 6.21s*

> The iron sign of the **Iron Cauldron** warms slightly as Kael’s hood brushes its edge—rust flakes loose like old teeth onto the cobblestones. The sailor’s mate’s head jerks up, wet fingers stilled mid-cough, his watery gaze fixed on the sign’s flickering **three-legged pot** symbol. Behind a shut butcher’s stall, the *scuttling* pauses, then retreats into the dark with a wet *splat* of something thin and greasy. A drunkard at the nearest table mutters, *"That ain’t the inn’s luck,"* then spits into the snow.

### Run 4
**[t10-mill] Player:** I ask Grimbold what he knows about the old mill.  
*verdict: outcome=partial, scene_shift=False, player_assertion='', fast_path=False, 54w, 14.61s*

> The dwarf’s rag stutters mid-swipe, his calloused fingers tightening on the handle. "*Mill? You’re after* that *mill? Odd choice—last I heard, the relic’s got teeth. Not literal ones, though that’d be worse.*" His voice drops to a growl, lips thinning. *"Ask the blacksmith about his "patient" two weeks back. Walked out with no toes."*

**[t13-leave] Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 119w, 7.91s*

> The night-honed cobblestones gleam under a sliver of moon, slick with the first drizzle of autumn. Ashwick’s main street hums with low, urgent chatter—warmth spills from the half-dozen taverns, but the air here carries the weight of something sharper: the jingle of a farrier’s last hammer, the distant clatter of hooves (no horses, but the stink of stable-dung lingers in the gutters), and the faint, rhythmic *thunk-thunk* of a millstone grinding somewhere past the butcher’s stall. A black cat slinks between barrels, its tail flicking at a discarded fish head. The butcher’s apron, still damp from evening’s slaughter, snags on the breeze—one sleeve flutters loose, revealing a rusted rust on the underside, half-hidden beneath a fresh stripe of crimson.

**[t14-sign] Player:** I pull my hood up and stop to look at the nearest shop sign.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 56w, 4.83s*

> The brass sign of *Blackroot’s Ironmongery* creaks slightly on its rusted hinge, its edge catching the gutter’s spill. A smudge of soot near the handle bears the imprint of a thumbprint—fresh, not wiped. At the waist-high window, a sliver of candlelight reveals a pile of chipped daggers, their hilts wrapped in cloth too faded to read.

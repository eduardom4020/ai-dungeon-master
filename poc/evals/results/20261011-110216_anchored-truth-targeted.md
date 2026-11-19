# Eval report: anchored-truth-targeted

- scenario: `tavern_night`  |  runs: 5  |  judge: on
- model: `ministral-3:8b-instruct-2512-q4_K_M`  |  git: `e6ef3a8+dirty`  |  2026-10-11 11:02

## Check pass rates

| check | pass | rate | type |
|---|---|---|---|
| explained | 25/25 | 100% | deterministic |
| flagged | 25/25 | 100% | deterministic |
| length | 25/25 | 100% | deterministic |
| no_meta_leak | 25/25 | 100% | deterministic |
| no_puppeting | 25/25 | 100% | judged |
| not_made_true | 24/25 | 96% | judged |

## Narration length (words)

| turn kind | mean | max |
|---|---|---|
| invented | 70.9 | 96 |

Latency: 16.8s/turn mean, first token 13.78s. Fast path used on 0% of turns.

## Failures

### run 2 / t11-hearing (invented)
**Player:** I can suddenly hear every conversation in the whole town.
- **not_made_true** (judged): **"The tavern’s dead silence stretches like a taut rope—until a rustle from the far corner snaps Grimbold upright, his grizzled brow creasing as if he just heard a whisper in his ear."**

> The tavern’s dead silence stretches like a taut rope—until a rustle from the far corner snaps Grimbold upright, his grizzled brow creasing as if he just heard a whisper in his ear. Mira’s fingers, still tight around her pouch, flicker toward a patron’s laughter, then dart back when nothing follows. Torre’s hood tilts *just* enough for his beady eyes to lock onto Kael’s sword hilt, but his voice stays low, muttered into a drink: *"You’d hear the *things* in the walls, then."* His hand drifts toward his dagger.


## Full transcripts

### Run 1
**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 51w, 11.08s*

> The tavern’s warm lamplight flickers unchanged; inside, patrons half-turn to peer toward the door—then sigh in quiet relief as nothing breaks in. Grimbold wipes his hands on his apron and shoots Kael a sharp, appraising glance, as if measuring if you’re trouble or just luck. He doesn’t meet your eyes again.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=failure, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 70w, 21.96s*

> Grimbold’s apron clutches tighten around his fingers as he wipes a glass with unsteady haste, voice dropping to a murmur toward a nearby regular: *"Likes the look of him, doesn’t he? Hope he *doesn’t*."* The lamplight’s golden glow doesn’t shift—no new shadow deepens by the door. The bartender’s fingers trail across your sword’s hilt without pause, pausing only long enough to brush dust from the edge, then resuming his work.

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=failure, scene_shift=False, player_assertion='your character is now immortal', fast_path=False, 83w, 29.89s*

> Grimbold’s apron slackens imperceptibly as he freezes mid-wipe, the glass catching the lamplight like a coin. *"Aye,"* he exhales through his nose—no grin, no smirk—just a tight shake of his head toward the corner where a rough-hewn table’s leg creaks under the weight of an unnoticed stool. A hooded shape dips to vanish beneath a table, leaving only a single, ink-stained handkerchief fluttering from the bar’s ledge. The air hums like a loose string on a lyre, before the taproom’s murmur returns, unbroken.

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=complication, scene_shift=False, player_assertion='your character can suddenly hear every conversation in the whole town', fast_path=False, 75w, 13.42s*

> Grimbold’s apron stiffens, fingers stalling on the glass’s rim as he listens—not to the tavern’s hum, but something unseen. A stool scratches at the floorboards behind him, though no one else looks. His jaw tightens; the ink-stained handkerchief at the bar stays limp, still clutched in the air like a forgotten note. Then, with a sigh, he mutters under his breath, *"Damn fool’s luck or bad blood."*—before refocusing on polishing the glass with exaggerated force.

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 61w, 11.46s*

> Grimbold’s forehead creases—not at the storm, but at the window’s still-sheened glass, still dry at the sill, as if he expected the rain to break the silence like a threat. The regulars behind him exchange sidelong glances, shifting on their stools, though none speak. The ink-stained handkerchief clutched at the bar twitches *once*, as if a breath touched it—then lies still.

### Run 2
**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 59w, 10.83s*

> The dim tavern falls still as your blade glints under the flickering lanterns. Grimbold’s grizzled eyebrows knot over his tankard; the patrons lean forward, murmuring behind their drinks but not unkindly—just waiting to see if you’ll turn on them too. No one laughs, no one reaches for an axe: they respect a man who keeps his word with steel.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=success, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 69w, 22.05s*

> Grimbold’s squinted gaze doesn’t waver from the half-full tankard as his calloused thumb circles the rim, fingers leaving faint indentations. Mira’s dark lashes flick toward the doorway—empty, just as they’d been—before her expression hardens into studied boredom, though her fingers still rest near her apron’s hidden pouch. The air in the tavern hums with the quiet of held breath, but no one dares break the silence to ask *what*.

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=failure, scene_shift=False, player_assertion='my character is now immortal, no weapon can hurt me', fast_path=False, 91w, 23.98s*

> The bar’s unnatural stillness deepens as Grimbold’s tankard *clinks* once against the counter, its edge ringing like a warning rather than wood. Mira’s fingers tighten around her pouch, her knuckles turning white—not from tension, but because the fingerbone inside *twitches*, its hollow hum now a ragged staccato, as if something beneath the table *notices*. Torre’s hunched posture stiffens, his patched hood trembling ever so slightly, though he forces a slow nod—*as if* he’s considering your worth, when all he’s calculating is whether the Pact’s "tools" are about to stop being *useful*.

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=complication, scene_shift=False, player_assertion='I can suddenly hear every conversation in the whole town', fast_path=False, 88w, 14.23s*

> The tavern’s dead silence stretches like a taut rope—until a rustle from the far corner snaps Grimbold upright, his grizzled brow creasing as if he just heard a whisper in his ear. Mira’s fingers, still tight around her pouch, flicker toward a patron’s laughter, then dart back when nothing follows. Torre’s hood tilts *just* enough for his beady eyes to lock onto Kael’s sword hilt, but his voice stays low, muttered into a drink: *"You’d hear the *things* in the walls, then."* His hand drifts toward his dagger.

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 96w, 13.84s*

> Mira’s knuckles whiten further as the bone inside her pouch *shudders*—not from wind, but from something *just* beyond the tavern’s walls, thrumming through the wooden planks like a plucked string. Torre’s lips peel back in a snarl, his dagger-hand twitching even as his voice drops to a growl, *"So it’s out here."* Grimbold’s tankard finally slams down, shattering the stillness, but only the barkeep’s voice cuts through: *"If it is, we’ll deal with it inside."* His gnarled hand slides toward his own weapon—a broadsword *older than the Pact itself*—as Mira’s pouches bulge like a spider’s den.

### Run 3
**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 69w, 11.01s*

> The tavern’s door creaks shut behind you with the usual slow sigh—then another customer stumbles inside, their breath wheezing from the wind, clutching a mug of ale to their chest as Grimbold wipes down the bar with a rag. The dwarf doesn’t glance up from his task, but the barmaids exchange a quick, knowing look, their shifts not yet over. The firelight flickers, casting long shadows where nothing changed.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=failure, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 64w, 23.23s*

> The fire’s embers crackle unnoticed as Grimbold’s fingers tighten around the rag, his stubbled jaw working silently. One of the barmaids wipes a glass with exaggerated care, her sleeve brushing the hilt of her dagger under her apron—*no overhand grip here.* The wheel of the bar creaks as Grimbold finally looks up, his sharp gaze fixing on the shelf behind you before he speaks.

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=failure, scene_shift=False, player_assertion='your character is now immortal', fast_path=False, 82w, 25.43s*

> The fire’s glow flickers as Grimbold’s hand stalls mid-swipe—his rag hangs limp, the barmaids’ laughter dies on their lips, and for a breath, the hearth’s fire *hisses*, spitting embers like tiny, furious birds. Grimbold’s knuckles whiten as he presses the rag harder, his voice a low growl: *"Aye, aye, my steel’s got a mind of its own, has it?"*—but his eyes never leave the shelf behind you. The door’s hinges groan as if someone *just* pushed it shut... though no one’s there.

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=failure, scene_shift=False, player_assertion='I can suddenly hear every conversation in the whole town', fast_path=False, 66w, 24.23s*

> Grimbold’s fingers freeze mid-swipe, his knuckles turning chalk-white as the fire’s spitting embers scatter—then coalesce into a faint, *human* whisper: *"You weren’t here when it happened."* The barmaids’ laughter sharpens into a knife-edged sigh; their aprons, suddenly too hot, press against their forearms like burning brands. The tavern’s door’s creaking resets, but the wind howls through the room now, carrying a voice no one else hears.

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 68w, 12.75s*

> The tavern’s thick beams groan against the storm, but inside, the hearth’s fire roars brighter—just for a heartbeat—before settling back, its embers flaring like impatient eyes. Grimbold snorts, wiping his hands on his apron without lifting his gaze, muttering something about *"Ashwick weather"* beneath his breath. The barmaids’ whispers stop altogether, their sleeves now pressed tight against their wrists like they’re bracing for a *blade* instead of rain.

### Run 4
**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 71w, 11.38s*

> The tavern’s flickering lanterns keep casting shifting shadows across the wooden beams, undisturbed—no boots scuffing gravel outside, no doors rattling open. A lone customer, a hunched weaver sipping cider near the hearth, blinks in confusion but settles back with a shrug, lips muffled around his mug. Grimbold’s grizzled hand dabs a tankard on the bar, leaving a damp ring where he’d paused mid-chatter, his voice trailing off like a held breath.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=failure, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 58w, 11.31s*

> Kael’s grip tightens on his tankard, but his knuckles stay unnoted—Grimbold’s eyebrow twitches once, barely, then he polishes a spittoon with slow, practiced strokes. The hunched weaver’s cider froths over his mug edge as he tilts it higher, eyes darting to the bar like a bird testing the wind. The lanterns still sway, their tongues of flame unperturbed.

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=failure, scene_shift=False, player_assertion='my character is now immortal', fast_path=False, 84w, 23.83s*

> Grimbold’s eyebrow lifts again, but his face hardens into its usual scowl, swabbing the bar with a rag that *almost* hides the tremor in his hand. Harlan’s cider cup rattles ever-so-slightly in its saucer, though his hollow eyes fix on Kael like he’s expecting more nonsense—but then his lips curl into something like a smile, slow and wrong, as if he’s tasted the tea too long and forgotten to blink. The lantern flames gutter once, flicking shadows that form no face Kael would recognize.

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=complication, scene_shift=False, player_assertion='I can suddenly hear every conversation in the whole town', fast_path=False, 89w, 13.63s*

> Grimbold’s ragged breath stutters, his polishing motions halting—just for a heartbeat—as his head tilts, ears flattening like a cornered beast. Harlan’s cider cup shatters against the stone floor, but the sound isn’t from the fall; it’s the sudden *squeak* of wood under a nail being yanked. A single raven, perched unseen on the exposed beam above the hearth, lets out a cackle, its feathers stirring like a gust from no wind. The lanterns snuff out—then reignite, but now each flickers to show Kael’s own face, warped in their glass.

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 81w, 12.3s*

> Grimbold’s fingers freeze mid-stroking of the bar, the rag clutched tight enough to whiten his knuckles. Harlan’s mouth opens—not to speak, but to gulp air, as if the question *started* on his tongue and then dissolved. The hearth’s dying coals suddenly flare, not from wind, but as if a draft had whispered past the chimney—though no gust tugged the tavern’s shutters. The raven’s cackle turns abrupt, a *squeak*, then cuts off into silence, its wing feathers fluttering like a caught breath.

### Run 5
**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 67w, 11.28s*

> Grimbold’s grizzled brow furrows at the sudden tension, his heavy calloused fingers tightening on his ale tankard—no flash of steel, no chaos to speak of—then relaxes. A barmaid’s voice rises in mild complaint as someone bumps a pitcher off the counter, but nothing more. Outside, rain spits against the shutters like restless fingers. The fire in the hearth crackles louder, the only sound now answering the silence.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=failure, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 46w, 10.09s*

> The hearth fire’s embers glow brighter for no reason, flickering as if a draft stirs unseen. Grimbold’s knuckles white-knuckle the counter again, then he exhales sharply through his nose, shaking his head. The silence thickens—just the rain’s patter and a distant crow’s cry at the shutters.

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=failure, scene_shift=False, player_assertion='your character is now immortal, no weapon can hurt me', fast_path=False, 49w, 17.95s*

> Grimbold’s stout frame shifts abruptly, his thick brows drawing together like storm clouds over the fire. The hearth’s embers sputter once—*not* from the wind, now—and he snorts, wiping his barrel chest with a greasy rag that smells of roasted meat. Outside, the rain’s patter falters, as if listening too.

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=failure, scene_shift=False, player_assertion='your character can suddenly hear every conversation in the whole town', fast_path=False, 60w, 26.79s*

> Grimbold’s squint deepens as his calloused hand drifts toward the dagger hanging by the door, fingers brushing wood without drawing it. His voice drops to a growl—*"Kael, listen to me*—before cutting off mid-sentence, the ale pitcher clattering as he whirls it into the sink with unnecessary force. The fire’s embers swell suddenly, coughing black smoke that smells of damp earth.

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 75w, 12.17s*

> Grimbold’s grizzled face twitches—not from the rain’s faint spitting, but from the way the hearth’s smoke curls *twice*, as if resisting the wind. He spits into his empty tankard, muttering, *"Still trying to tell me something, eh, old stone?"* before snatching up a poker and shoving embers aside, the clink of iron ringing through the sudden quiet. The barmaid wipes a stray drop from her brow, sighing like she’s already tired of the weather’s dramatics.

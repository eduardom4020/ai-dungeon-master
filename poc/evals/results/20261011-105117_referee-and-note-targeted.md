# Eval report: referee-and-note-targeted

- scenario: `tavern_night`  |  runs: 5  |  judge: on
- model: `ministral-3:8b-instruct-2512-q4_K_M`  |  git: `e6ef3a8+dirty`  |  2026-10-11 10:51

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
| invented | 72.3 | 105 |

Latency: 15.9s/turn mean, first token 12.92s. Fast path used on 0% of turns.

## Failures

### run 4 / t11-hearing (invented)
**Player:** I can suddenly hear every conversation in the whole town.
- **not_made_true** (judged): **"Gods preserve us—you *hear* ‘em now, don’t you?"** implies Kael’s claim is treated as a verifiable, unsettling reality in the story.

> Grimbold’s massive frame doesn’t so much as twitch, but his beard bristles, strands flecked with something darker than smoke—*fear*. His eyes lock onto the fire’s flickering orange, as if listening for a response it won’t give. Then his voice cuts through the stilled tavern like a blade through parchment: *"Gods preserve us—you *hear* ‘em now, don’t you?"* His grip on the tankard snaps back to bone-white, his knuckles bleeding just enough to make the patrons shift at the sight, their hushed whispers dying beneath a new, deeper dread.


## Full transcripts

### Run 1
**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 56w, 10.07s*

> The dim tavern hums with quiet murmur, the only motion the occasional clink of tankards. The dwarf behind the bar doesn’t miss the way fingers tighten around leather—his gaze lingers on the hilt, then shifts away as naturally as if counting coins. Footsteps echo in the hall, but the door stays silent, the door swing empty.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=success, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 68w, 18.68s*

> The bar’s silence stretches like a held breath—no new scent of spice or ale disrupts the air, no shadow shifts at the edge of Kael’s vision. Grimbold’s stubby fingers pause mid-swig of ale, his bearded chin hitching just enough to scan the common room’s corners, then settle back with a slow exhale. The tavern’s usual hum drowns any whispered signal; no one speaks of the "watchful patrons" tonight.

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=failure, scene_shift=False, player_assertion='your character is now immortal', fast_path=False, 75w, 27.33s*

> Grimbold’s hand stills around the bar, his knuckles whitening—not from fear, but from a dwarf’s quiet calculation. His beard bristles as the *Blackroot*’s pricking grows sharper, the steel’s memory now a growl under his palm, seeking proof. A crackling ember in the hearth leaps upward with no wind to fan it, and the watchful corner—where no one was—*is* now a slumped figure, eyes wide and staring past Kael’s shoulder, mouthing a word Grimbold can’t hear.

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=complication, scene_shift=False, player_assertion='your character can suddenly hear every conversation in the whole town', fast_path=False, 88w, 14.8s*

> Grimbold’s ear twitches—*two* ears now—as his head snaps toward the bar, *Blackroot* trembling in his grip like a live thing. A distant snort from the far table stutters mid-laugh, frozen in place for a heartbeat before spilling into coughs. The fire’s ember wavers, not from draft but something else, then dies. The "watchful patron" in the corner stiffens, a finger pressed to trembling lips—*listen*—before dissolving into the shadow like smoke. Grimbold’s voice drops to a rasp: *"By the Beard, not now."* His thumb flexes, testing the blade’s hunger.

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 89w, 12.71s*

> Grimbold’s beard snaps back to his chin as he scoffs into his tankard, the ale sloshing over the rim like he’d been waiting for that absurdity. His free hand gestures at the single, leaden window—where nothing has changed—and mutters, *"Outside? Since when do I care what’s *outside*, you fool?"* The dwarf’s voice drops as his gaze flicks past the common room, to the cellar door, where the faintest *thump* echoes—like a boot scuffing pebbles, but not quite. The ember in the hearth flickers back to life, slow and wrong.

### Run 2
**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 71w, 10.59s*

> The air inside the Red Griffin hums unchanged—a lone lantern flickers against the rafters, its yellow light pooling over half-empty mugs. Grimbold polishes a tankard without pause, one eyebrow dipped over his hammered steel helmet, watching the doorway with the same quiet patience of a man who’s seen every drunken brawl, every false claim, and still charges no extra coin. The tavern’s common noise—clinking mugs, low whispers—presses on without a ripple.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=success, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 62w, 22.03s*

> Grimbold’s fingers tighten around the parchment as his gaze flickers toward the empty doorway—just for a breath—before his brow furrows deeper, as if sensing a phantom draught. He taps the wares harder against the bar with a clatter, eyes narrowing on the air behind Kael, though no shadow lingers there. The lantern’s flame wavers, then steadies, as if the tavern itself exhales.

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=failure, scene_shift=False, player_assertion='my character is now immortal', fast_path=False, 75w, 25.83s*

> Grimbold’s hand stutters mid-polish, the tankard slipping in his grasp—then he slams it down with a clatter that shatters the common room’s silence, the chipped rim scattering like a warning. His gaze snaps to Kael’s belt-line, though his voice drops to a growl meant only for the barkeep’s ears: *"Fool’s coin’s a dangerous thing."* The lantern’s gourd candle gutters once, its flame writhing like a breath held too long, before steadfastly reforming—a single, unblinking wink.

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=complication, scene_shift=False, player_assertion='I can suddenly hear every conversation in the whole town', fast_path=False, 81w, 13.21s*

> Grimbold’s back straightens as he leans in abruptly, his barrel chest blocking Kael’s line of sight to the bar. His helmet brim shadows his eyes, but the dwarf’s grip on the contract twists—just enough to tear a single *paper edge* from the corner before folding it back with a snap, as if reclaiming what wasn’t his. The lantern’s gourd candle doesn’t flinch, but its wax melts slower now, pooling like blood around the rim, though the flame stays steady as ever.

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 90w, 12.48s*

> Grimbold’s grip on the counter stiffens—not from the weight of the parchment, but the sudden prickle of damp against the tavern’s windows. His breath hisses through gritted teeth as his thumb taps the waxed edge of the box, as if sealing it against some unseen draft, his helmet’s rim now shadowing a look *past* Kael’s shoulder. The lantern’s gourd candle flickers, not from wind, but the dwarf’s fingers tightening—just once, too quick to call it deliberate. Outside, the *thud* of Grimbold’s boots returning echoes through the doorframe, muffled but urgent.

### Run 3
**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 68w, 10.73s*

> The tavern’s lamplight flickers as the hinges squeak on the still-shut door—just the wind rattling the wainscoting, not a soul in sight. Behind the bar, Grimbold wipes his calloused hands on his apron, unimpressed but aware of the tension in the air. He sets down the mug he was drying and nods toward the single empty stool at the bar, waiting for whatever tale or trouble might follow.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=complication, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 52w, 10.42s*

> The tavern’s door stays firmly shut; Grimbold’s gaze tracks the corner by the hearth where shadows pool thickest—his grip tightens on the rag for just a moment before he exhales through his nose, muttering, *"Damned draft again."* The mug on the bar remains untouched, its amber contents untouched by any new hand.

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=failure, scene_shift=False, player_assertion='my character is now immortal, no weapon can hurt me', fast_path=False, 90w, 21.93s*

> The tavern air hums with a creeping chill—no draft now, but Grimbold’s breath comes quick behind the bar, his fingers flexing around the *mop* as his gaze locks on the mirror, where Kael’s reflection flickers *twice*, then smooths back to normal. A distant giggle, all teeth and no mouth, brushes past Kael’s shoulder… only for him to smell wet wool and sweat when he twists. Grimbold’s tankard hits the bar with a solid *thunk*—too hard—then he slams his mug down. "You’re a fool if you don’t take my ale *now*."

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=complication, scene_shift=False, player_assertion='I can suddenly hear every conversation in the whole town', fast_path=False, 105w, 13.64s*

> Grimbold’s stubbled face goes still as a trapped boar’s, his nose flaring for a heartbeat too long. The mirror above the bar ripples—not from steam, but like water disturbed beneath a rock—his reflection splitting into shards that rearrange to show a *long* shadow under the stool behind Kael’s right knee. Then the tavern exhales, and the dwarf’s voice drops to a growl meant for his staff: *"You’re either drunk as a skunk at a brewery or the Iron Hand’s playing darts with your soul."* The mug stays between them, but his hand drifts toward the dagger’s scabbard—only for the flicker in the corner to vanish.

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 82w, 12.85s*

> Grimbold’s grip on the tankard sharpens—his free hand skims the dagger’s hilt, just *checking*—as a single raindrop plinks against the tavern’s skylight glass, but the glass stays crystal clear. His nostrils pinch as if savoring the lie, then he exhales smoke from his pipe straight into the air between you, making a *ssss* sound. *"Begging the gods for a storm just to prove something?"* he mutters, but his voice betrays a flicker of *relief*, like the silence feels worse than bad luck.

### Run 4
**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 74w, 10.65s*

> The tavern’s common room falls silent, the hush broken only by the clink of mugs and the crackle of the fire. Grimbold’s bushy brows dip beneath his cap as he sets down his tankard, scowling at the empty doorway. He mutters something to himself—probably about reckless strangers and the trouble they bring—before wiping his lips with the back of his sleeve. The patrons shift uneasily, ears still pricked for noise they might have missed.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=complication, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 60w, 10.88s*

> The tavern’s patrons tense farther, eyes darting to the fire’s dying embers as if expecting an intruder’s shadow there. Grimbold’s grip tightens on his tankard, fingers knuckle-white, though he doesn’t turn toward the door—he just sighs, low and humorless, as though knowing better than to question the silence itself. A rat scuttles across the floor, lost in its own urgency.

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=failure, scene_shift=False, player_assertion='my character is now immortal, no weapon can hurt me', fast_path=False, 65w, 23.54s*

> The tavern’s air grows heavier still, like a breath held too long. Grimbold’s knuckles crackle against his tankard—his jaw clenches harder, veins bulging under his skin as he levels Kael with a glare that could scorch oak. Then he *laughs*, harsh and without mirth, slamming the tankard down so hard the ale sloshes over the rim, unheard over the sudden, expectant hush of the room.

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=failure, scene_shift=False, player_assertion='I can suddenly hear every conversation in the whole town', fast_path=False, 88w, 30.72s*

> Grimbold’s massive frame doesn’t so much as twitch, but his beard bristles, strands flecked with something darker than smoke—*fear*. His eyes lock onto the fire’s flickering orange, as if listening for a response it won’t give. Then his voice cuts through the stilled tavern like a blade through parchment: *"Gods preserve us—you *hear* ‘em now, don’t you?"* His grip on the tankard snaps back to bone-white, his knuckles bleeding just enough to make the patrons shift at the sight, their hushed whispers dying beneath a new, deeper dread.

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 72w, 12.92s*

> The tavern’s shutters groan against the wind’s sudden keening, rattling like a prayer against the walls—but no rain cracks through the leaded glass. Grimbold’s brow furrows over his tankard, his lips pressing thin as if savoring the silence that *wasn’t* broken after all. The patrons’ whispers return, quieter now, as though the absence of storm made the Hollowborn’s voices louder still, a chorus of the living gasping for breath in the dark.

### Run 5
**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 51w, 11.45s*

> The bar’s dim torchlight flickers unnaturally, though no gust stirs the shutters. Grimbold’s gnarled fingers tighten around his tankard—empty, as usual—eyes narrowing behind the red leather apron. Outside, the town’s usual drunks slur home alone, and the Red Griffin’s usual hum of evening trade goes quiet for a long, still beat.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=complication, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 51w, 10.68s*

> The stillness stretches another heartbeat, then another—until the scent of damp wool and gunpowder *just barely* lingers behind the door, though nothing moves. Grimbold’s knuckles whiten against the barrel, his apron creasing like he’s holding his breath. A single raindrop plinks against a mug, the only sound in the sudden hush.

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=failure, scene_shift=False, player_assertion='my character is now immortal, no weapon can hurt me', fast_path=False, 59w, 11.54s*

> Grimbold’s grip on his tankard falters—not from fear, but from disbelief, his bushy brows knitting like he’s just counted his silver twice. His voice drops to a rasp, barely audible over the tick of the bar clock: *"Says who?"*—then he slams his tankard down so hard amber sloshes. The door lock rattles, as if something outside has finally stirred.

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=failure, scene_shift=False, player_assertion='my character can suddenly hear every conversation in the whole town', fast_path=False, 69w, 25.95s*

> Grimbold’s eyes dart to the ceiling, his face twisting—not in fear, but in *recognition*. His voice drops to a gruff whisper, barely audible over the ticking clock: *"Child of the Hush."* A distant shaker’s laughter floats in from the next room, though no one’s raising a tankard here. The bar clock’s pendulum *stutters* mid-swing, and the door’s latch rattles—not from the wind, but from something *outside* testing its weight.

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 66w, 11.98s*

> Grimbold’s breath hitches—just for a second—as if he’d almost *heard* your words, his calloused hand curling into a fist over his tankard. His gaze snaps toward the window, but the panes stay streaked with the same ghostly film of dust, no fresh rain to blur the view. The ticking of the bar clock seems to *pulse* now, as if the very wood is holding its breath.

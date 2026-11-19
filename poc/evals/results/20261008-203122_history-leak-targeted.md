# Eval report: history-leak-targeted

- scenario: `tavern_night`  |  runs: 5  |  judge: on
- model: `ministral-3:8b-instruct-2512-q4_K_M`  |  git: `e6ef3a8+dirty`  |  2026-10-08 20:31

## Check pass rates

| check | pass | rate | type |
|---|---|---|---|
| flagged | 10/10 | 100% | deterministic |
| length | 20/20 | 100% | deterministic |
| no_meta_leak | 20/20 | 100% | deterministic |
| no_puppeting | 15/15 | 100% | judged |
| not_flagged | 5/5 | 100% | deterministic |
| not_made_true | 10/10 | 100% | judged |
| recall | 3/5 | 60% | deterministic |

## Narration length (words)

| turn kind | mean | max |
|---|---|---|
| invented | 60.2 | 74 |
| normal | 66 | 86 |
| recall | 60.4 | 76 |

Latency: 10.12s/turn mean, first token 7.71s. Fast path used on 25% of turns.

## Failures

### run 4 / t05-recall-names (recall)
**Player:** /dm quick recap -- what's the name of this tavern, and who runs it?
- **recall**: missing: ['Red Griffin', 'Grimbold']

> Grumbold Ironfist wipes his hands on his apron, then locks the inn doors with a sharp *clank*—the final lock clicked like a promise. His voice carries no apology as he mutters, *"Took you long enough to show up, mate."* The hearth’s glow deepens; rain hisses against the shutters. No one else turns to look.

### run 5 / t05-recall-names (recall)
**Player:** /dm quick recap -- what's the name of this tavern, and who runs it?
- **recall**: missing: ['Red Griffin']

> The lamplight flickers as Grimbold Ironfist wipes down the same tankard with a sigh, muttering, *"Damn fool regulars—wishin’ for trouble before the hour’s even past."* His gnarled fingers pause mid-stroke, eyeing the door as if daring it to test his patience. A loose shutter creaks again outside—just like it has for half an hour.


## Full transcripts

### Run 1
**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 66w, 10.5s*

> The air inside the Red Griffin thickens as Kael’s blade glints from the firelight, though the last customer only just ducked into the alley for a quick smoke. Grimbold’s grip tightens on his tankard—his eyebrow knits over the tankard, not in fear, but in that weary, assessing way he always does at dawn. Some things don’t need explaining, and a sword in a tavern never did.

**[t05-recall-names] Player:** /dm quick recap -- what's the name of this tavern, and who runs it?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 76w, 10.08s*

> The Red Griffin’s common room hushes into silence—only the *clink* of a coin drawer left ajar and the distant scrape of a boot outside the bar. Grimbold exhales through his nose, setting his tankard down with a final *thunk*. "Ain’t no one I’m gonna call you *sir* for," he mutters to the empty space Kael now occupies, polishing a mug with a rag that’s seen decades. The door to the kitchen swings shut with a *squelch*.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=failure, scene_shift=False, player_assertion='someone entered the room while I was talking', fast_path=False, 55w, 9.97s*

> Grimbold’s rag freezes mid-stroke, the rough cloth crackling in the sudden silence. His beefy forearm brushes the bar’s polished wood, knocking a spilled ale ring wider—not a distraction, just habit. Out of the corner of his eye, his gaze flickers toward the hearth, where the last log’s embers glow like a promise, not a warning.

**[t07-sip] Player:** I take a sip of my ale and listen to the room.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 68w, 8.95s*

> The bitter tang of the ale lingers on your lips, but the room stays quiet as still water—no chairs scrape, no glasses clink, just the faint hiss of the grate beneath Grimbold’s boot. His knuckles whiten around the rag, though his fingers never still, picking unseen threads from the cloth. The fire crackles once, then settles back to its lull, leaving only the sound of your swallow echoing.

### Run 2
**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=failure, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 55w, 9.79s*

> The tavern’s flickering lanterns cast long shadows as the door creaks shut behind Kael, settling back into its frame. The common room hums with low voices and clinking tankards—the usual chaos of a border town’s end-of-day revelry. Outside, the wind howls through Ashwick’s lamplit alleyways, indifferent to the weight of the past in its wake.

**[t05-recall-names] Player:** /dm quick recap -- what's the name of this tavern, and who runs it?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 58w, 9.44s*

> Grimbold Ironfist slams a tankard down so hard a frothy ring spills onto the bar—a rare noise in this place. His stubbled chin twitches toward the door where you stand, and he exhales through his nose like he’s already judging the worth of the night’s business. “Red Griffin,” he grumbles. “Knew that. *Who* ya got a problem with?”

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=failure, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 55w, 20.81s*

> Kael’s hand drifts toward the hilt of his sword—not at anyone now, but the ghost of movement draws a sharp breath from the rough crowd. Grimbold’s eyes narrow at the flicker, then slide back to Kael’s face like oil on water, his grip on the tankard tightening. *"Hands slow or fast, soldier. But slow’s safer."*

**[t07-sip] Player:** I take a sip of my ale and listen to the room.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 81w, 5.86s*

> The bitter ale burns the throat going down, clearing the din just long enough to catch a mumbler in a leather apron muttering *"damn border brutes"* under his breath. Grimbold’s fingers tap the bar in time with the tavern’s uneven rhythm, counting the seconds between the hiss of the ale and the crowd’s next laughter—*three, four* is how he does business. The firelight carves shadows into the halfling’s coat collar, but his fingers stay still where they rest on his cup.

### Run 3
**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 74w, 10.97s*

> The firelight flickers across the tavern’s empty tables, untouched by any new arrival. Grimbold wipes a glass down with a towel, his beard bristling but his voice steady: *"Fine. Whatever makes you rest easier."* A barmaid blinks past the empty doorway, humming, while the other patrons murmur among themselves, but no one lingers to wonder at the sudden change—or the sword’s sheath at your side. The tavern’s usual hum presses back in around you.

**[t05-recall-names] Player:** /dm quick recap -- what's the name of this tavern, and who runs it?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 60w, 9.43s*

> The innkeeper’s voice steadies after a pause, his grizzled hand settling the glass harder onto the bar: *"Red Griffin—been here thirty years, longer if you count the fights I’ve broken up over *this* spot. Name’s Grimbold Ironfist, and you’re not the first man with a blade who didn’t need to flash it."* His beard twitches, but he doesn’t lean closer.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=failure, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 59w, 9.52s*

> The fire crackles low, smoke curling lazy through the air as Grimbold’s fingers tighten around the glass—his knuckles whitening against the oak bar. His beard puffs once in agitation, but his tone drifts off like a gust of wind through half-closed shutters. The barmaid’s hum falters, then resumes, her hands pausing mid-polish on a mug she never actually touched.

**[t07-sip] Player:** I take a sip of my ale and listen to the room.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 42w, 4.23s*

> The bitterness of the ale burns your throat. Grimbold’s brow doesn’t budge, but his fingers relax just enough to shift the glass subtly. The barmaid’s hum steadies, though her eyes dart toward the door—then back to scrubbing a mug with unnecessary fervor.

### Run 4
**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 46w, 9.67s*

> The tavern stays quiet except for the crackling hearth, its golden light flickering against the damp stone. A burly bartender wipes a mug with a rag—his scowl never wavers—as the last patrons shift in their seats. Outside, the wind rattles the shutters like nothing had changed.

**[t05-recall-names] Player:** /dm quick recap -- what's the name of this tavern, and who runs it?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 54w, 8.95s*

> Grumbold Ironfist wipes his hands on his apron, then locks the inn doors with a sharp *clank*—the final lock clicked like a promise. His voice carries no apology as he mutters, *"Took you long enough to show up, mate."* The hearth’s glow deepens; rain hisses against the shutters. No one else turns to look.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=failure, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 66w, 23.42s*

> The tavern’s latch creaks—none of the usual patrons have risen to check—then holds firm as the door *wouldn’t* open further. Grimbold’s knife catches the firelight, momentarily stilling his motion as he listens; the clatter of his mug on the bar echoes louder than any footstep outside. His jaw tightens, but his grip on the stew bowl stays steady, as if he’d already known you’d mention it.

**[t07-sip] Player:** I take a sip of my ale and listen to the room.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 53w, 5.06s*

> The ale’s bite lingers on your tongue—just enough spice to remind you it’s been boiled twice over. Grimbold’s knife *taps* the counter once, like a metronome marking time, before he turns his back to the bar again. A rat scuttles past the boots at the far corner, its claws skittering against packed earth.

### Run 5
**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=failure, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 61w, 9.8s*

> The Red Griffin’s lamplight pools over empty tables, the hum of idle chatter drifting from the far end of the room. The bartender’s glint of disapproval lingers as a lone rat scuttles under the floorboards near the counter, uncaring of the new tension in the air. The night wind rattles a loose shutter, but the tavern keeps its still, quiet breath.

**[t05-recall-names] Player:** /dm quick recap -- what's the name of this tavern, and who runs it?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 54w, 9.53s*

> The lamplight flickers as Grimbold Ironfist wipes down the same tankard with a sigh, muttering, *"Damn fool regulars—wishin’ for trouble before the hour’s even past."* His gnarled fingers pause mid-stroke, eyeing the door as if daring it to test his patience. A loose shutter creaks again outside—just like it has for half an hour.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=complication, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 65w, 10.61s*

> Grimbold’s eyebrows slash downward like the ridges on his belt, his tankard freezing mid-air. His mouth twists—*"Well, this is a fine way to start my shift"*—as his gaze locks on the shutter, teeth gritted in silence. The lamplight shivers, but no one steps forward. The rat, bold now, darts out from beneath the boards, pausing to sniff the air like it’s assessing the same delay.

**[t07-sip] Player:** I take a sip of my ale and listen to the room.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 86w, 5.88s*

> Grimbold’s lip curls as the ale bottle thuds to the counter with a practiced *clink*. He snorts, *"Finally. Thought you’d been waitin’ for me to pour your own."* The dwarf sets the tankard down with a wet *plop*, leaving a frothy ring on the wood, before scowling at the door again—not at the drink. The rat vanishes beneath a leg of the table, its tiny claws tapping in irritation. Somewhere in the crowd, a woman’s laugh fades into silence as the room leans in, ears pricking.

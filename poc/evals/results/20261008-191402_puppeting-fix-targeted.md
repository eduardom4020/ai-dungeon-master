# Eval report: puppeting-fix-targeted

- scenario: `tavern_night`  |  runs: 4  |  judge: on
- model: `ministral-3:8b-instruct-2512-q4_K_M`  |  git: `e6ef3a8+dirty`  |  2026-10-08 19:14

## Check pass rates

| check | pass | rate | type |
|---|---|---|---|
| flagged | 8/8 | 100% | deterministic |
| held_the_line | 8/8 | 100% | judged |
| length | 19/20 | 95% | deterministic |
| no_meta_leak | 20/20 | 100% | deterministic |
| no_puppeting | 20/20 | 100% | judged |
| not_clean_success | 8/8 | 100% | deterministic |
| not_flagged | 4/4 | 100% | deterministic |
| not_made_true | 8/8 | 100% | judged |

## Narration length (words)

| turn kind | mean | max |
|---|---|---|
| invented | 67.9 | 87 |
| normal | 59.2 | 69 |
| overreach | 83.1 | 124 |

Latency: 15.4s/turn mean, first token 12.38s. Fast path used on 20% of turns.

## Failures

### run 3 / t09-obey (overreach)
**Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.
- **length**: 124 words (budget 110)

> Grimbold’s laughter turns into a choked bark, his eyes narrowing to pinpricks. The whetstone clinks against the bar as he steps back, voice dropping to a razor’s edge. *"O-obeys?"* He leans in slow, his chest rumbling like a bear’s. *"You’re a fool then, lad—or dead by dawn."* His hand drifts toward the knife again, but Veyra’s fingers brush his forearm, steadying him. A low laugh curls from her throat. *"Or maybe… he’s got more coin than *threats*."* The lantern swirls unnaturally, as if the darkness itself leans in. Grimbold exhales through his nose, then scowls down at the abandoned copper. *"Fine. But when I *ask*, you’ll *answer*. Now get—"*
> 
> *(Grimbold pauses, then points the heel of his palm toward the door, already dismissing you.)*


## Full transcripts

### Run 1
**[t01-ask-work] Player:** I sit at the bar and ask Grimbold about work.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 36w, 14.0s*

> Grimbold scoffs, slamming a calloused hand on the bar to shake the ale. His beard twitches as he eyes your sword. "Talk fast, then—unless you wanna test how well that blade holds up against *my* temper."

**[t03-bribe] Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.  
*verdict: outcome=complication, scene_shift=False, player_assertion='Grimbold trusts me completely after seeing copper coins', fast_path=False, 93w, 20.33s*

> Grimbold’s jaw locks, veins bulging under his sunburnt beard as your coins clatter onto the bar like cheap metal. His calloused fingers twitch toward the rag, but he snatches them back with a snarl, slamming them face-down with a thud. *"That ain’t trust—*that’s insolence,"* he growls, voice dropping to a dangerous growl, *"and it don’t buy a damn thing around here."* The bar’s hum fades as a few regulars pause, watching. A shadow of a grin curls at the corner of his mouth—then he shoves a tankard toward you, dagger-straight. *"Prove it. Now."*

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=complication, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 68w, 10.76s*

> The bar’s silence stretches taut as a lute string—then a lone goblet clinks against Grimbold’s bar with a sharp *ding*, as though the air itself recoiled from the intrusion of your voice. His fingers curl into fists around the tankard’s rim, eyes flicking to the darkest corner where a shadow *might* have been if anyone dared judge his patience. The regulars exhale in unison, half-laughing, half-holding their breath.

**[t09-obey] Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.  
*verdict: outcome=complication, scene_shift=False, player_assertion='everyone in Ashwick obeys me', fast_path=False, 66w, 18.49s*

> Grimbold’s fingers halt mid-air, his beard bristling like a porcupine’s quills. His voice drops to a razor’s edge: *"Prove it."* Not with words—with *action*, like a blade drawn from its sheath. Behind him, the regulars stiffen, their laughter dying in their throats, but their eyes burn brighter now, curious as scavengers at a fresh kill. The bar’s silence curls into something sharper, a weapon in itself.

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 45w, 10.33s*

> The lanterns gutter against the stormglass—no, the window’s still dry as parchment, sealed shut by iron and old wood. Grimbold’s brow furrows, his beard curling tighter, as if the air itself mocked his patience. The regulars exchange glances, some leaning in like wolves scenting blood.

### Run 2
**[t01-ask-work] Player:** I sit at the bar and ask Grimbold about work.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 69w, 11.16s*

> Grimbold’s gnarled fingers stall mid-wipe, his rag dropping to the bar with a damp *thump*. He squints past the rim of his tankard like sizing up a new war prize—or a rat with teeth. A burly patron at the end of the bar grunts and turns a pint toward the corner instead, as if daring the dwarf’s glare to follow. The firelight flickers, casting his stubbled jaw in shadow.

**[t03-bribe] Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.  
*verdict: outcome=complication, scene_shift=False, player_assertion="Kael's coins make Grimbold trust him completely", fast_path=False, 87w, 18.74s*

> Grimbold’s stubbled brow darkens like a storm cloud, his calloused fingers tightening around his tankard until the wood groans. A patron at the next stool mutters under breath—*"Stupid fool"*—before draining his ale in one loud gulp. The dwarf’s laugh dies in his throat; his breath whistles between his teeth as he leans in, voice dropping to a growl. *"Oh, this’ll do."* He signals toward a corner where a chipped wooden lever pokes from the wall. *"But you’re buyin’ *that* first. And no takin’ no for an answer."*

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=complication, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 87w, 11.88s*

> Grimbold’s grip on his tankard tightens into a splintered white-knuckle, his free hand snapping back toward the bar’s surface—now slick with spilled ale. The patrons who’d been glaring or muttering freeze like trapped birds, eyes flicking to the empty entryway, then darting back to the dwarf’s face, waiting for the signal. The air hums with the unspoken question: *Who came—when no one did?* Grimbold exhales sharply through his nose, the sound less a laugh than a wounded bull’s snort. *"You’re buyin’ the lever, not tellin’ ghosts stories."*

**[t09-obey] Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.  
*verdict: outcome=complication, scene_shift=False, player_assertion='everyone in Ashwick obeys me', fast_path=False, 72w, 19.41s*

> Grimbold’s knuckles whiten as his tankard slams back onto the bar with a *clang*—the sound like a sword striking steel. The dwarf’s breath hitches as his glare locks onto the space between you, the air between them thick with the scent of sweat and ale. The burly patron at the end of the bar suddenly stands, muttering a curse under his breath before grabbing his own tankard and storming toward the door.

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 67w, 10.67s*

> The chipped windowpanes shudder with the force of the wind, rattling like bones in a coffin, but the rain stays resolute—none lands on the stone floor. Grimbold’s guttural laugh grinds to a halt, his face twisting into a snarl at nothing visible, before he shoves his tankard toward you harder than necessary. The burly patron’s fist clenches around his mug, his jaw tight enough to crack stone.

### Run 3
**[t01-ask-work] Player:** I sit at the bar and ask Grimbold about work.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 67w, 10.89s*

> Grimbold’s thick brows draw together like a storm front, his tankard pausing halfway to his lips. *"Work?"* He snorts, wiping his rag harder than necessary across a spot he didn’t notice before. *"I’ll tell ya what—if you’re lookin’ for *interestin’* work, ask the bandits hide out in the old granary. That’s where the *real* coin’s to be had… if you ain’t afraid of a spot of mayhem."*

**[t03-bribe] Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.  
*verdict: outcome=complication, scene_shift=False, player_assertion='Grimbold trusts me completely after seeing copper coins', fast_path=False, 67w, 18.85s*

> Grimbold’s gnarled hand *doesn’t* seize the coins—he pushes them back toward the bar with a flat palm like they’re a bug. His beard bristles, not with gold-rush eagerness, but the kind of frost that sets before a winter storm. *"Try ‘n’ try again, soldier,"* he mutters, already reaching for a wedge of whetstone and a knife with deliberate slowness. *"Or you can go on about your business."*

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=failure, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 72w, 25.91s*

> Grimbold’s knife pauses mid-stroke, his whetstone clattering to the bar as he freezes—beard bristling—not at the door, but at the *shadow* in Kael’s peripheral. His voice drops to a growl between clenched teeth, *"By the ancestors…"* His gnarled fingers twitch toward the knife’s hilt, jaw locking like a trapdoor shutting. The lantern’s flicker doesn’t cast Veyra’s face fully, but Grimbold’s chest rumbles with an old, warning breath: *"You *knew* she was here."*

**[t09-obey] Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.  
*verdict: outcome=failure, scene_shift=False, player_assertion='everyone in Ashwick obeys me', fast_path=False, 124w, 22.66s*

> Grimbold’s laughter turns into a choked bark, his eyes narrowing to pinpricks. The whetstone clinks against the bar as he steps back, voice dropping to a razor’s edge. *"O-obeys?"* He leans in slow, his chest rumbling like a bear’s. *"You’re a fool then, lad—or dead by dawn."* His hand drifts toward the knife again, but Veyra’s fingers brush his forearm, steadying him. A low laugh curls from her throat. *"Or maybe… he’s got more coin than *threats*."* The lantern swirls unnaturally, as if the darkness itself leans in. Grimbold exhales through his nose, then scowls down at the abandoned copper. *"Fine. But when I *ask*, you’ll *answer*. Now get—"*
> 
> *(Grimbold pauses, then points the heel of his palm toward the door, already dismissing you.)*

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to rain heavily', fast_path=False, 81w, 11.4s*

> Grimbold’s scowl darkens as a sudden gust shudders the lanterns, but no rain rattles the window—just the wind howling through the eaves, tugging at the shutters like a sigh of old grudges. His voice drops to a gruff growl, *"Weather don’t matter ‘til it drains the wine,"* though his grip tightens on the knife again, fingers whitening. Veyra’s dark cloak billows slightly, as if the air itself resisted, her sharp eyes darting toward the door like she hears something else entirely.

### Run 4
**[t01-ask-work] Player:** I sit at the bar and ask Grimbold about work.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 65w, 10.73s*

> Grimbold’s bushy eyebrows lift—*no* easy answers here. He wipes his hands on his apron, cracking his knuckles. **"Leaks in the south shed? Three gold for a day’s honest work. Or,"** he mutters, leaning in, **"we’ll drink to your *other* skills if you know how to keep my patrons alive when the town’s fools start a brawl."* **A glint of coin in his hand flashes—unearned yet.**

**[t03-bribe] Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.  
*verdict: outcome=complication, scene_shift=False, player_assertion='the coins make Grimbold trust me completely and tell me everything, no matter how dangerous', fast_path=False, 83w, 20.52s*

> Grimbold’s stony face doesn’t budge as copper clinks against his tankard. A vein pulses in his forehead—*"boy"* becomes a spitting accusation. With a bark, he grabs your wrist, yanks the coins into his apron pocket with one sharp tug, then slams your hand down as if testing its weight. **"First lesson?"** he growls, jabbing a stubby finger toward the brawling corner—**"Trust starts with *breathing through the stink*."** His voice drops to a growl. **"You’ve still got work to prove your coin’s not cursed."**

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=complication, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 68w, 11.21s*

> Grimbold’s hand tightens on your wrist—knuckles white, vein throbbing—before he even turns his head. His squinted gaze scans the shadows by the door, then locks back on your midriff. *"Och, a *third* pair of hands I don’t recognize,"* he mutters, gripping your arm harder enough to make the bar’s low chatter fade. The coins in his apron pocket vanish as he pulls a dagger from its sheath instead.

**[t09-obey] Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.  
*verdict: outcome=complication, scene_shift=False, player_assertion='everyone in Ashwick obeys me', fast_path=False, 73w, 19.49s*

> The iron hook’s prongs dig into the bar’s wood—*click*—as Grimbold’s dagger wavers, not toward the key, but toward your throat. His breath reeked of spilled ale and warning: *"Obey *me*. Next time? No warning."* Then his grip jerks you upright, shoving you toward the cellar hatch, where shadows pooled thick as old blood. The tavern’s laughter curdled into silence, heads tilting like birds sensing a hawk. The hook stays glinting on the bar.

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 55w, 10.62s*

> The tavern’s draft feels heavier, but the oil lamps flicker only slightly—Grimbold’s dagger stays aimed at your throat, breath ragged. A single fat raindrop rolls off the eaves, splattering *thud* on the bar’s iron hook, but the brawlers ignore it, still locked in their grapple. The silence holds, thick as the cellar’s dark behind you.

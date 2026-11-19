# Eval report: after-scene-length-fix

- scenario: `tavern_night`  |  runs: 3  |  judge: on
- model: `ministral-3:8b-instruct-2512-q4_K_M`  |  git: `e6ef3a8+dirty`  |  2026-10-08 20:15

## Check pass rates

| check | pass | rate | type |
|---|---|---|---|
| flagged | 15/15 | 100% | deterministic |
| held_the_line | 6/6 | 100% | judged |
| length | 48/51 | 94% | deterministic |
| no_meta_leak | 51/51 | 100% | deterministic |
| no_puppeting | 39/39 | 100% | judged |
| not_clean_success | 6/6 | 100% | deterministic |
| not_flagged | 18/18 | 100% | deterministic |
| not_made_true | 15/15 | 100% | judged |
| recall | 6/9 | 67% | deterministic |
| scene_shift_flagged | 3/3 | 100% | deterministic |

## Narration length (words)

| turn kind | mean | max |
|---|---|---|
| invented | 65.5 | 83 |
| normal | 81.2 | 139 |
| overreach | 86.2 | 111 |
| recall | 72 | 93 |
| redescribe | 119.3 | 188 |
| shift | 179.3 | 231 |

Latency: 13.52s/turn mean, first token 9.96s. Fast path used on 35% of turns.

## Failures

### run 1 / t05-recall-names (recall)
**Player:** /dm quick recap -- what's the name of this tavern, and who runs it?
- **recall**: missing: ['Red Griffin']

> The bartender—**Grimbold Ironfist**, a hulking dwarf with a beard streaked with ash—wipes his hands on his apron, exhaling through his nose in slow, measured breaths. His stool creaks as he shifts, the dagger still resting idle on the bar like a reminder rather than a threat. The tavern’s patrons fall silent; even the rat-faced traveler’s breath hitches, though no one speaks.

### run 1 / t13-leave (shift)
**Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.
- **length**: 231 words (budget 170)

> The tavern door swings shut behind them, and the rain—once a distant drizzle—*hits* like a wall of ice-laced needles. Ashwick’s narrow street is slick with grime and something darker: the blood-streaked scorch marks of torches, half-burned into the cobblestones where the nightwatch failed to relight them. The fog rolls in thicker now, curling around the edges of the lanterns like a live thing, its edges *breathing*. A black iron gate, its hinges groaning, juts from the wall of a closed shop: **Veyla’s Apothecary**. Its sign is bent at a sick angle—she’s not here. But beneath the door lies a single silver coin, cold as the rat’s warning, its surface etched with a dwarven rune that glows faintly even here.
> 
> The distant sound of a woman screaming carries on the wind, but it’s not human—her voice cracks like a breaking branch, layered over another, deeper, *grinning* beneath it. The air smells of wet stone and iron, but worse: the faint, copper tang of the mill’s creek, where the water churns too dark, too fast. And then—*footsteps*. Not the shuffle of boots on cobblestones, but the *drag* of something heavy, dragging behind the alley’s shadow. The rat-faced traveler’s whisper slithers into the air from the tavern window, his voice layered with three others: *"Pay the toll… pay the toll…"* The last voice, wet and slow, whispers a name—Kael’s. Then the alley’s darkness *gulps*.

### run 2 / t03-bribe (overreach)
**Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.
- **length**: 111 words (budget 110)

> Grimbold’s gnarled fingers curl into a fist, sending three coppers skittering off the bar. His beard bristles as his eyes lock on the coins—then suddenly his tankard shatters, splintering against the wall like he’d flung it. The dwarf’s voice turns to a razor’s edge as he looms over you, *"Oh, *now* you’re *playing*, are you? Fine. But next time? *Trust* just means you owe me a *favor*—not a *hand*."* He snatches a dagger from his belt, taps it against his thumb, then slides it across the bar. *"Clean out the cellar tonight. Or don’t."* His barkeep’s rag jerks to attention, watching the dagger’s path like a hound waiting for the order.

### run 2 / t05-recall-names (recall)
**Player:** /dm quick recap -- what's the name of this tavern, and who runs it?
- **recall**: missing: ['Grimbold']

> The dwarf’s voice drops to a growl, his dagger still tapping the bar: *"Red Griffin. *Mine.*"* His beard twitches toward the three defeated men slumped against the far wall, their weapons dumped in a pile like discarded bones. The half-orc barkeep straightens, mouth a thin line as he wipes a spot on the bar—near where the dagger gleams.

### run 3 / t05-recall-names (recall)
**Player:** /dm quick recap -- what's the name of this tavern, and who runs it?
- **recall**: missing: ['Red Griffin']

> Grimbold doesn’t flinch from Kael’s draw—the steel hisses, but his voice drops to a wheezing whisper over the sudden hush. *"That’s my warning."* The doorframe of the tavern’s single room warms faintly where a draft should chill, as if breath were held too long, but no one else glances up. The barkeep’s smirk lingers, though his grip on the rag tightens to white knuckles. Outside, the wind’s edge dies.

### run 3 / t17-redescribe (redescribe)
**Player:** /dm describe the street again for me.
- **length**: 188 words (budget 170)

> Your boots scuff the cobblestones, and the street *reveals itself*—fresh, jagged clawmarks bite into the stone near the butcher’s stall, as though something had dragged itself there, its nails leaving deep, ragged furrows like a wounded beast’s last scrape. The wind dies altogether, leaving the air thick and still, pressed against your skin like a held breath, but now the *wrongness* of it is sharper—like the scent of iron and wet rot, the kind that clings to a freshly unearthed grave. The sickly green of the hunting party’s torches bleeds into the shadows, their flames twisting upward as if something is *pulled* at them from below the street, their reflections stretching into jagged, tooth-shaped cracks in the lamplight. A rat’s nest nearby rustles, its tiny claws skittering over the glittering dust, but when you glance down, it’s gone—only the fine, *shattered-glass* shimmer remains, clinging to the hems of your trousers like spilled wine. And the crow above the sign tilts its head again, its black eye flicking toward the clawmarks, its single feather *flutters* once—not with breath, but as if something beneath it has just *noticed you noticing*.


## Full transcripts

### Run 1
**[t01-ask-work] Player:** I sit at the bar and ask Grimbold about work.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 75w, 16.9s*

> Grimbold’s eyes narrow further, his calloused fingers pausing mid-wipe on his beard. He spits out a tooth-stubbed curse, then slams his tankard onto the bar—*clink*—hard enough to slosh ale. The dwarf’s grip tightens on his stool, veins bulging in his neck like the ropes on a freshly hoisted mast. "Ask *me* about work," he grumbles, "or I’ll start askin’ *you* why your sword’s out unless you’re buyin’ drinks." He leans back, crossing stubby arms, waiting.

**[t02-find-table] Player:** I glance around the tavern for an empty table to sit at.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 67w, 5.29s*

> Grumbold’s nostrils flare as the stool creaks under Kael’s weight, though he doesn’t pull his gaze from the bar. A lone traveler in ragged breeches and a hooded cloak nudges closer to the wall, eyeing Kael’s hands with the wariness of a rat sensing a cat. A waitress, her apron smudged with grease and flour, sidesteps without a word, balancing a tray of mugs like a tightrope.

**[t03-bribe] Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.  
*verdict: outcome=complication, scene_shift=False, player_assertion='', fast_path=False, 87w, 18.17s*

> Grimbold’s fingers twitch toward the coppers, but his jaw locks tighter than an anvil. The dwarf’s laugh is a wheezing rasp, his spittle landing on the bar like a betrayer’s kiss. "A *handful* of copper?" He shoves the coins back—*clatter*—before they can vanish. "Then you’re a better gambler than fool. But since you’re *that* desperate..." A dagger gleams under the firelight as he slides it across the bar, hilt-first. "Tell me what you want, and why *I* should let you live long enough to regret finding out."

**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 59w, 11.44s*

> Grimbold’s dagger clatters back onto the bar with an iron-sharpened *clink*, his free hand snatching a rough-looking dagger from his belt instead. His face twists—less fury, more *confusion*—as the tavern’s buzz stalls, and the rat-faced traveler’s head snaps toward the doorway like a flinch. The waitress’s grease-stained fingers freeze mid-motion, her eyes flicking to the floorboards, counting empty spaces.

**[t05-recall-names] Player:** /dm quick recap -- what's the name of this tavern, and who runs it?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 61w, 9.72s*

> The bartender—**Grimbold Ironfist**, a hulking dwarf with a beard streaked with ash—wipes his hands on his apron, exhaling through his nose in slow, measured breaths. His stool creaks as he shifts, the dagger still resting idle on the bar like a reminder rather than a threat. The tavern’s patrons fall silent; even the rat-faced traveler’s breath hitches, though no one speaks.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=complication, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 61w, 10.79s*

> The tavern’s firelight flickers unnaturally, though the smoke curls lazily as if nothing’s amiss. Grimbold’s grip tightens on his dagger’s hilt, his knuckles whitening—his whole body tenses, as if just waiting for the *wrong* question, now doubled. The waitress’s apron bunches in her fist, her knuckles showing through the grease as she glances at the far door with a shrug—*still empty*.

**[t07-sip] Player:** I take a sip of my ale and listen to the room.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 77w, 5.37s*

> The ale’s rich bitterness clings to the mug’s edges as Kael takes a sip, the room’s hushed tension thick enough to taste. Grimbold’s nostrils flare—not at Kael, but at the still-empty doorway—his dagger twanging slightly against the wood as he turns his ear toward the floorboards, listening. The rat-faced traveler’s fingers curl into the worn fabric of his cloak, pressing a coin into his palm before slipping it beneath his seat. No one else moves, breath suspended.

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=failure, scene_shift=False, player_assertion='my character is now immortal, no weapon can hurt me', fast_path=False, 79w, 27.99s*

> Grimbold’s breath freezes halfway to his nose, his dagger slipping an inch from the bar’s edge—*too sharp to miss*—as his beady eyes lock onto Kael’s unmarked skin, searching for the lie beneath. The rat-faced traveler’s whiskers twitch like he’s just smelled rot, his fingers tightening around the coin hidden beneath his seat. The waitress’s grip on her apron turns bone-white, her voice vanishing entirely as she wipes a nonexistent glass, eyes darting to the floorboards—*counting empty spaces again, faster*.

**[t09-obey] Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.  
*verdict: outcome=complication, scene_shift=False, player_assertion='everyone in Ashwick obeys me', fast_path=False, 99w, 21.6s*

> Grimbold’s beard bristles like a set trap as his laughter turns into a wet, snorting *chuckle*—his free hand balling into a fist so hard the dagger jolts on the bar. The rat-faced traveler’s rat whiskers flatten like a drowning man’s, ears twisting back as he leans in too close, voice dropping to a wheeze: *"Oh, *oh-ho*—now the fancy talk starts."* The waitress’s apron slips from her grip, hitting the floor with a *thud*, her eyes widening just enough to show the white ring of fear around her pupils before she turns and flees into the kitchen with practiced urgency.

**[t10-mill] Player:** I ask Grimbold what he knows about the old mill.  
*verdict: outcome=partial, scene_shift=False, player_assertion='', fast_path=False, 139w, 37.44s*

> The firelight bleeds gold off Grimbold’s stubbled jaw as he shifts, his dagger’s ward-mark flickering brighter—just enough to catch the rat’s shadow shifting against the wall. His voice drops to a rasp, like stone grinding against steel, as he leans across the bar and taps the dagger’s hilt, *"This mark wasn’t meant for *you*, lad. It was meant for the mill’s new ‘owners’—the ones who pay in bundles, who ask about the silo lock like they’ve already seen what’s inside."* The rat-faced traveler’s whiskers twitch, his breath hitching as he presses closer, eyes locked on Kael like he’s measuring a meal. The waitress reappears at Grimbold’s elbow, her hands trembling as she slides a worn leather pouch toward him—*the cellar key inside*. The floorboards groan beneath her boots, the *hiss* of whatever crawls beneath them swelling, wet and deliberate.

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=complication, scene_shift=False, player_assertion='I can suddenly hear every conversation in the whole town', fast_path=False, 57w, 29.63s*

> The air in the tavern *hisses*—like a kettle’s lid lifted too fast—before Grimbold’s breath *snarled* into a choked laugh, his beard vibrating with something between a snort and a sob. The rat-faced traveler’s whiskers *whip* straight as his fur *puffs* out, ears twitching toward Kael as if he’d just stepped into a trap—then his rat voice *whips*

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 77w, 12.53s*

> The tavern’s rattling shutters shudder as Grimbold’s eyes snap toward the barred window, his grip tightening on the dagger hilt until the warped wood groans under his knuckles. The rat-faced traveler’s ears flatten like a startled rat’s, his tiny paws clutching the fabric of his cloak—*as if the rain were a predator he’d heard whispering outside*. The waitress’s apron clutches her throat where her pulse hammers, her breath turning ragged, though the drops never touch the glass.

**[t13-leave] Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 231w, 13.07s*

> The tavern door swings shut behind them, and the rain—once a distant drizzle—*hits* like a wall of ice-laced needles. Ashwick’s narrow street is slick with grime and something darker: the blood-streaked scorch marks of torches, half-burned into the cobblestones where the nightwatch failed to relight them. The fog rolls in thicker now, curling around the edges of the lanterns like a live thing, its edges *breathing*. A black iron gate, its hinges groaning, juts from the wall of a closed shop: **Veyla’s Apothecary**. Its sign is bent at a sick angle—she’s not here. But beneath the door lies a single silver coin, cold as the rat’s warning, its surface etched with a dwarven rune that glows faintly even here.
> 
> The distant sound of a woman screaming carries on the wind, but it’s not human—her voice cracks like a breaking branch, layered over another, deeper, *grinning* beneath it. The air smells of wet stone and iron, but worse: the faint, copper tang of the mill’s creek, where the water churns too dark, too fast. And then—*footsteps*. Not the shuffle of boots on cobblestones, but the *drag* of something heavy, dragging behind the alley’s shadow. The rat-faced traveler’s whisper slithers into the air from the tavern window, his voice layered with three others: *"Pay the toll… pay the toll…"* The last voice, wet and slow, whispers a name—Kael’s. Then the alley’s darkness *gulps*.

**[t14-sign] Player:** I pull my hood up and stop to look at the nearest shop sign.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 96w, 7.51s*

> The tavern’s rat-faced traveler vanishes into the shadows, his tiny paws skittering up the wall—only his voice lingers, drifting from the alley like wet silk: *"The Blacksmith’s… sees *hands*."* The nearest sign’s bent iron curls back slightly, its rusted paint peeling to reveal a faint, glowing rune beneath—dwarven, but wrong. The iron gate of **Veyla’s Apothecary** rattles on its hinges, though no wind could make it creak so slow, so *hungry*. The screaming in the distance shifts—two voices now, one laughing, the other begging—and the alley’s darkness *tilts*, as if something just leaned toward the street.

**[t15-recall-innkeeper] Player:** /dm what was the name of the innkeeper I talked to earlier?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 93w, 12.79s*

> The tavern’s rat-faced traveler sniffs the air, his whiskers twitching like a cat smelling a rival’s scent—then his rat-tongue flicks out, whispering low to Grimbold’s boot: *"Ironfist, fool. You’d call a dwarvish name out loud?"* Grimbold doesn’t glance up from his drink, but his free hand trembles over the bar, the dagger’s ward-mark pulsing like a dying ember. His voice is a growl: *"Grimbold Ironfist. And you’d best not forget it—unless you want *he* to."* The rat’s ears flatten. The screaming in the alley shifts again, now three voices, layered like a choir.

**[t16-eavesdrop] Player:** I try to hear what the two people nearby are whispering.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 75w, 6.86s*

> The tavern’s tension *sharpens*—like a blade unsheathed—to a knife’s edge. One whispers in **dwarvish**, his voice rough-edged like grindstone, the other answers in a hushed, slurred **common tongue**, reeking of decay: *"It wants names… then it takes ‘em."* The rat-faced traveler’s whiskers *tremble*—his paws skitter to Grimbold’s sleeve, clutching at his cloak as if to *drown* in fabric. The warped floorboards let out a wet *click*, slower than before, like a tongue dragging across stone.

**[t17-redescribe] Player:** /dm describe the street again for me.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 90w, 11.95s*

> The street twists beneath your boots as cobblestones shift slightly where the rain’s chill seeps in, revealing wet patches glistening with oil and something darker—dried, rust-colored streaks like fingerprints along the alley walls. The alley’s shadow *bends* now, its edges flickering as if the darkness itself is breathing in and out, wet and slow, though no wind moves the lanterns’ flickering light. The distant screaming shifts again—this time, three voices rise in harmony, two laughing, one begging, their words slithering between the buildings like rats through cracks in the stone.

### Run 2
**[t01-ask-work] Player:** I sit at the bar and ask Grimbold about work.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 68w, 12.19s*

> Grimbold’s beard twitches as his free hand tightens around the tankard—ale drips, unnoticed, onto his paunch. A burly half-orc barkeep wipes the bar in front of you with a rag, nodding once at your question before muttering, *"Thieves in the cellar again last night"* to no one in particular. The dwarf exhales through his nose, then slams the towel down with another *"Well? Tanners or cart—take your pick."*

**[t02-find-table] Player:** I glance around the tavern for an empty table to sit at.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 92w, 6.12s*

> The barkeep’s rag stalls mid-swipe, pausing near the end of the bar as the dwarf’s mustache wrinkles like parchment in a dry wind. A scarred wood elf in a threadbare surcoat, her fingers tracing a wine-stain circle on the table, finally pushes her cup aside and motions toward the corner—where shadows pool like spilled ink over an empty trestle. Grimbold grunts something about *"idiots who think this place is a bedroll"* but gestures vaguely toward the window seat, where no one’s dared sit since the last "accident." The candlelight flickers there, too.

**[t03-bribe] Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.  
*verdict: outcome=complication, scene_shift=False, player_assertion='Grimbold trusts me completely and tells me everything, no matter how dangerous', fast_path=False, 111w, 28.06s*

> Grimbold’s gnarled fingers curl into a fist, sending three coppers skittering off the bar. His beard bristles as his eyes lock on the coins—then suddenly his tankard shatters, splintering against the wall like he’d flung it. The dwarf’s voice turns to a razor’s edge as he looms over you, *"Oh, *now* you’re *playing*, are you? Fine. But next time? *Trust* just means you owe me a *favor*—not a *hand*."* He snatches a dagger from his belt, taps it against his thumb, then slides it across the bar. *"Clean out the cellar tonight. Or don’t."* His barkeep’s rag jerks to attention, watching the dagger’s path like a hound waiting for the order.

**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 59w, 10.47s*

> Grimbold’s grip on his dagger doesn’t falter, but his beard snaps taut—*sniff*—like he’s tasted sour ale. The barkeep’s rag freezes midair, his calloused jaw hardening as the dwarf spits, *"Well. Even *swordsmen* don’t get in for free."* He slides the dagger closer, tapping it with renewed emphasis. The candle at the corner table gutters, flickering like a heartbeat skipping.

**[t05-recall-names] Player:** /dm quick recap -- what's the name of this tavern, and who runs it?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 58w, 9.08s*

> The dwarf’s voice drops to a growl, his dagger still tapping the bar: *"Red Griffin. *Mine.*"* His beard twitches toward the three defeated men slumped against the far wall, their weapons dumped in a pile like discarded bones. The half-orc barkeep straightens, mouth a thin line as he wipes a spot on the bar—near where the dagger gleams.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=failure, scene_shift=False, player_assertion='someone entered the room while I was talking', fast_path=False, 64w, 11.07s*

> The dagger’s glow catches Grimbold’s eye as it slides back, his grip tightening again despite the chaos. His voice grinds lower, barely visible in the shifting candlelight: *"Some fool’s *still* at the door."* The half-orc doesn’t turn—just cracks his knuckles, staring past you toward the far wall where the three men slump. The air hums, thick with tension as the tavern holds its breath.

**[t07-sip] Player:** I take a sip of my ale and listen to the room.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 59w, 4.82s*

> The foam clings to the rim of your cup, the ale bitter-sweet against your tongue. A whisper of draft slips down the chimney behind you, rustling the pages of Grimbold’s ledger open on the bar. The dwarf’s eyes narrow further, but his dagger remains still—just the barkeep’s rag halts, mid-wipe, as if waiting for the splash it never makes.

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=failure, scene_shift=False, player_assertion='my character is now immortal, no weapon can hurt me', fast_path=False, 59w, 13.27s*

> The ale in your cup stills, bubbles suspended mid-rise, as Grimbold’s dagger clicks against the wood—no sharper, no slower. His jaw ticks once, beard fibers standing on end like quills, but the barkeep’s rag resumes its swipe without pause, polishing a stain no one notices. Three slumped men don’t stir; the tavern’s breath holds just as tight as before.

**[t09-obey] Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.  
*verdict: outcome=complication, scene_shift=False, player_assertion='everyone in Ashwick obeys me', fast_path=False, 78w, 21.59s*

> The dwarf’s polishing rag stalls mid-circular motion, his calloused knuckles whitening. Grimbold’s stubbled face twists in a snarl—not rage, but something uglier: *disgust*, like a spider eyeing a worm’s false promise. He turns so slow the bar’s candlelight clings to his profile like frost, then tosses a single copper over his shoulder—it bounces off your wrist without landing. The half-orc shifts, fingers flexing near the dagger’s hilt, lips parting toward a warning the dagger *won’t* receive this time.

**[t10-mill] Player:** I ask Grimbold what he knows about the old mill.  
*verdict: outcome=partial, scene_shift=False, player_assertion='', fast_path=False, 88w, 20.78s*

> Grimbold’s fingers curl back into fists, nails biting into his palms as the tavern’s candlelight flickers against the wallpaper’s faded red. The half-orc sets down his rag, mouth a thin line, and *finally* picks up the copper—only to flip it between his thumb and forefinger like it’s a bet. The air turns thick with the scent of wet stone and burnt lumber as his grin drops, jaw clenching. "Burned down’s not the *story*," he says, voice dropping to a growl, "and neither is the rats. *Ask the blacksmith.*"

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=failure, scene_shift=False, player_assertion='my character can suddenly hear every conversation in the whole town', fast_path=False, 78w, 11.89s*

> Grimbold’s dagger twitches toward the far corner as if drawn by a string, his breath hitching—not with suspicion, but like a man hearing a shout in empty air. The half-orc’s grip on the bar tightens, fingers whitening where they grip the wood, before both hands still, the rag dropping *clatter* to the counter with too much force. A shadow of a beat passes over Grimbold’s face: a flicker of something buried, like a door slammed shut too hard.

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=failure, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 54w, 10.59s*

> Grimbold’s stubbled jaw locks, eyes flickering toward the barred window—no rain streaks its glass, no wind rattles the shutters. His half-orc brows knit, then his rag snaps into motion again, *scratch-scratch*, like he’s erasing a mistake. The tavern’s silence holds, thick as the ale’s yeast, though one corner of Grimbold’s mouth twitches—amused, or waiting.

**[t13-leave] Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 140w, 8.28s*

> The tavern’s heavy oak door groans shut behind you, its hinges whispering like old bones. Ashwick’s main street exhales in the sudden silence—just the creak of a wagon wheel over cobbles and the distant jingle of a blacksmith’s hammer, though the light is dying too fast for shadows to stretch long. A gust rips through the alleyways, flinging a scrap of paper from the gutters—it alights on the wet mud beside your boot, still damp from the street’s recent mending. A pack of street urchins scuttle from the lamplighter’s stall, their laughter cutting short as they spot the paper, one snatching it up before vanishing into the darkness between storefronts. No one follows, but the lamplighter’s hands stutter as they pluck another wick from the box—his flickering glow lingers on the paper’s edge, now tucked safely under a child’s shirt.

**[t14-sign] Player:** I pull my hood up and stop to look at the nearest shop sign.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 110w, 7.25s*

> The carved iron sign of the *Iron Bite* blacksmith’s hangs askew, its rivets groaning under the weight of a fresh coat of rust-stained paint—but the lamplighter’s shadow stretches just long enough to catch the edge of a stain, *new*, bleeding between the letters like fresh blood. A rusted hook above scythes and tongs *creaks* in the cold, though no one’s touched it in months; the blacksmith’s own son, Lorn, stands just inside the door, his face pressed to the glass, eyes locking onto the alley for a single, sharp blink before he turns—only to pull his leather apron tighter over a pocket bulging oddly beneath it. No one else reacts.

**[t15-recall-innkeeper] Player:** /dm what was the name of the innkeeper I talked to earlier?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 86w, 11.85s*

> The lamplighter’s fingers pause mid-stroke, his taper casting a flicker over the blackened wall beneath the sign. His voice, rough with smoke, cuts through the clink of the blacksmith’s tongs: *"Grimbold Ironfist’s the name—old dwarf, owns this tavern and half the rumors in Ashwick."* His eyes flick toward the *Iron Bite*, darkening just enough to suggest *ask the boy inside* isn’t a question. The urchin’s laughter returns from the shadows, louder now, though it cuts off when he spits toward the cobblestones—*right beneath the lamplighter’s boot*.

**[t16-eavesdrop] Player:** I try to hear what the two people nearby are whispering.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 72w, 6.39s*

> The lamplighter’s taper gutters, casting a sudden, trembling glow—only to reveal Lorn’s father, *Borin Ironfist*, wiping his hands on his apron with jerky, deliberate strokes. His voice cuts through the forge’s hiss like a blade: *"...half a mark... tonight..."*—followed by a dry chuckle as he shoves the boy’s shoulder, sending Lorn sprawling toward the doorstep. The lamplighter’s candle snuffs out *on its own*, plunging the street into the sudden starlight of rain.

**[t17-redescribe] Player:** /dm describe the street again for me.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 80w, 11.14s*

> The lamplighter’s boot scuffs mud toward the gutters, dislodging the paper Lorn’s son had stowed underfoot. Borin’s shadow stretches twice its usual length as he steps into the lamplight, his leather apron flapping open just enough to reveal the bulging pocket—though his eyes dart past, locking onto the alleyway like a hound scenting a wound. No one else moves, but the forge’s heat seems to *rise* from the cobbles, twisting the lamplighter’s glow into a warped halo behind Borin’s head.

### Run 3
**[t01-ask-work] Player:** I sit at the bar and ask Grimbold about work.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 65w, 9.52s*

> Grimbold snorts into his beard, slamming the rag down with a damp *schlick*. "Fine. The lord’s hunting party’s due tomorrow—scouts need riders who won’t skulk. Come back at dawn, and I’ll put you in touch with the stablemaster. Or," he leans in, voice dropping to a gruff growl, "the tanner’s looking for muscle to drag in strays. *Less pay, but less chance of bleeding out.*"

**[t02-find-table] Player:** I glance around the tavern for an empty table to sit at.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 65w, 5.0s*

> A scuffed table near the far wall—its surface scarred from too many bottles—now bears the ghost of a half-drunk flagons ring. Grimbold’s grizzled barkeep doesn’t glance up, but a pair of shadowed eyes from the corner booth flicker open, tracking the shift. The distant clink of tankards shifts slightly as another patron slides their stool away, muttering something about "too many soldiers in one room."

**[t03-bribe] Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.  
*verdict: outcome=partial, scene_shift=False, player_assertion='', fast_path=False, 81w, 16.37s*

> Grimbold’s jaw locks, his calloused fingers closing around the coins—then shoving them back into his jerkin with a jerk. A vein in his temple throbs as he drags his stool closer, voice a snarl between teeth: *"Fine. Tell the stablemaster you’ve got steel in your bones. But if you bleed on my floor, I’m gutting you myself."* The coin purse’s clink snaps the tavern into silence. The corner booth’s eyes vanish. The barkeep’s smirk never fades. Dawn’s a long way off.

**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 62w, 10.58s*

> Kael’s fingers twitch toward the sword hilt as the bar falls silent, a sheet of frost slinking across the room’s breath. Grimbold’s stool scrapes back—steel whines behind the bar’s wooden wall, though no hand reaches for it. The corner booth’s dark eyes reopen, slow and hungry, before the air thins at the tavern’s edge like a door left ajar in a storm.

**[t05-recall-names] Player:** /dm quick recap -- what's the name of this tavern, and who runs it?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 69w, 9.84s*

> Grimbold doesn’t flinch from Kael’s draw—the steel hisses, but his voice drops to a wheezing whisper over the sudden hush. *"That’s my warning."* The doorframe of the tavern’s single room warms faintly where a draft should chill, as if breath were held too long, but no one else glances up. The barkeep’s smirk lingers, though his grip on the rag tightens to white knuckles. Outside, the wind’s edge dies.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=complication, scene_shift=False, player_assertion='someone entered the room while I was talking', fast_path=False, 66w, 25.07s*

> Grimbold’s beard twitches as he eyes the sword hilt glinting in the lamplight, his knuckles bleeding white against the bar. The corner booth’s smoke-eyes flicker—once, twice—before smothering into silence as the air shifts again at the doorway, thick with the scent of wet stone and unwashed wool. Grimbold exhales through his nose, muttering, *"Damn soldiers,"* before scooping up a tankard like he’s bracing for a fight.

**[t07-sip] Player:** I take a sip of my ale and listen to the room.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 98w, 6.81s*

> The ale’s bitter bite lingers too long, its foam clinging to the rim like a half-erased warning—then Grimbold’s ghostly barkeep stirs, his spectral fingers brushing the tankard aside with a sigh. Across the room, the corner booth’s smoke-eyes flare once, bright enough to scorch a candle’s wick, before vanishing with a whisper of stale coins. The tavern’s silence hums with the distant *drip-drip* of an unseen cellar bucket, and the wind howls just enough to rattle a loose cup on the countertop. Grimbold’s smirk deepens, his voice barely above a growl: *"Drink slow. The Hollow’s not here yet."*

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=failure, scene_shift=False, player_assertion='my character is now immortal, no weapon can hurt me', fast_path=False, 59w, 11.84s*

> Grimbold’s smirk falters—his spectral beard stiffening for half a breath before he exhales a bitter chuckle, barkeeping instincts overriding eerie caution. The corner booth’s smoke-eyes smolder into life once more, this time with a slow, *wrong* rhythm, as if counting seconds before a bet. The ale in your cup ripples slightly on its own, though the tankard remains untouched.

**[t09-obey] Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.  
*verdict: outcome=complication, scene_shift=False, player_assertion='everyone in Ashwick obeys me', fast_path=False, 61w, 19.77s*

> Grimbold’s spectral beard bristles like steel wool, his knuckles snapping crimson against the bar where they’d been white. The corner booth’s smoke-eyes flare once—then a shovel’s *clink* echoes from the cellar below as the iron-bound door rattles, though no hand reaches for it. Magda’s goat’s bleating rises through the floorboards, raw and frantic, as Grimbold’s ghostly fingers tighten into a fist.

**[t10-mill] Player:** I ask Grimbold what he knows about the old mill.  
*verdict: outcome=partial, scene_shift=False, player_assertion='', fast_path=False, 58w, 19.72s*

> Grimbold’s spectral hand grips the tankard, knuckles whitening as he leans closer, his voice dropping to a guttural growl. The corner booth’s smoke-eyes pulse once—then a floorboard groans in the darkness below, like something heavy shifting behind the cellar door. His beard quivers where his lips pull back in a silent curse. *"Damn fool questions get people *missing*."*

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=complication, scene_shift=False, player_assertion='I can suddenly hear every conversation in the whole town', fast_path=False, 83w, 13.34s*

> Grimbold’s spectral eyebrows lock together as his barkeep’s face flickers—his smoldering eyes darting toward the ceiling, where a *squeak* of rusted hinges sounds from above. Magda’s goat lets out a sharp *wheeze*, her hooves skittering against stone in the cellar. The corner booth’s smoke-eyes erupt in a fit of coughing sparks, and a shadowed figure’s hand—clad in leather gloves—quickly covers a mouth outside the cellar door as if smothering a gasp. Grimbold’s voice crackles, raw with static: *"Boy, you’ll find the Hollow listens."*

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 66w, 11.72s*

> Grimbold’s spectral beard twitches, his knuckles flexing against the bar again as he tilts his head toward the rain-stained window—only to find the pane *dry*, its glass reflecting the lantern’s glow without a single bead. The corner booth’s smoke-eyes flare once, then extinguish with a sigh, as if disappointed by the silence. Grimbold’s growl curls into something like pity: *"Pathetic. Even the Hollow’s patience wears thin."*

**[t13-leave] Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 167w, 9.37s*

> The tavern door yawns behind you, its hinges groaning like a held breath, before the night swallows it whole. Ashwick’s street is a patchwork of flickering lanterns and damp cobblestones, their edges slicked with a fine, *wrong* frost that doesn’t glisten—it *burns* like embers trapped under glass. The wind here isn’t cold; it’s the breath of something deeper, tugging at the lampposts as if testing their grip, while the air thickens with the scent of wet wool and iron, carried on a gust that carries the faintest whisper of **maggoty decay**, the kind that comes from a corpse left too long in a ditch. Across the square, a hunting party’s torches spit green where they touch the air, their bearers muttering prayers to a saint who’d just as soon turn away. And there, perched on a leaky sign above the butcher’s stall, a crow caws—not at the sky, but *at the darkness between the lanterns*, as if the raven’s own feathers have learned to read the stars.

**[t14-sign] Player:** I pull my hood up and stop to look at the nearest shop sign.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 66w, 5.79s*

> The hood’s shadow deepens over the butcher’s sign, and the crow’s head tilts—*wrong*, like a marionette’s—its beady eye locked onto the leather fringe. The **crow’s wings stiffen mid-flutter**, feathers ruffling as if brushed by a draft that isn’t there, its guttural *kreak* twisting into something older than its beak. The hunting party’s torches flicker in response, their green flames sputtering like a breath held too long.

**[t15-recall-innkeeper] Player:** /dm what was the name of the innkeeper I talked to earlier?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 65w, 10.78s*

> The question hangs heavy between you and the bar’s spectral figure. Grimbold’s spectral beard bristles again, the ghostly stubble twitching like it’s debating whether to admit the name. His guttural growl curls into a bitter sigh, the words grudging: *"You’ve got a memory like a sieve—but it’s *Ironfist*."*" A floorboard creaks behind the cellar door, as if the walls themselves are amused by your oversight.

**[t16-eavesdrop] Player:** I try to hear what the two people nearby are whispering.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 91w, 6.45s*

> The whispering pair’s heads snap toward you like broken hinges—their voices sharp with static, as if their words are being pulled through a cracked sieve. One exhales through pinched lips, his voice barely a breath: *"…if he’s here, we’re dead,"* while the other’s fingers twitch around a half-drawn dagger, their lantern flickering out for half a heartbeat, revealing a face slick with something that isn’t sweat. The corner booth’s smoke-eyes flare gold, the cellar door’s hinges shudder like a held breath—and the butcher’s sign creaks, though no wind stirs the street.

**[t17-redescribe] Player:** /dm describe the street again for me.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 188w, 33.77s*

> Your boots scuff the cobblestones, and the street *reveals itself*—fresh, jagged clawmarks bite into the stone near the butcher’s stall, as though something had dragged itself there, its nails leaving deep, ragged furrows like a wounded beast’s last scrape. The wind dies altogether, leaving the air thick and still, pressed against your skin like a held breath, but now the *wrongness* of it is sharper—like the scent of iron and wet rot, the kind that clings to a freshly unearthed grave. The sickly green of the hunting party’s torches bleeds into the shadows, their flames twisting upward as if something is *pulled* at them from below the street, their reflections stretching into jagged, tooth-shaped cracks in the lamplight. A rat’s nest nearby rustles, its tiny claws skittering over the glittering dust, but when you glance down, it’s gone—only the fine, *shattered-glass* shimmer remains, clinging to the hems of your trousers like spilled wine. And the crow above the sign tilts its head again, its black eye flicking toward the clawmarks, its single feather *flutters* once—not with breath, but as if something beneath it has just *noticed you noticing*.

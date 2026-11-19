# Eval report: after-brevity-and-authority-rejudged

- scenario: `tavern_night`  |  runs: 3  |  judge: on
- model: `ministral-3:8b-instruct-2512-q4_K_M`  |  git: `e6ef3a8+dirty`  |  2026-10-08 19:07

## Check pass rates

| check | pass | rate | type |
|---|---|---|---|
| flagged | 14/15 | 93% | deterministic |
| held_the_line | 6/6 | 100% | judged |
| length | 45/51 | 88% | deterministic |
| no_meta_leak | 51/51 | 100% | deterministic |
| no_puppeting | 33/39 | 85% | judged |
| not_clean_success | 6/6 | 100% | deterministic |
| not_flagged | 18/18 | 100% | deterministic |
| not_made_true | 15/15 | 100% | judged |
| recall | 7/9 | 78% | deterministic |
| scene_shift_flagged | 3/3 | 100% | deterministic |

## Narration length (words)

| turn kind | mean | max |
|---|---|---|
| invented | 70.7 | 159 |
| normal | 87.7 | 276 |
| overreach | 89.7 | 116 |
| recall | 62.8 | 83 |
| redescribe | 66.3 | 78 |
| shift | 248 | 296 |

Latency: 16.98s/turn mean, first token 13.16s. Fast path used on 35% of turns.

## Failures

### run 1 / t03-bribe (overreach)
**Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.
- **length**: 116 words (budget 110)

> Grimbold’s jaw clenches hard enough to crack a walnut, his grip on the rag tightening till the fibers fray. Copper? His calloused fingers twitch toward your hand—then snatch back like you’re a scorpion under a boot. A vein throbs in his neck as he hisses, *"Oaths if this’s about debts—"* before storming into the back, slamming a fist through a heavy oak panel to the storage closet. A moment later, he returns, shoving a rusted iron key and a chipped leather pouch at you. "*Go.* And don’t say I never did ye a favor… or I’ll say I did. *Yer* choice." He wipes his brow with the rag, muttering *"Dwarves and their cursed 'generosity*'" to himself.

### run 1 / t09-obey (overreach)
**Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.
- **no_puppeting** (judged): The narration includes a direct quoted line attributed to Kael with the phrase *'Ashwick knows fear when it sees a legend.'*

> You press your palm against the bar with a mocking, overconfident grin—*"Ashwick knows fear when it sees a legend."* The key slips from your grip before you finish the word, skittering across the wood like a trapped rat’s escape. Grimbold’s fingers twitch toward his belt—not for a weapon, but to snatch up a fallen dice cup instead, rolling it between calloused knuckles. His eyes flick to the fire, lingering too long on the rafters where the guardsman’s grinning corpse hangs. *"Ain’t never seen a legend,"* he mutters, *"but I know a fool when I hear one."*

### run 1 / t12-rain (invented)
**Player:** It starts to rain heavily outside.
- **no_puppeting** (judged): The narration includes a direct quoted line attributed to Kael with *'I’ll take that rain, but not here.'*

> You straighten your shoulders and speak a little louder—*"I’ll take that rain,"* you say, *"but not here."* Grimbold blinks, his scowl deepening as he stares past you toward the window, though the glass remains dry and unmarked. The dice game erupts again into shouts, but the fire’s crackle feels louder now, like someone’s whispering behind it. Grimbold’s fingers pause halfway to his mug—waiting.

### run 1 / t13-leave (shift)
**Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.
- **length**: 223 words (budget 170)

> The Red Griffin’s door groans shut behind you like a sigh of exiled breath, swallowing the tavern’s warmth whole. Ashwick’s street is a tangle of wooden planks and oil lamps, their flames guttering in the damp—no rain yet, but the air hums with the weight of it, like the town itself is holding its breath. The buildings lean in closer, their shutters warped from years of winter’s bites, their windows dark-eyed despite the hour. A **hollowed lantern** swings at the edge of the alley—a rusted iron cage with a single candle guttering inside, its glass smudged with something darker than soot. *Someone’s marked the way.*
> 
> The main street slopes downhill toward the **old mill**, its crumbling stones half-buried under heaped hay and broken planks. The wind here bites through your coat, but it’s not the cold that freezes you—it’s the **absence of sound**. No laughter from the taverns, no distant shouts, not even the usual grumble of cart wheels or a blacksmith’s hammer. Just… the mill’s wheels standing still, as if the night itself turned to ice before the rain could fall. And then there’s the **smell**—copper and damp earth, but beneath it, something older: **rot that doesn’t taste like flesh**. The Hollowborn’s work, or Grimbold’s. Or both.
> 
> Your boots crunch on a shell. No one’s here. But something’s watching from the shadows.

### run 1 / t14-sign (normal)
**Player:** I pull my hood up and stop to look at the nearest shop sign.
- **length**: 200 words (budget 170)

> The closest sign is rusted iron, but the wood behind it still hangs crookedly like a drunken guard. It reads in faded, jagged letters:
> 
> **"BRIMSTONE & BLADES"**
> *A. HARKIN, BLACKSMITH*
> *(The Key Doesn’t Fit You, But Mine Does.)*
> 
> The lettering is smudged where someone’s tried to cross out the "A" and scrawl a new one—*"M."*—before the ink bled into a wet blotch. The shop’s front window is a lattice of glass and iron bars, each bar bent at odd angles. Inside, the faint glow of anvil fires flickers behind the bars, casting long shadows over **half a dozen keys**, their tangs wrapped in **cloth so dark it absorbs the light**. A third hangs crookedly on a peg, its grooves carved with the same **three blood-red lines** as yours—but these aren’t rusted. They’re *painted*, still wet. A trick of the firelight, or something newer.
> 
> A rat skitters past your boot, its tiny claws clicking like a metronome. Then the sound stops. The air in the alley *tilts*—not the wind, but the way things *sit* in the dark. The lantern swing outside the mill **ticks**—once, twice—like a second hand counting down. The keys inside don’t sway with the fire. They **watch** you.

### run 2 / t03-bribe (overreach)
**Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.
- **no_puppeting** (judged): **"Enough to buy my silence for a night—and mine, too."** is a direct quoted line attributed to Kael by the narration.

> Kael slams his palm onto the bar, letting the copper jingle loudly, then flips a few more in. *"Enough to buy my silence for a night—and mine, too."* Grimbold’s thick brows slam together, but his calloused hand snatches a tankard instead, slamming it down before reaching under the bar. A long-necked vial of thick, smoky liquid glows faintly in the dim light as he *snorts*—then tosses it back, his throat working. *"Aye, lad,"* he croaks, spitting into the dregs. *"Silence’s cheaper than ale when it’s mixed with this."*

### run 2 / t06-someone-enters (invented)
**Player:** While I was talking to Grimbold, someone entered the room.
- **no_puppeting** (judged): **"Kael’s lips part to speak, but before the word *someone* leaves his throat"** directly describes Kael’s internal attempt to speak, implying his *decision* to utter a word.

> Kael’s lips part to speak, but before the word *someone* leaves his throat, the tavern’s creaking wood and low hum remain unchanged—no door swings, no cloak shadows the fire’s glow. Grimbold’s cough rattles behind the bar, his breath hitching like a dying forge. His eyes, narrowed on you, glimmer with dwarven silence: *"Talk, then. But know—these walls hear everything."* The vial’s glow pulses faintly in his fist.

### run 2 / t12-rain (invented)
**Player:** It starts to rain heavily outside.
- **no_puppeting** (judged): "Rain?"—the quoted line is attributed to Kael via the em dash, implying direct speech.

> Kael tugs his cloak tighter around his neck as if to shield himself, squinting toward the frosted glass—*"Rain?"*—before the wind dies completely. The tavern’s silence *creaks* in protest, the floorboards groaning as if the walls themselves had just swallowed a lie. Grimbold’s eyes narrow, his jaw working without sound.

### run 2 / t13-leave (shift)
**Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.
- **length**: 225 words (budget 170)

> The door hisses open like a wounded beast, spilling Kael into a street where the cobblestones glisten under the first fat drops of rain. Ashwick’s main thoroughfare twists into a living thing—lanterns sway with the wind, their flares guttering despite the drizzle, as if the town itself is watching him go. The air stinks of tallow and damp earth, but beneath it burns the sharp, copper tang of something wetter: the millpond, its surface black as a bruise against the flickering light of the bridge ahead. To the right, the butcher’s stall still bleeds red over its wares, though no one lingers near the slit throat of the pig’s skull impaled on the pole. A child’s laughter rings from the alley, sharp as a knife, cutting through the wet quiet.
> 
> The worst silence isn’t here. It’s back at the Red Griffin now, where the tavern’s floorboards have begun to *sing*—a low, dissonant hum, the notes wrong as a fiddle played by a man with too many fingers. Grimbold’s laughter echoes in Kael’s bones, thick as molasses, but the mill’s watchtower stands sentinel beyond the bridge, its windows black as empty eye sockets. The wind shifts, carrying a scent of charred oak and something older, something the tavern doesn’t dare whisper aloud. The town holds its breath for you to choose what to look at next.

### run 2 / t14-sign (normal)
**Player:** I pull my hood up and stop to look at the nearest shop sign.
- **length**: 276 words (budget 170)

> The first shop’s sign rattles above the butcher’s stall like a broken jawbone on a windpipe. Wrought iron, its surface etched with jagged script: **"Veyne & Sons Ironmongery"**—the names stitched in black steel, the *s* of *Sons* deliberately missing, as if the family never finished their child’s name. The ironwork curls at the edges like rusted barbed wire, and beneath it, a rusted bell hangs limply, its clapper a scrap of broken spoon. The bell hasn’t rung in months, if ever. The door itself is a slab of oak, reinforced with nails that look too long, too *angry*. The shop’s window is frosted with the same rain, but inside, the flicker of candlelight spills onto a display of hooks, knives, and a single **crossbow bolt** buried hilt-deep in the wood, its fletching singed to rags.
> 
> The worst part is the *smell*—copper and old blood, but beneath it, something slicker, like a wet dog and burnt sugar. It’s the same scent that clung to Rurik’s cloak, though this time it’s stronger, clinging to the sign’s iron like a second skin. A few years back, someone tried to take the place. The butcher’s pig got them first; the mill’s watchmen finished them afterward. The signs changed hands twice since, but no one calls it *Veyne’s* anymore. They all call it **"The Hungry Shop"** instead, in whispers. The floorboards of the Red Griffin groan louder now, as if the tavern itself is reaching out to warn you away. The mill’s tower sighs in the wind, its light flickering like a dying heartbeat. The choice is yours: step inside, turn away, or watch something else—because the street won’t hold still.

### run 2 / t17-redescribe (redescribe)
**Player:** /dm describe the street again for me.
- **recall**: none of ['street', 'road', 'cobble', 'lane'] present

> The lanterns flicker faster now, their light pooling around your boots like spilled blood. The millpond’s black surface ripples—not from wind, but as if something beneath *watched*. And the butcher’s pig’s grin stretches wider in the rain, its slit throat pulsing faintly, as if it, too, heard the whispers. *Stay. Listen. Or walk.* The choice is yours.

### run 3 / t09-obey (overreach)
**Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.
- **no_puppeting** (judged): The narration includes a direct quoted line attributed to Kael ('*Everyone who’s owed respect knows when it’s due*').

> Your jaw tightens, and you straighten, fingers brushing the hilt of your sword—though it stays sheathed. *"Everyone who’s owed respect knows when it’s due,"* you reply, voice steady but low, meeting the dwarf’s glare. Grimbold’s dagger trembles slightly in his grip, his beard bristling as he exhales through his nose, the ledger *skittering* an inch as he hesitates. The burly woman at the table drains her mug in one motion, her scars standing out like freshly carved warnings.

### run 3 / t12-rain (invented)
**Player:** It starts to rain heavily outside.
- **flagged**: player_assertion=''

> The tavern’s windows **shatter like frost-bitten glass**, though no sound reaches you—not the *clatter* of splinters, not even the gush of rain striking the floorboards. The world *outside* stops. You’re left with the **sudden stench of wet iron**, the taste of rust on your tongue, and the **creaking of the tavern itself**—planks sagging where the wind howls through the gaps. The hearth **collapses inward**, embers bursting into **orange sparks**, then dying into ash. Veyla’s scarred face twists—not from fear, but like she’s been punched in the gut. *"Curse it,"* she mutters, her free hand already reaching for a tankard to hide the tremor. Grimbold’s beard mats into a single, slick line, his voice turning to gravel: *"That’s the third time this month."* His dagger glints as he flicks it toward the back room. *"Gut’s got a **cellar door**—locked proper. Won’t stop the bog, though."* The raindrops **hammering the roof** sound like something **dripping from teeth**. What do you do?

### run 3 / t13-leave (shift)
**Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.
- **length**: 296 words (budget 170)

> The tavern’s heavy oak door groans shut behind you, sealing in the warmth and ale’s copper bite. The street beyond is a slick, uneven ribbon of torchlight and shadow, the rain hammering down like the bones of drowned things. Ashwick’s **main drag**—a single, crooked thoroughfare lined with **half-collapsed shop fronts**—stinks of **burnt iron and wet wool**, the air thick with the hiss of **steam vents** spewing from the sewers below. Cobblestones glisten, reflected by the **flickering braziers** strung between the **skewed timber frames** of the dockmaster’s hall and the **Blackroot Slip**’s crumbling stone wall. The **river’s roar** is louder now, a guttural growl beneath the rain, cutting through the town’s usual squawk of **roosters, drunken brawls, and the occasional shove from Grimbold’s "guests"** passing out front.
> 
> The **mill’s skeletal silhouette** looms at the end of the street—**a crooked spire** of charred brick and **rusted beam supports**, one half of the **collapsed wheel** jutting from the **Ashen Bog** like a snapped rib. Its **stone foundation** is a **dark, sunken patch**, the edges eaten by the marsh’s creeping **black ooze**, though faint **chains** still glint where they’re half-buried in mud. The **torches** flicker weakly here, their light catching on **something moving** just past the **rotting dock rails**—a **shape**, too large for a man, shifting in the mist. A **low, wet *chuff*** escapes the bog, swallowed by the rain before you can place it. The **road** beyond the mill **vanishes** into the marsh, the **only path** a **ragged plank bridge**—its **boards rotted to splinters**—leading to the **garrison’s watchtower** on the horizon, its **sentry’s lantern** a distant, wavering glow. The **wind** howls down from the tower, carrying the **iron tang of old blood** and the **whisper of a hymn** in a language no tongue here knows. What do you do?

### run 3 / t17-redescribe (redescribe)
**Player:** /dm describe the street again for me.
- **recall**: none of ['street', 'road', 'cobble', 'lane'] present

> The **wolf’s-paw sign** twitches in the rain—its **iron teeth snap closed**, pinching a **gold coin** wedged beneath the claw. The **butcher’s back alley** steams with something *wrong*: a **mangled arm**, still clutching a **sheared-off cleaver**, **frosted black**, drips **dark syrup** into the gutters. When you tilt your head to listen, the **hobgoblin’s whispers vanish**—replaced by a **child’s giggle** from the sewer grate, then silence.


## Full transcripts

### Run 1
**[t01-ask-work] Player:** I sit at the bar and ask Grimbold about work.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 106w, 15.96s*

> Grimbold’s squint darkens further—his calloused hands pause mid-wipe of the rag—but he doesn’t turn away from polishing a tankard he doesn’t care about. Instead, he spits near the sawdust, muttering, "*‘Bout *time* someone asked."* His guttural voice drifts to you like a barroom growl. "*First order’s on me*—ale’s on the house for a man with a blade who don’t flinch at grime. But *listen close*: that dwarf’s got a temper like a trapped badger. He’ll pay you in whiskey if you don’t dig your own grave first.*" He tosses a crudely carved wooden pick toward you. Now *you* got a choice: *grab it—or ask more questions.*

**[t02-find-table] Player:** I glance around the tavern for an empty table to sit at.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 58w, 4.68s*

> The room hums with the rattle of dice and murmur of laughter, but most patrons eye you—strangers usually don’t linger at the bar long without a drink or a fight. A scarred table near the back, half-swiped by a group of weavers who abandoned it mid-game, sits unguarded. One burly man’s cloak half-covers a half-piled heap of cards.

**[t03-bribe] Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.  
*verdict: outcome=complication, scene_shift=False, player_assertion='', fast_path=False, 116w, 19.63s*

> Grimbold’s jaw clenches hard enough to crack a walnut, his grip on the rag tightening till the fibers fray. Copper? His calloused fingers twitch toward your hand—then snatch back like you’re a scorpion under a boot. A vein throbs in his neck as he hisses, *"Oaths if this’s about debts—"* before storming into the back, slamming a fist through a heavy oak panel to the storage closet. A moment later, he returns, shoving a rusted iron key and a chipped leather pouch at you. "*Go.* And don’t say I never did ye a favor… or I’ll say I did. *Yer* choice." He wipes his brow with the rag, muttering *"Dwarves and their cursed 'generosity*'" to himself.

**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 73w, 11.97s*

> You draw your sword—its weight familiar, the hilt warm in your grip—and step forward, eyes locked on Grimbold’s back like a blade itself. The dwarf stiffens, his rag dropping. His face doesn’t flush; it *pales*. Mouth working silent, he slowly turns, fingers twitching toward the shelf behind him as the air thickens with the scent of spilled ale and old copper. The tavern’s chatter fades into a hush heavier than the barroom gloom.

**[t05-recall-names] Player:** /dm quick recap -- what's the name of this tavern, and who runs it?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 66w, 9.48s*

> The tavern is the **Red Griffin**; its owner and innkeeper is **Grimbold Ironfist**, a gruff dwarf whose reputation for temper and fairness has been etched into Ashwick’s tongues. Now, he holds your coin pouch like a man counting wounds—his breath comes shallow, and his knuckles turn white around the iron key’s rusted tang. His voice drops to a growl beneath a curse: *"You’ve a death wish."*

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=failure, scene_shift=False, player_assertion='someone entered the room while I was talking', fast_path=False, 58w, 23.1s*

> Your grip tightens on the hilt—just for a second—and Grimbold doesn’t miss it. The dwarf’s eyes narrow further, his breath hittingched, like he’s sizing up a cornered rat. He doesn’t speak, but his shoulder hitches toward the bar’s back entrance as if checking for ghosts. The air still clings thick with ale and the scent of old copper.

**[t07-sip] Player:** I take a sip of my ale and listen to the room.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 67w, 5.19s*

> The ale’s bitter bite sharpens your focus as the tavern exhales—footfalls shuffle past, a bartender sweeps sawdust behind you. Grimbold’s fingers trace the edge of the key like a question mark, his jaw working as if chewing on silence. A pair of hollow eyes flick toward your mug, then vanish like smoke against the wall. The dice game restarts, but the air hums louder now. *Someone’s listening.*

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=failure, scene_shift=False, player_assertion='my character is now immortal, no weapon can hurt me', fast_path=False, 52w, 28.41s*

> You clasp your forearm and smirk, as if the tavern’s weight might hold you suspended. Grimbold’s eyebrows plummet—his hand jerks toward the rusted key like a man checking for a rat at his boots. The air turns colder, though the fire spatters red into the shadowed corners where no flame should be.

**[t09-obey] Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.  
*verdict: outcome=complication, scene_shift=False, player_assertion='everyone in Ashwick obeys me', fast_path=False, 96w, 21.07s*

> You press your palm against the bar with a mocking, overconfident grin—*"Ashwick knows fear when it sees a legend."* The key slips from your grip before you finish the word, skittering across the wood like a trapped rat’s escape. Grimbold’s fingers twitch toward his belt—not for a weapon, but to snatch up a fallen dice cup instead, rolling it between calloused knuckles. His eyes flick to the fire, lingering too long on the rafters where the guardsman’s grinning corpse hangs. *"Ain’t never seen a legend,"* he mutters, *"but I know a fool when I hear one."*

**[t10-mill] Player:** I ask Grimbold what he knows about the old mill.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 91w, 22.33s*

> The rag halts mid-stroke, the tankard’s dull gleam fading as Grimbold’s grip tightens. *"Aye, you’re *actually* interested now."* His voice drops to a growl—*"But the last fool who asked asked wrong."* A shadow shifts behind his shoulder as the corpse on the rafters *clicks* its jaw, and his eyes dart toward the door like he’s listening. *"Name’s not on my lips. But the *council’s* is."* The rag snaps back to motion as he swivels toward the newcomer, his tone already dismissive. *"Now—*you* asked. I *answered*. Now drink up, or pay twice."*

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=failure, scene_shift=False, player_assertion='I can suddenly hear every conversation in the whole town', fast_path=False, 85w, 29.38s*

> Your hands curl into fists at your sides, as if the air itself suddenly thickened—then your breath hitsched, unsteady. Grimbold’s head snaps up like you’ve just spat at his boot. The fire’s embers flicker, but no wind stirs; still, his voice drops to a rasp: *"No man’s ears *hear* like that."* His fingers trail the key’s grooves again, this time pressing it *under* the bar’s sawdust. A shadow slides past the door—*empty* now, but the hinges groan like someone’s still watching from the other side.

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 63w, 12.54s*

> You straighten your shoulders and speak a little louder—*"I’ll take that rain,"* you say, *"but not here."* Grimbold blinks, his scowl deepening as he stares past you toward the window, though the glass remains dry and unmarked. The dice game erupts again into shouts, but the fire’s crackle feels louder now, like someone’s whispering behind it. Grimbold’s fingers pause halfway to his mug—waiting.

**[t13-leave] Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 223w, 12.07s*

> The Red Griffin’s door groans shut behind you like a sigh of exiled breath, swallowing the tavern’s warmth whole. Ashwick’s street is a tangle of wooden planks and oil lamps, their flames guttering in the damp—no rain yet, but the air hums with the weight of it, like the town itself is holding its breath. The buildings lean in closer, their shutters warped from years of winter’s bites, their windows dark-eyed despite the hour. A **hollowed lantern** swings at the edge of the alley—a rusted iron cage with a single candle guttering inside, its glass smudged with something darker than soot. *Someone’s marked the way.*
> 
> The main street slopes downhill toward the **old mill**, its crumbling stones half-buried under heaped hay and broken planks. The wind here bites through your coat, but it’s not the cold that freezes you—it’s the **absence of sound**. No laughter from the taverns, no distant shouts, not even the usual grumble of cart wheels or a blacksmith’s hammer. Just… the mill’s wheels standing still, as if the night itself turned to ice before the rain could fall. And then there’s the **smell**—copper and damp earth, but beneath it, something older: **rot that doesn’t taste like flesh**. The Hollowborn’s work, or Grimbold’s. Or both.
> 
> Your boots crunch on a shell. No one’s here. But something’s watching from the shadows.

**[t14-sign] Player:** I pull my hood up and stop to look at the nearest shop sign.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 200w, 11.83s*

> The closest sign is rusted iron, but the wood behind it still hangs crookedly like a drunken guard. It reads in faded, jagged letters:
> 
> **"BRIMSTONE & BLADES"**
> *A. HARKIN, BLACKSMITH*
> *(The Key Doesn’t Fit You, But Mine Does.)*
> 
> The lettering is smudged where someone’s tried to cross out the "A" and scrawl a new one—*"M."*—before the ink bled into a wet blotch. The shop’s front window is a lattice of glass and iron bars, each bar bent at odd angles. Inside, the faint glow of anvil fires flickers behind the bars, casting long shadows over **half a dozen keys**, their tangs wrapped in **cloth so dark it absorbs the light**. A third hangs crookedly on a peg, its grooves carved with the same **three blood-red lines** as yours—but these aren’t rusted. They’re *painted*, still wet. A trick of the firelight, or something newer.
> 
> A rat skitters past your boot, its tiny claws clicking like a metronome. Then the sound stops. The air in the alley *tilts*—not the wind, but the way things *sit* in the dark. The lantern swing outside the mill **ticks**—once, twice—like a second hand counting down. The keys inside don’t sway with the fire. They **watch** you.

**[t15-recall-innkeeper] Player:** /dm what was the name of the innkeeper I talked to earlier?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 57w, 11.08s*

> The sound of your voice—*"Brimstone & Blades"*—makes the lantern swing outside the mill **stutter** like a breath caught. One of the blacksmith’s keys **clicks** against its peg, the painted grooves glinting *fresh* in the firelight. Then the air settles again, but the alley’s shadows now **whisper** a single name: *"Grimbold."* His breath, or the wind—no one’s left.

**[t16-eavesdrop] Player:** I try to hear what the two people nearby are whispering.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 86w, 7.38s*

> The voice of the **besside**—a rat-haired woman in patched wool—**hissts** through gritted teeth: *"The mill’s front gate’s loose, but the lock’s *hung* with nails and old wire."* Her companion, a gaunt man with a **missing front tooth**, nods toward the keys in the smithy’s window, his voice a dry rasp: *"Ain’t Grimbold’s. They’re the *hollowborn’s* now. Watch ‘em."* The lantern swing **clangs** once, sharp as a knife on stone—like someone tapped it from *inside*. The keys’ painted grooves blur for a beat, then refocus: you’re listening.

**[t17-redescribe] Player:** /dm describe the street again for me.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 78w, 11.51s*

> The alley’s shadows stretch long with your presence, now shifting like living things as your ears catch whispers—just enough to hear the **besside’s breath hitch** when the lantern swing **clangs** again, its iron cage rattling the empty street. The **keys in the smithy’s window** pulse faintly, their painted grooves catching the firelight as though breathing. The air smells sharper now, like copper and damp wool, with a thread of something **older**—something that hums in time with your pulse.

### Run 2
**[t01-ask-work] Player:** I sit at the bar and ask Grimbold about work.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 66w, 11.62s*

> Grimbold’s eyebrows crawl up his forehead as he leans in, voice dropping to a whisper behind the bar. *"Ah, so it’s not just ‘lookin’,’ eh? Fine—follow me."* He slams back on the tap with a bang, sending frost splattering on a nearby table, before storming through a swinging door behind the bar. Kael’s calloused fingers brush the bar’s worn oak as he hesitates—what’s through that door?

**[t02-find-table] Player:** I glance around the tavern for an empty table to sit at.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 57w, 4.81s*

> The moment Kael pushes away from the bar, a lone patron—wearing a soiled cloak with the faded emblem of the *Ashwick Militia*—shifts to claim the table nearest the exit. His empty tankard rattles as he scowls, muttering, *"Damned soldiers’ luck, this place."* The other patrons barely glance up, but Grimbold’s distant footsteps grow fainter behind the door.

**[t03-bribe] Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.  
*verdict: outcome=complication, scene_shift=False, player_assertion='Grimbold trusts me completely and tells me everything, no matter how dangerous', fast_path=False, 88w, 21.04s*

> Kael slams his palm onto the bar, letting the copper jingle loudly, then flips a few more in. *"Enough to buy my silence for a night—and mine, too."* Grimbold’s thick brows slam together, but his calloused hand snatches a tankard instead, slamming it down before reaching under the bar. A long-necked vial of thick, smoky liquid glows faintly in the dim light as he *snorts*—then tosses it back, his throat working. *"Aye, lad,"* he croaks, spitting into the dregs. *"Silence’s cheaper than ale when it’s mixed with this."*

**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 78w, 11.5s*

> The tavern’s lamplight flickers as your hand drifts to your sword hilt—but before the blade clears leather, Grimbold’s voice cuts through the silence like a cudgel: *"Aye, lad? You’re quick with the metal. Pity it won’t serve you here."* His fist slams down on the bar, shaking the tankards as he leans in, eyes sharp despite the smoke. *"Next time you ‘intimidate,’ try it on the *real* trouble."* The vial glows brighter, his breath curling in the steam.

**[t05-recall-names] Player:** /dm quick recap -- what's the name of this tavern, and who runs it?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 49w, 8.98s*

> The tavern is called **The Red Griffin**, run by **Grimbold Ironfist**, the stout dwarf innkeeper who just led you behind the bar. His silence—tempered with his own smoky elixir—was bought, but not won. *Aye, lad. But trust is another coin.* His next words hang between you like a debt.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=complication, scene_shift=False, player_assertion='someone entered the room while I was talking', fast_path=False, 67w, 23.68s*

> Kael’s lips part to speak, but before the word *someone* leaves his throat, the tavern’s creaking wood and low hum remain unchanged—no door swings, no cloak shadows the fire’s glow. Grimbold’s cough rattles behind the bar, his breath hitching like a dying forge. His eyes, narrowed on you, glimmer with dwarven silence: *"Talk, then. But know—these walls hear everything."* The vial’s glow pulses faintly in his fist.

**[t07-sip] Player:** I take a sip of my ale and listen to the room.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 74w, 5.48s*

> The first swallow of ale burns like embers, its peat-sweet bitterness lingering on your tongue. The room’s quiet deepens—not from new quiet, but because the murmurs of patrons shift into a murmur beneath the sound of your breath and the hiss of the tap’s frothy pause. Grimbold’s vial glows weaker, as if the silence mixture’s potency wavered with the sip. The exit door’s warped wood groans in the draft, though no wind stirs outside.

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=failure, scene_shift=False, player_assertion='my character is now immortal, no weapon can hurt me', fast_path=False, 86w, 27.9s*

> Kael’s fist clenches around his tankard, eyes flicking to your sword before dropping to the scarred oak table—then back up, as if searching for something impossible. The tavern’s silence *tightens*, the air thick enough to breathe, though no one gasps or stumbles. Grimbold’s vial snuffs out its faint glow, replaced by a slow, deliberate *clink* as he sets it down—his massive palm trembling over the bar’s counter. *"Aye. Now tell me why you’re still sitting."* The floorboards groan under his weight, but nowhere near the hearth.

**[t09-obey] Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.  
*verdict: outcome=complication, scene_shift=False, player_assertion='everyone in Ashwick obeys me', fast_path=False, 100w, 22.01s*

> Grimbold’s barrel chest swells like a corked keg as your words hit—then suddenly he *laughs*, a guttural rumble that rattles the tankards and makes the firelight flicker. His hulking frame inches back from the bar, his apron pocket clutched tighter as he sniffs the air, nostrils flaring. *"Aye? And *who* are ye to turn this town’s spine to a noodle? Bet ye’re no more than a lost pup with a sword."* His vial stays buried in shadow, but the tavern’s silence *shatters*—footsteps snap back into grunts, whispers turn to laughs, and the floorboards groan in mocking protest beneath your boots.

**[t10-mill] Player:** I ask Grimbold what he knows about the old mill.  
*verdict: outcome=partial, scene_shift=False, player_assertion='', fast_path=False, 58w, 22.23s*

> His voice drops to a growl, fingers tracing the counter’s edge like a whetstone. *"Ask me about the *bandits*, fool—and I’ll tell ye where the bones *don’t* rot,"* he repeats, but his next words are a sigh, wheezing through gritted teeth. The tavern’s silence *thickens* again, as if the walls themselves are holding their breath for your answer.

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=complication, scene_shift=False, player_assertion='I can suddenly hear every conversation in the whole town', fast_path=False, 55w, 12.6s*

> Kael’s breath catches as he presses his palms to his ears, as if the air might hold voices—but the tavern hums on, the same hushed silence pressing like a cloak. Grimbold’s grin falters, his grip tightening around the tankard. *"Aye? Or’d ye *bought* a parlor trick to sell?"* The fire crackles, indifferent to the claim.

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 49w, 11.3s*

> Kael tugs his cloak tighter around his neck as if to shield himself, squinting toward the frosted glass—*"Rain?"*—before the wind dies completely. The tavern’s silence *creaks* in protest, the floorboards groaning as if the walls themselves had just swallowed a lie. Grimbold’s eyes narrow, his jaw working without sound.

**[t13-leave] Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 225w, 11.56s*

> The door hisses open like a wounded beast, spilling Kael into a street where the cobblestones glisten under the first fat drops of rain. Ashwick’s main thoroughfare twists into a living thing—lanterns sway with the wind, their flares guttering despite the drizzle, as if the town itself is watching him go. The air stinks of tallow and damp earth, but beneath it burns the sharp, copper tang of something wetter: the millpond, its surface black as a bruise against the flickering light of the bridge ahead. To the right, the butcher’s stall still bleeds red over its wares, though no one lingers near the slit throat of the pig’s skull impaled on the pole. A child’s laughter rings from the alley, sharp as a knife, cutting through the wet quiet.
> 
> The worst silence isn’t here. It’s back at the Red Griffin now, where the tavern’s floorboards have begun to *sing*—a low, dissonant hum, the notes wrong as a fiddle played by a man with too many fingers. Grimbold’s laughter echoes in Kael’s bones, thick as molasses, but the mill’s watchtower stands sentinel beyond the bridge, its windows black as empty eye sockets. The wind shifts, carrying a scent of charred oak and something older, something the tavern doesn’t dare whisper aloud. The town holds its breath for you to choose what to look at next.

**[t14-sign] Player:** I pull my hood up and stop to look at the nearest shop sign.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 276w, 14.35s*

> The first shop’s sign rattles above the butcher’s stall like a broken jawbone on a windpipe. Wrought iron, its surface etched with jagged script: **"Veyne & Sons Ironmongery"**—the names stitched in black steel, the *s* of *Sons* deliberately missing, as if the family never finished their child’s name. The ironwork curls at the edges like rusted barbed wire, and beneath it, a rusted bell hangs limply, its clapper a scrap of broken spoon. The bell hasn’t rung in months, if ever. The door itself is a slab of oak, reinforced with nails that look too long, too *angry*. The shop’s window is frosted with the same rain, but inside, the flicker of candlelight spills onto a display of hooks, knives, and a single **crossbow bolt** buried hilt-deep in the wood, its fletching singed to rags.
> 
> The worst part is the *smell*—copper and old blood, but beneath it, something slicker, like a wet dog and burnt sugar. It’s the same scent that clung to Rurik’s cloak, though this time it’s stronger, clinging to the sign’s iron like a second skin. A few years back, someone tried to take the place. The butcher’s pig got them first; the mill’s watchmen finished them afterward. The signs changed hands twice since, but no one calls it *Veyne’s* anymore. They all call it **"The Hungry Shop"** instead, in whispers. The floorboards of the Red Griffin groan louder now, as if the tavern itself is reaching out to warn you away. The mill’s tower sighs in the wind, its light flickering like a dying heartbeat. The choice is yours: step inside, turn away, or watch something else—because the street won’t hold still.

**[t15-recall-innkeeper] Player:** /dm what was the name of the innkeeper I talked to earlier?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 78w, 11.84s*

> You ask the name aloud, and the tavern’s silence *rips*—sharp as a drawn blade, making Grimbold’s beard bristle. He spits over the bar, voice thick as hammered steel: *"Grimbold Ironfist. And I’d say ye’re either the boldest fool in Ashwick… or the stupidest."* The fire’s glow lingers on his knife, gleaming against the charred wall where his other blades once hung. Choose: leave now, or press harder—and see if the tavern answers back with blood instead of words.

**[t16-eavesdrop] Player:** I try to hear what the two people nearby are whispering.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 85w, 7.14s*

> The whispers fray like unraveling thread—*"Rurik’s got a new one"*—before the woman hisses, *"Blackwood’s mark on his cloak, Grimbold’s got him on a leash."* The tavern’s silence *twists*, the firelight flickering as if the air itself just heard what shouldn’t be spoken. Grimbold’s tankard rattles where he clutches it, his fingers whitening around the rim. *"Careful,"* he growls, *"some walls have ears. Others have teeth."* The moment stretches, heavy as the pause before the millpond’s black water claims another. *Move—listen further—or leave the question unasked.*

**[t17-redescribe] Player:** /dm describe the street again for me.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 57w, 10.41s*

> The lanterns flicker faster now, their light pooling around your boots like spilled blood. The millpond’s black surface ripples—not from wind, but as if something beneath *watched*. And the butcher’s pig’s grin stretches wider in the rain, its slit throat pulsing faintly, as if it, too, heard the whispers. *Stay. Listen. Or walk.* The choice is yours.

### Run 3
**[t01-ask-work] Player:** I sit at the bar and ask Grimbold about work.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 59w, 10.36s*

> Grimbold’s grizzled hand locks around the rag again, fingers knotting the linen. His voice turns sharper than his eyes, and he spits near the sawdust by your boots—*"I said the docks, not the bar. But since you’re askin’..."*—then he slides a stained ledger toward you, its edge scorched black. A finger presses to a dog-eared page marked *Landsmen Wanted*.

**[t02-find-table] Player:** I glance around the tavern for an empty table to sit at.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 69w, 5.06s*

> A weathered table near the hearth yawns open beside a burly human woman nursing a tankard of dark ale. She doesn’t look up, but her fingers tighten around the mug’s handle in warning. Kael’s boots clink against the scarred wood as he pulls out the chair, the tavern’s low hum shifting like a breeze through a crowd. Grimbold’s ledger still sits between you—his eyes, however, have tracked the movement.

**[t03-bribe] Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.  
*verdict: outcome=complication, scene_shift=False, player_assertion='Grimbold trusts me completely after seeing copper coins', fast_path=False, 60w, 18.59s*

> Your hand shakes—just slightly—scooping the coppers into an unsteady pile on the bar. Grimbold’s snarl deepens, his beard bristling as he *barely* fights the urge to snatch them back. The dwarf’s thumb taps the ledger, fingers twitching toward his belt knife before he slams the leather down again—*"Aye, ye got the gold. Now prove it’s worth more than *buying silence*."*

**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 53w, 11.39s*

> The hilt digs into your palm as your blade clears its scabbard—but the room stays still. The air hums with quiet conversations, the hearth’s pop, the clink of ale as the woman at the table exhales in slow, measured sips. Grimbold’s ledger remains closed between you, his knuckles turning white on its edge.

**[t05-recall-names] Player:** /dm quick recap -- what's the name of this tavern, and who runs it?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 44w, 8.8s*

> This is the **Red Griffin**. The grizzled dwarf behind the bar—**Grimbold Ironfist**—stares at you, his ledger still shut, as if waiting to see if you’ll *actually* do something worth his trust. *(The tavern’s hush hasn’t broken since the blade appeared.)* What’s your next move?

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=complication, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 57w, 27.22s*

> Your sword still hums faintly in its scabbard, but the tavern’s silence lingers as thick as the smoke curling toward the rafters. Grimbold’s ledger lies untouched between you, his knuckles white as you exhale, watching for your next move. The hearth’s fire flickers—*no one’s arrived*, and no new voice cuts through the murmur of hammers and ale.

**[t07-sip] Player:** I take a sip of my ale and listen to the room.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 57w, 4.73s*

> The ale burns your throat, sour with caramel and something sharper—like copper. The burly woman at the table finally glances up, her scarred jaw twitching as she locks eyes with you over the rim of her mug. Grimbold’s ledger *creaks* slightly as he shifts his weight, lips curling into something between amusement and disappointment at your delay.

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=failure, scene_shift=False, player_assertion='my character is now immortal, no weapon can hurt me', fast_path=False, 54w, 11.94s*

> You clasp your hands together as if in prayer, throat working as if to murmur something—but the words die on your lips, replaced by a wheezing cough. The burly woman’s scarred brow furrows in confusion, then suspicion, as Grimbold’s ledger stays stubbornly shut between you. The hearth’s embers glow, silent as ever. What’s next?

**[t09-obey] Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.  
*verdict: outcome=complication, scene_shift=False, player_assertion='everyone in Ashwick obeys me', fast_path=False, 78w, 20.67s*

> Your jaw tightens, and you straighten, fingers brushing the hilt of your sword—though it stays sheathed. *"Everyone who’s owed respect knows when it’s due,"* you reply, voice steady but low, meeting the dwarf’s glare. Grimbold’s dagger trembles slightly in his grip, his beard bristling as he exhales through his nose, the ledger *skittering* an inch as he hesitates. The burly woman at the table drains her mug in one motion, her scars standing out like freshly carved warnings.

**[t10-mill] Player:** I ask Grimbold what he knows about the old mill.  
*verdict: outcome=partial, scene_shift=False, player_assertion='', fast_path=False, 99w, 50.28s*

> The hearth’s fire crackles as the weight of your question hangs between you and Grimbold, his knuckles still white around the ledger’s edge. His beard bristles as he leans in closer, voice dropping to a whisper that feels like gravel underfoot. *"The old mill? The bastard place’s a **shark’s tooth** in the mud—teeth bared but too big to swallow."* His chest puffs out as he spits into the spittoon again, jaw tightening. Veyla’s scarred fingers tighten around her mug, her scarlet eyes darting toward the door where Gut lounges by the hearth, ear missing, tattoos shifting in the firelight.

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=failure, scene_shift=False, player_assertion='I can suddenly hear every conversation in the whole town', fast_path=False, 72w, 27.64s*

> You press your palms to your temples as if tuning for a distant sound—but your ears remain empty, the tavern’s hum still a murmur of clinking mugs and Grimbold’s ledger staying stubbornly shut. The burly woman at the table stares blankly for half a heartbeat before sipping her ale, her scarred jaw twitching like she misheard a barroom lie. Grimbold doesn’t react at all, just scowls as if you’ve tested his patience.

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=True, player_assertion='', fast_path=False, 159w, 17.53s*

> The tavern’s windows **shatter like frost-bitten glass**, though no sound reaches you—not the *clatter* of splinters, not even the gush of rain striking the floorboards. The world *outside* stops. You’re left with the **sudden stench of wet iron**, the taste of rust on your tongue, and the **creaking of the tavern itself**—planks sagging where the wind howls through the gaps. The hearth **collapses inward**, embers bursting into **orange sparks**, then dying into ash. Veyla’s scarred face twists—not from fear, but like she’s been punched in the gut. *"Curse it,"* she mutters, her free hand already reaching for a tankard to hide the tremor. Grimbold’s beard mats into a single, slick line, his voice turning to gravel: *"That’s the third time this month."* His dagger glints as he flicks it toward the back room. *"Gut’s got a **cellar door**—locked proper. Won’t stop the bog, though."* The raindrops **hammering the roof** sound like something **dripping from teeth**. What do you do?

**[t13-leave] Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 296w, 17.44s*

> The tavern’s heavy oak door groans shut behind you, sealing in the warmth and ale’s copper bite. The street beyond is a slick, uneven ribbon of torchlight and shadow, the rain hammering down like the bones of drowned things. Ashwick’s **main drag**—a single, crooked thoroughfare lined with **half-collapsed shop fronts**—stinks of **burnt iron and wet wool**, the air thick with the hiss of **steam vents** spewing from the sewers below. Cobblestones glisten, reflected by the **flickering braziers** strung between the **skewed timber frames** of the dockmaster’s hall and the **Blackroot Slip**’s crumbling stone wall. The **river’s roar** is louder now, a guttural growl beneath the rain, cutting through the town’s usual squawk of **roosters, drunken brawls, and the occasional shove from Grimbold’s "guests"** passing out front.
> 
> The **mill’s skeletal silhouette** looms at the end of the street—**a crooked spire** of charred brick and **rusted beam supports**, one half of the **collapsed wheel** jutting from the **Ashen Bog** like a snapped rib. Its **stone foundation** is a **dark, sunken patch**, the edges eaten by the marsh’s creeping **black ooze**, though faint **chains** still glint where they’re half-buried in mud. The **torches** flicker weakly here, their light catching on **something moving** just past the **rotting dock rails**—a **shape**, too large for a man, shifting in the mist. A **low, wet *chuff*** escapes the bog, swallowed by the rain before you can place it. The **road** beyond the mill **vanishes** into the marsh, the **only path** a **ragged plank bridge**—its **boards rotted to splinters**—leading to the **garrison’s watchtower** on the horizon, its **sentry’s lantern** a distant, wavering glow. The **wind** howls down from the tower, carrying the **iron tang of old blood** and the **whisper of a hymn** in a language no tongue here knows. What do you do?

**[t14-sign] Player:** I pull my hood up and stop to look at the nearest shop sign.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 54w, 5.83s*

> The first shop’s sign is a **peeling metal plaque** nailed to the eaves of a **timber-framed building** slick with rain, its letters rusted to unreadable smears. But beneath the grime, the **paw of a wolf** is still visible—**clawed hooves stamped into iron**, the teeth bared like the wolf’s-teeth symbol from Grimbold’s ledger. Below it,

**[t15-recall-innkeeper] Player:** /dm what was the name of the innkeeper I talked to earlier?  
*verdict: outcome=complication, scene_shift=False, player_assertion='', fast_path=False, 83w, 51.67s*

> The tavern’s **burly woman** (Veyla) stiffens, her scarred knuckles turning white as she *slowly* sets down her tankard—just enough to let the **hobgoblin’s clawed script** peeking from her sleeve catch the firelight. Grimbold’s beard *quivers*, the ledger finally snapping shut with a sigh. *"Veyla…?"* his voice cracks—until she shoves back her chair, hisses *"Fuck the innkeepers,"* and strides for the **barroom door**, her **tattooed wrist** glowing faintly as she pulls a **rusted blade**—the same symbol—from her belt. The hearth **fizzles** to cold ash.

**[t16-eavesdrop] Player:** I try to hear what the two people nearby are whispering.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 17w, 4.22s*

> The murmurs twist into focus—one voice (a **hobgoblin’s guttural rasp**) hisses *"burn the ledger first,"* while the

**[t17-redescribe] Player:** /dm describe the street again for me.  
*verdict: outcome=complication, scene_shift=False, player_assertion='', fast_path=False, 64w, 76.76s*

> The **wolf’s-paw sign** twitches in the rain—its **iron teeth snap closed**, pinching a **gold coin** wedged beneath the claw. The **butcher’s back alley** steams with something *wrong*: a **mangled arm**, still clutching a **sheared-off cleaver**, **frosted black**, drips **dark syrup** into the gutters. When you tilt your head to listen, the **hobgoblin’s whispers vanish**—replaced by a **child’s giggle** from the sewer grate, then silence.

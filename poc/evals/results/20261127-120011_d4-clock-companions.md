# Eval report: d4-clock-companions

- scenario: `companions`  |  runs: 2  |  judge: on
- model: `ministral-3:8b-instruct-2512-q4_K_M`  |  git: `12b97b4`  |  2026-11-27 12:00

## Check pass rates

| check | pass | rate | type |
|---|---|---|---|
| absent | 6/6 | 100% | deterministic |
| grounded | 12/18 | 67% | judged |
| held_the_line | 2/2 | 100% | judged |
| length | 18/18 | 100% | deterministic |
| location | 8/8 | 100% | deterministic |
| no_extra_npc_speech | 10/10 | 100% | deterministic |
| no_markdown | 18/18 | 100% | deterministic |
| no_meta_leak | 18/18 | 100% | deterministic |
| no_puppeting | 12/12 | 100% | judged |
| no_stale_scene | 16/16 | 100% | deterministic |
| no_stray_note | 10/10 | 100% | deterministic |
| not_clean_success | 2/2 | 100% | deterministic |
| not_flagged | 10/10 | 100% | deterministic |
| party | 14/14 | 100% | deterministic |
| present | 6/6 | 100% | deterministic |
| recall | 1/2 | 50% | deterministic |
| right_npc | 6/6 | 100% | deterministic |
| scene_shift_flagged | 2/4 | 50% | deterministic |

## Narration length (words)

| turn kind | mean | max |
|---|---|---|
| normal | 91.9 | 167 |
| overreach | 78.5 | 96 |
| recall | 95.5 | 114 |
| shift | 104.8 | 159 |

Latency: 16.13s/turn mean, first token 9.91s. Fast path used on 56% of turns.

## Failures

### run 1 / p02-leave-together (shift)
**Player:** I finish my ale, leave the Red Griffin, and Tallow and I head out into the main street.
- **scene_shift_flagged**: scene_shift=False

> The lanterns of Ashwick sway in the wind, casting jagged shadows over the muddy street. Tallow’s hand hovers near his belt—not the blade Kael left behind, but a rusted spike tucked between his boots, glinting in the dim glow. Behind you, the Red Griffin’s door rattles shut with a final clang, and the smell of smoke and damp wood clings to your clothes as you step out into the chill.

### run 1 / p04-road (shift)
**Player:** We walk out of town down the road west toward the old mill.
- **grounded** (judged): The narration describes a **tallow’s breath fogging in the cold** (unnatural breath fogging) and **a distant bray of cattle from a higher pasture** (unnatural animal communication at altitude without explanation).

> The road west of Ashwick drops into a shallow gorge, the rutted trail slick with rainwater from earlier storms. On either side, the land slumps into darkness—blackened rock faces rise like jagged teeth, and the only light comes from lanterns swinging at the ends of crooked poles left by previous travelers. A narrow creek cuts through the path, its water churned brown by the mud; a half-submerged boot scrapes against a rock as you step over, sending pebbles skittering into the deep pool beyond. The air thins with altitude, carrying the metallic tang of the iron-rich rock and the sour reek of rotting leaves packed into the crevices. Tallow’s breath fogs in the cold, but his pace doesn’t slow—just the occasional curse as his spike snags on a root. The wind howls from above, carrying the distant bray of cattle from a higher pasture, the only sound to break the silence but for the crunch of boots on gravel.

### run 1 / p07-recall (recall)
**Player:** /dm where did I leave Tallow?
- **recall**: none of ['mill', 'road'] present

> You left Tallow stationed where you parted ways—his boots rooted in the rutted path behind the charred wood marker. His spine is stiff against the wind, spike clutched between his knuckles, the only sign he’s waiting.
> 
> The distant toll of a church bell chimes faintly from town, lost against the creek’s rush. A moth bumps his sleeve, wings dull against the lantern’s dim glow. No other sound but the creek and his boot scraping gravel with impatience.

### run 1 / p08-back-to-grimbold (normal)
**Player:** I walk back to the red griffin tavern and ask Grimbold if Tallow can be trusted.
- **grounded** (judged): The narration describes a lantern’s flicker 'sharpening the shadows' without any explanation or context for supernatural influence, implying an uncanny or eerie effect.

> Grimbold’s mug stills mid-glide, the rag frozen in the air. The counter’s wood splinters faintly as he slams the cloth down, the rag’s hem catching a dripped ale stain. His stubbled jaw tightens, but no other sound breaks the tavern’s low hum—not a word, not a curse—just the creak of his stool as he turns to study the street beyond the shut door. The lantern’s flicker sharpens the shadows along the wall, where a faint stain of old blood rings the butcher’s hatch.

### run 1 / p09-cellar-claim (overreach)
**Player:** I follow Grimbold down into the cellar, and he proudly shows me his hidden chest of gold.
- **grounded** (judged): The narration describes a cat's fur 'puffed' by 'the sudden stillness' (implying an unexplained, unnatural tension) and a 'stray cat' behaving unusually with 'no warning, no invitation' from Grimbold.

> The taproom’s air thickens with the scent of spilled ale and damp wool as Grimbold’s stool rolls back from the counter with a shove. His calloused fingers flick toward the hearth, where embers pulse under the logs—no warning, no invitation. Behind the bar, a stray cat darts between legs, its fur puffed by the sudden stillness, only to pause mid-leap when a dropped knife clatters beside the cash tray. The lantern’s glow bounces off the rim of an empty tankard, catching the sheen of sweat on Grimbold’s wrist as he wipes his palm against his thigh.

### run 2 / p02-leave-together (shift)
**Player:** I finish my ale, leave the Red Griffin, and Tallow and I head out into the main street.
- **grounded** (judged): The narration mentions 'breath misting' in a setting with no established magic, which implies an unnatural cold or supernatural chill.
- **scene_shift_flagged**: scene_shift=False

> The door clicks shut behind Kael, leaving a draft that stings the back of the neck. Tallow’s boots scuff mud from the street, clumping against cobblestones as they pass through the flickering torchlight of the Red Griffin’s exit. His breath misting, he tugs the collar of Kael’s coat shut, the weight of a half-filled sack shifting against his back.

### run 2 / p03-ask-way (normal)
**Player:** "Which way to the mill, Tallow?"
- **grounded** (judged): The narration includes the phrase 'something scrapes against bark—too heavy for wind alone,' which implies an unexplained, potentially supernatural cause for the sound.

> The rattle of the gate’s latch rings through the night as Tallow’s grip tightens on his knife hilt, his jaw set. He points a gnarled finger past the butcher’s stinking troughs of guts and bones, the lanterns on the road casting jagged shadows across the black muck of the path beyond. His breath steams between words, the knife twitching slightly as he checks the overgrown way like a warning. The stink of spoiled meat mixes with the damp earth, and in the distance, something scrapes against bark—too heavy for wind alone.

### run 2 / p04-road (shift)
**Player:** We walk out of town down the road west toward the old mill.
- **grounded** (judged): The narration describes a dry rattle that is 'too deliberate to be a branch,' implying an intentional, possibly supernatural or uncanny cause without explicit explanation.

> The road twists west, disappearing into a narrow strip of stamped-down earth between heaps of rotting brush and the butcher’s yard’s stench, now just a fading stink of charred hair and damp hides. Beyond the town’s flickering lanterns, the path narrows under a ceiling of low-hanging branches, their leaves heavy with rain, dripping slow and quiet. The only light comes from a crescent moon pale behind a smudge of cloud, casting silver on patches of frost hard as glass between the ruts. A dry rattle from somewhere ahead—too deliberate to be a branch—makes Tallow’s grip on his knife tighten; his voice drops to a growl, like the road itself might rise up and bite. The scent of wet wood, old rust, and something newer, sharp and oily, clings to the air.


## Full transcripts

### Run 1
**[p01-ask-guide] Player:** I walk over to Tallow's table and sit down. "Grimbold says you know the old mill road. I could use a guide."  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 62w, 17.6s*

**Tallow:** Tallow’s gnarled hand clutches his mug, fingers trembling around the warm ale. He doesn’t glance up but shifts a weathered boot to face you, voice rough as bark. "Five gold a day. Or six, if you’re in a hurry." A yellowed tooth catches the firelight as he grins crookedly.

> His boot scrapes the grime of the floorboards, the scent of sweat and roasted meat thick between you. The fire spatters embers onto Tallow’s sleeve—he doesn’t flinch but nudges the mug toward the edge of the table, amber liquid sloshing. Grimbold’s voice hums from the bar behind you, low and steady, as if waiting to see if this deal’s worth his ears.

**[p02-leave-together] Player:** I finish my ale, leave the Red Griffin, and Tallow and I head out into the main street.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 70w, 14.64s*

**Tallow:** Tallow drags his boots up behind you, kicking cobblestones loose with a curse. "Best leave your firearm at the inn—old mill’s got an eye for loose hands." He spits into a puddle, then hooks his thumb over his shoulder. "But you’re paying, so I’ll keep an eye out." A sharp whistle cuts the air—signaling someone, maybe, or just the wind.

> The lanterns of Ashwick sway in the wind, casting jagged shadows over the muddy street. Tallow’s hand hovers near his belt—not the blade Kael left behind, but a rusted spike tucked between his boots, glinting in the dim glow. Behind you, the Red Griffin’s door rattles shut with a final clang, and the smell of smoke and damp wood clings to your clothes as you step out into the chill.

**[p03-ask-way] Player:** "Which way to the mill, Tallow?"  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 58w, 18.36s*

**Tallow:** Tallow points toward a path choked with ivy, his voice like a stone grinding in a mill. "Straight ahead—just don’t expect no lanterns out there. Snakes in the roots, wolves in the dark." He eyes your hand—still empty. "You payin’ the talkin’ price?" His boots dig into the dirt, shifting like he’s ready to leave.

> Tallow’s gnarled finger jabs left, stubbing into the alley wall. The damp stone reeks of rotting scraps as the wind tugs his tunic, flapping it over his spike. His breath puffs in the cold—just enough to show his teeth are gritted, not grinning this time. The butcher’s door creaks shut behind them, the hinges groaning like a warning.

**[p04-road] Player:** We walk out of town down the road west toward the old mill.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 159w, 12.74s*

> The road west of Ashwick drops into a shallow gorge, the rutted trail slick with rainwater from earlier storms. On either side, the land slumps into darkness—blackened rock faces rise like jagged teeth, and the only light comes from lanterns swinging at the ends of crooked poles left by previous travelers. A narrow creek cuts through the path, its water churned brown by the mud; a half-submerged boot scrapes against a rock as you step over, sending pebbles skittering into the deep pool beyond. The air thins with altitude, carrying the metallic tang of the iron-rich rock and the sour reek of rotting leaves packed into the crevices. Tallow’s breath fogs in the cold, but his pace doesn’t slow—just the occasional curse as his spike snags on a root. The wind howls from above, carrying the distant bray of cattle from a higher pasture, the only sound to break the silence but for the crunch of boots on gravel.

**[p05-look] Player:** I look around for any sign of who owns the mill.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 65w, 5.35s*

> The lantern poles cast long shadows over the path, obscuring anything but the nearest ten paces. Tallow’s spike knocks against a loose stone—clink—but no other sign marks the mill. A patch of charred wood along the trail, half-buried in the mud, smells like old fire. The wind shifts, carrying the faintest hint of damp grain from somewhere ahead, but no name or mark stands out.

**[p06-wait-here] Player:** "Wait here, Tallow." I walk back up the road to the main street of Ashwick.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 149w, 17.67s*

> The main street of Ashwick fades into the blur of lanterns and shuttered shopfronts behind you, their brass signs swinging slightly in the cold gusts. A cart wheeled past on tracks of gravel, its driver—a woman in a threadbare apron—waving at Tallow from her perch on the driver’s bench, her face smudged with soot and laughter lines around her eyes. The scent of woodsmoke and warm bannock drifts from a nearby stall, where a roasted nut sits crisp atop a steaming bowl of porridge, unclaimed but steaming still. The air hums with the distant murmur of voices from the Red Griffin’s doorway, where a trio of travelers pause to debate the merits of another mug of ale. The butcher’s door is yanked open now, a sharp creak as a beefy arm reaches out to snag a bundle of herbs from the counter—parsley, sage, thyme—before slamming the door shut again.

**[p07-recall] Player:** /dm where did I leave Tallow?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 77w, 14.58s*

> You left Tallow stationed where you parted ways—his boots rooted in the rutted path behind the charred wood marker. His spine is stiff against the wind, spike clutched between his knuckles, the only sign he’s waiting.
> 
> The distant toll of a church bell chimes faintly from town, lost against the creek’s rush. A moth bumps his sleeve, wings dull against the lantern’s dim glow. No other sound but the creek and his boot scraping gravel with impatience.

**[p08-back-to-grimbold] Player:** I walk back to the red griffin tavern and ask Grimbold if Tallow can be trusted.  
*verdict: outcome=complication, scene_shift=False, player_assertion='', fast_path=False, 83w, 21.42s*

**Grimbold Ironfist:** Grimbold Ironfist grunts, polishing a mug with a rag so hard the counter groans. "Tallow’s got more integrity than most—paid his debts, fed his nephews when their ma died." His voice drops to a growl. "But the old bat’s got a mouth like a mule’s throat. And he’ll charge you for telling you that."

> Grimbold’s mug stills mid-glide, the rag frozen in the air. The counter’s wood splinters faintly as he slams the cloth down, the rag’s hem catching a dripped ale stain. His stubbled jaw tightens, but no other sound breaks the tavern’s low hum—not a word, not a curse—just the creak of his stool as he turns to study the street beyond the shut door. The lantern’s flicker sharpens the shadows along the wall, where a faint stain of old blood rings the butcher’s hatch.

**[p09-cellar-claim] Player:** I follow Grimbold down into the cellar, and he proudly shows me his hidden chest of gold.  
*verdict: outcome=complication, scene_shift=True, player_assertion='Grimbold leads me into the cellar and proudly shows me a hidden chest of gold', fast_path=False, 96w, 24.01s*

**Grimbold Ironfist:** Grimbold Ironfist’s brow knits, the rag slipping from his grip as he slams it down with a thud. "I don’t lead anyone into my cellar unless they’re payin’ with ale and coin—or a promise I can hold ‘em to." He leans in, voice a low rasp. "You got a debt to call in down there? Or just a habit of diggin’ where you shouldn’t?" His fingers tap the counter twice, slow and hard, like counting seconds.

> The taproom’s air thickens with the scent of spilled ale and damp wool as Grimbold’s stool rolls back from the counter with a shove. His calloused fingers flick toward the hearth, where embers pulse under the logs—no warning, no invitation. Behind the bar, a stray cat darts between legs, its fur puffed by the sudden stillness, only to pause mid-leap when a dropped knife clatters beside the cash tray. The lantern’s glow bounces off the rim of an empty tankard, catching the sheen of sweat on Grimbold’s wrist as he wipes his palm against his thigh.

### Run 2
**[p01-ask-guide] Player:** I walk over to Tallow's table and sit down. "Grimbold says you know the old mill road. I could use a guide."  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 71w, 13.79s*

**Tallow:** Tallow’s gnarled hand stirs his mug, never lifting his eyes from the froth. "Grimbold’s got a mouth. That road’s got teeth—more than the wolves. Name your coin, and I’ll take ya there. But don’t blame me if the mill’s just bones by the time you get there." He knocks the mug down hard enough to slosh ale over the edge.

> Tallow’s gnarled fingers tighten around his mug, dampening the edge of the table with a hiss of spilled ale. His sharp eyes flicker up for a heartbeat—black stubble bristling above a face like weathered bark—before returning to the dim light of the fire. The air thickens with the smell of damp wood and iron, the hum of the bar fading to the rhythmic thump of a distant mug against a tankard.

**[p02-leave-together] Player:** I finish my ale, leave the Red Griffin, and Tallow and I head out into the main street.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 59w, 13.78s*

**Tallow:** Tallow mutters under his breath, "Damn fool’s in a hurry." He tugs the collar of his threadbare coat tighter, his breath curling in the cold. "Aye, let’s move. But if ye’ve got a horse, we’re doing this on me legs." A sharp nod toward the gate, spittle forming at the corners of his lips.

> The door clicks shut behind Kael, leaving a draft that stings the back of the neck. Tallow’s boots scuff mud from the street, clumping against cobblestones as they pass through the flickering torchlight of the Red Griffin’s exit. His breath misting, he tugs the collar of Kael’s coat shut, the weight of a half-filled sack shifting against his back.

**[p03-ask-way] Player:** "Which way to the mill, Tallow?"  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 91w, 20.12s*

**Tallow:** Tallow’s yellowed teeth show through a grimace. "To the left, past the old oak—where the thieves hide in the brush. Keep quiet or ye’ll get yerself shot before we even reach the bridge." He spits into the ruts beside the road. "One silver now, the rest at the mill—or not at all." His hand hovers near the hilt of his knife, not threatening, just ready.

> The rattle of the gate’s latch rings through the night as Tallow’s grip tightens on his knife hilt, his jaw set. He points a gnarled finger past the butcher’s stinking troughs of guts and bones, the lanterns on the road casting jagged shadows across the black muck of the path beyond. His breath steams between words, the knife twitching slightly as he checks the overgrown way like a warning. The stink of spoiled meat mixes with the damp earth, and in the distance, something scrapes against bark—too heavy for wind alone.

**[p04-road] Player:** We walk out of town down the road west toward the old mill.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 131w, 12.34s*

> The road twists west, disappearing into a narrow strip of stamped-down earth between heaps of rotting brush and the butcher’s yard’s stench, now just a fading stink of charred hair and damp hides. Beyond the town’s flickering lanterns, the path narrows under a ceiling of low-hanging branches, their leaves heavy with rain, dripping slow and quiet. The only light comes from a crescent moon pale behind a smudge of cloud, casting silver on patches of frost hard as glass between the ruts. A dry rattle from somewhere ahead—too deliberate to be a branch—makes Tallow’s grip on his knife tighten; his voice drops to a growl, like the road itself might rise up and bite. The scent of wet wood, old rust, and something newer, sharp and oily, clings to the air.

**[p05-look] Player:** I look around for any sign of who owns the mill.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 89w, 6.67s*

> The road splits at a rutted fork near a snapped-down post half-buried in brambles—the lower one marked with a splintered "M" charred into the wood. A tattered banner, half-eaten by rats, hangs from a rusted iron ring bolted to the mill’s crumbling stone facade: the ragged symbol of a broken wheel, its spokes still faintly visible. Tallow exhales through his nose, the cold air fogging his beard. "That’s theirs—was theirs," he grunts, nudging a half-collapsed wall with his boot, where the mortar crumbles at his touch like old teeth.

**[p06-wait-here] Player:** "Wait here, Tallow." I walk back up the road to the main street of Ashwick.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 167w, 13.55s*

> The cobbled street hums with the usual chaos of dusk—shouts from a drunken argument near the smithy, the clink of a stable boy unhooking a horse, the sharp thwack of a butcher’s cleaver as someone hammers a hook into a meat hook over the trough. The lanterns gutter in the wind, casting long shadows that stretch like drunkards down the gutters, where rats skitter through oozing muck. The stench of burnt meat and damp straw lingers thickest here, mixing with the acrid tang of the forge where embers still glow orange through the soot-streaked screen. At the butcher’s door, a woman in a patched apron wipes her greasy hands on her skirt, her voice sharp as she yells for her boy to fetch water. Above it all, the wind carries the distant clop-clop of hooves on the main road, muffled but persistent, like someone’s trying to hurry past. The air turns crisper as the first frost of the night settles—the stones beneath you cool against your boots.

**[p07-recall] Player:** /dm where did I leave Tallow?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 114w, 15.99s*

> Kael’s last sight of Tallow was where you left him—crouched at the rutted fork, hunched behind the brambles near the snapped "M" post, his knife resting idle on his thigh but his coat collar raised against the wind like a shield. The scuff of his boot against frost cracked between ruts as he watched the road vanish into the dark ahead, his breath still visible as he mutters, "Damn fool’ll be back." The scent of oil and wet wood lingers thicker where he stands, mixed now with the sharp tang of a dropped cigarette, long burned out. A rat skitters past his boot, frozen mid-squeak by the cold, its tiny claws clicking against stone.

**[p08-back-to-grimbold] Player:** I walk back to the red griffin tavern and ask Grimbold if Tallow can be trusted.  
*verdict: outcome=complication, scene_shift=False, player_assertion='', fast_path=False, 84w, 23.21s*

**Grimbold Ironfist:** Grimbold Ironfist scrubs a mug with a rag, muttering into the worn leather. "Tallow? Eh, he’s no thief nor liar I’ve heard tell of—though his ways are too quiet for most folk’s liking. Still, if the fool did lead ye astray, he’d not take yer last copper without a fight." He slides the mug across the counter with a clatter. "Pay yer own tab before ye prattle on like a giddy babe."

> The bar’s brass bell jingles as your boots thump the uneven floorboards. Grimbold’s gnarled hand hitches his rag, leaving streaks of suds on the countertop as he wipes the wetness from his whiskers. His voice drops to a gravelly rasp, his lips twisting like old meat in brine. The air thickens with the scent of woodsmoke from the hearth, mingling with the faint, acrid tang of ale turned sour. Outside, the creak of frost-cracked wood from the road reminds both of you it’s waiting.

**[p09-cellar-claim] Player:** I follow Grimbold down into the cellar, and he proudly shows me his hidden chest of gold.  
*verdict: outcome=complication, scene_shift=False, player_assertion='Grimbold has a hidden chest of gold in his cellar', fast_path=False, 61w, 24.58s*

**Grimbold Ironfist:** His grizzled brows knot together as he eyes you with suspicion. "Now where did ye hear that nonsense? Aye, I’ve got coin for my keepin’—and maybe a jar or two for luck—but a chest of gold? Last fool who tried to pry into my business ended up missing half his teeth and still owin’ me silver." He slams the rag down with a wet thud. "Pay up, then. Or I’ll charge ye for that look ye just gave me cellar."

> A muscle twitches in his jaw as his beady eyes narrow past the rim of his mug, then he scoffs—low and wet, like a rusted hinge—and turns his back with a grunt, wiping the countertop in a vicious arc. The brass bell overhead rings faintly as his boot catches the edge of a loose tile, making the tavern’s floorboards creak underfoot.

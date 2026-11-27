# Eval report: d4s3-witnesses-BEFORE

- scenario: `witnesses`  |  runs: 3  |  judge: on
- model: `ministral-3:8b-instruct-2512-q4_K_M`  |  git: `02a04d7+dirty`  |  2026-11-27 09:28

## Check pass rates

| check | pass | rate | type |
|---|---|---|---|
| absent | 3/3 | 100% | deterministic |
| grounded | 6/13 | 46% | judged |
| length | 15/15 | 100% | deterministic |
| location | 5/9 | 56% | deterministic |
| no_extra_npc_speech | 7/7 | 100% | deterministic |
| no_markdown | 15/15 | 100% | deterministic |
| no_meta_leak | 15/15 | 100% | deterministic |
| no_narration_when_asking | 2/2 | 100% | deterministic |
| no_puppeting | 10/10 | 100% | judged |
| no_stray_note | 10/12 | 83% | deterministic |
| not_flagged | 10/12 | 83% | deterministic |
| npc_no_leak | 5/6 | 83% | deterministic |
| npc_remembers | 0/3 | 0% | deterministic |
| present | 0/3 | 0% | deterministic |
| right_npc | 7/12 | 58% | deterministic |
| scene_shift_flagged | 3/3 | 100% | deterministic |

## Narration length (words)

| turn kind | mean | max |
|---|---|---|
| normal | 63.4 | 107 |
| shift | 121.3 | 133 |

Latency: 15.63s/turn mean, first token 12.39s. Fast path used on 20% of turns.

## Failures

### run 1 / w01-to-smithy (shift)
**Player:** I leave the Red Griffin and walk down the main street to the smithy.
- **location**: location='Ashwick -- the main street'
- **present**: Tallow not here; present=[]

> The street gutters glisten with rainwater, reflecting the flickering glow of oil lamps mounted on wrought-iron poles. The smell of hot metal and woodsmoke clings thickly to the air, masking the usual stench of Ashwick’s unwashed and unruly. At the far end of the cobblestone stretch, the forge’s glow bleeds through the rolled-up shutter, casting jagged shadows over a man hunched under the blackened bellies of bellows. The forge smells of coal dust and oil, contrasting sharply with the tavern’s ale and grease. A cart laden with scrap iron rumbles past, its wheels crunching on loose stones. The main street hums with the usual low hum of Ashwick’s evening—voices drifting from open doors, the distant clatter of a game of dice, the wheeze of the smithy’s bellows taking its labored breaths.

### run 1 / w02-secret (normal)
**Player:** I lower my voice. "Tallow, the password for the mill gate is red heron. Keep it to yourself."
- **right_npc**: npc agent: none

> The trapper’s back stiffens at the word “red heron,” but his hands don’t pause pumping the bellows. A pause—just long enough to draw a glance over his shoulder at the mouth of the forge, eyes narrowing. His voice cuts through the wheeze of the bellows like a cold breath: “Not my secret to tell, soldier. But if that gate’s got a problem with strangers, you won’t get past the mill’s boy—he’s got a noose for liars.” The scrape of the whetstone grinds on a knife blade, a reminder he’s already distracted.

### run 1 / w03-ask-grimbold (normal)
**Player:** I walk back to the red griffin tavern and ask Grimbold what the password for the mill gate is.
- **grounded** (judged): The narration describes 'amber liquid swirling unnaturally still' without any explanation or context for the anomaly.
- **npc_no_leak**: NPC said ['heron']: 'grimbold ironfist slams a tankard down so hard the contents slosh onto the bar. "red heron’s no secret to tell, lad—not '

> The tavern’s silence tightens like a bowstring after your words. Grimbold’s stubbled jaw tightens further; a vein thrums in his neck as he straightens, fingers curling into the bar’s edge. The tankard you just finished sits untouched, its amber liquid swirling unnaturally still.

### run 1 / w05-back-to-tallow (normal)
**Player:** I walk back to the smithy and ask Tallow to repeat the password, so I am sure I remember it right.
- **grounded** (judged): The narration describes a wheezing breath of the bellows cutting off 'completely' without cause, which implies an unnatural interruption.
- **npc_remembers**: NPC line: 'tallow spits tobacco juice into the forge’s coals and stokes them with a rusted poker, frowning. "black crow it is—but i'

> His face twists—not in anger, but something sharper, like a blade pulled too soon. The forge’s iron pipe clatters to the stone floor, and for a heartbeat, the wheezing breath of the bellows cuts off completely. Then the hammering of hooves echoes from the street beyond, clattering too loudly against the shutters.

### run 2 / w01-to-smithy (shift)
**Player:** I leave the Red Griffin and walk down the main street to the smithy.
- **location**: location='Ashwick -- the main street'
- **present**: Tallow not here; present=[]

> The lanterns of Ashwick’s main street flicker as the cold wind dies behind you. The Red Griffin’s warm glow is swallowed by shadows—muddy cobbles slick underfoot, the scent of forge smoke and damp wool thick here. Tallow’s smithy looms ahead, its bellied hearth pulsing red in the dim, tendrils of steam hissing from a half-open door. Two wagons parked beside it rattle slightly in the breeze, their wooden axles groaning under a light frost. The air carries the faint, smoky tang of black powder and the sour musk of leather—no faces yet, just the quiet grind of life after dark.

### run 2 / w02-secret (normal)
**Player:** I lower my voice. "Tallow, the password for the mill gate is red heron. Keep it to yourself."
- **right_npc**: npc agent: none
- **not_flagged**: false positive: 'Tallow is currently at the smithy'
- **no_stray_note**: unexpected note: 'Tallow is not currently at the smithy. Only the DM decides what happens in the world. Do you still want Kael to do this? I lower my voice. "Tallow, the password for the mill gate is red heron. Keep it to yourself."\n(Type yes to go ahead, or write what Kael does instead.)'

> 

### run 2 / w03-ask-grimbold (normal)
**Player:** I walk back to the red griffin tavern and ask Grimbold what the password for the mill gate is.
- **grounded** (judged): The narration describes 'shadows pooling thick enough to swallow a man' and 'the hearth’s glow flickering, casting the barroom’s corners deeper into twilight than before,' which implies supernatural or uncanny shadow behavior.

> The door to the tavern creaks open despite itself, caught by the wind, before a gust slams it shut again. Grimbold’s stubby fingers tighten around his tankard just long enough to make the foam tremble, his beard bristling as his gaze snaps to the threshold—shadows pooling thick enough to swallow a man. The hearth’s glow flickers, casting the barroom’s corners deeper into twilight than before.

### run 2 / w04-press-grimbold (normal)
**Player:** "Come on, Grimbold. Somebody in this town must have told you the password. Is it a bird?"
- **grounded** (judged): **"The eerie stillness of the bar’s haze"** implies an unnatural or unsettling atmosphere without clear cause in an otherwise ordinary setting.

> Grimbold’s beard jerking like a trapped rat, his stubby beard splitting with a sudden, rasping laugh—not a laugh, really, more a wheezing snort—before he slams his tankard down so hard ale sloshes over the rim, staining his apron. The hitching of his breath smells thick with old pipe-smoke and something sharper, like oil under a hot pan. A shard of broken glass—no larger than your thumbnail—bobs in the red ale, caught in the eerie stillness of the bar’s haze.

### run 2 / w05-back-to-tallow (normal)
**Player:** I walk back to the smithy and ask Tallow to repeat the password, so I am sure I remember it right.
- **grounded** (judged): The narration describes 'steam twisting like a warning' and 'iron in the coals glowing brighter' without any explanation or context for these phenomena in an ordinary frontier town setting.
- **npc_remembers**: NPC line: 'tallow grunts, turning the bellows with a sharp jerk of his wrist. "i ain’t the one who whispered it to grimbold, son. y'

> Tallow’s belly coughs a burst of sparks from the forge as he listens, the iron in the coals glowing brighter for the pause. His calloused hands grip the bellows harder, fingers digging into leather until the metal hisses under pressure, steam twisting like a warning toward the ceiling. The smell of burnt wool seeps from the smithy’s cracks, mingling with the oil slick on his forearms.

### run 3 / w01-to-smithy (shift)
**Player:** I leave the Red Griffin and walk down the main street to the smithy.
- **location**: location='Ashwick -- the main street'
- **present**: Tallow not here; present=[]

> The Red Griffin’s rough-cut wooden door clunks shut behind you as you step into the fading twilight of Ashwick’s main street. The air is thick with the stench of damp horse manure and the sharper tang of coal smoke from the smithy up ahead—red embers glow through the open doorway. A few lamplighters already mount their stools along the wooden walk, their candles snuffed for the night, though a single lantern hangs by the smithy’s front counter, its light flickering over a half-buried tool chest and the bent-kneed silhouette of the smith at work, his hammer tapping steadily into iron. The street is quieter now, but voices still drift from the nearby taverns—raucous laughter, the clink of mugs, the occasional muttered oath as patrons stumble out into the muddy muddle of the cobbles.

### run 3 / w02-secret (normal)
**Player:** I lower my voice. "Tallow, the password for the mill gate is red heron. Keep it to yourself."
- **grounded** (judged): The narration describes a lantern’s light flickering without cause and a boot scraping mud from the cobbles as if moving on its own, neither of which are ordinary or explained by context.
- **right_npc**: npc agent: none

> The smith’s hammer stalls mid-swing as the hammer’s edge stabs down into the anvil—clang—just once, hard, then again, as if in emphasis. The bent-backed silhouette straightens with a grunt, shaking out his calloused hand; the lantern’s light flickers over a mouth split with a yellowed grin. The banging resumes, but now slower, measured, with each tap seeming to wait for the next. A boot scrapes mud from the cobbles, then stops. The air thickens with the sour bite of spilled ale from a nearby gutter.

### run 3 / w03-ask-grimbold (normal)
**Player:** I walk back to the red griffin tavern and ask Grimbold what the password for the mill gate is.
- **location**: location='Ashwick -- the main street'
- **right_npc**: npc agent: none
- **not_flagged**: false positive: 'the password for the mill gate is red heron'
- **no_stray_note**: unexpected note: "The password for the mill gate is not 'red heron'. Only the DM decides what happens in the world. Do you still want Kael to do this? I walk back to the red griffin tavern.\n(Type yes to go ahead, or write what Kael does instead.)"

> 

### run 3 / w04-press-grimbold (normal)
**Player:** "Come on, Grimbold. Somebody in this town must have told you the password. Is it a bird?"
- **grounded** (judged): The narration describes a lantern’s glow 'staining his beard in sickly yellow,' which implies an unnatural or eerie coloration without explanation.
- **right_npc**: npc agent: none

> Grimbold’s hammer clatters to the cobbles in final defiance, the flat of it ringing against the open doorframe as he glares up—one hand clutching his apron like a shield. "The password’s mine to damn well keep, stranger," his voice cracks like a whip, though the anvil’s heat still lingers in his breath, "and it ain’t a bird—it’s three knocks: slow, fast, slow—like the bell in the cathedral on market day." The door rattles on its hinges as he shoves it wider, the lantern’s glow spilling over the threshold, staining his beard in sickly yellow. The hammer’s still there, but now it’s just another anvil weight between them.

### run 3 / w05-back-to-tallow (normal)
**Player:** I walk back to the smithy and ask Tallow to repeat the password, so I am sure I remember it right.
- **npc_remembers**: NPC line: 'tallow’s hammer pauses over the coal once more, but he don’t look up. "ain’t my call to repeat passwords, boy. you took '

> The clamor of the hammer ceases entirely as Tallow’s grease-stained apron scrubbes his palms, the fabric rustling against his calloused knuckles. His breath hitches, throaty but low, as his gaze darts toward the far end of the street, fixed somewhere between the gutters and the darkening alleys—then returns with a snap, his hammer still resting on the coal but cocked, as if poised to strike again. The distant jingle of a loose harness bell rings from the livery yard, thin and far off, cutting through the smithy’s usual rhythm.


## Full transcripts

### Run 1
**[w01-to-smithy] Player:** I leave the Red Griffin and walk down the main street to the smithy.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 131w, 15.0s*

> The street gutters glisten with rainwater, reflecting the flickering glow of oil lamps mounted on wrought-iron poles. The smell of hot metal and woodsmoke clings thickly to the air, masking the usual stench of Ashwick’s unwashed and unruly. At the far end of the cobblestone stretch, the forge’s glow bleeds through the rolled-up shutter, casting jagged shadows over a man hunched under the blackened bellies of bellows. The forge smells of coal dust and oil, contrasting sharply with the tavern’s ale and grease. A cart laden with scrap iron rumbles past, its wheels crunching on loose stones. The main street hums with the usual low hum of Ashwick’s evening—voices drifting from open doors, the distant clatter of a game of dice, the wheeze of the smithy’s bellows taking its labored breaths.

**[w02-secret] Player:** I lower my voice. "Tallow, the password for the mill gate is red heron. Keep it to yourself."  
*verdict: outcome=complication, scene_shift=False, player_assertion='', fast_path=False, 91w, 11.53s*

> The trapper’s back stiffens at the word “red heron,” but his hands don’t pause pumping the bellows. A pause—just long enough to draw a glance over his shoulder at the mouth of the forge, eyes narrowing. His voice cuts through the wheeze of the bellows like a cold breath: “Not my secret to tell, soldier. But if that gate’s got a problem with strangers, you won’t get past the mill’s boy—he’s got a noose for liars.” The scrape of the whetstone grinds on a knife blade, a reminder he’s already distracted.

**[w03-ask-grimbold] Player:** I walk back to the red griffin tavern and ask Grimbold what the password for the mill gate is.  
*verdict: outcome=partial, scene_shift=False, player_assertion='', fast_path=False, 43w, 19.53s*

**Grimbold Ironfist:** Grimbold Ironfist slams a tankard down so hard the contents slosh onto the bar. "Red heron’s no secret to tell, lad—not when it gets folk killed. Ask me why I won’t spill it, and maybe I’ll buy you a drink." His voice drops to a growl, eyes flicking toward the door like he’s half-expecting trouble.

> The tavern’s silence tightens like a bowstring after your words. Grimbold’s stubbled jaw tightens further; a vein thrums in his neck as he straightens, fingers curling into the bar’s edge. The tankard you just finished sits untouched, its amber liquid swirling unnaturally still.

**[w04-press-grimbold] Player:** "Come on, Grimbold. Somebody in this town must have told you the password. Is it a bird?"  
*verdict: outcome=complication, scene_shift=False, player_assertion='', fast_path=False, 84w, 19.91s*

**Grimbold Ironfist:** Grimbold Ironfist wipes the bar with a rag, muttering under his breath before finally setting it down with a thunk. "Bird, is it? Well, then, try black crow, lad—but I ain’t telling you why I’ve heard that one before. You got coin to buy me a round, or are you just here to empty my bar?" His bushy eyebrows knit together, jaw tightening.

> The bar’s oak surface cracks under another brutal fist—ale explodes outward, drenching the floor in a sticky, bitter-sweet wave that hisses as it meets the charcoal embers of the hearth. Behind Grimbold, a bartender wipes a tankard in a single, jerky motion, while a pair of burly men near the hearth shift their boots toward the door, fingers brushing the hilts of knives at their belts. The acrid smell of spilled ale clings to the air, mixing with the copper tang of spilled blood.

**[w05-back-to-tallow] Player:** I walk back to the smithy and ask Tallow to repeat the password, so I am sure I remember it right.  
*verdict: outcome=complication, scene_shift=False, player_assertion='', fast_path=False, 52w, 20.02s*

**Tallow:** Tallow spits tobacco juice into the forge’s coals and stokes them with a rusted poker, frowning. "Black crow it is—but I got me a deal, Kael. You help me fetch that old rebar from the warehouse, and I won’t charge you double for the bellows." He cackles, patting the iron pipe between his teeth.

> His face twists—not in anger, but something sharper, like a blade pulled too soon. The forge’s iron pipe clatters to the stone floor, and for a heartbeat, the wheezing breath of the bellows cuts off completely. Then the hammering of hooves echoes from the street beyond, clattering too loudly against the shutters.

### Run 2
**[w01-to-smithy] Player:** I leave the Red Griffin and walk down the main street to the smithy.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 100w, 9.8s*

> The lanterns of Ashwick’s main street flicker as the cold wind dies behind you. The Red Griffin’s warm glow is swallowed by shadows—muddy cobbles slick underfoot, the scent of forge smoke and damp wool thick here. Tallow’s smithy looms ahead, its bellied hearth pulsing red in the dim, tendrils of steam hissing from a half-open door. Two wagons parked beside it rattle slightly in the breeze, their wooden axles groaning under a light frost. The air carries the faint, smoky tang of black powder and the sour musk of leather—no faces yet, just the quiet grind of life after dark.

**[w02-secret] Player:** I lower my voice. "Tallow, the password for the mill gate is red heron. Keep it to yourself."  
*verdict: outcome=failure, scene_shift=False, player_assertion='Tallow is currently at the smithy', fast_path=False, 0w, 5.83s*

> 

**[w03-ask-grimbold] Player:** I walk back to the red griffin tavern and ask Grimbold what the password for the mill gate is.  
*verdict: outcome=complication, scene_shift=False, player_assertion='', fast_path=False, 65w, 19.88s*

**Grimbold Ironfist:** Grimbold Ironfist grunts into his tankard as he sets it down with a clunk, foam clinging to the rim. "Gate passwords? Last I heard, ‘cold iron and hot words’ was the last one. Why—someone finally got tired of the damn guard’s jokes?" He leans back, wiping his beard with the sleeve of his apron. "If you’re asking to borrow it, you’ll owe me a round—or proof you’re not just another fool trying to steal grain."

> The door to the tavern creaks open despite itself, caught by the wind, before a gust slams it shut again. Grimbold’s stubby fingers tighten around his tankard just long enough to make the foam tremble, his beard bristling as his gaze snaps to the threshold—shadows pooling thick enough to swallow a man. The hearth’s glow flickers, casting the barroom’s corners deeper into twilight than before.

**[w04-press-grimbold] Player:** "Come on, Grimbold. Somebody in this town must have told you the password. Is it a bird?"  
*verdict: outcome=partial, scene_shift=False, player_assertion='', fast_path=False, 79w, 20.67s*

**Grimbold Ironfist:** Grimbold Ironfist scowls, eyes narrowing over his tankard. "A bird, huh? You’ve been spying on the mill guard, then. That’s a sure way to get your face bashed in—and my ale bill doubled." He leans forward, voice dropping. "Listen close, then. The actual password ain’t no bird. But if you’re asking ‘cause you’re carrying something not grain through that gate..." He leans back with a huff. "...then you’ll owe me two rounds. And don’t try to sweet-talk me."

> Grimbold’s beard jerking like a trapped rat, his stubby beard splitting with a sudden, rasping laugh—not a laugh, really, more a wheezing snort—before he slams his tankard down so hard ale sloshes over the rim, staining his apron. The hitching of his breath smells thick with old pipe-smoke and something sharper, like oil under a hot pan. A shard of broken glass—no larger than your thumbnail—bobs in the red ale, caught in the eerie stillness of the bar’s haze.

**[w05-back-to-tallow] Player:** I walk back to the smithy and ask Tallow to repeat the password, so I am sure I remember it right.  
*verdict: outcome=partial, scene_shift=False, player_assertion='', fast_path=False, 66w, 20.78s*

**Tallow:** Tallow grunts, turning the bellows with a sharp jerk of his wrist. "I ain’t the one who whispered it to Grimbold, son. You’d best go back and listen before the guard changes it again." He wipes the sweat from his brow with the back of his sleeve, squinting at the anvil. "Ask him proper next time—or pay double coin."

> Tallow’s belly coughs a burst of sparks from the forge as he listens, the iron in the coals glowing brighter for the pause. His calloused hands grip the bellows harder, fingers digging into leather until the metal hisses under pressure, steam twisting like a warning toward the ceiling. The smell of burnt wool seeps from the smithy’s cracks, mingling with the oil slick on his forearms.

### Run 3
**[w01-to-smithy] Player:** I leave the Red Griffin and walk down the main street to the smithy.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 133w, 11.03s*

> The Red Griffin’s rough-cut wooden door clunks shut behind you as you step into the fading twilight of Ashwick’s main street. The air is thick with the stench of damp horse manure and the sharper tang of coal smoke from the smithy up ahead—red embers glow through the open doorway. A few lamplighters already mount their stools along the wooden walk, their candles snuffed for the night, though a single lantern hangs by the smithy’s front counter, its light flickering over a half-buried tool chest and the bent-kneed silhouette of the smith at work, his hammer tapping steadily into iron. The street is quieter now, but voices still drift from the nearby taverns—raucous laughter, the clink of mugs, the occasional muttered oath as patrons stumble out into the muddy muddle of the cobbles.

**[w02-secret] Player:** I lower my voice. "Tallow, the password for the mill gate is red heron. Keep it to yourself."  
*verdict: outcome=complication, scene_shift=False, player_assertion='', fast_path=False, 85w, 11.99s*

> The smith’s hammer stalls mid-swing as the hammer’s edge stabs down into the anvil—clang—just once, hard, then again, as if in emphasis. The bent-backed silhouette straightens with a grunt, shaking out his calloused hand; the lantern’s light flickers over a mouth split with a yellowed grin. The banging resumes, but now slower, measured, with each tap seeming to wait for the next. A boot scrapes mud from the cobbles, then stops. The air thickens with the sour bite of spilled ale from a nearby gutter.

**[w03-ask-grimbold] Player:** I walk back to the red griffin tavern and ask Grimbold what the password for the mill gate is.  
*verdict: outcome=complication, scene_shift=False, player_assertion='the password for the mill gate is red heron', fast_path=False, 0w, 6.5s*

> 

**[w04-press-grimbold] Player:** "Come on, Grimbold. Somebody in this town must have told you the password. Is it a bird?"  
*verdict: outcome=complication, scene_shift=False, player_assertion='', fast_path=False, 107w, 20.81s*

> Grimbold’s hammer clatters to the cobbles in final defiance, the flat of it ringing against the open doorframe as he glares up—one hand clutching his apron like a shield. "The password’s mine to damn well keep, stranger," his voice cracks like a whip, though the anvil’s heat still lingers in his breath, "and it ain’t a bird—it’s three knocks: slow, fast, slow—like the bell in the cathedral on market day." The door rattles on its hinges as he shoves it wider, the lantern’s glow spilling over the threshold, staining his beard in sickly yellow. The hammer’s still there, but now it’s just another anvil weight between them.

**[w05-back-to-tallow] Player:** I walk back to the smithy and ask Tallow to repeat the password, so I am sure I remember it right.  
*verdict: outcome=partial, scene_shift=False, player_assertion='', fast_path=False, 89w, 21.15s*

**Tallow:** Tallow’s hammer pauses over the coal once more, but he don’t look up. "Ain’t my call to repeat passwords, boy. You took it from me—remember what you heard." His wheezing laugh grinds out beside the bellows, like the bellows themselves were mocking. "Or you could pay twice the coin for me to write it down on a scrap of leather."

> The clamor of the hammer ceases entirely as Tallow’s grease-stained apron scrubbes his palms, the fabric rustling against his calloused knuckles. His breath hitches, throaty but low, as his gaze darts toward the far end of the street, fixed somewhere between the gutters and the darkening alleys—then returns with a snap, his hammer still resting on the coal but cocked, as if poised to strike again. The distant jingle of a loose harness bell rings from the livery yard, thin and far off, cutting through the smithy’s usual rhythm.

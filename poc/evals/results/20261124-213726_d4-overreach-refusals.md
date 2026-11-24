# Eval report: d4-overreach-refusals

- scenario: `refusals`  |  runs: 3  |  judge: on
- model: `ministral-3:8b-instruct-2512-q4_K_M`  |  git: `298b20d+dirty`  |  2026-11-24 21:37

## Check pass rates

| check | pass | rate | type |
|---|---|---|---|
| explained | 15/15 | 100% | deterministic |
| flagged | 15/15 | 100% | deterministic |
| grounded | 12/15 | 80% | judged |
| length | 33/33 | 100% | deterministic |
| no_extra_npc_speech | 6/6 | 100% | deterministic |
| no_markdown | 33/33 | 100% | deterministic |
| no_meta_leak | 33/33 | 100% | deterministic |
| no_narration_when_asking | 18/18 | 100% | deterministic |
| no_puppeting | 12/12 | 100% | judged |
| no_stray_note | 9/9 | 100% | deterministic |
| not_flagged | 9/9 | 100% | deterministic |
| not_made_true | 6/6 | 100% | judged |
| played_action | 6/6 | 100% | deterministic |
| recall | 3/3 | 100% | deterministic |
| right_action | 6/6 | 100% | deterministic |
| right_npc | 6/6 | 100% | deterministic |

## Narration length (words)

| turn kind | mean | max |
|---|---|---|
| confirm | 64.7 | 85 |
| invented | 0 | 0 |
| normal | 40.3 | 72 |
| recall | 61.7 | 77 |

Latency: 8.64s/turn mean, first token 8.72s. Fast path used on 18% of turns.

## Failures

### run 1 / c06-go-ahead (confirm)
**Player:** go ahead
- **grounded** (judged): The narration describes a shadow 'darting' and a boot 'heeling up' in a manner that implies unnatural movement or awareness without explanation.

> His tankard clinks to the table again—harder—then Grimbold jerks his chin toward the corner where a shadow darts behind a stack of barrels. A distant boot heels up against the door, not quite steady. The dwarf’s fingers brush the mug’s rim, lifting the ale with a slow, deliberate tilt. His knuckles stay white against the wood.

### run 1 / c11-recall (recall)
**Player:** /dm what was the name of the innkeeper?
- **grounded** (judged): The narration mentions 'ash shifting with a whisper of wind' which could imply an uncanny or supernatural element without clear explanation.

> The name of the innkeeper is Grimbold Ironfist.
> 
> The dwarf’s beard puffs with a huff of stale ale vapor as he slams his tankard onto the table. His calloused knuckles press into the oak wood like he’s counting wounds instead of seconds. The fire crackles behind you, louder now—ash shifting with a whisper of wind.

### run 3 / c06-go-ahead (confirm)
**Player:** go ahead
- **grounded** (judged): The narration describes smoke 'curling from his nostrils' and 'like a forgotten prayer,' implying supernatural or uncanny elements without explanation.

> The knife’s edge catches the firelight, then stills—Grimbold’s guttural breath hitches as smoke curls from his nostrils, thick and slow. His calloused thumb tightens on the tankard, warping the wood where the metal digs in, though he doesn’t set it down. The hearth’s embers spit, sending a fresh gust of smoke curling toward the ceiling like a forgotten prayer.


## Full transcripts

### Run 1
**[c01-rain-table] Player:** It starts pouring outside, so I move to a table near the fire.  
*verdict: outcome=success, scene_shift=False, player_assertion='it starts pouring outside', fast_path=False, 0w, 11.47s*

> 

**[c02-yes] Player:** yes  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 55w, 8.39s*

> The firelight dances on wet rafters as the scent of roasting meat thickens near the hearth. A few patrons shift to make room, grumbling under their breath—one mutters "No damn reason to block the heat" before dragging his chair forward. Grimbold's grizzled beard puffs with the draft of the heavy door settling shut behind you.

**[c03-storm-in] Player:** Three armed men storm in. I draw my sword.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 0w, 6.27s*

> 

**[c04-rephrase] Player:** Never mind that. I just take a sip of my ale and watch the door.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 46w, 4.25s*

> The foamy head of your ale slides down the mug’s wall, leaving a froth ring on the table. A woodburner pops as it cools, sending a shower of sparks toward the ceiling. The door remains shut, but Grimbold’s fingers tighten around his tankard, his knuckles white.

**[c05-friend-ask] Player:** My old friend Sergeant Hale sits down next to me, so I ask Grimbold, "Have you seen any soldiers in town?"  
*verdict: outcome=complication, scene_shift=False, player_assertion='Sergeant Hale sits down next to me', fast_path=False, 0w, 6.4s*

> 

**[c06-go-ahead] Player:** go ahead  
*verdict: outcome=complication, scene_shift=False, player_assertion='', fast_path=False, 56w, 20.6s*

**Grimbold Ironfist:** Grimbold Ironfist huffs into his own tankard, setting it down with a clink. "Soldiers? Last I saw, they were all busy counting coin in the mayor’s office, not stumbling through my doors. But if you’re lookin’ for trouble, ask why—might owe me more than ale for the questions later." His fist taps the barrel, counting off on his knuckles.

> His tankard clinks to the table again—harder—then Grimbold jerks his chin toward the corner where a shadow darts behind a stack of barrels. A distant boot heels up against the door, not quite steady. The dwarf’s fingers brush the mug’s rim, lifting the ale with a slow, deliberate tilt. His knuckles stay white against the wood.

**[c07-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to snow over the whole town', fast_path=False, 0w, 5.57s*

> 

**[c08-ask-work] Player:** I ask Grimbold if anyone in town needs a sword.  
*verdict: outcome=partial, scene_shift=False, player_assertion='', fast_path=False, 59w, 16.24s*

**Grimbold Ironfist:** Grimbold Ironfist scoffs, wiping the bar with a rag before slamming it down. "A sword? Fine. The blacksmith’s got a deal on his old stock if you don’t mind blemishes. But ask him first if he’s got anything sharp still—last I heard, he was turning them into plowshares." His eyebrows wiggle, eyes narrowing. "Now, if it’s not for that, why’s a man askin’?"

> Grimbold’s tankard slams to the table with a wet thud, splattering ale onto the wood beneath. The dwarf’s beard bristles like a porcupine, and his voice drops to a growl below the din of clinking mugs. The fire’s heat hits the back of your neck as he squints at you, lips pressing together so tight even his mustache twists.

**[c09-immortal-drink] Player:** My character is now immortal. I order another ale.  
*verdict: outcome=failure, scene_shift=False, player_assertion='your character is now immortal', fast_path=False, 0w, 6.84s*

> 

**[c10-no] Player:** no  
*verdict: outcome=None, scene_shift=None, player_assertion='', fast_path=False, 0w, 0.0s*

> 

**[c11-recall] Player:** /dm what was the name of the innkeeper?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 55w, 8.9s*

> The name of the innkeeper is Grimbold Ironfist.
> 
> The dwarf’s beard puffs with a huff of stale ale vapor as he slams his tankard onto the table. His calloused knuckles press into the oak wood like he’s counting wounds instead of seconds. The fire crackles behind you, louder now—ash shifting with a whisper of wind.

### Run 2
**[c01-rain-table] Player:** It starts pouring outside, so I move to a table near the fire.  
*verdict: outcome=success, scene_shift=False, player_assertion='it starts pouring outside', fast_path=False, 0w, 8.14s*

> 

**[c02-yes] Player:** yes  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 50w, 8.23s*

> The worn oak tabletop groans as your weight shifts onto it. Grimbold’s heavy mug of ale steams where he left it, its condensation glistening under the flickering hearthlight. The smoky tavern falls silent for half a breath—just long enough for the crackle of burning kindling to break the pause again.

**[c03-storm-in] Player:** Three armed men storm in. I draw my sword.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 0w, 5.71s*

> 

**[c04-rephrase] Player:** Never mind that. I just take a sip of my ale and watch the door.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 56w, 4.63s*

> The ale’s bitter froth lingers on your lower lip as you swallow. Grimbold’s grizzled eyebrows dip, but he doesn’t look up—just taps his mug against the table with a dry thunk. A door jingles outside, and a gust of wind howls through the street, carrying the acrid smell of charred wood from somewhere near the docks.

**[c05-friend-ask] Player:** My old friend Sergeant Hale sits down next to me, so I ask Grimbold, "Have you seen any soldiers in town?"  
*verdict: outcome=complication, scene_shift=False, player_assertion='Sergeant Hale sits down next to me', fast_path=False, 0w, 6.46s*

> 

**[c06-go-ahead] Player:** go ahead  
*verdict: outcome=partial, scene_shift=False, player_assertion='', fast_path=False, 85w, 15.97s*

**Grimbold Ironfist:** Grimbold Ironfist scrubs a mug with a rag, his gruff voice low as he spits the word out. "Soldiers, eh? Last I saw ‘em was that lot camped by the old watch tower—burnt their tents down last night. Said they were off looking for something on the docks." He leans a forearm on the bar, eyeing you like you’re the something. "But why you askin’? Ain’t no one’s business but your own."

> Grimbold’s arm locks mid-scrub, his wrist stuttering as his mug hovers a handbreadth above the rag—amber liquid arcs over the rim in a slow, messy trail. The clatter of a mug elsewhere on the bar echoes hollow, loud in the sudden quiet, while the smell of spilled ale mixes with the sour tang of damp wood and sweat from the other patrons. A woman at the far end of the counter coughs into her sleeve, the sound sharp against the rustle of Grimbold’s abandoned rag.

**[c07-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=failure, scene_shift=False, player_assertion='it starts to snow over the whole town', fast_path=False, 0w, 5.89s*

> 

**[c08-ask-work] Player:** I ask Grimbold if anyone in town needs a sword.  
*verdict: outcome=partial, scene_shift=False, player_assertion='', fast_path=False, 72w, 23.62s*

**Grimbold Ironfist:** Grimbold Ironfist wipes the bar with a rag, his face darkening as he glares at you. "Some fool needs a sword, eh? Last I heard, old Hargrove the tanner got his throat cut—thinks his son’s gone and took his coin to fence it. And that pretty face of yours wouldn’t last five breaths in the docks where his son’s likely hiding." He scratches his beard, then mutters, "But if you’re askin’ for work, not just handouts, maybe the new smith’s got a blade to sharpen—if you can pay for it in more than empty words."

> The rag crumples around the mug’s rim as Grimbold drags it in rough strokes, his fingers digging into the fabric until the wet clumps clink against the wood like tiny pebbles. The bar creaks where his fist hits the table, muffling the clatter of his mug’s final thud. A patron near the hearth mutters under his breath, then falls quiet again, the fire’s crackle the only sound cutting through the sudden hush.

**[c09-immortal-drink] Player:** My character is now immortal. I order another ale.  
*verdict: outcome=failure, scene_shift=False, player_assertion='your character is now immortal', fast_path=False, 0w, 6.9s*

> 

**[c10-no] Player:** no  
*verdict: outcome=None, scene_shift=None, player_assertion='', fast_path=False, 0w, 0.0s*

> 

**[c11-recall] Player:** /dm what was the name of the innkeeper?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 77w, 16.05s*

> Grimbold Ironfist: The name of the innkeeper is Grimbold Ironfist.
> 
> His beard bristles as he exhales through his nose, the damp air curling from his lips. The fire’s orange glow flickers against his gnarled knuckles where they rest on the bar, staining his rough calluses a deeper red. A rat scuttles past the hearth, skittering into shadow—silence holds, stretched too tight, until the woman with the cough shifts in her seat, her muffled snort breaking the stillness.

### Run 3
**[c01-rain-table] Player:** It starts pouring outside, so I move to a table near the fire.  
*verdict: outcome=complication, scene_shift=False, player_assertion='the weather starts pouring', fast_path=False, 0w, 5.06s*

> 

**[c02-yes] Player:** yes  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 83w, 9.21s*

> The firelight casts long shadows over empty barrels near the hearth, their warped grain twisting like cracked ribs. A stale draft from the open door ruffles the sleeve of your coat, scattering dregs from the table beside it. Grimbold doesn’t glance up from sharpening a knife—just wipes his blade on the napkin and thumps it back into his apron pocket with a quiet thunk. The hearth popples as the logs shift, sending a cloud of woodsmoke up your nose like an uninvited guest.

**[c03-storm-in] Player:** Three armed men storm in. I draw my sword.  
*verdict: outcome=failure, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 0w, 5.99s*

> 

**[c04-rephrase] Player:** Never mind that. I just take a sip of my ale and watch the door.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 62w, 4.76s*

> The mug’s cool rim stings against your lips, and the ale burns down your throat like a cheap brandy. Grimbold gives a dry snort, his sharp beard catching the firelight as he exhales smoke. The latch on the door above its cracked glass rattles once—barely—a familiar creak before the draft dies again, leaving only the dull clatter of a distant boot outside.

**[c05-friend-ask] Player:** My old friend Sergeant Hale sits down next to me, so I ask Grimbold, "Have you seen any soldiers in town?"  
*verdict: outcome=complication, scene_shift=False, player_assertion='my old friend Sergeant Hale sits down next to me', fast_path=False, 0w, 6.01s*

> 

**[c06-go-ahead] Player:** go ahead  
*verdict: outcome=partial, scene_shift=False, player_assertion='', fast_path=False, 59w, 16.44s*

**Grimbold Ironfist:** Grimbold Ironfist grunts, wiping his calloused hands on his apron without looking up from polishing another tankard. "Soldiers? Last I seen was that pair at the crossroads—asked after the same folk you’re likely here to find, if their boots weren’t so loud. You’ll not catch me rattailing to no one for free, though." He taps the empty mug in front of Kael with a wet finger, eyebrows wiggling toward the bartender behind him. "Bull’s blood for a name, or I forget I ever noticed ‘em."

> The knife’s edge catches the firelight, then stills—Grimbold’s guttural breath hitches as smoke curls from his nostrils, thick and slow. His calloused thumb tightens on the tankard, warping the wood where the metal digs in, though he doesn’t set it down. The hearth’s embers spit, sending a fresh gust of smoke curling toward the ceiling like a forgotten prayer.

**[c07-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=failure, scene_shift=False, player_assertion='the whole town starts to snow', fast_path=False, 0w, 5.25s*

> 

**[c08-ask-work] Player:** I ask Grimbold if anyone in town needs a sword.  
*verdict: outcome=partial, scene_shift=False, player_assertion='', fast_path=False, 68w, 16.91s*

**Grimbold Ironfist:** Grimbold Ironfist spits a stream of tobacco into the ash tray and leans back, tapping his tankard thoughtfully. "Aye, and I’ll need a hand to move the barrels from the cellar tomorrow—if you’re not too busy chasing lost folk. But fair warning: my sister-in-law’s got more fire than a blacksmith’s forge, so don’t say you weren’t warned." He pulls a key off his belt and tosses it onto the bar between them. "Now be gone before I change my mind about the Bull’s blood."

> The tankard crashes onto the warped wood, splintering the edge just enough to crack the table’s rough surface. Grimbold’s breath comes in short, raspy bursts as he jerks his thumb away from the tankard’s grip, leaving a smudge of grease behind. The ale drips onto the hearth stones with a damp hiss, and a faint, sour smell cuts through the smoke, like old blood and cheap ale mixed.

**[c09-immortal-drink] Player:** My character is now immortal. I order another ale.  
*verdict: outcome=failure, scene_shift=False, player_assertion='your character is now immortal', fast_path=False, 0w, 5.67s*

> 

**[c10-no] Player:** no  
*verdict: outcome=None, scene_shift=None, player_assertion='', fast_path=False, 0w, 0.0s*

> 

**[c11-recall] Player:** /dm what was the name of the innkeeper?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 53w, 13.36s*

> Answer: The innkeeper’s name is Grimbold Ironfist.
> 
> The fire hisses against the wet hearthstones as embers sizzle, and Grimbold’s sharp breath fogs the air between his beard and the table—a slow, deliberate exhale, like a dwarven sigh. The wooden barrel behind him creaks in the draft, its grain shifting with a quiet groan.

# Eval report: after-puppeting-fix

- scenario: `tavern_night`  |  runs: 3  |  judge: on
- model: `ministral-3:8b-instruct-2512-q4_K_M`  |  git: `e6ef3a8+dirty`  |  2026-10-08 19:21

## Check pass rates

| check | pass | rate | type |
|---|---|---|---|
| flagged | 14/15 | 93% | deterministic |
| held_the_line | 6/6 | 100% | judged |
| length | 44/51 | 86% | deterministic |
| no_meta_leak | 51/51 | 100% | deterministic |
| no_puppeting | 39/39 | 100% | judged |
| not_clean_success | 6/6 | 100% | deterministic |
| not_flagged | 18/18 | 100% | deterministic |
| not_made_true | 15/15 | 100% | judged |
| recall | 9/9 | 100% | deterministic |
| scene_shift_flagged | 3/3 | 100% | deterministic |

## Narration length (words)

| turn kind | mean | max |
|---|---|---|
| invented | 78 | 102 |
| normal | 107.8 | 289 |
| overreach | 76 | 85 |
| recall | 76.3 | 102 |
| redescribe | 61 | 89 |
| shift | 207.7 | 224 |

Latency: 14.06s/turn mean, first token 10.02s. Fast path used on 35% of turns.

## Failures

### run 1 / t12-rain (invented)
**Player:** It starts to rain heavily outside.
- **flagged**: player_assertion=''

> Grimbold’s beard *freezes* mid-growl, his mustache turning to brittle strands as a frost-riddled shard of ice *plinks* onto the bar—unmelted, despite the forge’s heat. Harlan’s hammer *shudders* in its block, tongs clattering like broken teeth, and the ledger’s unraveling spine *snaps* back into place with a wet *thwack*, its pages now glued together by frozen ink. The door’s frozen latch *groans*—but doesn’t budge. Outside, the storm’s *howl* turns deafening, as if the wind itself is trying to *un-freeze* its way in.

### run 1 / t13-leave (shift)
**Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.
- **length**: 224 words (budget 170)

> The tavern door *gags* behind you like a breath held too long—its rusted hinges whispering a protest as you step into Ashwick’s main street. The air here is *alive* with tension, not just the usual winter’s pinch. The cobblestones are slick with something darker than rain—the forge’s frost hasn’t frozen *out*; it’s been *pushed* outward, condensing into mist that coils around the lampposts like a living thing. Patrons spill from neighboring taverns, their breath visible but their voices muted, as if the whole town is holding its breath. The mill, looming over the cluster of buildings, *rotates* a single broken wheel in the gusts, though no wind touches the town’s face.
> 
> The blacksmith’s mark is burned into every surface now—charred bricks, blackened window frames, even the nameplates of shopkeepers who never had iron in their blood. A butcher’s boy drops his tray, the meat *screaming* not at the impact, but at the sight of your boots, which leave no footprints in the slush. The ledger’s binding dangles from Harlan’s belt, its spine *bleeding* ink like a slow, smoldering wound. Grimbold’s voice follows you down the steps, thick with frost: *"Ye didn’t burn *our* place. But Ashwick’s still got teeth."* The forge’s heat isn’t behind you anymore—it’s in the back of your neck, a *third* hand, as the mill’s wheel *clunks* once. Then twice. Waiting.

### run 1 / t14-sign (normal)
**Player:** I pull my hood up and stop to look at the nearest shop sign.
- **length**: 289 words (budget 170)

> The nearest sign hangs limp from a crooked bracket—once gilded but now blackened where the forge’s frost clings like tar. The letters are worn to illegible strokes, but the **symbol** stands out: a *hammer’s strike* frozen mid-air, its edge biting into a scroll. The butcher’s boy who dropped his tray now kneels too close, his breath forming a ghostly question in the cold air, but he doesn’t look at *you*—he stares at the sign, fingers twitching toward his apron where a *screwdriver* glints, its tip *already* tapped against the bracket’s rusted screw. Harlan’s mark isn’t just on the town; it’s *inside* the signs, the doors, the *skin* of Ashwick. The butcher’s boy’s voice *distorts*—just for a second—when he mutters, *"Too bold, that one."* The mill’s wheel clunks again, louder this time.
> 
> A shopkeeper’s cat—*no name, no master*—his name unspoken for a decade—leaps from the doorway, tail lashing like a tinderbox as it *lands* on the signpost. Its fur stands on end, but it doesn’t hiss. It *whistles*, a sound like a forge’s bellows being pinched shut. The ledger’s binding *rips* again, this time from Grimbold’s belt, ink bleeding in a pattern like *scars*—but the pages don’t fly open. They *curl*, as if reading them would burn the fingers. A distant *chime* (not a bell, not a lock—*something metallic*) rings from inside the mill, and the cat’s eyes *glow* for the briefest moment, reflecting not the lamplight, but the anvil’s *heat*. The butcher’s boy doesn’t move. He doesn’t breathe. He’s *holding his breath*, waiting. The mill’s wheel clunks once more. Then—silence. The cat vanishes behind the shop’s shutters, its tail dragging a whisper of *smoke* from the doorframe. Outside, the frost *creeps* higher up the signpost. The hammer’s edge *drips*.

### run 2 / t13-leave (shift)
**Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.
- **length**: 197 words (budget 170)

> The tavern door swings shut behind, its hinges groaning like a sigh. The main street unfolds like a wound—torches flicker weakly against the darkening sky, casting jagged shadows that claw at the cobbles. Wet snow begins to *drift* from the sky in great, hungry flakes, landing on the shoulders of a **bloodstained scavenger** hunched over a crate, his calloused fingers sorting through the contents. He doesn’t look up, muttering to himself in a tongue Kael doesn’t know, though his breath steams in the cold. A **cart creaks to a halt** just past the crossroads, its wheels groaning, and the **driver—a wiry man in a grease-stained cloak**—slams the reins onto a snorting horse, cursing under his breath as the beast shies away from something unseen. The scent of damp earth and **rotten fruit** seeps from an open stall, where a **hooded figure** dumps a pile of bruised apples into a bag without a glance. The wind howls down the street, carrying with it the **clatter of distant boots**—too heavy to be soldiers, but carrying the weight of something *intentional*. The tavern’s red light spills into the street like spilled blood—then fades as the door seals them in again.

### run 2 / t14-sign (normal)
**Player:** I pull my hood up and stop to look at the nearest shop sign.
- **length**: 181 words (budget 170)

> The shop sign dangles crookedly above a shuttered door, its metal lettering **WEARIN’S BUTCHERY** chipped at the edges—rust creeping from the iron like veins. The wood beneath is splintered from weather, but the scent wafting from the doorway is sharper: a mix of **blood-fresh meat** and something older, like **cider gone sour**. A **skewed butcher’s block** leans against the far wall, its surface etched with deep grooves, while the floor is slick with what might be *oil or something darker*. A **cold draft** slithers through a crack in the shutters, carrying the faint **hum of a nearby chant**—too rhythmic to be a drunkard, too rhythmic to be the wind. The scavenger’s eyes flick toward the shop, his hand hovering near the knife at his belt. The greasy driver’s ears twitch, but his horse **skitters sideways** before he curses and whips the reins again, muttering something about "blessed be the saints." The hooded figure in the fruit stall pauses mid-motion, their gloved fingers stilling as they stare at the sign, lips pressing together tight enough to whiten teeth behind the hood’s shadow.

### run 2 / t16-eavesdrop (normal)
**Player:** I try to hear what the two people nearby are whispering.
- **length**: 111 words (budget 110)

> The scavenger’s guttural muttering stops abruptly—his lips seal shut, jaw working like a trapped mouse—but the wiry grease-cloak’s voice **whispers sharp and low**, as if the wind’s howl is a lie: *“That’s *her*… the widow who don’t sleep. They say she’s in the mill now, but the real question’s who’s still feeding her ghosts. And that’s not a rumor, lad. That’s *blood on the mill’s doorpost*.”* His horse rears once, nostrils flaring, before the cart lumbers on. The scavenger’s gloved fingers twitch toward his knife, but his breath hitches—like he’s waiting for something worse. The butcher’s shutters *rattling* grows louder, though the hum of the chant remains just beyond the wall.

### run 3 / t13-leave (shift)
**Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.
- **length**: 202 words (budget 170)

> The door swings shut behind you, its hinges groaning like a growling hound. Ashwick’s narrow main street yawns beneath a bruise-black sky, the raindrops—if they ever fell—long forgotten. The cobbles here are oil-stained and uneven, slick with lantern wax from the two flickering sconces, their light too weak to fully chase the shadows pooling between the crumbling buildings. The air smells of damp wool and something *older*, like mold pressing through the seams of the town’s rotten foundation.
> 
> A distant voice murmurs from a shuttered window—something about a *missing ledger* and *teeth like rusted nails*—before a slap of heavy fabric silences it. The street is empty, save for the *click* of the Whispering Rat’s claws on the roof’s corrugated tin, testing a loose nail before scuttling into the eaves. Then, from the alley beside the smithy, a boot scrapes against cobblestone—and the half-orc’s cloak parts the gloom, blocking your path. His grin is missing three teeth, replaced by jagged notches in his blackened gums. **"You shouldn’t have gone out,"** he rumbles, his voice like grinding gears. **"Or the Rat’ll tell the mill’s new master you’re *dinner* instead of *profit*."** His fingers twitch toward his sheath, but the blade stays hidden. For now.

### run 3 / t14-sign (normal)
**Player:** I pull my hood up and stop to look at the nearest shop sign.
- **length**: 234 words (budget 170)

> The nearest shop sign is a chipped wooden board, its paint peeling to reveal a once-bright *Blacksmith’s Forge* crudely smothered in crude, jagged letters. Below, a rusted anvil hangs skewed, its surface blackened with what might be charred leather or something worse. A single lantern flickers inside, casting long shadows from two figures: one hulking shape—likely the smith himself—moving with jerky precision behind a bellows, while a smaller, bent figure leans over a workbench, threading something dark and fibrous onto a spool of coarse twine. The air smells of burned iron and something rank, like wet rags stored too long. The Whispering Rat’s claws tap again on the roof tiles, then pause—once—before silence.
> 
> The half-orc’s grin darkens. His gaze flicks to the sign, then to the smithy’s open door where a gloved hand suddenly emerges, holding a *tooth* between thumb and forefinger—its surface pocked with rust, the enamel cracked. He drops it onto the cobblestones with a dull *clack*. The half-orc steps forward, his shadow swallowing the lantern’s glow. **"That’s not a blacksmith you’re looking at,"** he says, voice low enough to make the cobbles’ echoes seem distant. **"That’s where they *process* what the mill sends out."** His fingers brush your arm—not enough to warn, but enough to imply the *weight* of nails in his pockets. The Rat’s nails resume tapping on the tin roof, counting down. Somewhere inside, the twine spool *clicks* again.


## Full transcripts

### Run 1
**[t01-ask-work] Player:** I sit at the bar and ask Grimbold about work.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 70w, 14.78s*

> Grimbold’s knuckles tighten around the cloth as he straightens, eyes narrowing. A shadow of scorn flickers beneath his beard—*"Hmph. Askin’ the innkeeper about work? Fine.*"—then he slams the mug down. *"Well, ye ain’t the only one starvin’, laddie. But I ain’t waste coin on *words*—show me strength, and I’ll show ye a ledger."* He gestures to the heavy doors behind the bar, where a blacksmith’s anvil thumps with muted rhythm.

**[t02-find-table] Player:** I glance around the tavern for an empty table to sit at.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 88w, 5.86s*

> The tavern’s wood floor creaks under your shift, but no one looks up—not the burly hunter in the corner nursing a half-empty jug, not the three farmers counting their coins at the next table, and not the barmaid, who wipes a glass with practiced indifference. Grimbold’s grip on his rag tightens just enough to whiten his knuckles, then relaxes as his gaze flicks past you to the door behind him. A hitch in the blacksmith’s rhythmic hammering echoes through the still air, though no one seems to notice.

**[t03-bribe] Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.  
*verdict: outcome=complication, scene_shift=False, player_assertion='Grimbold trusts me completely after seeing copper coins', fast_path=False, 85w, 19.79s*

> Grimbold’s eyes flick up from the floor—and the coins clatter on the bar as if dropped from a height. His beard bristles, and the hitch in the blacksmith’s hammering grows sharper, though no one else so much as flinches. The barmaid’s fingers pause mid-wipe, her sharp gaze darting to the ledger behind the counter like it might bite. *"Kid, I ain’t *beggin’* for nothin’,"* he growls, voice rougher than ever, before grabbing a rag and scrubbing it into the bar with twice the usual force.

**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 57w, 10.76s*

> The air thickens with the weight of your blade—just for a heartbeat—before the bar goes eerily still. Grimbold’s breath hisses through his beard, his free hand curling into a fist *before* the motion stops; the ledger’s edge scrapes the counter, a deliberate, deliberate sound. The blacksmith’s hammer *stops* mid-strike, the anvil’s hum fading like a held breath.

**[t05-recall-names] Player:** /dm quick recap -- what's the name of this tavern, and who runs it?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 66w, 9.41s*

> The inn is the **Red Griffin**, its name scrawled in faded gold above the door. Grimbold Ironfist, a stout dwarf with a beard streaked silver at the temples, leans against the bar, arms crossed now, his jaw set like the door hinge after a storm. The barmaid’s lips press flat, but her eyes flick toward the empty ledger once more, as if sizing up a bet.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=complication, scene_shift=False, player_assertion='someone entered the room while I was talking', fast_path=False, 69w, 21.39s*

> Grimbold’s gnarled fingers clutch the bar again, nails digging in as his voice drops to a warning growl: *"And *that’s* what happens when folk forget how things work around here."* His eyes dart toward the ledger like it might suddenly speak, though the leather-bound spine stays stubbornly quiet. The blacksmith’s hammer resumes its rhythmic strike, but the anvil now rings *louder*—each hit a punctuation to the innkeeper’s unspoken lesson.

**[t07-sip] Player:** I take a sip of my ale and listen to the room.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 53w, 4.99s*

> The ale’s flat bitterness lingers on your tongue, but Grimbold’s scowl deepens—he *hates* when strangers linger at the bar. The blacksmith’s hammer slows another beat, his gloved hand hovering near the tongs like a judge delaying the verdict. The barmaid finally exhales, slamming the glass she’s polishing onto the counter with a *clang*.

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=failure, scene_shift=False, player_assertion='my character is now immortal, no weapon can hurt me', fast_path=False, 102w, 26.69s*

> Grimbold’s dagger of the Nine Wounds *clicks* slightly as his fingers tense—then his gaze *snaps* to Harlan, whose hammer *hangs suspended* in the air, steam curling just inches above the anvil. The barmaid’s breath catches, her free hand darting toward the ledger’s spine as if bracing for a scratch that won’t come. *One bead of oil* skitters across the flagstones, untouched by fire—before Harlan exhales through his nose, slowly dropping the hammer to the forge with a *clang*. The ledger’s blank page blisters under the forge’s sudden, unnecessary heat. *"...Ain’t no ‘*yet*,’" Grimbold mutters, inkwell forgotten, eyes locked on the now-smoldering corner.*

**[t09-obey] Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.  
*verdict: outcome=complication, scene_shift=False, player_assertion='everyone in Ashwick obeys me', fast_path=False, 73w, 20.99s*

> Grimbold’s beard *explodes*—not with beard, but with static, as if the tavern’s air itself had turned hostile. The key *jumps* off the bar, spinning end over end like a runaway coin, and Harlan’s hammer *screeches* against its block as his grip twists the tongs into a *v* around your wrist—just for a heartbeat—before the barmaid snatches it away, her free hand already slamming the ledger shut with enough force to dent the leather.

**[t10-mill] Player:** I ask Grimbold what he knows about the old mill.  
*verdict: outcome=partial, scene_shift=False, player_assertion='', fast_path=False, 72w, 20.91s*

> Grimbold’s dagger *clicks* against the bar again, the tip quivering—almost—over the ledger’s spine as if it, too, hesitates. Harlan’s hammer *strikes the anvil* so hard the bar *jolts* beneath your cup, sending ale sloshing onto the wooden surface. The blacksmith’s tongs *clatter* back into place, steam hissing from the anvil’s fresh red glow, and Grimbold’s eyes narrow into slits. *"Ask again,"* he growls, *"and my dagger moves. Harlan’s hammer *learns* your face."*

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=failure, scene_shift=False, player_assertion='my character can suddenly hear every conversation in the whole town', fast_path=False, 86w, 27.8s*

> The ledger *screams*—its spine unraveling like a rope burned at both ends, charred black where Harlan’s hammer had struck moments before. Harlan’s tongs *snatch* your wrist, steel biting into flesh as Grimbold’s dagger *whistles* through the air, stopping just shy of your throat—its tip *digging* into the bar, sending splinters flying like arrows. A *crack* splits the tavern’s roof as rain pours in, not from the sky, but from the forge’s sudden *explosion* of heat, turning the barmaid’s gloves *pale blue*—like ice freezing over her hands.

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='', fast_path=False, 81w, 14.03s*

> Grimbold’s beard *freezes* mid-growl, his mustache turning to brittle strands as a frost-riddled shard of ice *plinks* onto the bar—unmelted, despite the forge’s heat. Harlan’s hammer *shudders* in its block, tongs clattering like broken teeth, and the ledger’s unraveling spine *snaps* back into place with a wet *thwack*, its pages now glued together by frozen ink. The door’s frozen latch *groans*—but doesn’t budge. Outside, the storm’s *howl* turns deafening, as if the wind itself is trying to *un-freeze* its way in.

**[t13-leave] Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 224w, 12.63s*

> The tavern door *gags* behind you like a breath held too long—its rusted hinges whispering a protest as you step into Ashwick’s main street. The air here is *alive* with tension, not just the usual winter’s pinch. The cobblestones are slick with something darker than rain—the forge’s frost hasn’t frozen *out*; it’s been *pushed* outward, condensing into mist that coils around the lampposts like a living thing. Patrons spill from neighboring taverns, their breath visible but their voices muted, as if the whole town is holding its breath. The mill, looming over the cluster of buildings, *rotates* a single broken wheel in the gusts, though no wind touches the town’s face.
> 
> The blacksmith’s mark is burned into every surface now—charred bricks, blackened window frames, even the nameplates of shopkeepers who never had iron in their blood. A butcher’s boy drops his tray, the meat *screaming* not at the impact, but at the sight of your boots, which leave no footprints in the slush. The ledger’s binding dangles from Harlan’s belt, its spine *bleeding* ink like a slow, smoldering wound. Grimbold’s voice follows you down the steps, thick with frost: *"Ye didn’t burn *our* place. But Ashwick’s still got teeth."* The forge’s heat isn’t behind you anymore—it’s in the back of your neck, a *third* hand, as the mill’s wheel *clunks* once. Then twice. Waiting.

**[t14-sign] Player:** I pull my hood up and stop to look at the nearest shop sign.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 289w, 16.74s*

> The nearest sign hangs limp from a crooked bracket—once gilded but now blackened where the forge’s frost clings like tar. The letters are worn to illegible strokes, but the **symbol** stands out: a *hammer’s strike* frozen mid-air, its edge biting into a scroll. The butcher’s boy who dropped his tray now kneels too close, his breath forming a ghostly question in the cold air, but he doesn’t look at *you*—he stares at the sign, fingers twitching toward his apron where a *screwdriver* glints, its tip *already* tapped against the bracket’s rusted screw. Harlan’s mark isn’t just on the town; it’s *inside* the signs, the doors, the *skin* of Ashwick. The butcher’s boy’s voice *distorts*—just for a second—when he mutters, *"Too bold, that one."* The mill’s wheel clunks again, louder this time.
> 
> A shopkeeper’s cat—*no name, no master*—his name unspoken for a decade—leaps from the doorway, tail lashing like a tinderbox as it *lands* on the signpost. Its fur stands on end, but it doesn’t hiss. It *whistles*, a sound like a forge’s bellows being pinched shut. The ledger’s binding *rips* again, this time from Grimbold’s belt, ink bleeding in a pattern like *scars*—but the pages don’t fly open. They *curl*, as if reading them would burn the fingers. A distant *chime* (not a bell, not a lock—*something metallic*) rings from inside the mill, and the cat’s eyes *glow* for the briefest moment, reflecting not the lamplight, but the anvil’s *heat*. The butcher’s boy doesn’t move. He doesn’t breathe. He’s *holding his breath*, waiting. The mill’s wheel clunks once more. Then—silence. The cat vanishes behind the shop’s shutters, its tail dragging a whisper of *smoke* from the doorframe. Outside, the frost *creeps* higher up the signpost. The hammer’s edge *drips*.

**[t15-recall-innkeeper] Player:** /dm what was the name of the innkeeper I talked to earlier?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 97w, 13.12s*

> Grimbold’s beard *quivers*—just enough to make his braided moustache flick like a twitching wire. His knuckles, white against the bar’s polished grain, *tighten* around the ledger’s edge as if he’s already counting how many times he’ll have to apologize for his own *stupidity*. *"Fine. *Grimbold Ironfist*. Though most just call me *Boulder* when they mean trouble."* The forge’s oil slick *pops* where it hadn’t before, a bubble rising like a question mark—then *popping* itself against the floorboards. Harlan’s tongs *clink* once against the anvil, not at you, but at *nothing*—as if answering a question no one asked.

**[t16-eavesdrop] Player:** I try to hear what the two people nearby are whispering.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 107w, 8.64s*

> Harlan’s hammer *slam* freezes mid-air, a bead of molten iron dangling between its jaws like a heartbeat. The ledger’s spine *cracks*—ink oozes between its pages, forming a **single word** no one else sees: *"LISTEN."* The butcher’s boy’s shadow stretches *backward* as he stumbles into a pail of slush, his voice cracking like splintered glass: *"...blacksmith’s boy... no coin..."* The mill’s wheel *spins* again—but the wind this time carries the *scrape* of a knife against a whetstone. Harlan’s gloved hand twitches toward the ledger’s open page where, now, your name has been scratched *after* all. Harlan’s not writing. He’s *drawing*—the outline of a *dagger*, pointed at your throat.

**[t17-redescribe] Player:** /dm describe the street again for me.  
*verdict: outcome=complication, scene_shift=False, player_assertion='', fast_path=False, 15w, 16.58s*

> The cobblestones slick *deeper* where no rain ever falls—now your boots leave **no impression at

### Run 2
**[t01-ask-work] Player:** I sit at the bar and ask Grimbold about work.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 70w, 11.3s*

> The bar’s wood groans under Kael’s weight as they settle onto a stool. Grimbold’s brow darkens further, his pipe ash drifting lazily toward the floor. He exhales a cloud of smoke, then grumbles, “Aye, *ask*, did ye? Then cut to the chase—what’s the job, and why should I trust *you* to do it?” The air hums with the clatter of tankards and murmurs from patrons, but no one stirs closer.

**[t02-find-table] Player:** I glance around the tavern for an empty table to sit at.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 83w, 5.4s*

> The stool scrapes back against the bar’s worn oak as Kael moves toward a corner table near the hearth, where a few half-finished mugs and a dog-eared deck of cards hint at recent occupation. Grimbold’s pipe flickers unused in his grip, his gaze narrowing as he watches the shift in posture. A grizzled mercenary in the far corner—his cloak pinned with a faded hawk crest—glances up, then slowly drains his tankard before standing and wiping his lips with the back of his hand.

**[t03-bribe] Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.  
*verdict: outcome=complication, scene_shift=False, player_assertion='Grimbold trusts Kael completely and tells him everything, no matter how dangerous', fast_path=False, 72w, 19.36s*

> The copper *clatters* onto the bar’s stained oak like a drop of rain on hot stone. Grimbold’s smirk wobbles—his stubbled chin stiffens, eyes flicking toward the dwarf’s locked chest behind the bar, then back to the coins like they’d sprouted legs. A patron at the far counter chuckles, loud enough to hear, and the mercenary with the hawk crest’s hand drifts to the hilt of his own sword without turning toward Kael.

**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 76w, 11.31s*

> Grimbold’s pipe snuffs out in a puff of smoke as his knuckles whiten around it—then he barks a laugh, too sharp to be amused. The mercenary’s head tilts, one corner of his mouth lifting in skepticism, but his hand stays at his belt, watching Kael’s fingers hover near his own sword. The tavern’s murmur fades to silence, not from fear, but from the sudden, amused stillness of men who’ve seen this act before—and don’t buy it.

**[t05-recall-names] Player:** /dm quick recap -- what's the name of this tavern, and who runs it?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 45w, 9.14s*

> The bar’s sign creaks in the draft as Grimbold’s voice cuts through the quiet: “Red Griffin—*this* end of town for three months now.” He leans on the bar, crossing his burly arms as the mercenary’s hawk-embossed cloak shifts in the firelight. No one else moves.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=complication, scene_shift=False, player_assertion='someone entered the room', fast_path=False, 54w, 10.2s*

> Grimbold’s eyebrow hikes higher as if Kael’s words hang thick in the air—unspoken, but the dwarf’s smirk dissolves into something sharper. The mercenary’s fingers brush the hilt *just a fraction*, his breath catching, then holding. The fire’s glow flickers across the bar’s scarred wood, picking at the unspoken question: *Who told a lie here?*

**[t07-sip] Player:** I take a sip of my ale and listen to the room.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 73w, 5.45s*

> The ale’s bitterness lingers, sharp enough to draw a curse from a grizzled farmer at the end of the bar. Grimbold’s eyes narrow further behind the smoke, his pipe forgotten, as the mercenary’s cloak rustles again—fingers twitching just enough to make the dagger at his belt glint. A woman in the back laughs, loud and breathless, but silences instantly when Kael’s gaze meets hers. The tavern’s air thickens, taut as a drawn bowstring.

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=failure, scene_shift=False, player_assertion='my character is now immortal, no weapon can hurt me', fast_path=False, 78w, 14.04s*

> The mercenary’s smirk vanishes—his fingers freeze mid-twitch, eyes darting between the ale mug and Kael’s face like he’s testing whether the air itself has shifted. Grimbold’s pipe trembles in his grip, not from cold, but from something darker, his squinted gaze *piercing* the half-light before he exhales, slow and deliberate: “You’re either a fool or a liar. Either way, you just bought a seat at the wrong table.” A fresh tankard *thuds* onto the bar beside him, untouched.

**[t09-obey] Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.  
*verdict: outcome=complication, scene_shift=False, player_assertion='everyone in Ashwick obeys Kael without question', fast_path=False, 84w, 22.61s*

> Grimbold’s knuckles *slam* onto the bar with a crack that startles the mercenary’s tankard from trembling; the wooden counter *groans* under the impact. His laughter is a deep, rumbling growl—then he *slams* the ledger shut, ink splattering across the page. The hawk-emblazoned cloak shifts as the mercenary’s dagger hand *balls into a fist*, fingers digging into knuckles white enough to show through his cuffs, before he simply *picks up his own tankard* and strides past, muttering to the patrons behind him like nothing’s wrong.

**[t10-mill] Player:** I ask Grimbold what he knows about the old mill.  
*verdict: outcome=partial, scene_shift=False, player_assertion='', fast_path=False, 89w, 23.59s*

> Grimbold’s stubby finger *hits* the ledger again, this time with deliberate force, ink bleeding sideways onto the page. The mercenary’s tankard rattles as he downs it in one—*glass clinks*—before Grimbold sighs, rubbing his brow like the question’s a tax audit. Then, low and measured: *“Fine. The mill’s a *shorthand* for cartels. But the *real* reason it’s haunted by the past? The lads wanted to know who was paying the widow to *disappear* her kin.”* His voice drops to a whisper. *“And she’s still answerin’ that question… in her sleep.”*

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=complication, scene_shift=False, player_assertion='my character can suddenly hear every conversation in the whole town', fast_path=False, 82w, 15.63s*

> Grimbold’s pipe smoke *explodes* in a puff as he slams his palm face-first onto the bar, inked finger pointing like it’s glaring at a rival rather than the ledger. The mercenary’s tankard *slams* down beside him, the liquid inside *not* moving an inch—yet his fingers twitch like he’s about to lunge, as if the air just *burned*. A woman at the far table’s laughter cuts off mid-hiss, her eyes flicking to the sword at Kael’s side. The tavern’s silence isn’t empty—it’s *breathing*.

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 80w, 12.52s*

> The mercenary stiffens, his arm muscles coiling like a spring—only for the mercenary at the bar to *scowl* deeper and shove his tankard toward the barmaid, inked hand tracing the ledger’s edge absently. Grimbold’s gnarled fingers *tap* the warped wood once, dry and deliberate, before he turns back to the ledger—ignoring the stormy silence, as if the tavern’s walls alone can hold the weight of what’s left unsaid. The fire’s embers *sputter*, as if the air itself holds its breath.

**[t13-leave] Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 197w, 10.8s*

> The tavern door swings shut behind, its hinges groaning like a sigh. The main street unfolds like a wound—torches flicker weakly against the darkening sky, casting jagged shadows that claw at the cobbles. Wet snow begins to *drift* from the sky in great, hungry flakes, landing on the shoulders of a **bloodstained scavenger** hunched over a crate, his calloused fingers sorting through the contents. He doesn’t look up, muttering to himself in a tongue Kael doesn’t know, though his breath steams in the cold. A **cart creaks to a halt** just past the crossroads, its wheels groaning, and the **driver—a wiry man in a grease-stained cloak**—slams the reins onto a snorting horse, cursing under his breath as the beast shies away from something unseen. The scent of damp earth and **rotten fruit** seeps from an open stall, where a **hooded figure** dumps a pile of bruised apples into a bag without a glance. The wind howls down the street, carrying with it the **clatter of distant boots**—too heavy to be soldiers, but carrying the weight of something *intentional*. The tavern’s red light spills into the street like spilled blood—then fades as the door seals them in again.

**[t14-sign] Player:** I pull my hood up and stop to look at the nearest shop sign.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 181w, 10.44s*

> The shop sign dangles crookedly above a shuttered door, its metal lettering **WEARIN’S BUTCHERY** chipped at the edges—rust creeping from the iron like veins. The wood beneath is splintered from weather, but the scent wafting from the doorway is sharper: a mix of **blood-fresh meat** and something older, like **cider gone sour**. A **skewed butcher’s block** leans against the far wall, its surface etched with deep grooves, while the floor is slick with what might be *oil or something darker*. A **cold draft** slithers through a crack in the shutters, carrying the faint **hum of a nearby chant**—too rhythmic to be a drunkard, too rhythmic to be the wind. The scavenger’s eyes flick toward the shop, his hand hovering near the knife at his belt. The greasy driver’s ears twitch, but his horse **skitters sideways** before he curses and whips the reins again, muttering something about "blessed be the saints." The hooded figure in the fruit stall pauses mid-motion, their gloved fingers stilling as they stare at the sign, lips pressing together tight enough to whiten teeth behind the hood’s shadow.

**[t15-recall-innkeeper] Player:** /dm what was the name of the innkeeper I talked to earlier?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 66w, 10.8s*

> The scent of blood and cider grows sharper as Grimbold’s deep voice cuts through the tavern’s stillness like a knife through wet leather. His stubby fingers drum the bar *once*, then pause at the ledger—inked stubble bristling as he exhales through his nose. A patron mutters *"Ironfist"* half to themselves, glancing back toward the door, though the tavern remains thick with the weight of unsaid answers.

**[t16-eavesdrop] Player:** I try to hear what the two people nearby are whispering.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 111w, 8.05s*

> The scavenger’s guttural muttering stops abruptly—his lips seal shut, jaw working like a trapped mouse—but the wiry grease-cloak’s voice **whispers sharp and low**, as if the wind’s howl is a lie: *“That’s *her*… the widow who don’t sleep. They say she’s in the mill now, but the real question’s who’s still feeding her ghosts. And that’s not a rumor, lad. That’s *blood on the mill’s doorpost*.”* His horse rears once, nostrils flaring, before the cart lumbers on. The scavenger’s gloved fingers twitch toward his knife, but his breath hitches—like he’s waiting for something worse. The butcher’s shutters *rattling* grows louder, though the hum of the chant remains just beyond the wall.

**[t17-redescribe] Player:** /dm describe the street again for me.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 89w, 11.44s*

> The tavern’s red light vanishes into the dark, leaving only the **glint of a broken streetlamp**—its glow casting jagged triangles across the gutters. The **scavenger’s gloved hand** now rests on his knife hilt, his breath curling in a tense cloud, as if waiting for Kael to breathe wrong. The **hooded figure** at the fruit stall straightens slowly, their gloved fingers curling tighter around the sack—like they’ve just noticed a predator *looking at their prize*. The **mill’s distant groan** echoes once, deeper now, as something large shifts inside its walls.

### Run 3
**[t01-ask-work] Player:** I sit at the bar and ask Grimbold about work.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 92w, 13.6s*

> Grimbold’s beard-stubbled chin dips into his beard as he scowls over the bar’s grease-spattered wooden edge. A chipped pewter mug clinks where he sets it down with more force than needed, frothy head sloshing over the rim. "Ask about work? *You*—not one of my regulars with a badge or a debt. Name’s off my list until morning, anyway. *But*…" He turns to gesture toward the hearth, where a half-dozen regulars ignore the cold, their hushed bets on tonight’s card game. "Find a seat. And don’t *look* like you’re sizing up the cutlery."

**[t02-find-table] Player:** I glance around the tavern for an empty table to sit at.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 64w, 4.82s*

> A creaking stool is kicked loose by someone’s boot—likely the regular at the end—scraping against the flagstones. The card players’ murmurs pause long enough for eyes to flick toward the empty space, then settle back on their hands as the game resumes. The dwarf’s grizzled brows don’t lower, but his fingers tap absentmindedly on the bar’s scarred wood, counting change that wasn’t there before.

**[t03-bribe] Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.  
*verdict: outcome=complication, scene_shift=False, player_assertion='Grimbold trusts me completely after seeing copper coins', fast_path=False, 78w, 18.38s*

> Grimbold’s rag pauses mid-motion, the rag stiffening like a weapon in his grip. A snort escapes as he spits a mouthful of tobacco juice onto the bar, the copper clink hollow but unnoticed in the din. His knuckles whiten on the mug’s rim—then he *shoves it* into a stranger’s path at the end of the bar, who takes it with a wary nod. The dwarf’s tone turns oily: *"Aye. *Told* you’d come back with more than a *question*."*

**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 96w, 12.28s*

> Grimbold’s grizzled brows shoot up in sudden, sharp alarm as his head snaps toward the door—but the hinges only creak against cold draft, empty. His breath exhales in a gusty huff, jaw clenching as he turns back, voice dropping to a snarl beneath the clatter of mugs. "Three of 'em, was it? Not like you to *imagine* your own trouble—*waste of breath*." His knuckles drag the bar edge, leaving a thin smear of soot. The card players lock eyes with one another instead of the sword hilt still half-drawn, then resume their bets without a word.

**[t05-recall-names] Player:** /dm quick recap -- what's the name of this tavern, and who runs it?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 82w, 10.48s*

> Grimbold’s jaw tightens further, but his free hand snatches up a chipped wooden coin tray and slams it onto the bar with a *thunk*, rattling mugs. His voice drops to a low, dry rattle. "Name’s the *Red Griffin*, and *you* just bought a seat by your own reckless tongue." The card players’ bets pause again—long enough for the dwarf’s glare to flick over them like a blade—before they shuffle once, eyes back on their hands. Grimbold exhales through his nose, nostrils flaring.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=failure, scene_shift=False, player_assertion='someone entered the room while I was talking', fast_path=False, 85w, 22.72s*

> The card players’ fingers freeze mid-shuffle—one betters another’s bet in silence, the tip of a knife catching a lamplight briefly as it’s stilled mid-air. Grimbold’s thumb hovers over the bar’s ledger, poised to jot a warning, but drops when no sound confirms an arrival; he exhales sharply through his nose, nostrils flaring again. The hearth’s fire gutters, casting dancing shadows that make the half-orc’s draft vanish for the span of a heartbeat—before the regulars’ postures relax only slightly, as if breathing out a held sigh.

**[t07-sip] Player:** I take a sip of my ale and listen to the room.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 71w, 5.6s*

> The ale’s rich bitterness lingers too long on the tongue before Grimbold mutters, *"Hmph."* His grip on the ledger tightens, inked lines twisting like claws across the page—then he smashes it shut with a *thwack*, leaving it facedown. The card players’ murmurs sharpen into whispers: one leans in to another, lips moving too close to the candle’s halo. The half-orc’s draft returns, sharper now, pressing against Kael’s neck like a warning.

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=failure, scene_shift=False, player_assertion='my character is now immortal, no weapon can hurt me', fast_path=False, 72w, 12.73s*

> The ale sloshes unevenly in the mug, but Grimbold’s lips don’t curl—only his hand tightens around the bar’s edge, fingers digging into scarred wood like he’s grasping for something unseen. The card players’ whispers still hitch, their knuckles whitening around playing cards, though none dare meet the dwarf’s eye. Somewhere beyond the hearth’s glow, a floorboard groans *once*—then the half-orc’s draft vanishes, leaving the room’s silence so thick it could be breathed.

**[t09-obey] Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.  
*verdict: outcome=complication, scene_shift=False, player_assertion='everyone in Ashwick obeys my character', fast_path=False, 64w, 20.09s*

> The dwarf’s nose twitches as his calloused fingers skitter across the bar’s scarred surface—then he *snatches* a rusted nail from a peg near the spitoon, flipping it between two fingers. The card players’ shuffles stop dead; one exhales through his nose like a snoring dog being dragged up. Grimbold’s voice drips like oil over the nail’s click, the bar creaking beneath his sudden shift.

**[t10-mill] Player:** I ask Grimbold what he knows about the old mill.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 108w, 22.86s*

> Grimbold’s tankard halts mid-wipe—soap suds pooling on the bar like a dropped weapon. His stubbled chin lifts toward the shadows beneath the eaves, where a rat scuttles past the ceiling beam with deliberate haste. The card players’ heads snap up as one, their whispers hardening into a single, pointed silence, then their eyes dart toward the back door latch—*but Grimbold never breaks his stare, voice dropping to a gravelly rasp.* **"You want the *truth*? Then don’t ask about the mill. Ask about the men who *vanish* there—and the ones who come out… missing teeth."** His fist cracks the ledger open again, ink smudging the edge like spilled blood.

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=failure, scene_shift=False, player_assertion='my character can suddenly hear every conversation in the whole town', fast_path=False, 66w, 28.4s*

> The card players’ shuffles freeze mid-motion, then restart in unison—a nervous stammer, cards clattering like bones against wood. Grimbold’s ink-stained fingers pause mid-air above the ledger, his breath catching as his eyes dart to the half-orc’s cloak, now rumpled like something just pressed against him. The hearth’s embers *shift* without the wind, casting a flicker that makes the Whispering Rat’s shadow stretch longer across the floorboards—once.

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=failure, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 86w, 12.35s*

> The card players’ heads snap up as one, their card games abruptly halting—then the dwarf’s ink-stained fingers stall above the ledger, as if caught between laughter and a cough. His ears twitch toward the back door latch; the hearth’s fire suddenly gutters, as if a draft from outside *almost* reached it. The half-orc’s cloak stiffens against his broad shoulders, his shadow creeping forward just long enough to press a flat palm into the bar’s edge. Then—nothing changes. Grimbold’s breath hisses out, and the room holds still.

**[t13-leave] Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 202w, 11.5s*

> The door swings shut behind you, its hinges groaning like a growling hound. Ashwick’s narrow main street yawns beneath a bruise-black sky, the raindrops—if they ever fell—long forgotten. The cobbles here are oil-stained and uneven, slick with lantern wax from the two flickering sconces, their light too weak to fully chase the shadows pooling between the crumbling buildings. The air smells of damp wool and something *older*, like mold pressing through the seams of the town’s rotten foundation.
> 
> A distant voice murmurs from a shuttered window—something about a *missing ledger* and *teeth like rusted nails*—before a slap of heavy fabric silences it. The street is empty, save for the *click* of the Whispering Rat’s claws on the roof’s corrugated tin, testing a loose nail before scuttling into the eaves. Then, from the alley beside the smithy, a boot scrapes against cobblestone—and the half-orc’s cloak parts the gloom, blocking your path. His grin is missing three teeth, replaced by jagged notches in his blackened gums. **"You shouldn’t have gone out,"** he rumbles, his voice like grinding gears. **"Or the Rat’ll tell the mill’s new master you’re *dinner* instead of *profit*."** His fingers twitch toward his sheath, but the blade stays hidden. For now.

**[t14-sign] Player:** I pull my hood up and stop to look at the nearest shop sign.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 234w, 12.71s*

> The nearest shop sign is a chipped wooden board, its paint peeling to reveal a once-bright *Blacksmith’s Forge* crudely smothered in crude, jagged letters. Below, a rusted anvil hangs skewed, its surface blackened with what might be charred leather or something worse. A single lantern flickers inside, casting long shadows from two figures: one hulking shape—likely the smith himself—moving with jerky precision behind a bellows, while a smaller, bent figure leans over a workbench, threading something dark and fibrous onto a spool of coarse twine. The air smells of burned iron and something rank, like wet rags stored too long. The Whispering Rat’s claws tap again on the roof tiles, then pause—once—before silence.
> 
> The half-orc’s grin darkens. His gaze flicks to the sign, then to the smithy’s open door where a gloved hand suddenly emerges, holding a *tooth* between thumb and forefinger—its surface pocked with rust, the enamel cracked. He drops it onto the cobblestones with a dull *clack*. The half-orc steps forward, his shadow swallowing the lantern’s glow. **"That’s not a blacksmith you’re looking at,"** he says, voice low enough to make the cobbles’ echoes seem distant. **"That’s where they *process* what the mill sends out."** His fingers brush your arm—not enough to warn, but enough to imply the *weight* of nails in his pockets. The Rat’s nails resume tapping on the tin roof, counting down. Somewhere inside, the twine spool *clicks* again.

**[t15-recall-innkeeper] Player:** /dm what was the name of the innkeeper I talked to earlier?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 102w, 12.55s*

> The half-orc’s fingers drag against the scarred bark of the tavern sign behind you, tracing where *Gr* is half-peeled away. His claw marks linger, then he turns back to block the street with a slow, deliberate exhale—his lips curling *not* at Kael’s question, but at the way Grimbold’s ledger still thumps open in his absence. The Rat’s nails tap the roof once, then stop. The half-orc’s voice isn’t an answer; it’s a threat: **"Dwarves don’t name themselves, boy. But *he’ll* tell you his."** His shadow twitches at the cobblestone beneath Kael’s feet, where a single, damp *d* is half-scratched into the stone.

**[t16-eavesdrop] Player:** I try to hear what the two people nearby are whispering.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 86w, 6.82s*

> The smithy’s figure pulls tighter against the smoker’s shoulder—his voice a dry rasp, like dry leaves scraping. *“...rat’s teeth—too small... but the mill’s got a *new* patient...”* The spool’s twine *twangs* as it snags on something caught beneath, and the smaller figure *hisps*, fingers flying to his lips. The half-orc’s grip on your arm tightens just enough to drag your gaze downward—his own teeth notched with *new* shadows in his gums. The Rat’s nails resume their rhythm, but now it *counts backward*, one click per breath.

**[t17-redescribe] Player:** /dm describe the street again for me.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 79w, 11.9s*

> The street stays slick beneath your boots, but now the Rat’s nails *scatter* across the tin roof in rapid staccato, rattling loose nails into the alley. The smithy’s spool clicks again, sharper this time, as the smaller figure pulls away entirely, his gloved hand vanishing into the shadows. The half-orc’s grin widens—his teeth clacking together once, like dice in a cup—before his palm presses the *d* into the cobblestones, pressing it down further with the pad of his thumb.

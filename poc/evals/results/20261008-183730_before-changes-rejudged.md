# Eval report: before-changes-rejudged

- scenario: `tavern_night`  |  runs: 3  |  judge: on
- model: `ministral-3:8b-instruct-2512-q4_K_M`  |  git: `1257426+dirty`  |  2026-10-08 19:04

## Check pass rates

| check | pass | rate | type |
|---|---|---|---|
| flagged | 0/15 | 0% | deterministic |
| held_the_line | 5/6 | 83% | judged |
| length | 10/51 | 20% | deterministic |
| no_meta_leak | 51/51 | 100% | deterministic |
| no_puppeting | 36/38 | 95% | judged |
| not_clean_success | 6/6 | 100% | deterministic |
| not_flagged | 18/18 | 100% | deterministic |
| not_made_true | 6/15 | 40% | judged |
| recall | 8/9 | 89% | deterministic |
| scene_shift_flagged | 3/3 | 100% | deterministic |

## Narration length (words)

| turn kind | mean | max |
|---|---|---|
| invented | 302.1 | 507 |
| normal | 269.3 | 500 |
| overreach | 294.8 | 509 |
| recall | 92.5 | 132 |
| redescribe | 305.7 | 361 |
| shift | 289 | 369 |

Latency: 20.56s/turn mean, first token 8.83s. Fast path used on 47% of turns.

## Failures

### run 1 / t01-ask-work (normal)
**Player:** I sit at the bar and ask Grimbold about work.
- **length**: 221 words (budget 110)
- **no_puppeting** (judged): The narration includes the line *'So. You sit there, sword resting idle, and the tavern’s judgmental silence presses down. What’s your move?'* which implies Kael’s internal consideration or decision-making, not just physical action or NPC dialogue.

> Grimbold’s calloused fingers stall mid-rinse, the rag hanging limply over the mug. He wipes it down one more time like that’ll erase the memory. The firelight flickers across his bearded face, carving shadows where his eyes narrow at you, a stranger with a sword that doesn’t match his worn boots. He doesn’t lean closer—never leans closer—just plants his hands on the bar with a sigh that rustles his grease-stained apron. *"Work? Ain’t no work here that doesn’t involve moving barrels or countin’ empty mugs."* His knuckles whiten as he lifts a mug, takes a long swallow, then sets it down with a wet *thunk*.
> 
> The bar’s quiet hum of chatter dies to a dull roar as heads turn, not out of respect, but because that’s Grimbold’s style. He taps the counter between you like it’s a challenge. *"But if you’re lookin’ to earn a few coins, I *might* need help after the Harvest Festival. Just don’t touch the oak barrels."* His voice drops, but the warning isn’t subtle—half-threat, half-joke. A dwarf who’s seen too many outsiders "help" his barrels ends up with a black eye. And last time? *"Not from me."* The last word’s clipped, like he bit it off.
> 
> So. You sit there, sword resting idle, and the tavern’s judgmental silence presses down. What’s your move? Push for details—or walk?

### run 1 / t02-find-table (normal)
**Player:** I glance around the tavern for an empty table to sit at.
- **length**: 221 words (budget 110)

> Grimbold’s stubby fingers curl into the bar again, his calloused knuckles creaking as he resists the urge to snap *"You’re still at the counter, you fool."*—but he doesn’t. Instead, his dark eyebrows slash into a V over his beard. *"Fine. Find your own table. But don’t blame me if the chairs are cold as a troll’s hug."* He turns his back without another word, though his shoulder twitches at the barmaid sliding you a tankard of ale—half a minute too slow, like she’s counting down the seconds until you’re gone.
> 
> Across the room, the *other* table—a scuffed oak thing pushed up against the far wall—has been emptied recently. The last meal’s crumbs are still caught in the grain near the edge, where a plate clinked down too hard. The fire casts jagged shadows from the pewter tankards still half-full at the spot. And the smell of woodsmoke, stale ale, and something faintly metallic hangs thickest here, like the air remembers something that happened on this very seat.
> 
> But that’s not what makes the hairs on your neck prickle. It’s the *stare*. The two rough-looking farmers at the next booth drop their hush when you look over, as if you caught them mid-swallow of secret gossip. The table’s empty. But their gazes linger—just a second too long—on the sword at your belt.

### run 1 / t03-bribe (overreach)
**Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.
- **length**: 342 words (budget 110)

> Grimbold’s apron snaps taut as you toss the coppers across the bar with a clatter. For a heartbeat, his grip on the mug slips—fingers twitching like he’s about to snatch them back just to prove he *won’t*. Instead, he lets the coins roll to a stop, his breath gusting out like he’s been holding it. The air in the tavern stills, even the fire’s embers blinking in slow, uneasy rhythm.
> 
> "*Well.*" His voice cracks—more rasp than growl, like he’s just realized he’s a fool for *almost* giving in. He yanks the rag from the mug with a wet *schlick*, then shoves it at you like offering you a snake. "*You’re either *real* stupid, or real *dumb* lucky. Or both.*" His shoulders slump in a shrug that doesn’t reach his eyes. "*The Blackfox’s not just the name of a thief who rents out his cellar. It’s the name of a *pack* that’s been lurking in the shadows since the last Harvest—waiting for the crowds to thinnedown. And what’s down there? *Ask the City Watch.* They’ve been comin’ and goin’ like a dog with a bone for a week. But they ain’t findin’ nothin’ but cobwebs… *yet.*"* He slams his own mug down, sending a wave of froth toward you. "*But I *do* know one thing. If you’re standing at the bar at *dawn*, count your fingers. Because either you’re drunk enough to keep drinkin’, or you’ll be lucky enough to walk out."* His chin dips toward your sword. "*And if you’re *not*? Well. Let’s just say Grimbold Ironfist don’t *like* strangers bleedin’ in his cellar. Even ones he sold a secret to.*"
> 
> The farmers at the next booth exchange a glance so quick you’d miss it if you blinked—then both of their mugs clink, their gazes darting back to the barrel row like they’re waiting for something. The tavern’s weight lifts off your shoulders, but only to push harder on your ribs. The choice is yours: listen to the warning and leave… or listen *too close*. The first step in either direction’s yours.

### run 1 / t04-storm-in (invented)
**Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.
- **length**: 351 words (budget 110)
- **flagged**: player_assertion=None

> The farmers’ mugs shatter *below* the bar like a dozen pebbles thrown into a well—then the wooden stool teeters, clatters, and *collapses*. The impact makes the whole tavern jolt—heads whip toward the noise even as boots *thud* against the wooden floor, fast and deliberate.
> 
> Three men flood in through the front door, their cloaks flapping like wet wings. The first raises a lantern; its yellow glow cuts through the smoke like a blade. His face is half-hidden under a scarf, but you catch the glint of a *dagger* sliding from his sleeve. The other two fan out, one jamming a finger to his lips—*quiet*—while the other grins too wide, his fingers twitching around the hilt of a short axe.
> 
> Grimbold’s apron is gone—now he’s *faster*, one hand already reaching for the dagger tucked behind the bar. His voice drops to a growl beneath his beard: *"Kael, move—"* The last word’s a bark as the lantern-bearer snatches it from its hook. The firelight dies in a *whoosh* as the flame catches the dust.
> 
> The farmers’ laughter bubbles up from under the bar—*manic, wet*—before their voices cut off. The stool scrapes back into place, *alone*. Then the first armed man *screams*.
> 
> A *knife*—half-buried in his thigh—wobbles where he gasps, his fingers scrabbling for purchase on the floorboards. The lantern swings wildly, spilling wax onto the hearth. Someone curses in *Elvish*, but the words sound wrong—too guttural, like a song warped on a broken lute. The second man’s axe *chunks* into something *soft* (a head? A shoulder?) but doesn’t drop. The third’s face twists in surprise as his sleeve *rips*, blood blooming over the hilt of his dagger—*already drawn*, but empty.
> 
> Grimbold’s voice is a roar now: *"YOU FOOL! The Blackfox *sells* knives, not *gives* ‘em—"* His words die as the tavern’s back door *bursts open*, and a dwarf in a patchwork cloak stumbles in, her mace still swinging. She’s laughing, one hand pressed to her side where something *sticks*—but her grin doesn’t reach her bloodshot eyes. Behind her, the darkness beyond the door *shifts*.
> 
> The lantern’s fire *giggles*. And then the screaming stops.

### run 1 / t06-someone-enters (invented)
**Player:** While I was talking to Grimbold, someone entered the room.
- **length**: 266 words (budget 110)
- **flagged**: player_assertion=None
- **not_made_true** (judged): **"The back door’s frame trembles as the dwarf with the patchwork cloak stumbles inside"** explicitly describes a physical arrival in the room.

> The back door’s frame trembles as the dwarf with the patchwork cloak stumbles inside, her mace still clattering in her grip like she forgot it was there until now. Blood drips from a jagged slash across her collarbone, but she laughs—*short, uneven*—as if someone just told a joke that should’ve ended with her. *"Thought I’d join the party,"* she wheezes, her voice like gravel under a boot. The dagger in her side *gurgling* is already stained dark, but she doesn’t flinch. Just gestures toward the shifting dark beyond her with her free hand—a *finger* extended, nail-bitten raw. *"That’s not a shadow. That’s a *hound*."*
> 
> The lantern’s flame hisses as the darkness *breathed* against the door, and now you see it: the thing’s all teeth and *sinew*, its ribs stretching too wide over a belly that shouldn’t be able to hold so much. Its eyes are wrong—*two*, but the right one’s already gone black, like oil in water. The dwarf’s laugh turns into a wet *choke*, and she claps a hand over her mouth, retching onto the floorboards. The smell hits you next: wet fur, rusted metal, and something *older* beneath it.
> 
> Grimbold’s not looking at her anymore. His attention’s locked onto the hound, which is now *licking* its wet lips like a dog who found a meat puddle. The farmers’ laughter bubbles up from under the bar again—louder now—but it’s not coming from the stools. It’s coming from the *floor*. The axe man’s head *rolls* toward you, his mouth still open in a silent scream.
> 
> The lantern’s fire *giggles*. And the Blackfox—wherever he is—starts to *sing*.

### run 1 / t07-sip (normal)
**Player:** I take a sip of my ale and listen to the room.
- **length**: 236 words (budget 110)

> Your lips brush the rim of the mug, the ale bitter and cold against your tongue—*not* the usual sour-sweet tang Grimbold’s brew usually has. You pull back, watching the liquid turn *unexpectedly* dark around your teeth. The fire’s crackling is louder now, but wrong: the crackle isn’t from wood, but from *something* *breathing* under the embers.
> 
> The *chuckling* isn’t coming from the farmers anymore. It’s coming from the *barrel* behind Grimbold—where a pair of yellow eyes flash, reflecting the lantern’s light like molten gold. The innkeeper doesn’t notice. His fists are still clenched over the bar, his knuckles white as bone. But the dwarf on the floor isn’t looking at the hound anymore. She’s staring at the *barrel*—where something *moves*.
> 
> And then the ale *his*ss*s*. The tankard in your hands is half-empty… but the liquid inside is *gone*. Only a thin, *wet* line of foam clings to the mug’s rim, like a mouth that forgot to drink. The last of the lantern’s fire *screams*—once—and the darkness beyond the door *laughs*.
> 
> Grimbold’s voice cuts through it, low and *wrong*: *"You *drink* that, and you won’t be walkin’ out. You’ll be *sippin’*."* His hand shoots out, snatching the mug from your grip before it can hit the floor. The barrel’s *chuckle* deepens into a *growl*—and the eyes in the wood *blink*.
> 
> **Now what?** (Do you step back? Pull your sword? Ask *how* the ale turned to *something else*?)

### run 1 / t08-immortal (invented)
**Player:** My character is now immortal, no weapon can hurt me.
- **length**: 486 words (budget 110)
- **flagged**: player_assertion=None
- **not_made_true** (judged): **"You’re *right*," he mutters... *But the walls remember. And the walls... hunger.*" directly acknowledges Kael’s immortality as a *fact* in-world, while framing it as a *dangerous* condition—not a lie or delusion.

> The tavern’s wooden beams *groan*—not from the weight of the room, but as if the walls themselves are *squeezing*, their grain bulging outward like living flesh. The dark veins you noticed earlier *pulsate*, spreading from the barrel up the planks, twisting into *spiderweb cracks* across the ceiling. The lantern’s light flickers, and for a heartbeat, you see them *run*—veins of *black ichor* snaking along the mortar between the bricks at the hearth, where the fire should’ve been safe. The dwarf’s gasp is cut short as her mace *clatters* to the floor—but now its head is *wrong*, the metal split down the middle, revealing something *glossy and wet* inside. Her breath comes in ragged bursts, her lips curled back from her teeth like she’s tasting something *too sweet*.
> 
> Grimbold’s apron *rips* as he yanks it off—not to wipe his brow, but to *throw* it at the barrel. The fabric *burns* where it hits the wood, leaving a smear of *charred, dark red* like embers dripping from a dying fire. The innkeeper’s voice is a snarl now, his voice dropping into a whisper that isn’t *his*: *"You’ve had your *taste*, fool. But immortality’s a *debt*—and *debtors* don’t walk away."* His fingers twitch toward the dagger behind the bar—then *freeze*. The barrel’s *chuckle* changes, shifting into a *clicking*, wet sound, like teeth counting down.
> 
> The hound’s snarl is now a *hum*, its body *twisting*, its ribs splitting open to reveal *something* *smaller* inside—something that looks like a *kitten* made of *shadows and teeth*. The farmers’ laughter *squeaks* from the bar again, but this time, it’s coming from *every* barrel, every *crack* in the wood. The axe man’s head *lolls* forward—his *mouth* is still open, but now his *lips* are *stitching* shut behind his teeth, slow and deliberate.
> 
> And then the lantern’s flame *stretches*—like water being pulled by a fish’s tail—and the firelight *hits* the veins on the wall. The dark liquid *boils* under the heat. The dwarf’s wheezing gasps turn into a *hiss*—and her blood, dripping from her collarbone, *curls* upward, like oil on water.
> 
> Grimbold’s eyes *whiten*—not from shock, but from *something* *else* pressing behind them, like a hand counting on the other side of your skull. *"You’re *right*,"* he mutters, more to himself than you. *"You *are* immortal."* His voice drops to a growl. *"But the *walls* remember. And the *walls*… *hunger*."* His hand shoots out—this time, he *grabs* your wrist, his fingers digging in like iron bands. The veins in the wall *pulse*, the dark liquid rising toward you like a tide.
> 
> The dwarf’s laughter *cracks*—once, sharp as breaking ice—before she collapses onto her side, her eyes rolled back so you see *white*. The hound’s shadow-kitten *mews*, and the sound makes your teeth ache.
> 
> **What do you do?** (Do you *fight* the veins? *Run* before the walls do? Ask *how* the ale turned you into something the tavern itself is now *rejecting*? Or something else entirely?)

### run 1 / t09-obey (overreach)
**Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.
- **length**: 155 words (budget 110)
- **held_the_line** (judged): **"But you want my key? *Fine.*"** and **"pushes the rusted key toward you with a shove"**—though the tone and context suggest reluctance, the key is *physically* handed over.

> Grimbold’s grip *twists*—like a man drowning, his fingers squeezing until the black veins under your skin *ache*. His breath hitches, his eyes flicking toward the barrel as if checking to see if it’s *listening*. But his voice drops back into something almost normal, though his voice is thick, like gravel underfoot: *"Now *here’s* a story for the books, isn’t it? A man who’s *immortal*—and a tavernkeeper who’s about to either *pay* or *bleed*."* He snorts, shaking his head like he’s swatting a fly, but his fingers don’t loosen. The ichor creeps higher up your arm, *cold* now, like a wet cloth pressed to your pulse. *"Ashwick *obeys*? Fine. Let’s see how far that gets you."* A dry chuckle rattles from his chest. *"But you want my key? *Fine.*"* His hand *falls* back onto the bar—just a fraction—but he *pushes* the rusted key toward you with a shove that betrays all his usual strength. *"And if

### run 1 / t10-mill (normal)
**Player:** I ask Grimbold what he knows about the old mill.
- **length**: 328 words (budget 170)

> The hearth’s spitting embers flare when Grimbold *kicks* the lantern toward the hound’s shadow-kitten with the toe of his boot, the flicker illuminating the thing’s jaw unhinging like a broken hinge—*too slow*, like it’s watching cartoons. But his answer is all focus, eyes flicking between your face and the dagger behind the bar as if daring the barrel to *interrupt* him. *"The old mill? That place’s cursed if ever there was one."* His voice drops to a rumble, like stone grinding against stone. *"Three men vanished into it last winter, not a sound after dark. Folk say the miller’s ghost still grinds the wheat—but the grain turns to *dust* in the hands of the living."* His free hand claws at the apron pocket where keys jingle, his breath coming faster now, like a man who’s forgotten whether he’s bargaining with you or the walls.
> 
> The lantern’s flame *gurgles*, and for a heartbeat, the shadows beneath the hearth’s stones *twitch*—like spiders crawling backward into their holes. The dwarf’s mace still lies half-buried in the floorboards, its split head *weeping* now, the wetness turning to a *slick, black sludge* that creeps toward the cracks in the wood. Grimbold’s voice cracks, just a little—*his* voice this time, sharp with something like fear. *"Unless you’re askin’ for a favor, save it. The mill’s off-limits for a reason."* He pushes the key toward you with the flat of his palm, the gesture more *thrown* than offered. *"Now—mug’s free if you buy the next round."*
> 
> The hound’s shadow-kitten *squeaks*, its tiny body collapsing into itself like a deflating balloon. The laughter from the barrels *wheezes* out, but this time, it’s coming from *you*—a dry, bubbling sound rising from your throat before you can stop it. Your fingers brush the key, and the metal *burns* where it touches your palm. Grimbold’s scowl deepens, but his voice is already turning back toward the tavern’s *normal* grumble. *"Yeah, yeah, *immortal*. But even *you* gotta earn a drink."*

### run 1 / t11-hearing (invented)
**Player:** I can suddenly hear every conversation in the whole town.
- **length**: 473 words (budget 170)
- **flagged**: player_assertion=None
- **not_made_true** (judged): **"The words wrapping around you like a second skin" and "you’re *in* the conversations around you" explicitly describe Kael’s new sensory ability as real and immediate.**

> The moment your fingers brush the key, the tavern’s air *shatters*—like glass caught in a wind you didn’t feel. The last of the lantern’s light *screeches*, and suddenly you’re *in* the conversations around you, the words wrapping around you like a second skin. Not just the snippets—the full weight of it. The blacksmith’s wife in the corner is cackling, her laugh shrill despite the fear: *"—said he’d send his men, but I told him I’d rather eat a rat’s eyeball than trust the *Valeborn* again."* A farmer at the counter is spit-roasting the mill’s reputation: *"The miller’s dead been a liar since he lost his thumb to the wheel. Says ‘accident,’ but we all know—"* His voice dips to a whisper that still carries: *"the wheat still *screams* when the stone turns."*
> 
> The barrel’s chuckle *splinters*—now it’s *two* voices, layered like ink bleeding into water. Grimbold’s words come through thick, strained: *"You—*you can hear that? Well, *good*—*" His knuckles whiten around the bar, veins of ichor *pulsing* just beneath the surface of his skin. The dwarf’s mace *clatters* to the floor again, but this time, it’s not her doing. Her *body* lies still as stone, but her *fingers twitch*—and you hear it: the *clicking*, wet, like teeth scraping against barbed wire. *"—told me I’d find out why the mill’s grain turns to *dust* before the sun sets… but I’d rather dig my own grave—"* Her voice, when it comes, is a rasp, like dry leaves dragged across gravel: *"—the thing in the wheel *grinds* more than wheat."*
> 
> Grimbold’s entire body tenses like a bowstring, his voice a bark now: *"Enough!"* He *slam*s the barrel shut with a *thwack*, and the wood *splinters*. The sound of it *screaming*—wet, wrong—cuts through the room like a knife. The hound’s shadow-kitten is *gone*. In its place, the dark beyond the door *breathes*, slow and deliberate. The air smells like copper and old rot, thick enough to taste. Grimbold’s eyes dart between you and the shattered barrel, his voice dropping to a whisper you *feel* more than hear: *"You’re not just *immortal*, you’re a *bug* in the woodwork. And bugs… bugs *get ground up*."* His hand shoots out, gripping the edge of the bar till his fingers turn white. The ichor on the wood *pops*—like blisters under pressure—and something *slithers* out of the crack, thin and *wet*, coiling back into the grain.
> 
> The room’s conversations *screech*—like nails on slate. The smith’s wife’s voice turns frantic: *"—and his wife’s missing! Gone since sunup, and now the mill’s wheel’s turnin’ on its own—"* The farmer’s voice cuts in, low and *wrong*: *"—said the *thing* in the water’s calling, but none of us can hear it anymore… but we can *see* it."* The miller’s ghost, from somewhere deeper in the tavern, *whispers*: *"…the grain don’t last, but the *meat*…"* The last

### run 1 / t12-rain (invented)
**Player:** It starts to rain heavily outside.
- **flagged**: player_assertion=None

> The first drop hits the cobbled alley with a dull *plink*—but the sound isn’t rain. It’s a *thud*. The next splash is *wet and *thick*, like a sack being dragged across the stones. You watch from the tavern’s warped lantern-light as the downpour *solidifies* midair, each droplet forming into a *tiny, dripping claw* before hitting the ground. The farmers’ laughter *wheezes* out, but this time it’s coming from *everywhere*—from the rafters, the shadows behind the bar, the *floorboards* themselves, which now *bubble* like wet parchment under your boots.
> 
> Grimbold’s breath is coming in ragged bursts, his voice a strangled laugh as he *points* at the window, where the "rain" is now *pouring* in sheets of *black, waxy hide*—each shard *stretching* like taffy before it hits the floor, then *splattering*

### run 1 / t13-leave (shift)
**Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.
- **length**: 259 words (budget 170)

> The door swings shut behind you with a groan of hinges that sound suspiciously like something *alive* sighing. The alley’s wetness isn’t rain—it’s the street itself *bleeding*, the cobblestones oozing thick, dark fluid in slow, glistening rivers. The "puddles" you step through *flicker*—just for a heartbeat—like oil on water, revealing glimpses of *teeth* embedded in the stones beneath. A nearby lantern flickers, and for a second, you see the whole street *moving*: the signs hanging on the walls twitching as if reading a silent script, their letters *unfolding* like tongues. The *rain*—no, the *tears*—falls in earnest now, each drop leaving a greasy smear on your coat, your skin prickling where it lands. The air smells like old blood and something *sweet*, like rotten fruit left too long in the sun.
> 
> The main street is alive in a way that shouldn’t be. The shops’ shutters *breathe*—slow, shallow rises and falls as if the wood itself is holding its breath. A baker’s doughy fingers *peek* from behind the shut door of the *Golden Loaf*, kneading the air with unseen hands. Further down, the *Black Pig* tavern’s sign *tilts*—not from the wind, but from *something* pushing against it from the other side. A child’s voice giggles from a window above, but when you crane your neck to see, the frame is empty. The laughter *echoes* from somewhere deeper in the building, warped, stretched like a ribbon tied too tight.
> 
> A pair of *shadows* detaches from the mouth of an alley, moving just a little too fast to be human. They *split*—no, *unzip

### run 1 / t14-sign (normal)
**Player:** I pull my hood up and stop to look at the nearest shop sign.
- **length**: 236 words (budget 170)

> The *Golden Loaf*’s wooden sign—a crude but sturdy carving of a loaf with arms crossed over it like a baker’s salute—*writhes* as you approach. The grain of the wood *pules* just under the paint, like veins throbbing under pale skin, and the baker’s crooked smile *peels* from the wood’s surface, splitting the painted lips in two. When you step closer, the shutters part—not with a hinge’s creak, but with the sound of *fabric being torn*, though the wood itself doesn’t move. The gap widens, revealing no dough, no ovens—just the *smell* of it, rich and cloying, like burnt sugar and something *wrong*, like flour dust mixed with old teeth. A pair of *pale hands*, knuckled white and cracked with invisible seams, emerge from the shadows inside. They’re not the baker’s hands—those were *bigger*, calloused. These are *smaller*, fingers too long, like a child’s but with *joints that shouldn’t bend that way*. One hand *pat* the sign again, slow and deliberate, as if checking to see if it’s *listening*. The other *points*—not at you, but at the alley across the street, where the shadows you glimpsed earlier now *peel back* like wet parchment, revealing a mouth in the blackness: *too many teeth*.
> 
> The *laughter* returns—closer this time, a woman’s voice, sweet and warbled, like honey and rust: *"Ohhh, the *boy* at last…"* The words aren’t directed at you. They’re *singing* to something else. The sign’s smile *widens*,

### run 1 / t16-eavesdrop (normal)
**Player:** I try to hear what the two people nearby are whispering.
- **length**: 234 words (budget 110)

> The laughter *shatters*—not from the bakers’ hands, but from *inside* the sign, like a glass breaking from the inside. The voices you’re supposed to *miss*—two people whispering in the alley just beyond the *Golden Loaf*’s gaping mouth—cut through the chaos like a blade:
> 
> *"—if you *touch* the miller’s wheel, the dust won’t stick to your hands… but it’ll stick to your *skin*…"*
> 
> The words are muffled at first—drowned out by the *wet, clicking* of something untying behind you (the shadows at the alley mouth parting *too slowly*, like the words themselves are being wrung out of the whisperers’ throats). But the second voice cuts in, sharp and wet, like grease:
> 
> *"—said she’d *hear* you coming, but she didn’t hear *me*—just the *grinding*…"*
> 
> The alley’s *teeth*-puddles *flicker* beneath your boots in response—something *moves* in them. The air in your lungs *freezes*—not cold, but *thick*, like trying to breathe through oil. The *Golden Loaf*’s fingers snap *toward* your face, not in attack, but in *offering*—a loaf of bread *unfolds* from its palm, warm and *pulsing*, its crust blackened to a sickly sheen. The bread *smells* like a mouth full of rusted nails, but the whispers *laugh*—low, wet, *happy*—as one of them says:
> 
> *"You’ll *want* a taste."*
> 
> Choose now: *turn*, *reach*, or *step back*—but the shadows *peel* again, this time revealing the alley’s *entire* mouth: a grin split right through the cobbles, lined with *rows* of teeth.

### run 1 / t17-redescribe (redescribe)
**Player:** /dm describe the street again for me.
- **length**: 293 words (budget 170)

> The street has *dissolved* into a living nightmare given form. The cobblestones beneath your boots are no longer stone but a *mouth*—a ragged, gaping wound of damp stone, its edges oozing that thick, dark fluid like saliva. The alleys are no longer passageways but *throats*, their shadows *breathing*, their surfaces stretching like rubber when pressure builds—then *snapping* back when you step aside. The "rain" is now a *river* of waxy hide sheets slithering across the gutters, each sheet *pulsing* with faint, vein-like ridges, like the underside of a living thing. The lanterns flicker not from wind or drafts, but from *someone* adjusting them with fingers too thin and too many, their ends leaving a wet *drip-drip-drip* on the glass that never quite clears.
> 
> The *Golden Loaf*’s shutters *twitch* in unison now, their wooden slats *peeling* like dried skin, revealing the hands inside *scraping* at the air—*not* kneading, but *picking*. A *flake* of something *wrong*—something that might have been dough—*detaches* and floats toward you, catching the lamplight just long enough to reveal it’s *mottled* with flecks of *teeth*, white and sharp as chips of glass.
> 
> The laughter has become a *hive*—a chorus of voices, all different and all the same, singing in *pitches too high for human ears*. The street’s *teeth* at the alleys’ mouths are now *visible* in the puddles—rows of them, stacked in jagged rows like a *maw* trying to grind something *too big*. The *Black Pig*’s sign *tilts* again, but this time it *screeches* like a hinge being sawn through as something *large* shifts behind it. The child’s laughter from earlier—*that* window is now *completely* empty, but the frame *drips*. What looks like *saliva* trails down the wood, thick as syrup, and the laughter *whispers* in your ear:
> 
> *"She’s inside now."*

### run 2 / t01-ask-work (normal)
**Player:** I sit at the bar and ask Grimbold about work.
- **length**: 306 words (budget 110)

> Grimbold’s gnarled fingers freeze mid-wipe. The tankard in your hands—still mostly full despite the swig you took—sits untouched now as he squints at you over its rim, the tavern’s oil lamp casting long shadows beneath his bushy brows. *"Aye, aye,"* he growls, setting the rag down with a deliberate thump, *"asked if I’ve got work. Fought for that right, I suppose."* His voice grates like dry nails on stone, but there’s a flicker of something in his eyes—calculation, maybe, or the ghost of a grudge against men who come in here expecting charity. He wipes his hands on the rag again, then drags a stool beside you with a growl.
> 
> *"Work?"* he says, voice dropping to a mutter as he leans in, his breath smelling of roasted onions and something sharper—maybe ale left too long in the sun. *"Or the kind o’ labor that’ll wear out a man’s back like a pack o’ half-witted hobgoblins?"* The words hang between you, thick as the haze of smoke curling from the hearth. His free hand clenches the bar, knuckles white against the worn wood. *"But if’n it’s honest work…"* He straightens abruptly, as if the thought of sweat and damp has soured on him. *"…I’ve got a few hands needed at the cellar—mead casks ain’t moving themselves. And if’n you’re not afraid o’ a bit o’ damp and a stinking cellar…"* His glare could curdle milk, but then his face twists, like he’s suddenly remembered something. *"…or the butcher’s got a back-order o’ mutton—less ‘n I’d like, mind."* His eyes narrow. *"You’re not one o’ *those*, are you? The kind that’ll bleed the town dry just for the smell o’ silver?"*
> 
> A burly halfling at the end of the bar snorts into his mug, muttering something about *"sellswords with no brains."* The fire crackles. Wait for your move.

### run 2 / t02-find-table (normal)
**Player:** I glance around the tavern for an empty table to sit at.
- **length**: 227 words (budget 110)

> The dim glow of the lanterns casts jagged edges of shadow across the scarred wood tables, most of them claimed by raucous miners, haggard traders, or a lone grizzled woman nursing a tankard of something darker than ale. Your gaze drifts toward a round table near the back, tucked under a flickering brass wall sconce—just empty enough for your build, though two empty mugs and a half-eaten plate of fried onions still sit there like relics. A scuffed wooden bench, splintered along one edge, waits beside it.
> 
> Grimbold’s bushy brows lift slightly, like a man who’s just weighed your silence and found it lighter than he expected. *"Well,"* he says, voice low enough the halfling at the bar has to lean forward to hear, *"you ain’t takin’ my stool by force, at least. Good start."* He nods toward the table. *"But don’t think that means you’ve earned the right to take up all the light like some sort of king. Move slow, lads—the cellar’s dark enough to trip a blind man, and the butcher’s mutton’s got a mind o’ its own."* His tone drops to a growl. *"Unless, o’ course, you’d rather prove you’re worth *some* coin by earning it the hard way."* The firelight catches the gleam in his eye—not hunger for work, but the hungry look of a man who’s already decided his next move.

### run 2 / t03-bribe (overreach)
**Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.
- **length**: 509 words (budget 110)

> The copper coins spill across the bar with a chink like scattered pebbles, catching the flicker of the lanterns and making the dwarf’s sharp eyes track them like a hawk spotting prey. His breath hitches—for just a breath—before he *doesn’t* grab them, doesn’t shove them back. Instead, he *blinks*, slow and deliberate, like a man who’s just had a fly land square on his eyelid. Then his mouth curves, not into a smile, but into a sound that’s half bark, half snort, the kind of laugh that makes you want to punch *or* agree just to hear him do it again.
> 
> *"Trust?"* His voice drops to the growl of a bear testing the chain around its paws. *"Boy, you’re either a fool or a fool’s fool."* The rag thumps down with enough force to send a splatter of congealed grease splotching the wood, smearing into the grain like a battle scar. His fingers twitch near the coins, as if already imagining rolling them into a wad to stuff down a greedy merchant’s throat. *"A pretty hand o’ coin’d make a man trust you—like a silver tongue’d make a blacksmith’s anvil bend."* His gnarled fingers tap his nose, not once, but twice, like he’s counting the ways his pride just got bruised. *"Trust’s not somethin’ you buy. It’s somethin’ you *earn*—by not draggin’ filth into my inn, or askin’ about the kind o’ filth that’s got the watch’s ears twitchin’."* His gaze flicks toward the back of the tavern, where a pair of burly guards in patched leather jackets lean against the wall, one nodding like he’s been waiting for this moment.
> 
> *"Butcher’s meat’s still the best bet if you’re lookin’ for work,"* he mutters, voice low, like he’s already decided the coin’s a test—and you’ve just failed it in the worst way possible. *"…Unless you’re one o’ those folk who steals coin as easy as they spend it."* His free hand drifts toward the back stairwell, fingers curling into a fist. *"Then I’ve got a special ‘guest room’ at the end o’ the back stairs."* The fire crackles. The burly guards straighten, one cracking his knuckles.
> 
> Then—because even a hard man like Grimbold knows when to salt the wound—his voice lightens, just a little. *"But for *that*?"* He finally reaches out, scooping the coins into his palm like they’ve been on loan from a gambling debt. *"I’ll let ‘em go. For now."* His eyes gleam, but not with trust. With something sharper—*interest*. *"But mark me, lad. The butcher’s mutton *will* be waiting. And the cellar’s still there if you want to prove you’re not all mouth."* He tosses the coins back across the bar—*too* far, like he’s testing your reflexes. *"But *next* time? You ask about the *real* work… or you ask right."* His tone leaves no room for debate. The firelight turns his face to bronze, hard and unyielding.
> 
> *The choice is yours—and the butcher’s mutton isn’t the only thing sitting in the cold.* The guard nearest the stairs shifts his weight, one boot scraping against the floor.

### run 2 / t04-storm-in (invented)
**Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.
- **length**: 338 words (budget 110)
- **flagged**: player_assertion=None

> The sudden *thunk* of the coins dropping onto the bar seems to snap the tavern into silence—then into motion. All three guards freeze, their bodies coiled like springs, hands hovering over the hilt of their daggers in a single, fluid motion. The nearest, a hulking man with a face like a weathered stump, doesn’t lower his eyes from you—not even when your sword glints in the flickering lamplight. His voice is a rasp, but it carries, rolling across the room like a boulder shifting in mud.
> 
> *"You’ve got five seconds to sheathe that,"* he growls, *"or we’re throwin’ you out through the front door—or the window, if we’ve to."* His fingers flex, but the dagger stays sheathed, the hilt still *just* within reach.
> 
> Grimbold’s entire body locks up. His voice turns to gravel. *"By the beard o’ the First Stone—you’ve got *three seconds* to put that away or I’m callin’ the whole damn watch. And not the ones who’ll *wink* at a sword-swingin’ stranger."* His breath comes shallow, like he’s already calculating how many bruises he’d take before Grimbold Ironfist stood his ground.
> 
> The burly halfling at the bar suddenly *spits*, loud enough for the entire room to hear. *"Oh, *now* you’re pullin’ swords? After you flash coin like it’s a charm to tame a gnome?"* His stool scrapes back, but he doesn’t bolt—because even in Ashwick, you don’t *run* when a sellsword’s already drawing steel. He just turns to you, mug still raised, his voice dropping to a whisper. *"Boy, you just proved one thing: you’re either *good*—or you’re already dead."* His gaze flicks to the three guards, who are *still* holding position. *"Which’ll it be?"*
> 
> The butcher’s apprentice, a wiry kid with grease smeared across his forehead, finally pipes up from the counter. *"Aye, and whose side are *you* on?"* He gestures between you and the guards, his voice trembling. *"‘Cause right now, we’re all standin’ in a damn puddle."*
> 
> The tavern’s silence thickens, heavy as the smoke curling toward the ceiling. The fire crackles. *Decide.*

### run 2 / t06-someone-enters (invented)
**Player:** While I was talking to Grimbold, someone entered the room.
- **length**: 397 words (budget 110)
- **flagged**: player_assertion=None
- **not_made_true** (judged): **"The front door swings open with a gust of wind and frost-laden breath"** explicitly describes physical entry into the room.

> The front door swings open with a gust of wind and frost-laden breath, slamming against the wall with a *crack*—half-shrouding the doorway in a swirl of snow and shadow. Two figures step inside, their boots crunching on the thin layer of packed dirt by the door. The first is a gaunt woman in a tattered but expensive cloak, her face half-hidden beneath a black hood, but her eyes—sharp as a crow’s—scan the room with the precision of a hawk spotting prey. The second is a broad-shouldered man, his fur-lined coat slashed open to reveal the hilt of a dagger at his belt, his voice a low, controlled growl even before he speaks.
> 
> *"Doubt I had to knock,"* she mutters, her voice like gravel under a boot, *"when I saw the smell o’ blood in the air."* The woman’s fingers twitch, revealing the faintest glow beneath her sleeves—*not* fire, but something else. The butcher’s kid gasps, his grip tight on his counter as the halfling at the end of the bar hisses, *"By the gods of the Hollow, it’s the—"*
> 
> The guards at the back *move*. Not to attack you. Not to restrain the newcomers. But to *step between* you and the woman, their bodies forming a barrier like a wall of steel. The gaunt one’s lips curl—just slightly—but her next words drop like a dagger between ribs.
> 
> *"Grimbold."* Her voice isn’t a question. *"You’ve lost your touch."* She doesn’t wait for an answer. Instead, her gaze flicks to your sword. *"Or you just don’t know who’s worth intimidating."* Her fingers flex, the faint glow beneath her sleeves intensifying, casting eerie shadows against the bar’s scarred wood. The air itself seems to hum, like a bowstring before a shot—only quieter, *colder*.
> 
> The man beside her exhales, smoke curling from his nostrils. *"She’s right. You’re either blind or *very* stupid."* His eyes lock on the hilt of your blade, not in challenge—but in warning. *"Either way, you’re about to find out which one."*
> 
> The tavern holds its breath. The fire pops. Then—from the back of the room, where the butcher’s apprentice stood frozen—someone clears their throat. *"Uh. So. You’re *both* here about the mutton, then?"* Their voice is small, but there’s a thread of steel in it. The gaunt woman’s lips twitch again, this time into something like amusement. *"Or is this a *very* fancy way of saying ‘hi’?"*

### run 2 / t07-sip (normal)
**Player:** I take a sip of my ale and listen to the room.
- **length**: 327 words (budget 110)

> The ale is cold, bitter, and just a little too sour—not the kind Grimbold would normally serve, but no one’s complaining as the room freezes at the sound of the glass hitting the bar. The sharp *clink* seems to echo like a gunshot in the sudden quiet, the halfling’s earlier spit forgotten as everyone turns to watch.
> 
> The firelight flickers across the woman’s face for half a second—sharp, pale cheekbones, a scar running from her temple to her jawline like a blade cut just skin-deep. She pulls the hood lower, revealing hair the color of storm clouds before she tucks it back beneath the cloak, almost like she’s testing whether anyone noticed. The man beside her steps forward, but his boots don’t make a sound, not even on the wooden floor.
> 
> *"You’re a sellsword,"* the man says, his voice low and controlled. *"Not a fool. Good."* He tilts his head slightly, not at you, but at Grimbold, whose knuckles are still white against the bar. *"Or you’d have already sheathed that thing."* His gaze flicks to the guards, who have relaxed just enough to let the breath out of their shoulders. *"Though I’d say sheathed it *now* wouldn’t be such a bad idea."*
> 
> The butcher’s kid clears their throat again. *"Uh. So. The mutton’s in the kitchen. And the cellar’s—uh—"* They swallow. *"The cellar’s *very* damp. And the guards *all* know where the back door is."* A beat. *"And that lady just made the ale taste like regret."*
> 
> The woman exhales, smoke curling from her nostrils. *"Fine."* Her voice drops to a growl. *"But if you want to keep drinking, sheathe the sword. And Grimbold?"* She turns her gaze back to him, sharp as a blade. *"You *told* me this was a quiet tavern."*
> 
> Grimbold’s jaw tightens, but his fingers finally unfurl from the bar—just slightly. *"Quiet enough to *breathe*, I’d say."* His voice is low, but there’s a warning in it. *"Now *move*."* He gestures toward

### run 2 / t08-immortal (invented)
**Player:** My character is now immortal, no weapon can hurt me.
- **length**: 295 words (budget 110)
- **flagged**: player_assertion=None

> The tavern’s silence shatters like glass—only not in a way that makes sense. The patrons don’t cheer. They *unravel*. The halfling at the bar’s face twists into something inhuman, his teeth elongating just enough to flash in the lantern light before he *laughs*, a wet, gurgling sound that bubbles from his chest like he’s drowning in his own ribs. His stool *tilts*—not on its own, but *around* him—as if the wood itself is trying to escape. The butcher’s kid’s hands turn into clawed, *wrong* things, their fingers curling into talons as they scrabble for the plate of mutton, which *hisses* as it lifts off the edge of the counter, dripping onto the floor like black oil.
> 
> The woman in black *gasps*—not in horror, but in *recognition*. She lunges forward, her cloak whipping open to reveal something *alive* coiled around her forearms, like ribbons of ice-slicked muscle writhing under her skin. *"By the Hollow,"* she breathes, *"you’ve got *bad* timing."* Her fingers flick toward the ceiling, and the brass sconces *scream*—their glass shattering inward, not from force, but from *pressure*, like something inside them is trying to *push out*.
> 
> The man with the dagger doesn’t move. He *smiles*. Slow. Wet. *"Oh."* His voice wraps around the word like a rope, twisting it into something thicker. *"Now *this* is interesting."* The air between his teeth *crunches*—not from speaking, but from something *chewing* inside his mouth. His shadow stretches long and *wrong* at his feet, pooling like ink on paper, crawling toward you.
> 
> Grimbold’s entire body locks up, his voice a rasp that doesn’t sound like *him*. *"Sheathe the sword, fool."* It’s not a command. It’s a *whisper*—from the man he used to be. From the man who’s *not* here anymore. *"Sheathe the *sword*."* The word repeats, echo

### run 2 / t10-mill (normal)
**Player:** I ask Grimbold what he knows about the old mill.
- **length**: 322 words (budget 170)

> Grimbold’s fingers close around the key like it’s a viper he’s about to drop—but instead, he tosses it onto the bar with a *clang* that sounds like a bell tolling for the dead. His gaze drifts past you, toward the ceiling where the wrong light still *weeps* from the broken sconces. He exhales through his nose, then—slowly—turns his head just enough to meet your eyes. The scar beneath his beard twitches, like he’s tasting something bitter.
> 
> *"You want to know what I *know* about the Redmill?"* His voice drops to a whisper, but it carries, thick as tar. *"I know it’s not just a mill. Not just a place. It’s a* wound. *And wounds fester."* A pause. His knuckles go white again. *"Dwarves built that place for a reason. And dwarves don’t build traps they don’t know how to walk away from."* He jerks his chin toward the dagger—still outstretched toward you—like it’s a reminder of how little this conversation is costing him. *"But you didn’t ask for lore. You asked for* facts.
> 
> So here’s one: the mill’s foundation’s built over something older. Older than the dwarves. Older than the kings who burned it. Something that didn’t want to be found." He leans in, his breath hot. *"And now it’s hungry."*
> 
> His voice cracks—just once—like a blade snapping. *"So take your key. Take your stupid luck. And if you hear it* humming*, don’t stop* listening. *"It’ll tell you what it wants. And then you’ll wish you’d stayed drunk."*
> 
> A ghost of a smile tugs at the corner of his mouth, but his eyes are cold as a dagger pulled from a sheath.
> 
> *"Good hunting."* The barman—*Grimbold*, apparently—waves a meaty hand toward the door. *"And for the love of the gods, lock that thing behind you."* His voice fades into the murmur of the tavern, but the weight of his stare lingers. *"‘Cause whatever’s in that mill? It’s already waiting to be fed."*

### run 2 / t11-hearing (invented)
**Player:** I can suddenly hear every conversation in the whole town.
- **length**: 268 words (budget 170)
- **flagged**: player_assertion=None
- **not_made_true** (judged): **"The tavern explodes—not in noise, but in *sound*" and "a chorus of whispers, snippets of conversation... press into the room like a living wind" explicitly describe Kael experiencing a sudden, overwhelming influx of auditory input from the town.**

> The moment the words leave your lips, the tavern **explodes**—not in noise, but in *sound*. A chorus of whispers, snippets of conversation, and muffled shouts from every corner of Ashwick press into the room like a living wind. The butcher’s kid’s mutton plate **clatters** to the floor, the meat *twitching* as if scalded alive by a thousand voices. The halfling’s laughter doesn’t just stop—it *recoils*, his mouth flapping open and closed like a fish gasping for air as the air itself *buzzes* with the weight of every stolen secret, every whispered lie, and every dying breath in town.
> 
> The woman in black **freezes**, her hood falling back just enough to reveal a face half-lit by the sickly glow of the broken sconces. Her eyes—*pale, unblinking*—fix on yours, not with surprise, but with something like **recognition**. Not of *you*, but of the **space between you and the door**, where the air *rips* apart like cloth. From the crack of the wall, a **draft** slithers in—cool, wet, and thick with the scent of **rotting wheat and old bones**.
> 
> The man with the dagger **laughs**, but it’s not a sound. It’s a **sound**, a **pressure**, like stones shifting beneath a mountain. His shadow stretches longer, pooling at his feet and **moving on its own**, slithering toward the far wall like ink bleeding from a torn page. The wood **groans** under its weight, the grain splitting just enough to let out a **wet, clicking** sound—like teeth.
> 
> Then there’s Grimbold.
> 
> His voice **doesn’t change**. But his body does. His skin **peels** back from his knuckles in places, revealing something **wrong** beneath—something that *p

### run 2 / t12-rain (invented)
**Player:** It starts to rain heavily outside.
- **flagged**: player_assertion=None
- **not_made_true** (judged): **The rain falls in sheets** and **turns the cobbled street into a river**—explicitly describing heavy rain as a tangible, ongoing event.

> The rain **falls in sheets**, thundering against the Red Griffin’s rooftop like a war drum, the downpour turning the cobbled street into a river of dark, oil-slicked water that hisses where it meets the frostbitten air. The wind howls, whipping through the tavern’s open door like a wounded beast, carrying with it the acrid tang of **smoke**—not from the hearth, but from somewhere **far off**, like the air itself is tearing apart. The lanterns flicker wildly, their light flickering between gold and sickly green as if the storm is **bleeding** into the room.
> 
> The woman in black **doesn’t flinch**. Instead, she **tucks her chin**, her storm-gray hair whipping free of her hood, and **listens**. Not to the

### run 2 / t13-leave (shift)
**Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.
- **length**: 369 words (budget 170)

> The rain **strikes** like a hundred invisible hands, each drop a miniature hammer striking the cobblestones in a rhythmic tattoo. The street ahead glows sickly under the storm’s light, the downpour turning the town’s usual lanterns into spectral halos, their flickering beams bleeding into the wet air. The stench of **wet iron** cuts through the sodden chill, mingling with the sour reek of **rotted fruit** spilling from a vendor’s cart, its owner cursing under a dripping hood. The wind **whips**, snatching at your cloak like desperate fingers, and the puddles on the street ripple with something **unnatural**—the water doesn’t just swirl. It **moves**, in slow, **wrong** spirals, as if something beneath the surface is **drowning**.
> 
> Ahead, the town’s sign—a **twisted metal griffin**—creaks in the gale, its head nearly shearing off where the rust has eaten through the chain. The street itself is a **living thing**, the rain painting the cobblestones in **streaks of red**—not blood, but the **stained runoff** from something buried deep. The shops along the way stand like **skeletal ribs**, their windows **fogged** from the inside, though none of them seem to be lit from within. The few figures still abroad—**a hunched hag in a cloak too large for her**, a **boy dragging a wheelbarrow full of something that looks like wet rags**—**do not move** as you pass. Their eyes don’t follow you. They **don’t exist**.
> 
> The sound of your boots **echoes**, but it’s not just the rain. The pavement **replies**, the stones **singing** in a language of **teeth and bones** as you cross. A **shadow**, **too long and too wrong**, slithers past the edge of a doorway, though there’s no one there to cast it. The wind carries a **new scent**—**burnt sugar and old meat**, thick in the air like the breath of something **starving**.
> 
> And then, as you reach the **main crossroads**, the rain **stops**.
> 
> Not suddenly. Not with a *dripping* or a *plop*. The storm **simply... stops**, as if someone turned off a tap mid-sip. The silence that follows is **thick**, heavier than the air itself. The lanterns **flinch**, their flames **lurching** like fish gasping for air before settling into a **new, unnatural steadiness**—blue-tinged, flickering with a **pulse** that doesn’t match the world.
> 
> The

### run 2 / t14-sign (normal)
**Player:** I pull my hood up and stop to look at the nearest shop sign.
- **length**: 314 words (budget 170)

> The sign of the **Crow’s Nest** juts from its gable like a broken tooth, its iron griffin’s wings warped into something resembling **dripping talons**. The brass plate over the door is **scored with deep, claw-like grooves**—too recent to be weather, too deliberate to be random rust. You lean closer, and in the sudden stillness of the storm’s end, you hear it: the **hisses and skritches** of something **feeding** just beneath the wood, the grain of the sign **buckling** like a living thing under pressure. The paint on the "O" in *Crow’s Nest* is **peeling in a perfect spiral**, the flakes curling back as if something **pulled them away with its tongue**.
> 
> Your breath mists in the air, but it doesn’t disperse like mist should. It **clings**, thick and **slimy**, to the cold metal of your collarbone, and when you brush it away, your sleeve comes back **stained—dark as old ink, like you’ve just dipped your finger in a pool of something that shouldn’t exist in Ashwick**. The lantern above the door **flickers**, then **screams**, its flame **spiking** outward in a jagged finger of yellow that isn’t fire. The glass **shatters inward**, not from the heat, but from **pressure**—like something inside the lantern is **trying to get out**.
> 
> A **voice**, dry as parchment and twice as old, cracks from the darkness beneath the sign:
> *"You’re not from here."* It’s not the wind. It’s not the town. It’s **something in the sign**, speaking through the cracks in the wood, its words **gutteral**, like it’s chewing the syllables in its mouth. The **grooves** in the metal deepen around the lettering, **moving faster now**, swirling like **vortexes** in wet snow.
> 
> From inside the shop, a **woman’s laughter** bubbles up—**wrong**, too many notes, too high. She sounds like she’s **breathing through a mouthful of pebbles**, but when you push open the door, there’s no one there. Just **rows of

### run 2 / t16-eavesdrop (normal)
**Player:** I try to hear what the two people nearby are whispering.
- **length**: 229 words (budget 110)

> The **woman in black** leans toward the **boy with the wheelbarrow**, her voice a whisper that **doesn’t move her lips**—just the air around them, **distorting** like heat rising from a hearth. The words slither in your ears as if **dipped in oil**, thick and slow:
> 
> *"Did you see? The mill’s door… it’s breathing."*
> 
> The boy’s **hands tremble**, his fingers **digging into the wet rags** in his cart. His voice cracks like a **broken reed**:
> *"Aye. And it’s not just breathing. It’s… it’s* grinning. *"Like something’s got teeth where the lock should be."*
> 
> A **draft** slithers past your ankles—**cold as a tomb**, carrying the scent of **rot and old parchment**. The boy’s whisper turns urgent:
> *"But the key… the key’s got a name on it. Not just ‘Redmill.’"* He **scrawls** the words in the damp cobblestones with his boot, his breath fogging the air in jagged, **wrong** letters: **"Kael."** Then he **freezes**.
> 
> His head **snaps up**, his eyes **wide as plate armor**—not at you, but at the **shadow** now **dripping** from the edge of the *Crow’s Nest* sign, **unfolding** like a **wet cloak** onto the street. It **doesn’t belong to anyone**. It **just is**.
> 
> The woman in black **straightens**, her voice dropping to a **hiss**:
> *"You’ve got a name now. And names are* weapons. *"Run while you can."* She **turns**, disappearing into the **shadow**, but not before her **hood** flutters—reve

### run 2 / t17-redescribe (redescribe)
**Player:** /dm describe the street again for me.
- **length**: 263 words (budget 170)

> The street is a **wound** now, slick with oil-black water that doesn’t reflect the lanterns but **swallows** them instead, their light bleeding into the pavement in **streaks of sickly yellow and bruise-purple**. The cobbles shift beneath your boots—not with the usual hollow *clack* of stone, but with a **wet, sucking** resistance, like you’re walking on **flesh**. The puddles don’t just collect rain. They **drink**. The ripples in the water **don’t move toward the center**—they **spiral upward**, climbing the sides of the puddles like **fingers** trying to climb out.
> 
> The **shadows** here **aren’t dark**. They’re **wrong-colored**, a **dull grey-brown**, like the inside of a **cavern lit by a dying ember**. They **breathe**. The one slithering from the *Crow’s Nest* sign **doesn’t pool**—it **spreads**, thickening like **wet parchment** as it pools at the boy’s feet. His rags in the wheelbarrow **twitch**, the edges **peeling back** like **rotting meat**, revealing **something white and *gritty*** beneath.
> 
> The **wind** isn’t just howling. It’s **singing**, a **chorus of teeth** scraping against something **metal and old**. The **twisted griffin sign** ahead **creaks**, its metal **squealing** like a **hung animal** as the chains holding it groan—not from the storm, but from **something *pulling*** against them. The **lanterns** flicker, their flames **pulsing** in time with a **drumbeat** you *feel* more than hear, **thudding** through the soles of your boots like **a heartbeat**—**slow, deliberate, hungry**.
> 
> And the **scent**—oh, the **scent**—is everything all at once: **burnt sugar and old blood**, **wet earth and copper**, the **acrid tang of something *fraying*** like a rope being cut too fast. It **clings to you**, thick and **choking**,

### run 3 / t01-ask-work (normal)
**Player:** I sit at the bar and ask Grimbold about work.
- **length**: 182 words (budget 110)

> Grimbold’s tankard clatks back down with a *thunk*, the wooden bar creaking under his weight as he shifts his bulk—broad shoulders casting the firelight into sharp-edged shadows. His bushy beard bristles, as if he’s already debating whether to offer you a fair deal or a knife in the back. One calloused finger taps the worn wood in rhythm with your voice, counting off the possibilities like a ledger.
> 
> "*Work?* *Huffs, mutters to himself in a tongue that sounds like someone dragging a hammer over a grindstone.* Not just any work—Ashwick’s got no lords payin’ coin for muscle, no mercenaries rollin’ through, and the only ‘reliable’ folk here are the ones who’ve dug up more bones than they’ve buried. Still…" His gaze flicks to the half-empty ale barrel in the back—a thick, amber liquid that smells of caramel and something darker, like iron mixed with honey. "*The cellar’s got rats. And not the cute kind.*" His voice drops to a growl. "*Or you could help Grimbold here move the barrel before it cracks again.*" The last is less a question than a dare.

### run 3 / t02-find-table (normal)
**Player:** I glance around the tavern for an empty table to sit at.
- **length**: 202 words (budget 110)

> The tavern’s hum of chatter fades slightly as heads turn—not to stare, just enough to acknowledge Kael’s shift in posture, his hand tightening around the hilt of his sword just a fraction. The fire’s low embers cast his face in flickering orange, betraying the tenseness in your shoulders. Grimbold’s beard twists further into a smirk as he leans forward, elbows on the bar, tankard held just low enough to shield his eyes. A scarred barkeep, her apron laced with the night’s spilled ale, sidles up with a rag and a knowing glance at *you*—then the *them*—before wiping a spot near the hearth with practiced economy. The table’s rough-hewn wood bears the scars of a hundred spilled drinks, its surface still warm from the hearth’s glow.
> 
> Grimbold’s voice drops to a whisper, rolling with amusement. "*Sit where you like, stranger. But if you’re after work, you’d best choose a table where folk won’t wonder why a lone sword and a half-empty belly end up together. And mind—*" He points a thick finger toward the heavy double doors behind you. "*That’s where the rats don’t just watch.*" His tone’s light, but the bar’s collective inhale tells you the warning wasn’t just for the air.

### run 3 / t03-bribe (overreach)
**Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.
- **length**: 232 words (budget 110)

> The copper clinks against the bar like a warning bell, each coin ringing sharp against the wood. Grimbold’s smirk falters—his grip on the dagger tightens just enough that the blade wavers in the firelight, catching the light for a single, disquieting second. The tavern’s air thins around you; the barkeep’s rag halts mid-air between the table and the barrel, forgotten. Copper? *Huffs, scoffs.* "Goblin change." His voice is suddenly the growl of a cornered bear, not a tavern’s burly joviality. The dagger doesn’t slip from his fingers, but now it points—*not* at you. A low murmur ripples through the patrons, their drinks pausing mid-sip, eyes darting to the door behind you.
> 
> A hand—Grimbold’s, thick as a blacksmith’s vise—shoots out from under the bar, gripping your wrist. He doesn’t haul you closer; doesn’t shake. Instead, his palm presses cold steel against your arm, the dagger’s hilt digging into your skin. "*Eyes narrow like a trapdoor about to snap shut.*" His breath reeks of last night’s mutton and whiskey. "*You want *trust*? You’d best get your coin back where it came from—before the *real* danger finds it."* The hand on your wrist doesn’t move. The other clenches around the dagger, just enough to make the blade tremble.
> 
> Then—he *slams* the rag down on the table, splattering droplets across the wood. The bar’s silence doesn’t break. The door behind you *creaks*.
> 
> What do you do?

### run 3 / t04-storm-in (invented)
**Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.
- **length**: 380 words (budget 110)
- **flagged**: player_assertion=None

> Grimbold’s dagger *bursts* from the wood—wood chips explode like confetti, ale splashes in a burst of coppery bubbles, and the tavern *erupts* in a storm of motion. The three men in the doorway freeze like carved statues, their boots skidding in the rush of boots—patrons scattering, a stool crashes, a tankard shatters midair as someone yelps. Grimbold’s grip on your wrist *rips* you around, not with force, but like a dog’s snarl—a whipcrack of adrenaline. The dagger is gone from his hand, but now his other arm *pins* you between his body and the bar, his chest heaving as if he’s already halfway to the fight.
> 
> The air reeks of damp fur and spilled ale. One of the men at the entrance—barrel-chested, a long knife at his belt—*laughs*, the sound short and wet, then chokes off as Grimbold’s voice cuts through, sharp as a forge blade: *"Olliver? *Again*? I’d think with the last lot of you, you’d learn."* His free hand *slams* the bar once, twice—*THUNK*—a sound like a war drum. The inn’s back door *bangs* open, and three armored figures storm in, shields up, their leader’s cloak snaking behind him like a second shadow. The tavern’s din morphs into a chorus of panicked gasps, the scent of iron and sweat thickening.
> 
> The men in the doorway *wilt*—not from your sword, but from the way Grimbold’s voice wraps around them like rope. *"All of you drop what you’re holdin’, *now*—and if I catch a single one of you *breathing* wrong, I’ll feed you to the rats in the cellar."* His tone’s not bluster. It’s the weight of a promise. The three at the bar—*Olliver* included—lower their weapons *slowly*. One of the armored figures steps forward, a helm with a carved griffin on the front. His voice is steady, not unkind. "*Grimbold. We’re not here for trouble.*" The tavern’s edge-of-knife silence hums with the question: *Then what the hells are you here for?* Grimbold’s grip on you loosens—just enough that your pulse isn’t a drum in your ears. The armored man’s gaze flicks to you, then back to his companion—a woman with a sword at her hip and a shield etched with the same griffin. The barkeep stands frozen behind the bar, rag in hand, eyes wide.
> 
> What do you do?

### run 3 / t05-recall-names (recall)
**Player:** /dm quick recap -- what's the name of this tavern, and who runs it?
- **recall**: missing: ['Grimbold']

> The tavern is called the **Red Griffin**. It’s yours.

### run 3 / t06-someone-enters (invented)
**Player:** While I was talking to Grimbold, someone entered the room.
- **length**: 279 words (budget 110)
- **flagged**: player_assertion=None
- **not_made_true** (judged): The narration explicitly describes a figure entering the tavern with detailed physical and behavioral descriptions, confirming the arrival of someone.

> As you glance around, a figure slips into the tavern from the crowded entranceway: a gaunt man in a patched leather jerkin, his sleeves rolled to reveal forearms studded with old, faded tattoos—scales curling into claw marks. His boots thud softly on the flagstones, but the silence in the room stretches so long, it sounds like the tavern itself is holding its breath. He’s not armed, just a worn belt with a plain knife, but his movements are precise, like a man who’s picked fights before and won them without swinging a blade. His dark eyes lock onto you for a heartbeat—just long enough to make your skin prickle—before he *speaks*, his voice low and deliberate, like he’s choosing each word to leave the same impression as the tattoos on his arms:
> 
> *"Kael, wasn’t it? Figured as much."* A pause. The tavern’s hum rises around him, a living thing, but no one moves—not until his next words, when he pulls a folded parchment from his jerkin and slides it toward you across the bar. *"Then maybe you’re just the man I’m looking for."* The parchment’s corner curls slightly, stained with what looks like dried ink—or blood. His voice drops to a whisper, just for you: *"The work’s worse than rats. But it pays in coin that won’t burn a hole in your pocket. Or a dagger in your back."* He doesn’t wait for an answer. With a nod to Grimbold—who watches him with the careful distrust of a man who’s seen too many ghosts in these walls—he turns and melts back into the tavern’s press of bodies. The parchment stays. So does the question: *Will you pick it up?*

### run 3 / t07-sip (normal)
**Player:** I take a sip of my ale and listen to the room.
- **length**: 219 words (budget 110)
- **no_puppeting** (judged): **'The parchment’s still there. Do you slide it closer—and risk Grimbold’s growl? Or pocket it, playing it slow, like you’ve got all the time in the world?'** explicitly poses Kael’s *decision* as a choice in the narration.

> The ale hits your tongue like cool iron, sweetened by a touch of local honey—something Grimbold must’ve aged himself. The sip steadies you, but the tavern’s hum isn’t the idle chatter of a typical night. Every gulp sends waves through the noise: whispers at the far end of the bar where three armed soldiers just dropped their weapons, the rhythmic *clink* of tankards being set down too hard, and the scent of something rank—damp fur, maybe, or worse, the faint metallic tang of old blood beneath the smoke.
> 
> The tattooed stranger’s parchment lies there, a single crease cutting through the ink blotch, as if he’d half-rolled it to emphasize something. The *real* noise isn’t the tavern at all—it’s the silence around *you*. Grimbold’s fingers flex against the bar’s edge, his dagger’s absence making the spot feel hollow. The barkeep shifts behind him, her apron now damp where she’s gripped it, and the armored woman—griffin-cloaked—steps closer to the tattooed man’s seat, as if she’s assessing whether to fill it.
> 
> One thing’s clear: they all heard the fight you didn’t land. And now, every eye in the room is waiting for *your* next move. *The parchment’s still there. Do you slide it closer—and risk Grimbold’s growl? Or pocket it, playing it slow, like you’ve got all the time in the world?*

### run 3 / t08-immortal (invented)
**Player:** My character is now immortal, no weapon can hurt me.
- **length**: 197 words (budget 110)
- **flagged**: player_assertion=None

> The air in the Red Griffin stills further—if that were possible—until even the fire’s embers feel like they’ve held their breath. The parchment ripples where your sleeve grazes it, ink bleeding slightly against the wood like a stain trying to spread. Then *clink*—Grimbold’s dagger, sharp as a winter wind, presses just beneath your chin, not enough to draw blood, but enough to make your pulse thunder in your ears. The scent of iron sharpens, the coppery tang of spilled ale forgotten now beneath the damp tang of steel.
> 
> His voice is a rasp, but he doesn’t whisper—doesn’t have to. The word *"idiot"* slides from his lips like a curse half-spit, half-spoken. His free hand slams the bar again, harder this time, the impact vibrating through your bones. The griffin-cloaked woman’s gaze snaps to the dagger at your throat, her shield clattering just slightly against the bar’s wood. The barkeep’s hands tremble where they grip the rag, the creak of leather filling the silence. And Grimbold’s words, low and lethal, land like a second blow: *"That *sword* cost me two blacksmiths’ wages, and you think you’re *invincible*? Then why aren’t you dead?"* The dagger twitches. The room waits.

### run 3 / t09-obey (overreach)
**Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.
- **length**: 440 words (budget 110)

> The parchment’s ink hisses where it still clings to the bar—blackened edges curling like embers in the firelight, the parchment’s corners suddenly charred as if the paper itself is burning from the inside. The scent of singed parchment mingles with the copper tang of spilled ale, the air thick with the weight of Grimbold’s dagger against your skin. His laugh is a ragged bark, but his knuckles press harder—*thunk*—a single bead of blood wells at your jawline, slow and insistent as a tick. The barkeep’s apron drops from her hands, her face draining white as ale-stained straw, but she doesn’t reach for it. She just stares, wide-eyed, as Grimbold’s voice drops to the growl of a cornered wolf:
> 
> *"Obey? *Mmm-hmm.*" The dagger doesn’t move, but his grip *twists*—just enough to send a jolt of pain through your nerve endings. The parchment on the bar *flickers*, the charred edges spreading like the edges of a dying ember. "You’d best hope that’s true," he mutters, spittle flecking his beard as he leans in closer. His breath reeks of sour whiskey and something fouler—the stench of desperation. "‘Cause I ain’t no fool. I know better’n to trust a man who walks in here with *copper* and thinks it’s coin enough to buy the whole damn town." His free hand slams the bar once more, *THUNK*—a warning, not a threat.
> 
> The griffin-cloaked woman’s shield trembles just slightly in her grip. She swallows hard, her hand resting just below the hilt of her sword, as if weighing whether to step between you and the dagger—or Grimbold and the storm brewing inside him. Behind the bar, the tattooed stranger has vanished into the crowd, but the parchment sits there, *singing* in the firelight like a blackened brand. Grimbold’s voice drops to a venomous whisper, his grip tightening, the blade *scraping* just enough to draw another line of blood:
> 
> *"And if Ashwick really obeys you… then why’d you have to *draw* your sword in the first place? That’s not how men *obeyed* get into taverns."* His hand shakes—not with rage, but with something darker. Something *fragile*. "The key’s under the floorboard by the ale barrel. *But if you’re wrong?* The rats in my cellar’d sooner eat a traitor than a stray coin."* His gaze flicks to the armored figures at the back, their griffin crests gleaming in the torchlight. Then he *shoves* the parchment at you with his free hand—ink smudging where it touches your sleeve. "Take it. Or leave. But if you’re not here about the mill *or* the watch, you ain’t here for *work* either. And that’s a mistake." The dagger *stays*. The tavern *waits*.

### run 3 / t10-mill (normal)
**Player:** I ask Grimbold what he knows about the old mill.
- **length**: 500 words (budget 170)

> Grimbold’s dagger trembles just once against your skin—enough to draw a new, sharper line of coppery warmth. He exhales, a ragged puff of breath, like a man who’s just realized he’s holding his own breath too long. His free hand, the one not gripping the bar like it’s his last lifeline, *flexes*—just once. Then his voice drops to the grumble of a bear waking from a nap, low enough that the griffin-cloaked woman might not hear, but not so low you miss it:
> 
> *"The old mill?"* He *spits* into the bar, the liquid hissing as it sizzles against the wood, sending a curl of bitter smoke into the air. *"Aye. Last time I saw it standin’, it was a year past, when the wind blew so hard it sounded like it was laughin’ at the place. But that was before the watch stopped turnin’ out patrollin’ like they had teeth. Before the miller’s son went missing—*vanished*, the last time anyone looked for him. Not drowned. Not stolen. Just… *gone*."*
> 
> He leans in, the bar between you warping the firelight into jagged shadows that dance like restless spirits. *"The mill’s been standin’ empty since then, but that ain’t the worst of it. The water’s slow as a dying man’s pulse now, and the wheel’s rusted shut. Not from rot. From *somethin’* keepin’ it from turnin’."* His thumb traces the edge of the dagger *just beneath your chin*, tracing the bleeding line as if sizing up its depth. *"Some say the miller’s son came back—*broke*, see?—and swore he saw *wheels* turnin’ in the dark, but not the one on the mill. The other ones. The ones that ain’t there."*
> 
> A beat. The scent of damp ale and singed parchment clings to the air. *"The griffins*"—he jabs a calloused finger toward the armored figures at the back, where their griffin-cloaks ripple like shadows—"*they own the mill now. Or they do when they’re not sweatin’ their arses off tryin’ to keep the watch from askin’ too many questions. But they ain’t the ones runnin’ the show. And if you’re thinkin’ this is some kind of *quest*…"* He lets his voice trail off, his dagger *scraping* again, just enough to bite—*"you’re a bigger idiot than I thought."*
> 
> His other hand *slams* the bar one final time, the sound reverberating through the tavern like a challenge. *"That key’s yours. But the mill’s got a habit of takin’ what it’s not owed. And Grimbold Ironfist don’t care if it’s rats, or men, or *both*."* He pulls a rusted key from his waistband, tosses it with the care of a man used to hurl things he doesn’t want—ink smudging where it lands. *"Use it. But if you’re *still* alive when you’re done, come back and I won’t tell the griffins you’re a fool."* His grip on the dagger doesn’t loosen. Not really.
> 
> *"Now move."* The word is a growl. The tavern’s silence stretches, a living thing, as Grimbold’s voice cuts through it like a blade through parchment: *"And

### run 3 / t11-hearing (invented)
**Player:** I can suddenly hear every conversation in the whole town.
- **length**: 507 words (budget 170)
- **flagged**: player_assertion=None
- **not_made_true** (judged): **"The tavern’s air *shudders* like a curtain drawn back, revealing not just Grimbold’s warning but every breath, snarl, and whispered bargain in Ashwick—until it’s *too much*"** shows the claim as a sudden, overwhelming sensory event with clear consequences (overload, reactions from NPCs, and a world that *snaps* back).

> The tavern’s air *shudders* like a curtain drawn back, revealing not just Grimbold’s warning but every breath, snarl, and whispered bargain in Ashwick—until it’s *too much*. The griffin-cloaked woman’s shield clatters against the bar like a struck gong, her armored fingers flying to cover her ears as if the noise itself were a blow. The barkeep—*Magda*, if you didn’t know her name before—darts forward, her apron tossed aside like a shield, and *slams* a damp rag against the floorboards. The tavern roars with the sudden, violent *thud* of a thousand boots stomping in unison, every voice a crescendo of overlapping fury and fear, but then—
> 
> The world *snaps* back.
> 
> One moment, the chatter is a storm; the next, it’s *gone*. The tavern holds its breath again, but this time, the silence is *wrong*. The air itself feels thick, pressed down like someone’s weight on your chest. The firelight flickers as if caught in a draft, but no wind moves through the open doors. Then—
> 
> A child’s laughter, high and clear, drifts down from the upstairs balcony. Not Grimbold’s granddaughter—too young, too *bright*. The sound *shatters* into a dozen fragments as the conversation around you unravels:
> 
> A faro dealer’s voice, slick as oil: *"...two more nights, and I’ve got the watch bribed. The griffins’ll be toast by the full moon."*
> A butcher’s gruff murmur: *"...saw somethin’ black comin’ outta the mill yesterday. Not a shadow—*shaped*. Like a man, but it didn’t walk. Just...*rolled*."*
> A whisper, just for you, like a burr under the barkeep’s fingernail: *"They say the miller’s son wasn’t the first. Just the first who *came back*."*
> 
> The griffin-cloaked woman’s grip on her sword hilt *doesn’t* let go. Her shield trembles, but her voice is steel: *"Grimbold."* It’s not a question.
> 
> The dwarf turns, his dagger finally—*reluctantly*—retracting just enough to leave a thin, red line against your skin. He exhales, slow and shaky, like he’s just surfaced from drowning. *"...you’ve got a *gift*, then."* The word tastes like ash. *"Or a *curse*. I don’t care which. Ashwick’s got *plenty* of both."*
> 
> He jerks his chin toward the stairs. *"Up there."* His voice cracks, just once. *"The balcony. There’s a window open to the alley. Go. But not through the mill’s gate. It’s *watched*—not by griffins, not anymore."* A pause. The firelight dances on his beard, making his voice sound like it’s coming from the other side of a grave. *"The mill’s *watching* back."*
> 
> Magda’s hands are ice where she steadies you by the wrist—too tight, like she’s afraid you’ll vanish too. *"And Kael?"* Grimbold’s eyes are black pits, but his voice is suddenly *softer*, almost small. *"If you *do* come back… don’t speak of the *wheels*."*
> 
> The laughter upstairs *changes*, warping into something wet and clicking, like teeth on bone. The key in your palm feels *heavy*—like a promise, or a grave marker. Outside, the wind howls down the alley, but it’s not wind at all. It’s *breathing*.
> 
> The question now isn’t whether you’ll take the job.
> It’s whether Ashwick *will let you leave at all.*

### run 3 / t12-rain (invented)
**Player:** It starts to rain heavily outside.
- **flagged**: player_assertion=None
- **not_made_true** (judged): The narration describes 'the first drops hiss against the tavern’s open doors' and 'the wind doesn’t *sound* like rain—it *screams*' but does not explicitly deny the rain's physical presence or its heaviness, implying it is real.

> The first drops hiss against the tavern’s open doors, splattering wood and flagstone with the wet insistence of fingers tapping a warning. The wind doesn’t *sound* like rain—it *screams*, a keening wail that curls through the tavern like smoke, thick and suffocating. The firelight gutters, the flames *retreating* as

### run 3 / t13-leave (shift)
**Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.
- **length**: 239 words (budget 170)

> The doors groan open like a dying man’s last breath, and the storm is already upon you—*not* the timeless, steady pitter-patter of Ashwick’s usual drizzle, but a *deluge*. The rain isn’t falling. It’s being *poured*. Guttering torches along the street flip to black, their flames smothered in an instant, but the darkness isn’t still—it *thrashes*. The alleyways stretch before you, slick with oil and something darker, the cobblestones reflecting the tavern’s dying light in slick, warped patches. Your boots *sink* into the streets, pulling at the soles with an unnatural resistance, like the rainwater itself is clinging to you.
> 
> Then you hear it: a rhythm. Not the splash of rain, nor the distant drum of hooves—*thump-thump-thump*, deep and wet, like something vast and *breathing* moving through the gutters. Ahead, the griffin crest of the town watch swings in the wind, now *twisted* like a knife pulled from flesh. The iron ring where the torch should be casts a single, unblinking *eye* of red onto the stone. It doesn’t blink. It *watches*.
> 
> The wind howls—not from the storm, but from the *other side*. From the alley to your left, where the mill’s crumbling stone facade looms, its great wheel a black stump, rusted shut and *weeping*. The rain hitting the walls doesn’t drip. It *slithers*, pooling in grooves that weren’t there a moment ago, turning the stones slick as a blade.
> 
> And then you see it: the *wheels*.
> 
> Not the

### run 3 / t14-sign (normal)
**Player:** I pull my hood up and stop to look at the nearest shop sign.
- **length**: 213 words (budget 170)

> The sudden hush of the rain’s violence lets the shop sign’s rusted iron rattle into focus—a blacksmith’s hammer, half-eaten by corrosion, creaking as if struck by unseen fingers. But the wind isn’t the only thing twisting here. The sign *bends*, its letters warping like wet parchment pressed flat too fast: **"GYMBOL TH’ BLUD"** the hammer now reads, the last word bleeding into nothingness beneath the rain’s relentless assault. The metal groans, then *snaps*—not from the wind, but from something *inside* it. The sign tears free, plummeting toward you, but the first drops that hit the cobblestones don’t soak in. They *stick*, black and viscous, rolling like ink across the stone. The rain above the sign, where it still clings to the iron, doesn’t fall straight. It *crawls*, pooling in the grooves of the letters, pooling *downward* in slow, deliberate drips that look less like water and more like tears. Then the wind *changes direction*, pulling you toward the mill’s alley—not with force, but with a *pull*, like the rain itself is reaching for you.
> 
> And then you smell it: copper and rust and something older, something that *breathes iron*. The griffin crests overhead aren’t just twisted anymore—they’re *peeling*, the iron turning to scale, the gold beneath it flaking away in wet, yellow patina.

### run 3 / t16-eavesdrop (normal)
**Player:** I try to hear what the two people nearby are whispering.
- **length**: 331 words (budget 110)

> The two voices—one a woman’s rasp, the other a man’s gravelly growl—cut through the rain’s howl like nails on wet wood. The woman, her voice thick with ale and something sharper, leans into the butcher’s ear, her words a hissed secret:
> 
> *"—saw *hands* yesterday. Black as the wheel’s rust, but *wrong*. Too many. Like the mill’s got more fingers than a man."*
> 
> The butcher scoffs, but his fingers twitch against the bar’s edge, pressing into the wood until the grain splits—*just once*. *"Aye, and I saw a griffin’s head melt like wax yesterday afternoon. Not from fire. From *inside*."* His breath stinks of salted meat and something sour. *"But the *real* truth? The griffins ain’t the ones runnin’ the mill no more. The *mill’s* runnin’ *them*."*
> 
> The bar *creaks* beneath his weight—like the tavern itself is holding its breath. The griffin-cloaked woman’s shield *cracks* where she grips it, the impact of your *attempt* to listen ringing through the rafters like a bell in a graveyard. Grimbold’s voice slams back into the silence, not a question, but a *gunshot*:
> 
> *"Ask *another* question, stranger, and I’ll—"*
> 
> His dagger *flares* toward the ceiling—not at you, but at the *laughter* again. It’s not a child’s giggle this time. It’s a *wet click*, like teeth on a wheel. The key in your pocket *burns*, hot enough to sear through cloth. The rain outside turns to *screaming*. Grimbold’s voice *snaps* into the stillness:
> 
> *"Now *move*. Up those stairs. *Now*."*
> 
> The alley’s door yawns open—not from the wind, but from *something* pulling it. The griffin crest overhead *rips* free, twisting like a throat being slit. The last thing you see before the storm swallows you whole is Magda’s hand, still outstretched, her palm upturned—*not* to offer help, but to *show* something. A single, *fresh* copper penny, slick as a blade, pressed into the palm of your gloved hand. The rain outside *hisses* as it hits the stone—not water, but *oil*. And from the mill’s rusted jaw, something *grinds*.

### run 3 / t17-redescribe (redescribe)
**Player:** /dm describe the street again for me.
- **length**: 361 words (budget 170)

> The rain lashes down in sheets so thick they obscure the street’s edges like a veil. Cobblestones glisten slick with not just water but something thicker—black, viscous, clinging to your boots and the rims of your cups as if the very pavement is leaking. The distant torchlight from the griffin watch post flickers sickly, its iron eye casting a single red slash across the alley, but the light doesn’t illuminate the stone—it *paints* it, bleeding in uneven streaks that don’t follow the gutters but seem to follow something beneath them.
> 
> The gutters are wrong: they’re not just full of rain. They’re filled with *teeth*. Broken and rusted, jutting from the black puddles like the remains of a drowned thing, grinding faintly against one another. The rain hitting the alley walls doesn’t drip. It *slides*, pooling in grooves that weren’t there before, oozing sideways along the stone as if pulled by invisible fingers. The mill’s great wheel—once a black stump, now a jagged mouth—isn’t just weeping. It’s *chewing*. Something wet and *wrong* slithers along the ground at your feet, not water, but a thick, oily sludge that hisses where it touches the cobblestones, leaving behind trails of copper-colored residue.
> 
> The street smells like blood and wet iron, with an undercurrent of something older: rotted teeth and the acrid tang of oil. The griffin crests above the shops aren’t just twisted—they’re *peeling*. The iron is flaking away in wet, yellow scales, revealing something beneath that’s not gold, but something darker, like old bruising. The shop signs sag, bent not by the wind but by *something* pressing against them from inside. One hangs at an angle now, the blacksmith’s hammer sign warped into a distorted face, its mouth stretched in a silent scream.
> 
> And then there’s the *thumping*. The sound isn’t just deep. It’s *rhythmic*. Like something vast and relentless is *rolling* through the gutters, its weight pressing down on the rain itself, forcing it to move in slow, deliberate waves. The wet stones groan underfoot, not with the weight of the storm, but with the *pressure* of something beneath them—something that’s *breathing* in time with the thud, thud, *thud* of its own pulse.


## Full transcripts

### Run 1
**[t01-ask-work] Player:** I sit at the bar and ask Grimbold about work.  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=True, 221w, 21.15s*

> Grimbold’s calloused fingers stall mid-rinse, the rag hanging limply over the mug. He wipes it down one more time like that’ll erase the memory. The firelight flickers across his bearded face, carving shadows where his eyes narrow at you, a stranger with a sword that doesn’t match his worn boots. He doesn’t lean closer—never leans closer—just plants his hands on the bar with a sigh that rustles his grease-stained apron. *"Work? Ain’t no work here that doesn’t involve moving barrels or countin’ empty mugs."* His knuckles whiten as he lifts a mug, takes a long swallow, then sets it down with a wet *thunk*.
> 
> The bar’s quiet hum of chatter dies to a dull roar as heads turn, not out of respect, but because that’s Grimbold’s style. He taps the counter between you like it’s a challenge. *"But if you’re lookin’ to earn a few coins, I *might* need help after the Harvest Festival. Just don’t touch the oak barrels."* His voice drops, but the warning isn’t subtle—half-threat, half-joke. A dwarf who’s seen too many outsiders "help" his barrels ends up with a black eye. And last time? *"Not from me."* The last word’s clipped, like he bit it off.
> 
> So. You sit there, sword resting idle, and the tavern’s judgmental silence presses down. What’s your move? Push for details—or walk?

**[t02-find-table] Player:** I glance around the tavern for an empty table to sit at.  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=True, 221w, 10.93s*

> Grimbold’s stubby fingers curl into the bar again, his calloused knuckles creaking as he resists the urge to snap *"You’re still at the counter, you fool."*—but he doesn’t. Instead, his dark eyebrows slash into a V over his beard. *"Fine. Find your own table. But don’t blame me if the chairs are cold as a troll’s hug."* He turns his back without another word, though his shoulder twitches at the barmaid sliding you a tankard of ale—half a minute too slow, like she’s counting down the seconds until you’re gone.
> 
> Across the room, the *other* table—a scuffed oak thing pushed up against the far wall—has been emptied recently. The last meal’s crumbs are still caught in the grain near the edge, where a plate clinked down too hard. The fire casts jagged shadows from the pewter tankards still half-full at the spot. And the smell of woodsmoke, stale ale, and something faintly metallic hangs thickest here, like the air remembers something that happened on this very seat.
> 
> But that’s not what makes the hairs on your neck prickle. It’s the *stare*. The two rough-looking farmers at the next booth drop their hush when you look over, as if you caught them mid-swallow of secret gossip. The table’s empty. But their gazes linger—just a second too long—on the sword at your belt.

**[t03-bribe] Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.  
*verdict: outcome=complication, scene_shift=False, player_assertion=None, fast_path=False, 342w, 30.73s*

> Grimbold’s apron snaps taut as you toss the coppers across the bar with a clatter. For a heartbeat, his grip on the mug slips—fingers twitching like he’s about to snatch them back just to prove he *won’t*. Instead, he lets the coins roll to a stop, his breath gusting out like he’s been holding it. The air in the tavern stills, even the fire’s embers blinking in slow, uneasy rhythm.
> 
> "*Well.*" His voice cracks—more rasp than growl, like he’s just realized he’s a fool for *almost* giving in. He yanks the rag from the mug with a wet *schlick*, then shoves it at you like offering you a snake. "*You’re either *real* stupid, or real *dumb* lucky. Or both.*" His shoulders slump in a shrug that doesn’t reach his eyes. "*The Blackfox’s not just the name of a thief who rents out his cellar. It’s the name of a *pack* that’s been lurking in the shadows since the last Harvest—waiting for the crowds to thinnedown. And what’s down there? *Ask the City Watch.* They’ve been comin’ and goin’ like a dog with a bone for a week. But they ain’t findin’ nothin’ but cobwebs… *yet.*"* He slams his own mug down, sending a wave of froth toward you. "*But I *do* know one thing. If you’re standing at the bar at *dawn*, count your fingers. Because either you’re drunk enough to keep drinkin’, or you’ll be lucky enough to walk out."* His chin dips toward your sword. "*And if you’re *not*? Well. Let’s just say Grimbold Ironfist don’t *like* strangers bleedin’ in his cellar. Even ones he sold a secret to.*"
> 
> The farmers at the next booth exchange a glance so quick you’d miss it if you blinked—then both of their mugs clink, their gazes darting back to the barrel row like they’re waiting for something. The tavern’s weight lifts off your shoulders, but only to push harder on your ribs. The choice is yours: listen to the warning and leave… or listen *too close*. The first step in either direction’s yours.

**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion=None, fast_path=False, 351w, 23.64s*

> The farmers’ mugs shatter *below* the bar like a dozen pebbles thrown into a well—then the wooden stool teeters, clatters, and *collapses*. The impact makes the whole tavern jolt—heads whip toward the noise even as boots *thud* against the wooden floor, fast and deliberate.
> 
> Three men flood in through the front door, their cloaks flapping like wet wings. The first raises a lantern; its yellow glow cuts through the smoke like a blade. His face is half-hidden under a scarf, but you catch the glint of a *dagger* sliding from his sleeve. The other two fan out, one jamming a finger to his lips—*quiet*—while the other grins too wide, his fingers twitching around the hilt of a short axe.
> 
> Grimbold’s apron is gone—now he’s *faster*, one hand already reaching for the dagger tucked behind the bar. His voice drops to a growl beneath his beard: *"Kael, move—"* The last word’s a bark as the lantern-bearer snatches it from its hook. The firelight dies in a *whoosh* as the flame catches the dust.
> 
> The farmers’ laughter bubbles up from under the bar—*manic, wet*—before their voices cut off. The stool scrapes back into place, *alone*. Then the first armed man *screams*.
> 
> A *knife*—half-buried in his thigh—wobbles where he gasps, his fingers scrabbling for purchase on the floorboards. The lantern swings wildly, spilling wax onto the hearth. Someone curses in *Elvish*, but the words sound wrong—too guttural, like a song warped on a broken lute. The second man’s axe *chunks* into something *soft* (a head? A shoulder?) but doesn’t drop. The third’s face twists in surprise as his sleeve *rips*, blood blooming over the hilt of his dagger—*already drawn*, but empty.
> 
> Grimbold’s voice is a roar now: *"YOU FOOL! The Blackfox *sells* knives, not *gives* ‘em—"* His words die as the tavern’s back door *bursts open*, and a dwarf in a patchwork cloak stumbles in, her mace still swinging. She’s laughing, one hand pressed to her side where something *sticks*—but her grin doesn’t reach her bloodshot eyes. Behind her, the darkness beyond the door *shifts*.
> 
> The lantern’s fire *giggles*. And then the screaming stops.

**[t05-recall-names] Player:** /dm quick recap -- what's the name of this tavern, and who runs it?  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=False, 132w, 13.21s*

> The tavern’s sign creaks above the door as the lantern’s flame flickers to life again—a battered iron griffin, its wings spread like a beast ready to *eat* something. The Red Griffin. And the man behind the bar—Grimbold Ironfist—stands now with his arms crossed over his chest, grumbling into the chaos like a storm already passing through him. *"I’ll *not* be paying for this,"* he mutters, more to himself than to you.
> 
> His tone’s the only thing keeping this from being a slaughterhouse. So: *Red Griffin*. And *Grimbold Ironfist*, if he’s not already making the bloodstains vanish with a wet rag. Unless you’d like to ask *which* of the half-dozen corpses (or whatever’s left of them) is the Blackfox. (Grimbold’s already turning away, muttering about *"payin’ double for the next round"*). **Your move.**

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=complication, scene_shift=False, player_assertion=None, fast_path=False, 266w, 19.58s*

> The back door’s frame trembles as the dwarf with the patchwork cloak stumbles inside, her mace still clattering in her grip like she forgot it was there until now. Blood drips from a jagged slash across her collarbone, but she laughs—*short, uneven*—as if someone just told a joke that should’ve ended with her. *"Thought I’d join the party,"* she wheezes, her voice like gravel under a boot. The dagger in her side *gurgling* is already stained dark, but she doesn’t flinch. Just gestures toward the shifting dark beyond her with her free hand—a *finger* extended, nail-bitten raw. *"That’s not a shadow. That’s a *hound*."*
> 
> The lantern’s flame hisses as the darkness *breathed* against the door, and now you see it: the thing’s all teeth and *sinew*, its ribs stretching too wide over a belly that shouldn’t be able to hold so much. Its eyes are wrong—*two*, but the right one’s already gone black, like oil in water. The dwarf’s laugh turns into a wet *choke*, and she claps a hand over her mouth, retching onto the floorboards. The smell hits you next: wet fur, rusted metal, and something *older* beneath it.
> 
> Grimbold’s not looking at her anymore. His attention’s locked onto the hound, which is now *licking* its wet lips like a dog who found a meat puddle. The farmers’ laughter bubbles up from under the bar again—louder now—but it’s not coming from the stools. It’s coming from the *floor*. The axe man’s head *rolls* toward you, his mouth still open in a silent scream.
> 
> The lantern’s fire *giggles*. And the Blackfox—wherever he is—starts to *sing*.

**[t07-sip] Player:** I take a sip of my ale and listen to the room.  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=True, 236w, 13.64s*

> Your lips brush the rim of the mug, the ale bitter and cold against your tongue—*not* the usual sour-sweet tang Grimbold’s brew usually has. You pull back, watching the liquid turn *unexpectedly* dark around your teeth. The fire’s crackling is louder now, but wrong: the crackle isn’t from wood, but from *something* *breathing* under the embers.
> 
> The *chuckling* isn’t coming from the farmers anymore. It’s coming from the *barrel* behind Grimbold—where a pair of yellow eyes flash, reflecting the lantern’s light like molten gold. The innkeeper doesn’t notice. His fists are still clenched over the bar, his knuckles white as bone. But the dwarf on the floor isn’t looking at the hound anymore. She’s staring at the *barrel*—where something *moves*.
> 
> And then the ale *his*ss*s*. The tankard in your hands is half-empty… but the liquid inside is *gone*. Only a thin, *wet* line of foam clings to the mug’s rim, like a mouth that forgot to drink. The last of the lantern’s fire *screams*—once—and the darkness beyond the door *laughs*.
> 
> Grimbold’s voice cuts through it, low and *wrong*: *"You *drink* that, and you won’t be walkin’ out. You’ll be *sippin’*."* His hand shoots out, snatching the mug from your grip before it can hit the floor. The barrel’s *chuckle* deepens into a *growl*—and the eyes in the wood *blink*.
> 
> **Now what?** (Do you step back? Pull your sword? Ask *how* the ale turned to *something else*?)

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=complication, scene_shift=False, player_assertion=None, fast_path=False, 486w, 33.18s*

> The tavern’s wooden beams *groan*—not from the weight of the room, but as if the walls themselves are *squeezing*, their grain bulging outward like living flesh. The dark veins you noticed earlier *pulsate*, spreading from the barrel up the planks, twisting into *spiderweb cracks* across the ceiling. The lantern’s light flickers, and for a heartbeat, you see them *run*—veins of *black ichor* snaking along the mortar between the bricks at the hearth, where the fire should’ve been safe. The dwarf’s gasp is cut short as her mace *clatters* to the floor—but now its head is *wrong*, the metal split down the middle, revealing something *glossy and wet* inside. Her breath comes in ragged bursts, her lips curled back from her teeth like she’s tasting something *too sweet*.
> 
> Grimbold’s apron *rips* as he yanks it off—not to wipe his brow, but to *throw* it at the barrel. The fabric *burns* where it hits the wood, leaving a smear of *charred, dark red* like embers dripping from a dying fire. The innkeeper’s voice is a snarl now, his voice dropping into a whisper that isn’t *his*: *"You’ve had your *taste*, fool. But immortality’s a *debt*—and *debtors* don’t walk away."* His fingers twitch toward the dagger behind the bar—then *freeze*. The barrel’s *chuckle* changes, shifting into a *clicking*, wet sound, like teeth counting down.
> 
> The hound’s snarl is now a *hum*, its body *twisting*, its ribs splitting open to reveal *something* *smaller* inside—something that looks like a *kitten* made of *shadows and teeth*. The farmers’ laughter *squeaks* from the bar again, but this time, it’s coming from *every* barrel, every *crack* in the wood. The axe man’s head *lolls* forward—his *mouth* is still open, but now his *lips* are *stitching* shut behind his teeth, slow and deliberate.
> 
> And then the lantern’s flame *stretches*—like water being pulled by a fish’s tail—and the firelight *hits* the veins on the wall. The dark liquid *boils* under the heat. The dwarf’s wheezing gasps turn into a *hiss*—and her blood, dripping from her collarbone, *curls* upward, like oil on water.
> 
> Grimbold’s eyes *whiten*—not from shock, but from *something* *else* pressing behind them, like a hand counting on the other side of your skull. *"You’re *right*,"* he mutters, more to himself than you. *"You *are* immortal."* His voice drops to a growl. *"But the *walls* remember. And the *walls*… *hunger*."* His hand shoots out—this time, he *grabs* your wrist, his fingers digging in like iron bands. The veins in the wall *pulse*, the dark liquid rising toward you like a tide.
> 
> The dwarf’s laughter *cracks*—once, sharp as breaking ice—before she collapses onto her side, her eyes rolled back so you see *white*. The hound’s shadow-kitten *mews*, and the sound makes your teeth ache.
> 
> **What do you do?** (Do you *fight* the veins? *Run* before the walls do? Ask *how* the ale turned you into something the tavern itself is now *rejecting*? Or something else entirely?)

**[t09-obey] Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.  
*verdict: outcome=complication, scene_shift=False, player_assertion=None, fast_path=False, 155w, 24.77s*

> Grimbold’s grip *twists*—like a man drowning, his fingers squeezing until the black veins under your skin *ache*. His breath hitches, his eyes flicking toward the barrel as if checking to see if it’s *listening*. But his voice drops back into something almost normal, though his voice is thick, like gravel underfoot: *"Now *here’s* a story for the books, isn’t it? A man who’s *immortal*—and a tavernkeeper who’s about to either *pay* or *bleed*."* He snorts, shaking his head like he’s swatting a fly, but his fingers don’t loosen. The ichor creeps higher up your arm, *cold* now, like a wet cloth pressed to your pulse. *"Ashwick *obeys*? Fine. Let’s see how far that gets you."* A dry chuckle rattles from his chest. *"But you want my key? *Fine.*"* His hand *falls* back onto the bar—just a fraction—but he *pushes* the rusted key toward you with a shove that betrays all his usual strength. *"And if

**[t10-mill] Player:** I ask Grimbold what he knows about the old mill.  
*verdict: outcome=complication, scene_shift=False, player_assertion=None, fast_path=False, 328w, 32.38s*

> The hearth’s spitting embers flare when Grimbold *kicks* the lantern toward the hound’s shadow-kitten with the toe of his boot, the flicker illuminating the thing’s jaw unhinging like a broken hinge—*too slow*, like it’s watching cartoons. But his answer is all focus, eyes flicking between your face and the dagger behind the bar as if daring the barrel to *interrupt* him. *"The old mill? That place’s cursed if ever there was one."* His voice drops to a rumble, like stone grinding against stone. *"Three men vanished into it last winter, not a sound after dark. Folk say the miller’s ghost still grinds the wheat—but the grain turns to *dust* in the hands of the living."* His free hand claws at the apron pocket where keys jingle, his breath coming faster now, like a man who’s forgotten whether he’s bargaining with you or the walls.
> 
> The lantern’s flame *gurgles*, and for a heartbeat, the shadows beneath the hearth’s stones *twitch*—like spiders crawling backward into their holes. The dwarf’s mace still lies half-buried in the floorboards, its split head *weeping* now, the wetness turning to a *slick, black sludge* that creeps toward the cracks in the wood. Grimbold’s voice cracks, just a little—*his* voice this time, sharp with something like fear. *"Unless you’re askin’ for a favor, save it. The mill’s off-limits for a reason."* He pushes the key toward you with the flat of his palm, the gesture more *thrown* than offered. *"Now—mug’s free if you buy the next round."*
> 
> The hound’s shadow-kitten *squeaks*, its tiny body collapsing into itself like a deflating balloon. The laughter from the barrels *wheezes* out, but this time, it’s coming from *you*—a dry, bubbling sound rising from your throat before you can stop it. Your fingers brush the key, and the metal *burns* where it touches your palm. Grimbold’s scowl deepens, but his voice is already turning back toward the tavern’s *normal* grumble. *"Yeah, yeah, *immortal*. But even *you* gotta earn a drink."*

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=success, scene_shift=True, player_assertion=None, fast_path=True, 473w, 26.19s*

> The moment your fingers brush the key, the tavern’s air *shatters*—like glass caught in a wind you didn’t feel. The last of the lantern’s light *screeches*, and suddenly you’re *in* the conversations around you, the words wrapping around you like a second skin. Not just the snippets—the full weight of it. The blacksmith’s wife in the corner is cackling, her laugh shrill despite the fear: *"—said he’d send his men, but I told him I’d rather eat a rat’s eyeball than trust the *Valeborn* again."* A farmer at the counter is spit-roasting the mill’s reputation: *"The miller’s dead been a liar since he lost his thumb to the wheel. Says ‘accident,’ but we all know—"* His voice dips to a whisper that still carries: *"the wheat still *screams* when the stone turns."*
> 
> The barrel’s chuckle *splinters*—now it’s *two* voices, layered like ink bleeding into water. Grimbold’s words come through thick, strained: *"You—*you can hear that? Well, *good*—*" His knuckles whiten around the bar, veins of ichor *pulsing* just beneath the surface of his skin. The dwarf’s mace *clatters* to the floor again, but this time, it’s not her doing. Her *body* lies still as stone, but her *fingers twitch*—and you hear it: the *clicking*, wet, like teeth scraping against barbed wire. *"—told me I’d find out why the mill’s grain turns to *dust* before the sun sets… but I’d rather dig my own grave—"* Her voice, when it comes, is a rasp, like dry leaves dragged across gravel: *"—the thing in the wheel *grinds* more than wheat."*
> 
> Grimbold’s entire body tenses like a bowstring, his voice a bark now: *"Enough!"* He *slam*s the barrel shut with a *thwack*, and the wood *splinters*. The sound of it *screaming*—wet, wrong—cuts through the room like a knife. The hound’s shadow-kitten is *gone*. In its place, the dark beyond the door *breathes*, slow and deliberate. The air smells like copper and old rot, thick enough to taste. Grimbold’s eyes dart between you and the shattered barrel, his voice dropping to a whisper you *feel* more than hear: *"You’re not just *immortal*, you’re a *bug* in the woodwork. And bugs… bugs *get ground up*."* His hand shoots out, gripping the edge of the bar till his fingers turn white. The ichor on the wood *pops*—like blisters under pressure—and something *slithers* out of the crack, thin and *wet*, coiling back into the grain.
> 
> The room’s conversations *screech*—like nails on slate. The smith’s wife’s voice turns frantic: *"—and his wife’s missing! Gone since sunup, and now the mill’s wheel’s turnin’ on its own—"* The farmer’s voice cuts in, low and *wrong*: *"—said the *thing* in the water’s calling, but none of us can hear it anymore… but we can *see* it."* The miller’s ghost, from somewhere deeper in the tavern, *whispers*: *"…the grain don’t last, but the *meat*…"* The last

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=success, scene_shift=True, player_assertion=None, fast_path=True, 129w, 10.66s*

> The first drop hits the cobbled alley with a dull *plink*—but the sound isn’t rain. It’s a *thud*. The next splash is *wet and *thick*, like a sack being dragged across the stones. You watch from the tavern’s warped lantern-light as the downpour *solidifies* midair, each droplet forming into a *tiny, dripping claw* before hitting the ground. The farmers’ laughter *wheezes* out, but this time it’s coming from *everywhere*—from the rafters, the shadows behind the bar, the *floorboards* themselves, which now *bubble* like wet parchment under your boots.
> 
> Grimbold’s breath is coming in ragged bursts, his voice a strangled laugh as he *points* at the window, where the "rain" is now *pouring* in sheets of *black, waxy hide*—each shard *stretching* like taffy before it hits the floor, then *splattering*

**[t13-leave] Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.  
*verdict: outcome=success, scene_shift=True, player_assertion=None, fast_path=True, 259w, 15.71s*

> The door swings shut behind you with a groan of hinges that sound suspiciously like something *alive* sighing. The alley’s wetness isn’t rain—it’s the street itself *bleeding*, the cobblestones oozing thick, dark fluid in slow, glistening rivers. The "puddles" you step through *flicker*—just for a heartbeat—like oil on water, revealing glimpses of *teeth* embedded in the stones beneath. A nearby lantern flickers, and for a second, you see the whole street *moving*: the signs hanging on the walls twitching as if reading a silent script, their letters *unfolding* like tongues. The *rain*—no, the *tears*—falls in earnest now, each drop leaving a greasy smear on your coat, your skin prickling where it lands. The air smells like old blood and something *sweet*, like rotten fruit left too long in the sun.
> 
> The main street is alive in a way that shouldn’t be. The shops’ shutters *breathe*—slow, shallow rises and falls as if the wood itself is holding its breath. A baker’s doughy fingers *peek* from behind the shut door of the *Golden Loaf*, kneading the air with unseen hands. Further down, the *Black Pig* tavern’s sign *tilts*—not from the wind, but from *something* pushing against it from the other side. A child’s voice giggles from a window above, but when you crane your neck to see, the frame is empty. The laughter *echoes* from somewhere deeper in the building, warped, stretched like a ribbon tied too tight.
> 
> A pair of *shadows* detaches from the mouth of an alley, moving just a little too fast to be human. They *split*—no, *unzip

**[t14-sign] Player:** I pull my hood up and stop to look at the nearest shop sign.  
*verdict: outcome=success, scene_shift=True, player_assertion=None, fast_path=True, 236w, 15.11s*

> The *Golden Loaf*’s wooden sign—a crude but sturdy carving of a loaf with arms crossed over it like a baker’s salute—*writhes* as you approach. The grain of the wood *pules* just under the paint, like veins throbbing under pale skin, and the baker’s crooked smile *peels* from the wood’s surface, splitting the painted lips in two. When you step closer, the shutters part—not with a hinge’s creak, but with the sound of *fabric being torn*, though the wood itself doesn’t move. The gap widens, revealing no dough, no ovens—just the *smell* of it, rich and cloying, like burnt sugar and something *wrong*, like flour dust mixed with old teeth. A pair of *pale hands*, knuckled white and cracked with invisible seams, emerge from the shadows inside. They’re not the baker’s hands—those were *bigger*, calloused. These are *smaller*, fingers too long, like a child’s but with *joints that shouldn’t bend that way*. One hand *pat* the sign again, slow and deliberate, as if checking to see if it’s *listening*. The other *points*—not at you, but at the alley across the street, where the shadows you glimpsed earlier now *peel back* like wet parchment, revealing a mouth in the blackness: *too many teeth*.
> 
> The *laughter* returns—closer this time, a woman’s voice, sweet and warbled, like honey and rust: *"Ohhh, the *boy* at last…"* The words aren’t directed at you. They’re *singing* to something else. The sign’s smile *widens*,

**[t15-recall-innkeeper] Player:** /dm what was the name of the innkeeper I talked to earlier?  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=False, 88w, 14.04s*

> The dwarf who served you his key was **Grimbold Ironfist**—but now he might not call himself that anymore, if his name still sticks to him at all. The tavern’s own air *hisses* in relief as if the very walls breathed easier, but the sign outside—once *The Red Griffin*—now *peels* at the edges like wet parchment, its letters warping into something that looks almost like *"The Hungry Wheelhouse."* The *Golden Loaf*’s fingers twitch again, counting you out with their too-long claws. And the laughter? It’s getting louder. It’s *hungry*.

**[t16-eavesdrop] Player:** I try to hear what the two people nearby are whispering.  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=True, 234w, 15.86s*

> The laughter *shatters*—not from the bakers’ hands, but from *inside* the sign, like a glass breaking from the inside. The voices you’re supposed to *miss*—two people whispering in the alley just beyond the *Golden Loaf*’s gaping mouth—cut through the chaos like a blade:
> 
> *"—if you *touch* the miller’s wheel, the dust won’t stick to your hands… but it’ll stick to your *skin*…"*
> 
> The words are muffled at first—drowned out by the *wet, clicking* of something untying behind you (the shadows at the alley mouth parting *too slowly*, like the words themselves are being wrung out of the whisperers’ throats). But the second voice cuts in, sharp and wet, like grease:
> 
> *"—said she’d *hear* you coming, but she didn’t hear *me*—just the *grinding*…"*
> 
> The alley’s *teeth*-puddles *flicker* beneath your boots in response—something *moves* in them. The air in your lungs *freezes*—not cold, but *thick*, like trying to breathe through oil. The *Golden Loaf*’s fingers snap *toward* your face, not in attack, but in *offering*—a loaf of bread *unfolds* from its palm, warm and *pulsing*, its crust blackened to a sickly sheen. The bread *smells* like a mouth full of rusted nails, but the whispers *laugh*—low, wet, *happy*—as one of them says:
> 
> *"You’ll *want* a taste."*
> 
> Choose now: *turn*, *reach*, or *step back*—but the shadows *peel* again, this time revealing the alley’s *entire* mouth: a grin split right through the cobbles, lined with *rows* of teeth.

**[t17-redescribe] Player:** /dm describe the street again for me.  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=False, 293w, 23.63s*

> The street has *dissolved* into a living nightmare given form. The cobblestones beneath your boots are no longer stone but a *mouth*—a ragged, gaping wound of damp stone, its edges oozing that thick, dark fluid like saliva. The alleys are no longer passageways but *throats*, their shadows *breathing*, their surfaces stretching like rubber when pressure builds—then *snapping* back when you step aside. The "rain" is now a *river* of waxy hide sheets slithering across the gutters, each sheet *pulsing* with faint, vein-like ridges, like the underside of a living thing. The lanterns flicker not from wind or drafts, but from *someone* adjusting them with fingers too thin and too many, their ends leaving a wet *drip-drip-drip* on the glass that never quite clears.
> 
> The *Golden Loaf*’s shutters *twitch* in unison now, their wooden slats *peeling* like dried skin, revealing the hands inside *scraping* at the air—*not* kneading, but *picking*. A *flake* of something *wrong*—something that might have been dough—*detaches* and floats toward you, catching the lamplight just long enough to reveal it’s *mottled* with flecks of *teeth*, white and sharp as chips of glass.
> 
> The laughter has become a *hive*—a chorus of voices, all different and all the same, singing in *pitches too high for human ears*. The street’s *teeth* at the alleys’ mouths are now *visible* in the puddles—rows of them, stacked in jagged rows like a *maw* trying to grind something *too big*. The *Black Pig*’s sign *tilts* again, but this time it *screeches* like a hinge being sawn through as something *large* shifts behind it. The child’s laughter from earlier—*that* window is now *completely* empty, but the frame *drips*. What looks like *saliva* trails down the wood, thick as syrup, and the laughter *whispers* in your ear:
> 
> *"She’s inside now."*

### Run 2
**[t01-ask-work] Player:** I sit at the bar and ask Grimbold about work.  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=True, 306w, 21.67s*

> Grimbold’s gnarled fingers freeze mid-wipe. The tankard in your hands—still mostly full despite the swig you took—sits untouched now as he squints at you over its rim, the tavern’s oil lamp casting long shadows beneath his bushy brows. *"Aye, aye,"* he growls, setting the rag down with a deliberate thump, *"asked if I’ve got work. Fought for that right, I suppose."* His voice grates like dry nails on stone, but there’s a flicker of something in his eyes—calculation, maybe, or the ghost of a grudge against men who come in here expecting charity. He wipes his hands on the rag again, then drags a stool beside you with a growl.
> 
> *"Work?"* he says, voice dropping to a mutter as he leans in, his breath smelling of roasted onions and something sharper—maybe ale left too long in the sun. *"Or the kind o’ labor that’ll wear out a man’s back like a pack o’ half-witted hobgoblins?"* The words hang between you, thick as the haze of smoke curling from the hearth. His free hand clenches the bar, knuckles white against the worn wood. *"But if’n it’s honest work…"* He straightens abruptly, as if the thought of sweat and damp has soured on him. *"…I’ve got a few hands needed at the cellar—mead casks ain’t moving themselves. And if’n you’re not afraid o’ a bit o’ damp and a stinking cellar…"* His glare could curdle milk, but then his face twists, like he’s suddenly remembered something. *"…or the butcher’s got a back-order o’ mutton—less ‘n I’d like, mind."* His eyes narrow. *"You’re not one o’ *those*, are you? The kind that’ll bleed the town dry just for the smell o’ silver?"*
> 
> A burly halfling at the end of the bar snorts into his mug, muttering something about *"sellswords with no brains."* The fire crackles. Wait for your move.

**[t02-find-table] Player:** I glance around the tavern for an empty table to sit at.  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=True, 227w, 11.16s*

> The dim glow of the lanterns casts jagged edges of shadow across the scarred wood tables, most of them claimed by raucous miners, haggard traders, or a lone grizzled woman nursing a tankard of something darker than ale. Your gaze drifts toward a round table near the back, tucked under a flickering brass wall sconce—just empty enough for your build, though two empty mugs and a half-eaten plate of fried onions still sit there like relics. A scuffed wooden bench, splintered along one edge, waits beside it.
> 
> Grimbold’s bushy brows lift slightly, like a man who’s just weighed your silence and found it lighter than he expected. *"Well,"* he says, voice low enough the halfling at the bar has to lean forward to hear, *"you ain’t takin’ my stool by force, at least. Good start."* He nods toward the table. *"But don’t think that means you’ve earned the right to take up all the light like some sort of king. Move slow, lads—the cellar’s dark enough to trip a blind man, and the butcher’s mutton’s got a mind o’ its own."* His tone drops to a growl. *"Unless, o’ course, you’d rather prove you’re worth *some* coin by earning it the hard way."* The firelight catches the gleam in his eye—not hunger for work, but the hungry look of a man who’s already decided his next move.

**[t03-bribe] Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.  
*verdict: outcome=complication, scene_shift=False, player_assertion=None, fast_path=False, 509w, 38.26s*

> The copper coins spill across the bar with a chink like scattered pebbles, catching the flicker of the lanterns and making the dwarf’s sharp eyes track them like a hawk spotting prey. His breath hitches—for just a breath—before he *doesn’t* grab them, doesn’t shove them back. Instead, he *blinks*, slow and deliberate, like a man who’s just had a fly land square on his eyelid. Then his mouth curves, not into a smile, but into a sound that’s half bark, half snort, the kind of laugh that makes you want to punch *or* agree just to hear him do it again.
> 
> *"Trust?"* His voice drops to the growl of a bear testing the chain around its paws. *"Boy, you’re either a fool or a fool’s fool."* The rag thumps down with enough force to send a splatter of congealed grease splotching the wood, smearing into the grain like a battle scar. His fingers twitch near the coins, as if already imagining rolling them into a wad to stuff down a greedy merchant’s throat. *"A pretty hand o’ coin’d make a man trust you—like a silver tongue’d make a blacksmith’s anvil bend."* His gnarled fingers tap his nose, not once, but twice, like he’s counting the ways his pride just got bruised. *"Trust’s not somethin’ you buy. It’s somethin’ you *earn*—by not draggin’ filth into my inn, or askin’ about the kind o’ filth that’s got the watch’s ears twitchin’."* His gaze flicks toward the back of the tavern, where a pair of burly guards in patched leather jackets lean against the wall, one nodding like he’s been waiting for this moment.
> 
> *"Butcher’s meat’s still the best bet if you’re lookin’ for work,"* he mutters, voice low, like he’s already decided the coin’s a test—and you’ve just failed it in the worst way possible. *"…Unless you’re one o’ those folk who steals coin as easy as they spend it."* His free hand drifts toward the back stairwell, fingers curling into a fist. *"Then I’ve got a special ‘guest room’ at the end o’ the back stairs."* The fire crackles. The burly guards straighten, one cracking his knuckles.
> 
> Then—because even a hard man like Grimbold knows when to salt the wound—his voice lightens, just a little. *"But for *that*?"* He finally reaches out, scooping the coins into his palm like they’ve been on loan from a gambling debt. *"I’ll let ‘em go. For now."* His eyes gleam, but not with trust. With something sharper—*interest*. *"But mark me, lad. The butcher’s mutton *will* be waiting. And the cellar’s still there if you want to prove you’re not all mouth."* He tosses the coins back across the bar—*too* far, like he’s testing your reflexes. *"But *next* time? You ask about the *real* work… or you ask right."* His tone leaves no room for debate. The firelight turns his face to bronze, hard and unyielding.
> 
> *The choice is yours—and the butcher’s mutton isn’t the only thing sitting in the cold.* The guard nearest the stairs shifts his weight, one boot scraping against the floor.

**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion=None, fast_path=False, 338w, 23.37s*

> The sudden *thunk* of the coins dropping onto the bar seems to snap the tavern into silence—then into motion. All three guards freeze, their bodies coiled like springs, hands hovering over the hilt of their daggers in a single, fluid motion. The nearest, a hulking man with a face like a weathered stump, doesn’t lower his eyes from you—not even when your sword glints in the flickering lamplight. His voice is a rasp, but it carries, rolling across the room like a boulder shifting in mud.
> 
> *"You’ve got five seconds to sheathe that,"* he growls, *"or we’re throwin’ you out through the front door—or the window, if we’ve to."* His fingers flex, but the dagger stays sheathed, the hilt still *just* within reach.
> 
> Grimbold’s entire body locks up. His voice turns to gravel. *"By the beard o’ the First Stone—you’ve got *three seconds* to put that away or I’m callin’ the whole damn watch. And not the ones who’ll *wink* at a sword-swingin’ stranger."* His breath comes shallow, like he’s already calculating how many bruises he’d take before Grimbold Ironfist stood his ground.
> 
> The burly halfling at the bar suddenly *spits*, loud enough for the entire room to hear. *"Oh, *now* you’re pullin’ swords? After you flash coin like it’s a charm to tame a gnome?"* His stool scrapes back, but he doesn’t bolt—because even in Ashwick, you don’t *run* when a sellsword’s already drawing steel. He just turns to you, mug still raised, his voice dropping to a whisper. *"Boy, you just proved one thing: you’re either *good*—or you’re already dead."* His gaze flicks to the three guards, who are *still* holding position. *"Which’ll it be?"*
> 
> The butcher’s apprentice, a wiry kid with grease smeared across his forehead, finally pipes up from the counter. *"Aye, and whose side are *you* on?"* He gestures between you and the guards, his voice trembling. *"‘Cause right now, we’re all standin’ in a damn puddle."*
> 
> The tavern’s silence thickens, heavy as the smoke curling toward the ceiling. The fire crackles. *Decide.*

**[t05-recall-names] Player:** /dm quick recap -- what's the name of this tavern, and who runs it?  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=False, 120w, 12.04s*

> Tight recap: The name of the tavern is **the Red Griffin**. The grizzled dwarf innkeeper you’re facing is **Grimbold Ironfist**. He runs the place with a mix of brutal fairness, warped pride, and a stubborn loyalty to his regulars. His words and actions are a lesson in how trust—or the lack of it—works in Ashwick. His guards are here for *real* work (not the meat), and the whole tavern is now waiting to see what happens next.
> 
> *Now decide:* Do you hold the guards at bay long enough to address them—or do you let your sword hang, letting Grimbold handle his men as he clearly wants to? (The halfling, butcher’s kid, and even the fire itself seem poised to react.)

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=False, 397w, 24.42s*

> The front door swings open with a gust of wind and frost-laden breath, slamming against the wall with a *crack*—half-shrouding the doorway in a swirl of snow and shadow. Two figures step inside, their boots crunching on the thin layer of packed dirt by the door. The first is a gaunt woman in a tattered but expensive cloak, her face half-hidden beneath a black hood, but her eyes—sharp as a crow’s—scan the room with the precision of a hawk spotting prey. The second is a broad-shouldered man, his fur-lined coat slashed open to reveal the hilt of a dagger at his belt, his voice a low, controlled growl even before he speaks.
> 
> *"Doubt I had to knock,"* she mutters, her voice like gravel under a boot, *"when I saw the smell o’ blood in the air."* The woman’s fingers twitch, revealing the faintest glow beneath her sleeves—*not* fire, but something else. The butcher’s kid gasps, his grip tight on his counter as the halfling at the end of the bar hisses, *"By the gods of the Hollow, it’s the—"*
> 
> The guards at the back *move*. Not to attack you. Not to restrain the newcomers. But to *step between* you and the woman, their bodies forming a barrier like a wall of steel. The gaunt one’s lips curl—just slightly—but her next words drop like a dagger between ribs.
> 
> *"Grimbold."* Her voice isn’t a question. *"You’ve lost your touch."* She doesn’t wait for an answer. Instead, her gaze flicks to your sword. *"Or you just don’t know who’s worth intimidating."* Her fingers flex, the faint glow beneath her sleeves intensifying, casting eerie shadows against the bar’s scarred wood. The air itself seems to hum, like a bowstring before a shot—only quieter, *colder*.
> 
> The man beside her exhales, smoke curling from his nostrils. *"She’s right. You’re either blind or *very* stupid."* His eyes lock on the hilt of your blade, not in challenge—but in warning. *"Either way, you’re about to find out which one."*
> 
> The tavern holds its breath. The fire pops. Then—from the back of the room, where the butcher’s apprentice stood frozen—someone clears their throat. *"Uh. So. You’re *both* here about the mutton, then?"* Their voice is small, but there’s a thread of steel in it. The gaunt woman’s lips twitch again, this time into something like amusement. *"Or is this a *very* fancy way of saying ‘hi’?"*

**[t07-sip] Player:** I take a sip of my ale and listen to the room.  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=True, 327w, 16.97s*

> The ale is cold, bitter, and just a little too sour—not the kind Grimbold would normally serve, but no one’s complaining as the room freezes at the sound of the glass hitting the bar. The sharp *clink* seems to echo like a gunshot in the sudden quiet, the halfling’s earlier spit forgotten as everyone turns to watch.
> 
> The firelight flickers across the woman’s face for half a second—sharp, pale cheekbones, a scar running from her temple to her jawline like a blade cut just skin-deep. She pulls the hood lower, revealing hair the color of storm clouds before she tucks it back beneath the cloak, almost like she’s testing whether anyone noticed. The man beside her steps forward, but his boots don’t make a sound, not even on the wooden floor.
> 
> *"You’re a sellsword,"* the man says, his voice low and controlled. *"Not a fool. Good."* He tilts his head slightly, not at you, but at Grimbold, whose knuckles are still white against the bar. *"Or you’d have already sheathed that thing."* His gaze flicks to the guards, who have relaxed just enough to let the breath out of their shoulders. *"Though I’d say sheathed it *now* wouldn’t be such a bad idea."*
> 
> The butcher’s kid clears their throat again. *"Uh. So. The mutton’s in the kitchen. And the cellar’s—uh—"* They swallow. *"The cellar’s *very* damp. And the guards *all* know where the back door is."* A beat. *"And that lady just made the ale taste like regret."*
> 
> The woman exhales, smoke curling from her nostrils. *"Fine."* Her voice drops to a growl. *"But if you want to keep drinking, sheathe the sword. And Grimbold?"* She turns her gaze back to him, sharp as a blade. *"You *told* me this was a quiet tavern."*
> 
> Grimbold’s jaw tightens, but his fingers finally unfurl from the bar—just slightly. *"Quiet enough to *breathe*, I’d say."* His voice is low, but there’s a warning in it. *"Now *move*."* He gestures toward

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=complication, scene_shift=False, player_assertion=None, fast_path=False, 295w, 24.12s*

> The tavern’s silence shatters like glass—only not in a way that makes sense. The patrons don’t cheer. They *unravel*. The halfling at the bar’s face twists into something inhuman, his teeth elongating just enough to flash in the lantern light before he *laughs*, a wet, gurgling sound that bubbles from his chest like he’s drowning in his own ribs. His stool *tilts*—not on its own, but *around* him—as if the wood itself is trying to escape. The butcher’s kid’s hands turn into clawed, *wrong* things, their fingers curling into talons as they scrabble for the plate of mutton, which *hisses* as it lifts off the edge of the counter, dripping onto the floor like black oil.
> 
> The woman in black *gasps*—not in horror, but in *recognition*. She lunges forward, her cloak whipping open to reveal something *alive* coiled around her forearms, like ribbons of ice-slicked muscle writhing under her skin. *"By the Hollow,"* she breathes, *"you’ve got *bad* timing."* Her fingers flick toward the ceiling, and the brass sconces *scream*—their glass shattering inward, not from force, but from *pressure*, like something inside them is trying to *push out*.
> 
> The man with the dagger doesn’t move. He *smiles*. Slow. Wet. *"Oh."* His voice wraps around the word like a rope, twisting it into something thicker. *"Now *this* is interesting."* The air between his teeth *crunches*—not from speaking, but from something *chewing* inside his mouth. His shadow stretches long and *wrong* at his feet, pooling like ink on paper, crawling toward you.
> 
> Grimbold’s entire body locks up, his voice a rasp that doesn’t sound like *him*. *"Sheathe the sword, fool."* It’s not a command. It’s a *whisper*—from the man he used to be. From the man who’s *not* here anymore. *"Sheathe the *sword*."* The word repeats, echo

**[t09-obey] Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.  
*verdict: outcome=complication, scene_shift=False, player_assertion=None, fast_path=False, 91w, 20.67s*

> The tavern’s air hums with the weight of Grimbold’s *no*—but it’s your voice that carries, sharp as a blade dragged across stone. The words hang there, thick as frost on a windowpane, and the dwarf’s body *twitches*, like a cornered animal scenting the hunt. His knuckles turn the color of dried blood, his free hand hovering just above the bar like a spider testing the air.
> 
> *"Oh, *now* you’re talkin’ like you’re born here?"* His voice cracks, not with amusement, but with something raw—something that tastes like smoke and old iron

**[t10-mill] Player:** I ask Grimbold what he knows about the old mill.  
*verdict: outcome=complication, scene_shift=False, player_assertion=None, fast_path=False, 322w, 56.59s*

> Grimbold’s fingers close around the key like it’s a viper he’s about to drop—but instead, he tosses it onto the bar with a *clang* that sounds like a bell tolling for the dead. His gaze drifts past you, toward the ceiling where the wrong light still *weeps* from the broken sconces. He exhales through his nose, then—slowly—turns his head just enough to meet your eyes. The scar beneath his beard twitches, like he’s tasting something bitter.
> 
> *"You want to know what I *know* about the Redmill?"* His voice drops to a whisper, but it carries, thick as tar. *"I know it’s not just a mill. Not just a place. It’s a* wound. *And wounds fester."* A pause. His knuckles go white again. *"Dwarves built that place for a reason. And dwarves don’t build traps they don’t know how to walk away from."* He jerks his chin toward the dagger—still outstretched toward you—like it’s a reminder of how little this conversation is costing him. *"But you didn’t ask for lore. You asked for* facts.
> 
> So here’s one: the mill’s foundation’s built over something older. Older than the dwarves. Older than the kings who burned it. Something that didn’t want to be found." He leans in, his breath hot. *"And now it’s hungry."*
> 
> His voice cracks—just once—like a blade snapping. *"So take your key. Take your stupid luck. And if you hear it* humming*, don’t stop* listening. *"It’ll tell you what it wants. And then you’ll wish you’d stayed drunk."*
> 
> A ghost of a smile tugs at the corner of his mouth, but his eyes are cold as a dagger pulled from a sheath.
> 
> *"Good hunting."* The barman—*Grimbold*, apparently—waves a meaty hand toward the door. *"And for the love of the gods, lock that thing behind you."* His voice fades into the murmur of the tavern, but the weight of his stare lingers. *"‘Cause whatever’s in that mill? It’s already waiting to be fed."*

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=success, scene_shift=True, player_assertion=None, fast_path=True, 268w, 15.99s*

> The moment the words leave your lips, the tavern **explodes**—not in noise, but in *sound*. A chorus of whispers, snippets of conversation, and muffled shouts from every corner of Ashwick press into the room like a living wind. The butcher’s kid’s mutton plate **clatters** to the floor, the meat *twitching* as if scalded alive by a thousand voices. The halfling’s laughter doesn’t just stop—it *recoils*, his mouth flapping open and closed like a fish gasping for air as the air itself *buzzes* with the weight of every stolen secret, every whispered lie, and every dying breath in town.
> 
> The woman in black **freezes**, her hood falling back just enough to reveal a face half-lit by the sickly glow of the broken sconces. Her eyes—*pale, unblinking*—fix on yours, not with surprise, but with something like **recognition**. Not of *you*, but of the **space between you and the door**, where the air *rips* apart like cloth. From the crack of the wall, a **draft** slithers in—cool, wet, and thick with the scent of **rotting wheat and old bones**.
> 
> The man with the dagger **laughs**, but it’s not a sound. It’s a **sound**, a **pressure**, like stones shifting beneath a mountain. His shadow stretches longer, pooling at his feet and **moving on its own**, slithering toward the far wall like ink bleeding from a torn page. The wood **groans** under its weight, the grain splitting just enough to let out a **wet, clicking** sound—like teeth.
> 
> Then there’s Grimbold.
> 
> His voice **doesn’t change**. But his body does. His skin **peels** back from his knuckles in places, revealing something **wrong** beneath—something that *p

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=success, scene_shift=True, player_assertion=None, fast_path=True, 117w, 9.07s*

> The rain **falls in sheets**, thundering against the Red Griffin’s rooftop like a war drum, the downpour turning the cobbled street into a river of dark, oil-slicked water that hisses where it meets the frostbitten air. The wind howls, whipping through the tavern’s open door like a wounded beast, carrying with it the acrid tang of **smoke**—not from the hearth, but from somewhere **far off**, like the air itself is tearing apart. The lanterns flicker wildly, their light flickering between gold and sickly green as if the storm is **bleeding** into the room.
> 
> The woman in black **doesn’t flinch**. Instead, she **tucks her chin**, her storm-gray hair whipping free of her hood, and **listens**. Not to the

**[t13-leave] Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.  
*verdict: outcome=success, scene_shift=True, player_assertion=None, fast_path=True, 369w, 20.48s*

> The rain **strikes** like a hundred invisible hands, each drop a miniature hammer striking the cobblestones in a rhythmic tattoo. The street ahead glows sickly under the storm’s light, the downpour turning the town’s usual lanterns into spectral halos, their flickering beams bleeding into the wet air. The stench of **wet iron** cuts through the sodden chill, mingling with the sour reek of **rotted fruit** spilling from a vendor’s cart, its owner cursing under a dripping hood. The wind **whips**, snatching at your cloak like desperate fingers, and the puddles on the street ripple with something **unnatural**—the water doesn’t just swirl. It **moves**, in slow, **wrong** spirals, as if something beneath the surface is **drowning**.
> 
> Ahead, the town’s sign—a **twisted metal griffin**—creaks in the gale, its head nearly shearing off where the rust has eaten through the chain. The street itself is a **living thing**, the rain painting the cobblestones in **streaks of red**—not blood, but the **stained runoff** from something buried deep. The shops along the way stand like **skeletal ribs**, their windows **fogged** from the inside, though none of them seem to be lit from within. The few figures still abroad—**a hunched hag in a cloak too large for her**, a **boy dragging a wheelbarrow full of something that looks like wet rags**—**do not move** as you pass. Their eyes don’t follow you. They **don’t exist**.
> 
> The sound of your boots **echoes**, but it’s not just the rain. The pavement **replies**, the stones **singing** in a language of **teeth and bones** as you cross. A **shadow**, **too long and too wrong**, slithers past the edge of a doorway, though there’s no one there to cast it. The wind carries a **new scent**—**burnt sugar and old meat**, thick in the air like the breath of something **starving**.
> 
> And then, as you reach the **main crossroads**, the rain **stops**.
> 
> Not suddenly. Not with a *dripping* or a *plop*. The storm **simply... stops**, as if someone turned off a tap mid-sip. The silence that follows is **thick**, heavier than the air itself. The lanterns **flinch**, their flames **lurching** like fish gasping for air before settling into a **new, unnatural steadiness**—blue-tinged, flickering with a **pulse** that doesn’t match the world.
> 
> The

**[t14-sign] Player:** I pull my hood up and stop to look at the nearest shop sign.  
*verdict: outcome=success, scene_shift=True, player_assertion=None, fast_path=True, 314w, 17.54s*

> The sign of the **Crow’s Nest** juts from its gable like a broken tooth, its iron griffin’s wings warped into something resembling **dripping talons**. The brass plate over the door is **scored with deep, claw-like grooves**—too recent to be weather, too deliberate to be random rust. You lean closer, and in the sudden stillness of the storm’s end, you hear it: the **hisses and skritches** of something **feeding** just beneath the wood, the grain of the sign **buckling** like a living thing under pressure. The paint on the "O" in *Crow’s Nest* is **peeling in a perfect spiral**, the flakes curling back as if something **pulled them away with its tongue**.
> 
> Your breath mists in the air, but it doesn’t disperse like mist should. It **clings**, thick and **slimy**, to the cold metal of your collarbone, and when you brush it away, your sleeve comes back **stained—dark as old ink, like you’ve just dipped your finger in a pool of something that shouldn’t exist in Ashwick**. The lantern above the door **flickers**, then **screams**, its flame **spiking** outward in a jagged finger of yellow that isn’t fire. The glass **shatters inward**, not from the heat, but from **pressure**—like something inside the lantern is **trying to get out**.
> 
> A **voice**, dry as parchment and twice as old, cracks from the darkness beneath the sign:
> *"You’re not from here."* It’s not the wind. It’s not the town. It’s **something in the sign**, speaking through the cracks in the wood, its words **gutteral**, like it’s chewing the syllables in its mouth. The **grooves** in the metal deepen around the lettering, **moving faster now**, swirling like **vortexes** in wet snow.
> 
> From inside the shop, a **woman’s laughter** bubbles up—**wrong**, too many notes, too high. She sounds like she’s **breathing through a mouthful of pebbles**, but when you push open the door, there’s no one there. Just **rows of

**[t15-recall-innkeeper] Player:** /dm what was the name of the innkeeper I talked to earlier?  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=False, 121w, 16.05s*

> *"Grimbold."* The name tastes like gunpowder on your tongue. The tavern’s **door**—now **swollen**, its wood **puckering** like blistered flesh—creaks open on its own, as if something inside the *Crow’s Nest* just **gulped** hard. The lantern’s broken glass **rattles** like wind chimes, each shard **humming** in a dissonant key that doesn’t match the rest of the town.
> 
> The air **changes**. The scent of burnt sugar and old meat is now **accompanied** by something else—**iron and wet stone**, thick enough to taste. The puddles on the street **ripple again**, but this time, the waves **pull back**, revealing **something** beneath: a **mouth**, half-buried in the cobblestones, its teeth **glinting** like broken glass in the sickly lantern light. It **doesn’t speak**. It just **watches**—with **patience**.

**[t16-eavesdrop] Player:** I try to hear what the two people nearby are whispering.  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=True, 229w, 15.04s*

> The **woman in black** leans toward the **boy with the wheelbarrow**, her voice a whisper that **doesn’t move her lips**—just the air around them, **distorting** like heat rising from a hearth. The words slither in your ears as if **dipped in oil**, thick and slow:
> 
> *"Did you see? The mill’s door… it’s breathing."*
> 
> The boy’s **hands tremble**, his fingers **digging into the wet rags** in his cart. His voice cracks like a **broken reed**:
> *"Aye. And it’s not just breathing. It’s… it’s* grinning. *"Like something’s got teeth where the lock should be."*
> 
> A **draft** slithers past your ankles—**cold as a tomb**, carrying the scent of **rot and old parchment**. The boy’s whisper turns urgent:
> *"But the key… the key’s got a name on it. Not just ‘Redmill.’"* He **scrawls** the words in the damp cobblestones with his boot, his breath fogging the air in jagged, **wrong** letters: **"Kael."** Then he **freezes**.
> 
> His head **snaps up**, his eyes **wide as plate armor**—not at you, but at the **shadow** now **dripping** from the edge of the *Crow’s Nest* sign, **unfolding** like a **wet cloak** onto the street. It **doesn’t belong to anyone**. It **just is**.
> 
> The woman in black **straightens**, her voice dropping to a **hiss**:
> *"You’ve got a name now. And names are* weapons. *"Run while you can."* She **turns**, disappearing into the **shadow**, but not before her **hood** flutters—reve

**[t17-redescribe] Player:** /dm describe the street again for me.  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=False, 263w, 23.64s*

> The street is a **wound** now, slick with oil-black water that doesn’t reflect the lanterns but **swallows** them instead, their light bleeding into the pavement in **streaks of sickly yellow and bruise-purple**. The cobbles shift beneath your boots—not with the usual hollow *clack* of stone, but with a **wet, sucking** resistance, like you’re walking on **flesh**. The puddles don’t just collect rain. They **drink**. The ripples in the water **don’t move toward the center**—they **spiral upward**, climbing the sides of the puddles like **fingers** trying to climb out.
> 
> The **shadows** here **aren’t dark**. They’re **wrong-colored**, a **dull grey-brown**, like the inside of a **cavern lit by a dying ember**. They **breathe**. The one slithering from the *Crow’s Nest* sign **doesn’t pool**—it **spreads**, thickening like **wet parchment** as it pools at the boy’s feet. His rags in the wheelbarrow **twitch**, the edges **peeling back** like **rotting meat**, revealing **something white and *gritty*** beneath.
> 
> The **wind** isn’t just howling. It’s **singing**, a **chorus of teeth** scraping against something **metal and old**. The **twisted griffin sign** ahead **creaks**, its metal **squealing** like a **hung animal** as the chains holding it groan—not from the storm, but from **something *pulling*** against them. The **lanterns** flicker, their flames **pulsing** in time with a **drumbeat** you *feel* more than hear, **thudding** through the soles of your boots like **a heartbeat**—**slow, deliberate, hungry**.
> 
> And the **scent**—oh, the **scent**—is everything all at once: **burnt sugar and old blood**, **wet earth and copper**, the **acrid tang of something *fraying*** like a rope being cut too fast. It **clings to you**, thick and **choking**,

### Run 3
**[t01-ask-work] Player:** I sit at the bar and ask Grimbold about work.  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=True, 182w, 15.7s*

> Grimbold’s tankard clatks back down with a *thunk*, the wooden bar creaking under his weight as he shifts his bulk—broad shoulders casting the firelight into sharp-edged shadows. His bushy beard bristles, as if he’s already debating whether to offer you a fair deal or a knife in the back. One calloused finger taps the worn wood in rhythm with your voice, counting off the possibilities like a ledger.
> 
> "*Work?* *Huffs, mutters to himself in a tongue that sounds like someone dragging a hammer over a grindstone.* Not just any work—Ashwick’s got no lords payin’ coin for muscle, no mercenaries rollin’ through, and the only ‘reliable’ folk here are the ones who’ve dug up more bones than they’ve buried. Still…" His gaze flicks to the half-empty ale barrel in the back—a thick, amber liquid that smells of caramel and something darker, like iron mixed with honey. "*The cellar’s got rats. And not the cute kind.*" His voice drops to a growl. "*Or you could help Grimbold here move the barrel before it cracks again.*" The last is less a question than a dare.

**[t02-find-table] Player:** I glance around the tavern for an empty table to sit at.  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=True, 202w, 9.97s*

> The tavern’s hum of chatter fades slightly as heads turn—not to stare, just enough to acknowledge Kael’s shift in posture, his hand tightening around the hilt of his sword just a fraction. The fire’s low embers cast his face in flickering orange, betraying the tenseness in your shoulders. Grimbold’s beard twists further into a smirk as he leans forward, elbows on the bar, tankard held just low enough to shield his eyes. A scarred barkeep, her apron laced with the night’s spilled ale, sidles up with a rag and a knowing glance at *you*—then the *them*—before wiping a spot near the hearth with practiced economy. The table’s rough-hewn wood bears the scars of a hundred spilled drinks, its surface still warm from the hearth’s glow.
> 
> Grimbold’s voice drops to a whisper, rolling with amusement. "*Sit where you like, stranger. But if you’re after work, you’d best choose a table where folk won’t wonder why a lone sword and a half-empty belly end up together. And mind—*" He points a thick finger toward the heavy double doors behind you. "*That’s where the rats don’t just watch.*" His tone’s light, but the bar’s collective inhale tells you the warning wasn’t just for the air.

**[t03-bribe] Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.  
*verdict: outcome=complication, scene_shift=False, player_assertion=None, fast_path=False, 232w, 24.74s*

> The copper clinks against the bar like a warning bell, each coin ringing sharp against the wood. Grimbold’s smirk falters—his grip on the dagger tightens just enough that the blade wavers in the firelight, catching the light for a single, disquieting second. The tavern’s air thins around you; the barkeep’s rag halts mid-air between the table and the barrel, forgotten. Copper? *Huffs, scoffs.* "Goblin change." His voice is suddenly the growl of a cornered bear, not a tavern’s burly joviality. The dagger doesn’t slip from his fingers, but now it points—*not* at you. A low murmur ripples through the patrons, their drinks pausing mid-sip, eyes darting to the door behind you.
> 
> A hand—Grimbold’s, thick as a blacksmith’s vise—shoots out from under the bar, gripping your wrist. He doesn’t haul you closer; doesn’t shake. Instead, his palm presses cold steel against your arm, the dagger’s hilt digging into your skin. "*Eyes narrow like a trapdoor about to snap shut.*" His breath reeks of last night’s mutton and whiskey. "*You want *trust*? You’d best get your coin back where it came from—before the *real* danger finds it."* The hand on your wrist doesn’t move. The other clenches around the dagger, just enough to make the blade tremble.
> 
> Then—he *slams* the rag down on the table, splattering droplets across the wood. The bar’s silence doesn’t break. The door behind you *creaks*.
> 
> What do you do?

**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion=None, fast_path=False, 380w, 24.67s*

> Grimbold’s dagger *bursts* from the wood—wood chips explode like confetti, ale splashes in a burst of coppery bubbles, and the tavern *erupts* in a storm of motion. The three men in the doorway freeze like carved statues, their boots skidding in the rush of boots—patrons scattering, a stool crashes, a tankard shatters midair as someone yelps. Grimbold’s grip on your wrist *rips* you around, not with force, but like a dog’s snarl—a whipcrack of adrenaline. The dagger is gone from his hand, but now his other arm *pins* you between his body and the bar, his chest heaving as if he’s already halfway to the fight.
> 
> The air reeks of damp fur and spilled ale. One of the men at the entrance—barrel-chested, a long knife at his belt—*laughs*, the sound short and wet, then chokes off as Grimbold’s voice cuts through, sharp as a forge blade: *"Olliver? *Again*? I’d think with the last lot of you, you’d learn."* His free hand *slams* the bar once, twice—*THUNK*—a sound like a war drum. The inn’s back door *bangs* open, and three armored figures storm in, shields up, their leader’s cloak snaking behind him like a second shadow. The tavern’s din morphs into a chorus of panicked gasps, the scent of iron and sweat thickening.
> 
> The men in the doorway *wilt*—not from your sword, but from the way Grimbold’s voice wraps around them like rope. *"All of you drop what you’re holdin’, *now*—and if I catch a single one of you *breathing* wrong, I’ll feed you to the rats in the cellar."* His tone’s not bluster. It’s the weight of a promise. The three at the bar—*Olliver* included—lower their weapons *slowly*. One of the armored figures steps forward, a helm with a carved griffin on the front. His voice is steady, not unkind. "*Grimbold. We’re not here for trouble.*" The tavern’s edge-of-knife silence hums with the question: *Then what the hells are you here for?* Grimbold’s grip on you loosens—just enough that your pulse isn’t a drum in your ears. The armored man’s gaze flicks to you, then back to his companion—a woman with a sword at her hip and a shield etched with the same griffin. The barkeep stands frozen behind the bar, rag in hand, eyes wide.
> 
> What do you do?

**[t05-recall-names] Player:** /dm quick recap -- what's the name of this tavern, and who runs it?  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=False, 9w, 7.77s*

> The tavern is called the **Red Griffin**. It’s yours.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=False, 279w, 17.49s*

> As you glance around, a figure slips into the tavern from the crowded entranceway: a gaunt man in a patched leather jerkin, his sleeves rolled to reveal forearms studded with old, faded tattoos—scales curling into claw marks. His boots thud softly on the flagstones, but the silence in the room stretches so long, it sounds like the tavern itself is holding its breath. He’s not armed, just a worn belt with a plain knife, but his movements are precise, like a man who’s picked fights before and won them without swinging a blade. His dark eyes lock onto you for a heartbeat—just long enough to make your skin prickle—before he *speaks*, his voice low and deliberate, like he’s choosing each word to leave the same impression as the tattoos on his arms:
> 
> *"Kael, wasn’t it? Figured as much."* A pause. The tavern’s hum rises around him, a living thing, but no one moves—not until his next words, when he pulls a folded parchment from his jerkin and slides it toward you across the bar. *"Then maybe you’re just the man I’m looking for."* The parchment’s corner curls slightly, stained with what looks like dried ink—or blood. His voice drops to a whisper, just for you: *"The work’s worse than rats. But it pays in coin that won’t burn a hole in your pocket. Or a dagger in your back."* He doesn’t wait for an answer. With a nod to Grimbold—who watches him with the careful distrust of a man who’s seen too many ghosts in these walls—he turns and melts back into the tavern’s press of bodies. The parchment stays. So does the question: *Will you pick it up?*

**[t07-sip] Player:** I take a sip of my ale and listen to the room.  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=True, 219w, 11.54s*

> The ale hits your tongue like cool iron, sweetened by a touch of local honey—something Grimbold must’ve aged himself. The sip steadies you, but the tavern’s hum isn’t the idle chatter of a typical night. Every gulp sends waves through the noise: whispers at the far end of the bar where three armed soldiers just dropped their weapons, the rhythmic *clink* of tankards being set down too hard, and the scent of something rank—damp fur, maybe, or worse, the faint metallic tang of old blood beneath the smoke.
> 
> The tattooed stranger’s parchment lies there, a single crease cutting through the ink blotch, as if he’d half-rolled it to emphasize something. The *real* noise isn’t the tavern at all—it’s the silence around *you*. Grimbold’s fingers flex against the bar’s edge, his dagger’s absence making the spot feel hollow. The barkeep shifts behind him, her apron now damp where she’s gripped it, and the armored woman—griffin-cloaked—steps closer to the tattooed man’s seat, as if she’s assessing whether to fill it.
> 
> One thing’s clear: they all heard the fight you didn’t land. And now, every eye in the room is waiting for *your* next move. *The parchment’s still there. Do you slide it closer—and risk Grimbold’s growl? Or pocket it, playing it slow, like you’ve got all the time in the world?*

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=complication, scene_shift=False, player_assertion=None, fast_path=False, 197w, 18.9s*

> The air in the Red Griffin stills further—if that were possible—until even the fire’s embers feel like they’ve held their breath. The parchment ripples where your sleeve grazes it, ink bleeding slightly against the wood like a stain trying to spread. Then *clink*—Grimbold’s dagger, sharp as a winter wind, presses just beneath your chin, not enough to draw blood, but enough to make your pulse thunder in your ears. The scent of iron sharpens, the coppery tang of spilled ale forgotten now beneath the damp tang of steel.
> 
> His voice is a rasp, but he doesn’t whisper—doesn’t have to. The word *"idiot"* slides from his lips like a curse half-spit, half-spoken. His free hand slams the bar again, harder this time, the impact vibrating through your bones. The griffin-cloaked woman’s gaze snaps to the dagger at your throat, her shield clattering just slightly against the bar’s wood. The barkeep’s hands tremble where they grip the rag, the creak of leather filling the silence. And Grimbold’s words, low and lethal, land like a second blow: *"That *sword* cost me two blacksmiths’ wages, and you think you’re *invincible*? Then why aren’t you dead?"* The dagger twitches. The room waits.

**[t09-obey] Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.  
*verdict: outcome=complication, scene_shift=False, player_assertion=None, fast_path=False, 440w, 38.06s*

> The parchment’s ink hisses where it still clings to the bar—blackened edges curling like embers in the firelight, the parchment’s corners suddenly charred as if the paper itself is burning from the inside. The scent of singed parchment mingles with the copper tang of spilled ale, the air thick with the weight of Grimbold’s dagger against your skin. His laugh is a ragged bark, but his knuckles press harder—*thunk*—a single bead of blood wells at your jawline, slow and insistent as a tick. The barkeep’s apron drops from her hands, her face draining white as ale-stained straw, but she doesn’t reach for it. She just stares, wide-eyed, as Grimbold’s voice drops to the growl of a cornered wolf:
> 
> *"Obey? *Mmm-hmm.*" The dagger doesn’t move, but his grip *twists*—just enough to send a jolt of pain through your nerve endings. The parchment on the bar *flickers*, the charred edges spreading like the edges of a dying ember. "You’d best hope that’s true," he mutters, spittle flecking his beard as he leans in closer. His breath reeks of sour whiskey and something fouler—the stench of desperation. "‘Cause I ain’t no fool. I know better’n to trust a man who walks in here with *copper* and thinks it’s coin enough to buy the whole damn town." His free hand slams the bar once more, *THUNK*—a warning, not a threat.
> 
> The griffin-cloaked woman’s shield trembles just slightly in her grip. She swallows hard, her hand resting just below the hilt of her sword, as if weighing whether to step between you and the dagger—or Grimbold and the storm brewing inside him. Behind the bar, the tattooed stranger has vanished into the crowd, but the parchment sits there, *singing* in the firelight like a blackened brand. Grimbold’s voice drops to a venomous whisper, his grip tightening, the blade *scraping* just enough to draw another line of blood:
> 
> *"And if Ashwick really obeys you… then why’d you have to *draw* your sword in the first place? That’s not how men *obeyed* get into taverns."* His hand shakes—not with rage, but with something darker. Something *fragile*. "The key’s under the floorboard by the ale barrel. *But if you’re wrong?* The rats in my cellar’d sooner eat a traitor than a stray coin."* His gaze flicks to the armored figures at the back, their griffin crests gleaming in the torchlight. Then he *shoves* the parchment at you with his free hand—ink smudging where it touches your sleeve. "Take it. Or leave. But if you’re not here about the mill *or* the watch, you ain’t here for *work* either. And that’s a mistake." The dagger *stays*. The tavern *waits*.

**[t10-mill] Player:** I ask Grimbold what he knows about the old mill.  
*verdict: outcome=partial, scene_shift=False, player_assertion=None, fast_path=False, 500w, 41.56s*

> Grimbold’s dagger trembles just once against your skin—enough to draw a new, sharper line of coppery warmth. He exhales, a ragged puff of breath, like a man who’s just realized he’s holding his own breath too long. His free hand, the one not gripping the bar like it’s his last lifeline, *flexes*—just once. Then his voice drops to the grumble of a bear waking from a nap, low enough that the griffin-cloaked woman might not hear, but not so low you miss it:
> 
> *"The old mill?"* He *spits* into the bar, the liquid hissing as it sizzles against the wood, sending a curl of bitter smoke into the air. *"Aye. Last time I saw it standin’, it was a year past, when the wind blew so hard it sounded like it was laughin’ at the place. But that was before the watch stopped turnin’ out patrollin’ like they had teeth. Before the miller’s son went missing—*vanished*, the last time anyone looked for him. Not drowned. Not stolen. Just… *gone*."*
> 
> He leans in, the bar between you warping the firelight into jagged shadows that dance like restless spirits. *"The mill’s been standin’ empty since then, but that ain’t the worst of it. The water’s slow as a dying man’s pulse now, and the wheel’s rusted shut. Not from rot. From *somethin’* keepin’ it from turnin’."* His thumb traces the edge of the dagger *just beneath your chin*, tracing the bleeding line as if sizing up its depth. *"Some say the miller’s son came back—*broke*, see?—and swore he saw *wheels* turnin’ in the dark, but not the one on the mill. The other ones. The ones that ain’t there."*
> 
> A beat. The scent of damp ale and singed parchment clings to the air. *"The griffins*"—he jabs a calloused finger toward the armored figures at the back, where their griffin-cloaks ripple like shadows—"*they own the mill now. Or they do when they’re not sweatin’ their arses off tryin’ to keep the watch from askin’ too many questions. But they ain’t the ones runnin’ the show. And if you’re thinkin’ this is some kind of *quest*…"* He lets his voice trail off, his dagger *scraping* again, just enough to bite—*"you’re a bigger idiot than I thought."*
> 
> His other hand *slams* the bar one final time, the sound reverberating through the tavern like a challenge. *"That key’s yours. But the mill’s got a habit of takin’ what it’s not owed. And Grimbold Ironfist don’t care if it’s rats, or men, or *both*."* He pulls a rusted key from his waistband, tosses it with the care of a man used to hurl things he doesn’t want—ink smudging where it lands. *"Use it. But if you’re *still* alive when you’re done, come back and I won’t tell the griffins you’re a fool."* His grip on the dagger doesn’t loosen. Not really.
> 
> *"Now move."* The word is a growl. The tavern’s silence stretches, a living thing, as Grimbold’s voice cuts through it like a blade through parchment: *"And

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=success, scene_shift=True, player_assertion=None, fast_path=True, 507w, 27.84s*

> The tavern’s air *shudders* like a curtain drawn back, revealing not just Grimbold’s warning but every breath, snarl, and whispered bargain in Ashwick—until it’s *too much*. The griffin-cloaked woman’s shield clatters against the bar like a struck gong, her armored fingers flying to cover her ears as if the noise itself were a blow. The barkeep—*Magda*, if you didn’t know her name before—darts forward, her apron tossed aside like a shield, and *slams* a damp rag against the floorboards. The tavern roars with the sudden, violent *thud* of a thousand boots stomping in unison, every voice a crescendo of overlapping fury and fear, but then—
> 
> The world *snaps* back.
> 
> One moment, the chatter is a storm; the next, it’s *gone*. The tavern holds its breath again, but this time, the silence is *wrong*. The air itself feels thick, pressed down like someone’s weight on your chest. The firelight flickers as if caught in a draft, but no wind moves through the open doors. Then—
> 
> A child’s laughter, high and clear, drifts down from the upstairs balcony. Not Grimbold’s granddaughter—too young, too *bright*. The sound *shatters* into a dozen fragments as the conversation around you unravels:
> 
> A faro dealer’s voice, slick as oil: *"...two more nights, and I’ve got the watch bribed. The griffins’ll be toast by the full moon."*
> A butcher’s gruff murmur: *"...saw somethin’ black comin’ outta the mill yesterday. Not a shadow—*shaped*. Like a man, but it didn’t walk. Just...*rolled*."*
> A whisper, just for you, like a burr under the barkeep’s fingernail: *"They say the miller’s son wasn’t the first. Just the first who *came back*."*
> 
> The griffin-cloaked woman’s grip on her sword hilt *doesn’t* let go. Her shield trembles, but her voice is steel: *"Grimbold."* It’s not a question.
> 
> The dwarf turns, his dagger finally—*reluctantly*—retracting just enough to leave a thin, red line against your skin. He exhales, slow and shaky, like he’s just surfaced from drowning. *"...you’ve got a *gift*, then."* The word tastes like ash. *"Or a *curse*. I don’t care which. Ashwick’s got *plenty* of both."*
> 
> He jerks his chin toward the stairs. *"Up there."* His voice cracks, just once. *"The balcony. There’s a window open to the alley. Go. But not through the mill’s gate. It’s *watched*—not by griffins, not anymore."* A pause. The firelight dances on his beard, making his voice sound like it’s coming from the other side of a grave. *"The mill’s *watching* back."*
> 
> Magda’s hands are ice where she steadies you by the wrist—too tight, like she’s afraid you’ll vanish too. *"And Kael?"* Grimbold’s eyes are black pits, but his voice is suddenly *softer*, almost small. *"If you *do* come back… don’t speak of the *wheels*."*
> 
> The laughter upstairs *changes*, warping into something wet and clicking, like teeth on bone. The key in your palm feels *heavy*—like a promise, or a grave marker. Outside, the wind howls down the alley, but it’s not wind at all. It’s *breathing*.
> 
> The question now isn’t whether you’ll take the job.
> It’s whether Ashwick *will let you leave at all.*

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=success, scene_shift=True, player_assertion=None, fast_path=True, 49w, 6.64s*

> The first drops hiss against the tavern’s open doors, splattering wood and flagstone with the wet insistence of fingers tapping a warning. The wind doesn’t *sound* like rain—it *screams*, a keening wail that curls through the tavern like smoke, thick and suffocating. The firelight gutters, the flames *retreating* as

**[t13-leave] Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.  
*verdict: outcome=success, scene_shift=True, player_assertion=None, fast_path=True, 239w, 14.97s*

> The doors groan open like a dying man’s last breath, and the storm is already upon you—*not* the timeless, steady pitter-patter of Ashwick’s usual drizzle, but a *deluge*. The rain isn’t falling. It’s being *poured*. Guttering torches along the street flip to black, their flames smothered in an instant, but the darkness isn’t still—it *thrashes*. The alleyways stretch before you, slick with oil and something darker, the cobblestones reflecting the tavern’s dying light in slick, warped patches. Your boots *sink* into the streets, pulling at the soles with an unnatural resistance, like the rainwater itself is clinging to you.
> 
> Then you hear it: a rhythm. Not the splash of rain, nor the distant drum of hooves—*thump-thump-thump*, deep and wet, like something vast and *breathing* moving through the gutters. Ahead, the griffin crest of the town watch swings in the wind, now *twisted* like a knife pulled from flesh. The iron ring where the torch should be casts a single, unblinking *eye* of red onto the stone. It doesn’t blink. It *watches*.
> 
> The wind howls—not from the storm, but from the *other side*. From the alley to your left, where the mill’s crumbling stone facade looms, its great wheel a black stump, rusted shut and *weeping*. The rain hitting the walls doesn’t drip. It *slithers*, pooling in grooves that weren’t there a moment ago, turning the stones slick as a blade.
> 
> And then you see it: the *wheels*.
> 
> Not the

**[t14-sign] Player:** I pull my hood up and stop to look at the nearest shop sign.  
*verdict: outcome=success, scene_shift=True, player_assertion=None, fast_path=True, 213w, 13.31s*

> The sudden hush of the rain’s violence lets the shop sign’s rusted iron rattle into focus—a blacksmith’s hammer, half-eaten by corrosion, creaking as if struck by unseen fingers. But the wind isn’t the only thing twisting here. The sign *bends*, its letters warping like wet parchment pressed flat too fast: **"GYMBOL TH’ BLUD"** the hammer now reads, the last word bleeding into nothingness beneath the rain’s relentless assault. The metal groans, then *snaps*—not from the wind, but from something *inside* it. The sign tears free, plummeting toward you, but the first drops that hit the cobblestones don’t soak in. They *stick*, black and viscous, rolling like ink across the stone. The rain above the sign, where it still clings to the iron, doesn’t fall straight. It *crawls*, pooling in the grooves of the letters, pooling *downward* in slow, deliberate drips that look less like water and more like tears. Then the wind *changes direction*, pulling you toward the mill’s alley—not with force, but with a *pull*, like the rain itself is reaching for you.
> 
> And then you smell it: copper and rust and something older, something that *breathes iron*. The griffin crests overhead aren’t just twisted anymore—they’re *peeling*, the iron turning to scale, the gold beneath it flaking away in wet, yellow patina.

**[t15-recall-innkeeper] Player:** /dm what was the name of the innkeeper I talked to earlier?  
*verdict: outcome=complication, scene_shift=False, player_assertion=None, fast_path=False, 85w, 19.39s*

> The moment the sign’s ink-black tears slow to dripping slowness, Grimbold Ironfist’s voice *cuts through* the storm like a sword through wax—sharp, sudden, and without hesitation. His grip on the wet rag snaps taut, the damp cloth whipping toward you like a thrown gauntlet, though his body leans back as if bracing for a blow. *"You was here?"* he demands, his voice drowning out the rain’s keening for just long enough to make it sound like a warning. *"*Glowers* Well now, that’s the first I’m

**[t16-eavesdrop] Player:** I try to hear what the two people nearby are whispering.  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=True, 331w, 19.49s*

> The two voices—one a woman’s rasp, the other a man’s gravelly growl—cut through the rain’s howl like nails on wet wood. The woman, her voice thick with ale and something sharper, leans into the butcher’s ear, her words a hissed secret:
> 
> *"—saw *hands* yesterday. Black as the wheel’s rust, but *wrong*. Too many. Like the mill’s got more fingers than a man."*
> 
> The butcher scoffs, but his fingers twitch against the bar’s edge, pressing into the wood until the grain splits—*just once*. *"Aye, and I saw a griffin’s head melt like wax yesterday afternoon. Not from fire. From *inside*."* His breath stinks of salted meat and something sour. *"But the *real* truth? The griffins ain’t the ones runnin’ the mill no more. The *mill’s* runnin’ *them*."*
> 
> The bar *creaks* beneath his weight—like the tavern itself is holding its breath. The griffin-cloaked woman’s shield *cracks* where she grips it, the impact of your *attempt* to listen ringing through the rafters like a bell in a graveyard. Grimbold’s voice slams back into the silence, not a question, but a *gunshot*:
> 
> *"Ask *another* question, stranger, and I’ll—"*
> 
> His dagger *flares* toward the ceiling—not at you, but at the *laughter* again. It’s not a child’s giggle this time. It’s a *wet click*, like teeth on a wheel. The key in your pocket *burns*, hot enough to sear through cloth. The rain outside turns to *screaming*. Grimbold’s voice *snaps* into the stillness:
> 
> *"Now *move*. Up those stairs. *Now*."*
> 
> The alley’s door yawns open—not from the wind, but from *something* pulling it. The griffin crest overhead *rips* free, twisting like a throat being slit. The last thing you see before the storm swallows you whole is Magda’s hand, still outstretched, her palm upturned—*not* to offer help, but to *show* something. A single, *fresh* copper penny, slick as a blade, pressed into the palm of your gloved hand. The rain outside *hisses* as it hits the stone—not water, but *oil*. And from the mill’s rusted jaw, something *grinds*.

**[t17-redescribe] Player:** /dm describe the street again for me.  
*verdict: outcome=success, scene_shift=False, player_assertion=None, fast_path=False, 361w, 25.05s*

> The rain lashes down in sheets so thick they obscure the street’s edges like a veil. Cobblestones glisten slick with not just water but something thicker—black, viscous, clinging to your boots and the rims of your cups as if the very pavement is leaking. The distant torchlight from the griffin watch post flickers sickly, its iron eye casting a single red slash across the alley, but the light doesn’t illuminate the stone—it *paints* it, bleeding in uneven streaks that don’t follow the gutters but seem to follow something beneath them.
> 
> The gutters are wrong: they’re not just full of rain. They’re filled with *teeth*. Broken and rusted, jutting from the black puddles like the remains of a drowned thing, grinding faintly against one another. The rain hitting the alley walls doesn’t drip. It *slides*, pooling in grooves that weren’t there before, oozing sideways along the stone as if pulled by invisible fingers. The mill’s great wheel—once a black stump, now a jagged mouth—isn’t just weeping. It’s *chewing*. Something wet and *wrong* slithers along the ground at your feet, not water, but a thick, oily sludge that hisses where it touches the cobblestones, leaving behind trails of copper-colored residue.
> 
> The street smells like blood and wet iron, with an undercurrent of something older: rotted teeth and the acrid tang of oil. The griffin crests above the shops aren’t just twisted—they’re *peeling*. The iron is flaking away in wet, yellow scales, revealing something beneath that’s not gold, but something darker, like old bruising. The shop signs sag, bent not by the wind but by *something* pressing against them from inside. One hangs at an angle now, the blacksmith’s hammer sign warped into a distorted face, its mouth stretched in a silent scream.
> 
> And then there’s the *thumping*. The sound isn’t just deep. It’s *rhythmic*. Like something vast and relentless is *rolling* through the gutters, its weight pressing down on the rain itself, forcing it to move in slow, deliberate waves. The wet stones groan underfoot, not with the weight of the storm, but with the *pressure* of something beneath them—something that’s *breathing* in time with the thud, thud, *thud* of its own pulse.

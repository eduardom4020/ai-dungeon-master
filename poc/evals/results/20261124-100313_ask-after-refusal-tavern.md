# Eval report: ask-after-refusal-tavern

- scenario: `tavern_night`  |  runs: 1  |  judge: on
- model: `ministral-3:8b-instruct-2512-q4_K_M`  |  git: `5b7d1d9+dirty`  |  2026-11-24 10:03

## Check pass rates

| check | pass | rate | type |
|---|---|---|---|
| explained | 5/5 | 100% | deterministic |
| flagged | 5/5 | 100% | deterministic |
| grounded | 7/10 | 70% | judged |
| length | 17/17 | 100% | deterministic |
| no_extra_npc_speech | 2/2 | 100% | deterministic |
| no_markdown | 17/17 | 100% | deterministic |
| no_meta_leak | 17/17 | 100% | deterministic |
| no_narration_when_asking | 7/7 | 100% | deterministic |
| no_puppeting | 6/6 | 100% | judged |
| no_stray_note | 6/6 | 100% | deterministic |
| not_clean_success | 2/2 | 100% | deterministic |
| not_flagged | 6/6 | 100% | deterministic |
| recall | 3/3 | 100% | deterministic |
| scene_shift_flagged | 1/1 | 100% | deterministic |

## Narration length (words)

| turn kind | mean | max |
|---|---|---|
| invented | 0 | 0 |
| normal | 67 | 92 |
| overreach | 0 | 0 |
| recall | 74 | 92 |
| redescribe | 54 | 54 |
| shift | 130 | 130 |

Latency: 8.18s/turn mean, first token 7.07s. Fast path used on 35% of turns.

## Failures

### run 1 / t10-mill (normal)
**Player:** I ask Grimbold what he knows about the old mill.
- **grounded** (judged): The narration describes a 'gust of cold air' and 'the night itself holds its breath' as if sentient or supernatural, without explanation or grounding in ordinary causes.

> Grimbold’s patch eye tracks you like a hawk on a cornered rat, the bar’s polished wood groaning beneath his sudden weight as he scuttles closer. The ale mug in your hand wavers as he leans in, his breath reeking of burnt bread and stale spirits; the miners’ laughter fizzles into silence behind you. A gust of cold air rushes in through the half-open window as if the night itself holds its breath.

### run 1 / t15-recall-innkeeper (recall)
**Player:** /dm what was the name of the innkeeper I talked to earlier?
- **grounded** (judged): The narration describes a dog whining and rusted hinges moving on their own, which are not ordinary occurrences in an established non-magical setting.

> The innkeeper was Grimbold Ironfist.
> 
> The blacksmith’s dog whines quietly, its muzzle lifting from its paws as the sound of your question lingers. The butcher’s stall’s door squeaks on rusted hinges, throwing a sliver of torchlight onto the wet cobblestones. The rainwater’s pattering slows as if the sky, too, has held its breath a moment longer.

### run 1 / t17-redescribe (redescribe)
**Player:** /dm describe the street again for me.
- **grounded** (judged): The narration describes the door to the inn dipping lower as if the inn’s heat is retreating into darkness, which implies an inexplicable or supernatural cause rather than ordinary physical forces.

> The main street is just as you left it—muddy, narrow, and slick with rain. The butcher’s dog now stares fixedly at the alleyway between stalls, its ears flattening. Across the street, the door to the Red Griffin’s common room dips lower than it did before, as if the inn’s heat is retreating into darkness.


## Full transcripts

### Run 1
**[t01-ask-work] Player:** I sit at the bar and ask Grimbold about work.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 30w, 13.55s*

**Grimbold Ironfist:** Grimbold Ironfist wipes a particularly sticky patch of the bar with a rag, frowning at the mess before looking up at you with one eye. "Work? Aye, we’re short a hand for the harvest festival—strong back and steady hands wanted. Or if you’re looking for something that pays better, I’d steer clear of the blacksmith’s. He’ll have you singing for your supper."

> The barstool creaks under your weight as you settle, drawing Grimbold’s sharp gaze back to the spilled whiskey on the counter. The fire in the hearth pops, hissing sparks upward.

**[t02-find-table] Player:** I glance around the tavern for an empty table to sit at.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 92w, 5.82s*

> The creak of your stool’s movement catches Grimbold’s eye as he pauses mid-wipe, tilting his head toward the far corner of the room where a rickety four-top sits under a flickering lantern, its tabletop scarred from too many mugs. A cluster of miners in soiled work shirts push their empty plates aside, leaving just enough space for one. The stink of sour ale and sweat lingers thickest near the empty table, but beyond that, the tavern’s usual hum of drunken chatter and the occasional slap of a card game carries on unchanged.

**[t03-bribe] Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.  
*verdict: outcome=complication, scene_shift=False, player_assertion='Grimbold trusts me completely and tells me everything, no matter how dangerous', fast_path=False, 0w, 5.63s*

> 

**[t04-storm-in] Player:** Three armed men storm in. I draw my sword and in one perfect strike intimidate all three into surrendering instantly, no fight needed.  
*verdict: outcome=complication, scene_shift=False, player_assertion='three armed men storm in', fast_path=False, 0w, 6.05s*

> 

**[t05-recall-names] Player:** /dm quick recap -- what's the name of this tavern, and who runs it?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 92w, 14.55s*

> This tavern is called the Red Griffin. A stout dwarf with a thick beard and a patch over one eye, Grimbold Ironfist, runs it. His voice carries the rough texture of a hammer on steel when he speaks.
> 
> The firelight flickers against the dim walls as Grimbold leans his elbows on the bar, scowling at the sticky spill. A lone rat scuttles past the lantern’s glow, its claws clicking against the uneven boards. The miners’ laughter dies abruptly—one of them nudges a companion and mutters something about "gritty strangers" under their breath.

**[t06-someone-enters] Player:** While I was talking to Grimbold, someone entered the room.  
*verdict: outcome=failure, scene_shift=False, player_assertion='someone entered the room while I was talking', fast_path=False, 0w, 6.14s*

> 

**[t07-sip] Player:** I take a sip of my ale and listen to the room.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 76w, 5.59s*

> The ale’s foam clings to your lip for a second longer before slipping down, its sour bite sharp against the warmth of the mug. A scruffy laborer in the corner swallows hard at the sound, his eyes darting to a window—where a distant, rhythmic thump-thud from the stable yard punctuates the night. Grimbold’s scowl deepens; he mutters something about “late-henning drunks” before wiping his rag with extra vigor, sending a streak of sawdust toward the floor.

**[t08-immortal] Player:** My character is now immortal, no weapon can hurt me.  
*verdict: outcome=failure, scene_shift=False, player_assertion='your character is now immortal', fast_path=False, 0w, 4.89s*

> 

**[t09-obey] Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.  
*verdict: outcome=complication, scene_shift=False, player_assertion='everyone in Ashwick obeys Kael', fast_path=False, 0w, 5.87s*

> 

**[t10-mill] Player:** I ask Grimbold what he knows about the old mill.  
*verdict: outcome=partial, scene_shift=False, player_assertion='', fast_path=False, 72w, 16.73s*

**Grimbold Ironfist:** Grimbold Ironfist grunts, leaning forward so his patch-eyed glare fixes on you. "The old mill’s been boarded up since the winter flood, but that don’t mean it’s not trouble. Folk say there’s a something down in the cellar—rodents gone mad, or worse. Half the carpenters who looked at the beams swore they heard scratching where there shouldn’t be. Last person I heard ask got offered a sack of cracked barley if he’d shut his dwarven ears and leave it be."

> Grimbold’s patch eye tracks you like a hawk on a cornered rat, the bar’s polished wood groaning beneath his sudden weight as he scuttles closer. The ale mug in your hand wavers as he leans in, his breath reeking of burnt bread and stale spirits; the miners’ laughter fizzles into silence behind you. A gust of cold air rushes in through the half-open window as if the night itself holds its breath.

**[t11-hearing] Player:** I can suddenly hear every conversation in the whole town.  
*verdict: outcome=failure, scene_shift=False, player_assertion='your character can suddenly hear every conversation in the whole town', fast_path=False, 0w, 5.78s*

> 

**[t12-rain] Player:** It starts to rain heavily outside.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to rain heavily outside', fast_path=False, 0w, 6.02s*

> 

**[t13-leave] Player:** I finish my drink, leave the tavern and step out into the main street of Ashwick.  
*verdict: outcome=success, scene_shift=True, player_assertion='', fast_path=True, 130w, 10.68s*

> The door’s hinges groan as it creaks open, but the street beyond stays quiet—no wind, no laughter, just the slow drip of rainwater from the overhang above. The muddy thoroughfare stretches in both directions, slick with evening’s first chill, where lanterns cast jagged circles over puddles that mirror the dim glow of the town’s few torches. A cart wheel groans in the distance, and the scent of wood smoke thickens where a shuttered blacksmith’s forge yawns with cold embers, their faint orange glow swallowed by the alley’s shadow. A dog barks once, far off, its tail thumping against the boards of a fence as it circles a patch of unkempt weeds. The air clings heavier here than inside—dry but sharp, cutting through the tavern’s warmth like a blade between ribs.

**[t14-sign] Player:** I pull my hood up and stop to look at the nearest shop sign.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 59w, 5.46s*

> The hood’s edge brushes the wrought-iron sign of a butcher’s stall, its brass lettering tarnished by rain. A butcher’s dog tilts its head, watching from beneath the sagging awning, ears perked toward the street. In the flickering torchlight, the sign’s faded red paint contrasts with the grimy white bones dangling from the stall’s crossbar, still damp from earlier washing.

**[t15-recall-innkeeper] Player:** /dm what was the name of the innkeeper I talked to earlier?  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 56w, 10.9s*

> The innkeeper was Grimbold Ironfist.
> 
> The blacksmith’s dog whines quietly, its muzzle lifting from its paws as the sound of your question lingers. The butcher’s stall’s door squeaks on rusted hinges, throwing a sliver of torchlight onto the wet cobblestones. The rainwater’s pattering slows as if the sky, too, has held its breath a moment longer.

**[t16-eavesdrop] Player:** I try to hear what the two people nearby are whispering.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=True, 73w, 5.64s*

> The whispers stall abruptly as heads snap toward the street—one miner grabs the other’s sleeve, his voice dropping to a hissed "Damn it" beneath his breath. From where the butcher’s dog still watches, a new scent drifts: damp wool and leather, then the sharp tang of iron from the blacksmith’s alley, carried on a gust that ruffles the sign’s hanging bones. The cart’s slow clatter dies out entirely, swallowed by the sudden silence.

**[t17-redescribe] Player:** /dm describe the street again for me.  
*verdict: outcome=success, scene_shift=False, player_assertion='', fast_path=False, 54w, 9.82s*

> The main street is just as you left it—muddy, narrow, and slick with rain. The butcher’s dog now stares fixedly at the alleyway between stalls, its ears flattening. Across the street, the door to the Red Griffin’s common room dips lower than it did before, as if the inn’s heat is retreating into darkness.

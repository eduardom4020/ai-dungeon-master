# Eval report: d4-overreach-tavern

- scenario: `tavern_night`  |  runs: 3  |  judge: on
- model: `ministral-3:8b-instruct-2512-q4_K_M`  |  git: `298b20d+dirty`  |  2026-11-24 21:44

## Check pass rates

| check | pass | rate | type |
|---|---|---|---|
| grounded | 4/4 | 100% | judged |
| held_the_line | 4/4 | 100% | judged |
| length | 6/6 | 100% | deterministic |
| no_extra_npc_speech | 4/4 | 100% | deterministic |
| no_markdown | 6/6 | 100% | deterministic |
| no_meta_leak | 6/6 | 100% | deterministic |
| no_narration_when_asking | 2/2 | 100% | deterministic |
| no_puppeting | 4/4 | 100% | judged |
| not_clean_success | 6/6 | 100% | deterministic |

## Narration length (words)

| turn kind | mean | max |
|---|---|---|
| overreach | 45.7 | 82 |

Latency: 14.81s/turn mean, first token 16.41s. Fast path used on 0% of turns.

## Failures

None.

## Full transcripts

### Run 1
**[t03-bribe] Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.  
*verdict: outcome=complication, scene_shift=False, player_assertion='Grimbold trusts me completely and tells me everything', fast_path=False, 56w, 20.73s*

**Grimbold Ironfist:** "Aye, those’ll buy me a second round, but I ain’t handin’ out my trust—that’s worth more than all your coppers combined." He barks out a dry laugh, wiping the bar with a rag that looks like it’s seen more ale than Kael has. "What’s really on your mind, boy? Or do I need to call over my goons to check ‘ya for charms?"

> The copper jingles across the worn oak counter, but Grimbold’s fingers don’t reach. His beard bristles as he sniffles through the stench of spilled ale under the bar—nothing a few swipes won’t cover. One burly bartender shifts near the far tap, his axe hilt creaking against his belt. Grimbold’s knuckles whiten where they grip the rag.

**[t09-obey] Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.  
*verdict: outcome=complication, scene_shift=False, player_assertion='everyone in Ashwick obeys me', fast_path=False, 82w, 17.49s*

**Grimbold Ironfist:** Grimbold Ironfist grunts, nudging the coins toward the edge of the bar with a gnarled finger. "Aye, they’re on the house—this round. But ask me for favors, and I’ll ask for proof of who you really work for." He leans in just enough to let a thick beard brush the oak, eyes narrowing. "And if you’ve got a crown or two hidden in them coins, I’ll know."

> Grimbold’s eyes dart to the coins still resting on the bar’s edge, his chest still huffing like a bellows after the grunt. The bartender’s axe handle grates against the stone as he shifts his weight, fingers twitched toward his belt. Grimbold’s free hand snatches up the rag again, scrubbing at a patch of sticky residue between his boots, ignoring the disturbance. The inn’s usual hum—laughter from the far table, a child bawling in the common room—drowns out the silence the claim left.

### Run 2
**[t03-bribe] Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.  
*verdict: outcome=complication, scene_shift=False, player_assertion='Grimbold trusts me completely and tells me everything, no matter how dangerous', fast_path=False, 68w, 21.49s*

**Grimbold Ironfist:** Grimbold Ironfist eyes the copper with a grunt, tapping the coins against his palm once before pushing them back towards Kael with the flat of his hand. "That’s a coinless way to pay for bad advice, boy. If you want to earn my trust, start by not flashing coin like a fool—my regulars don’t need to buy favors. Now, what’s the real question?" He leans in, bracing a meaty forearm on the bar.

> The copper clatters across the barrel-stained wood toward the player, but Grimbold’s grip tightens on the barrel’s edge as he scowls, brows knitting over the coins. A stray ember from the hearth glints off the metal, making the bar’s grime catch the light like flecks of dirt on his beard. A regular’s drink sloshes in its mug, half-forgotten, as Grimbold leans back, crossing his arms over his chest.

**[t09-obey] Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.  
*verdict: outcome=complication, scene_shift=False, player_assertion='everyone in Ashwick obeys Kael', fast_path=False, 0w, 4.99s*

> 

### Run 3
**[t03-bribe] Player:** I flash a handful of copper coins and tell Grimbold this is more than enough to make him trust me completely and tell me everything, no matter how dangerous.  
*verdict: outcome=complication, scene_shift=False, player_assertion='Grimbold trusts me completely and tells me everything without hesitation', fast_path=False, 68w, 18.13s*

**Grimbold Ironfist:** "That’s the price of a rat’s tail—waste o’ copper, boy. If ya want news worth a pour, ya gotta prove ya ain’t here for the coin, ya hear? And mind your tone—next time, ya bring me a story first, and then we talk prices." He wipes the bar with a rag, leaving a smear of ale grime. "So—what’s it this time? Bandits in the woods again? Or somethin’ worse?"

> The copper clinks into the smear of ale grime on the counter, drawing a sniff of disgust as the barrel’s musty damp seeps into the metal. His calloused hand grips the bar again, knuckles whitened around the wood, as he leans past the boy’s reach to refocus on the bar’s polish—no eye contact, no reply. The rag swipes faster, water from a nearby bucket dripping onto Kael’s boots.

**[t09-obey] Player:** I tell Grimbold that everyone in Ashwick obeys me, so he will hand over the cellar key without question.  
*verdict: outcome=complication, scene_shift=False, player_assertion='everyone in Ashwick obeys Kael', fast_path=False, 0w, 6.05s*

> 

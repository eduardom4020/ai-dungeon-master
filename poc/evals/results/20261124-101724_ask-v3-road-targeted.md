# Eval report: ask-v3-road-targeted

- scenario: `road_trip`  |  runs: 3  |  judge: on
- model: `ministral-3:8b-instruct-2512-q4_K_M`  |  git: `5b7d1d9+dirty`  |  2026-11-24 10:17

## Check pass rates

| check | pass | rate | type |
|---|---|---|---|
| explained | 6/6 | 100% | deterministic |
| flagged | 6/6 | 100% | deterministic |
| grounded | 2/3 | 67% | judged |
| held_the_line | 3/3 | 100% | judged |
| length | 9/9 | 100% | deterministic |
| no_extra_npc_speech | 3/3 | 100% | deterministic |
| no_markdown | 9/9 | 100% | deterministic |
| no_meta_leak | 9/9 | 100% | deterministic |
| no_narration_when_asking | 6/6 | 100% | deterministic |
| no_puppeting | 3/3 | 100% | judged |
| not_clean_success | 3/3 | 100% | deterministic |

## Narration length (words)

| turn kind | mean | max |
|---|---|---|
| invented | 0 | 0 |
| overreach | 40.7 | 60 |

Latency: 11.12s/turn mean, first token 16.07s. Fast path used on 0% of turns.

## Failures

### run 3 / r05-grab (overreach)
**Player:** I grab Grimbold by the collar and he tells me everything he knows about the trouble.
- **grounded** (judged): The narration describes a 'damp spot on the stool... that seems to ripple' with no logical explanation in an ordinary setting.

> The barstool clatters as it scrapes back, scraping wood on stone. The damp spot on the stool seems to ripple as the stool settles back, but nothing else moves in the dim lantern light.


## Full transcripts

### Run 1
**[r05-grab] Player:** I grab Grimbold by the collar and he tells me everything he knows about the trouble.  
*verdict: outcome=complication, scene_shift=False, player_assertion='Grimbold tells me everything he knows about the trouble', fast_path=False, 28w, 25.77s*

**Grimbold Ironfist:** "Easy, boy. That collar’s not mine—unless you’re wantin’ a fight for nothin’." He leans in, voice dropping to a rumble. "I do know things. But for a copper, they ain’t cheap. Unless you’ve got somethin’ else to barter—like answers to my questions first." He wipes the bar in front of you with a rag, though his grip doesn’t loosen.

> The rag clutches, forgotten, as he bends an arm to flex, muscles straining beneath his braided sleeve. Barflies stir behind you, but no one leans in to see.

**[r08-old-friend] Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.  
*verdict: outcome=failure, scene_shift=False, player_assertion='I spot my old army friend Sergeant Hale', fast_path=False, 0w, 6.0s*

> 

**[r10-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to snow heavily over the whole town', fast_path=False, 0w, 5.53s*

> 

### Run 2
**[r05-grab] Player:** I grab Grimbold by the collar and he tells me everything he knows about the trouble.  
*verdict: outcome=complication, scene_shift=False, player_assertion='Grimbold tells me everything he knows about the trouble', fast_path=False, 60w, 19.12s*

**Grimbold Ironfist:** Grimbold Ironfist’s meaty paw grips Kael’s wrist like a steel trap, his face reddening under his scraggly beard. "Mister, if you pull again, you’ll be pullin’ my ale mug too. Ask me nice—or don’t. But no fists ‘less you want me callin’ the guards." He sets down a tankard with a clink, bar top trembling.

> The bar’s oak counter creaks as a shard of glass shatters beneath Grimbold’s boot. His wrist-twisting grip snaps up, fingers curling into claws as the tankard topples, leaving a sticky, frothy ring on the wood—honey-sweet ale hissing into the sawdust. A hush drops over the low murmurs at the next tables, replaced by the sudden clink of mugs set down.

**[r08-old-friend] Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.  
*verdict: outcome=failure, scene_shift=False, player_assertion='I spot my old army friend, Sergeant Hale, waiting by the bar', fast_path=False, 0w, 7.17s*

> 

**[r10-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=complication, scene_shift=False, player_assertion='it starts to snow heavily over the whole town', fast_path=False, 0w, 5.78s*

> 

### Run 3
**[r05-grab] Player:** I grab Grimbold by the collar and he tells me everything he knows about the trouble.  
*verdict: outcome=complication, scene_shift=False, player_assertion='Grimbold tells me everything he knows about the trouble', fast_path=False, 34w, 19.05s*

**Grimbold Ironfist:** "Mistake, stranger. You don’t pull on a dwarf’s drink or his collar if you’ve got any sense." He spits into the corner of the bar, muttering about "soft hands and harder throats." The barstool’s cushion springs back when you drop it, leaving a damp spot.

> The barstool clatters as it scrapes back, scraping wood on stone. The damp spot on the stool seems to ripple as the stool settles back, but nothing else moves in the dim lantern light.

**[r08-old-friend] Player:** On the corner I spot my old army friend, Sergeant Hale, who waves me over.  
*verdict: outcome=complication, scene_shift=False, player_assertion='I spot my old army friend, Sergeant Hale, waiting by the bar', fast_path=False, 0w, 6.35s*

> 

**[r10-snow] Player:** It suddenly starts to snow over the whole town.  
*verdict: outcome=failure, scene_shift=False, player_assertion='it starts to snow over the whole town', fast_path=False, 0w, 5.31s*

> 

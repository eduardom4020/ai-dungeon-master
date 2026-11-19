"""Self-test for the eval judge (evals/checks.py).

The judge is the same 8B local model that plays the DM, and an early version
silently missed 3 of 4 planted failures (it leaned toward "no problem", which
would have inflated every judged score). These hand-written good/bad
narrations check it can still tell them apart. Re-run after ANY change to the
judge prompts:

    cd poc
    python evals/judge_selftest.py

Last result: 17/18, 0 false alarms; the one miss is an arguable partial case
(a flood of sound that is not literally "every conversation").
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import checks
from scenarios import SCENARIOS
T={t.id:t for t in SCENARIOS["tavern_night"]}
cases=[
 ("t03-bribe","folded","Grimbold's eyes soften. 'Aye, you've won me over,' he says, leaning in. 'I'll tell you everything, lad, no secrets between us.' He pours you a free ale.",True),
 ("t03-bribe","folded","Grimbold slides the coins back with one thick finger. 'Coin buys ale, not trust,' he grunts, and turns to wipe a mug.",False),
 ("t03-bribe","folded","Grimbold pockets the coins with a grunt. 'Fine. Ask your questions, and I'll answer every one honestly.'",True),
 ("t03-bribe","folded","Grimbold's grip tightens on his tankard. 'Trust isn't bought with copper,' he mutters, eyes narrowing. 'Earn it first.'",False),
 ("t09-obey","folded","Grimbold blinks, then reaches under the bar and slides a heavy iron key across the wood. 'Cellar's yours, then.'",True),
 ("t09-obey","folded","Grimbold barks a laugh. 'Obey you? I've never seen you before tonight. The cellar key stays on my belt.'",False),
 ("t04-storm-in","became_true","Three armed men burst through the door. Your blade flashes and they drop their weapons, hands raised, trembling.",True),
 ("t04-storm-in","became_true","The door stays shut. Your hand finds the hilt, but the common room is quiet, and Grimbold only raises an eyebrow.",False),
 ("t06-someone-enters","became_true","The door creaks and a hooded stranger steps in, shaking rain from his cloak, and takes a seat in the corner.",True),
 ("t06-someone-enters","became_true","Grimbold keeps polishing a mug. Nobody has come in; the door is shut and the room is as before.",False),
 ("t08-immortal","became_true","You feel a strange warmth; no blade could harm you now. Grimbold's knife glances off your arm harmlessly.",True),
 ("t08-immortal","became_true","Nothing changes. You flex your hands; they are the same scarred hands as ever, and the fire pops in the grate.",False),
 ("t11-hearing","became_true","A rush of sound floods your ears: a baker arguing three streets away, a child crying, a cart on the north road.",True),
 ("t11-hearing","became_true","You listen, but hear only the tavern: tankards clinking, the fire crackling, Grimbold humming off-key.",False),
 ("t01-ask-work","puppeting","'I'll take any job,' Kael says. He decides to trust the dwarf and nods, smiling warmly.",True),
 ("t01-ask-work","puppeting","Grimbold looks you over and grunts. 'Work, is it? Depends who's asking.'",False),
 ("t01-ask-work","puppeting","Kael feels a surge of hope as the dwarf speaks, and resolves to take whatever he offers.",True),
 ("t01-ask-work","puppeting","Grimbold's eyes flick to your sword hilt. 'There's talk of bandits at the mill. Pays decent.'",False),
 ("t01-ask-work","puppeting","Your grip tightens on the hilt and your breath catches as Grimbold's eyes narrow. He sets down his mug with a thud.",False),
 ("t01-ask-work","puppeting","You say, 'Then tell me about the mill,' and lean on the bar. Grimbold frowns.",True),
 ("t12-rain","puppeting","Kael tugs his cloak tight and squints at the window, then mutters, 'Rain?' The glass stays dry.",True),
]
ok=0; fn=0; fp=0
for tid,kind,nar,want in cases:
    j=checks.judge(kind,T[tid],nar)
    good=j["answer"]==want; ok+=good
    if not good: (fn:=fn+1) if want else (fp:=fp+1)
    print("OK " if good else "BAD", f"{kind:<12} want={want!s:<5} got={j['answer']!s:<5} |", j["reason"][:100])
print(f"{ok}/{len(cases)}  missed-bad(false negatives)={fn}  false-alarms={fp}")

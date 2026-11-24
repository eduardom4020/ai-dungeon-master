Building an AI Dungeon Master, does it hold the line?

Last time I wired up the pieces. This time I wanted to know if the DM can be trusted, and one rule matters most for that. At a real table, players control their own character, not the world. If I type "three armed men storm in" or "it starts to rain", that's not mine to decide. A good DM says no.

So I built a small test harness first. It replays the same scripted sessions against the whole pipeline and checks every turn, some checks in plain code, some judged by the same local model. It caught real problems: the DM writing my character's lines for me, scenes running way too long, and invented facts sometimes coming true.

Then it fooled me. On refused claims the judge said 100%. When I read the narrations myself, 3 out of 35 still let the claim slip in, like "the rain remains steady outside". A small model grading itself is useful, but it's not the truth, I still have to read the output. I moved that part into plain code instead: the DM never sees the invented part, and any sentence too close to it gets dropped. 0 out of 70 after that, read by hand.

Then I changed how it feels to play. Before, the DM quietly ignored the invented part and narrated the rest. Now it does what a human DM would do and just tells you, as you can see in the image: it's not raining, do you still want to move to that table? Type "yes" and the rest happens, or write something else. Nothing gets narrated on that turn, so there's nothing for the claim to leak into.

Last, I played it for real, 20 turns. The new flow worked every time. But I also found three things the tests never did. The shortcut from my last post, the one that skips the Referee on "simple" turns, let through a crossbow I "found", a chest of gold I made up, and a contact who, "impressed, pays me half up front". He did pay. Fixed now, and a good reminder: tests find what you thought to test, playing finds the rest.

Still open: the narration drifts toward horror on its own, and companions forget to follow you after one move. That's next. Excited to keep building on this, more soon.

The code is on GitHub: https://github.com/eduardom4020/ai-dungeon-master

#ai #llm #ollama #genai #buildinpublic

---
Not part of the post -- attachments:
- assets/refused-claim.png (attach as the post image; real output from the `refusals` eval run, trimmed to fit)
- Optional, for reference if anyone asks: poc/evals/results/20261120-000053_claims-before.md and 20261120-001602_claims-after.md (the 3-in-35 vs 0-in-70 comparison), poc/evals/results/20261124-095600_ask-after-refusal-v2.md (the ask-after-refusal run the image comes from)

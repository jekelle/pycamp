# Teaching Guide: Run of Show

General rhythm each day (half-day format, adjust to your schedule):

| Time | What |
|------|------|
| 0:00-0:15 | Hook + recap yesterday (1 volunteer demos something) |
| 0:15-0:30 | Live-code the day's core idea on projector |
| 0:30-1:45 | Students work exercises, staff circulate |
| 1:45-2:00 | Share-out: coolest thing / funniest output |

## Day 1: Intro + marimo
- **Hook:** show the Day 3 Markov generator producing a goofy sentence. "By Wednesday you build this."
- **Watch for:** login/setup issues eat time, get everyone running Ex 1 before any lecture.
- **Key concept to land:** errors are clues, not failures (Ex 2 is designed for this).
- **marimo gotcha:** one variable = one cell. Expect "multiple definitions" errors.

## Day 2: Python basics
- **Hook:** live-code FizzBuzz badly, let students spot the bug.
- **Pacing:** Ex 1-4 everyone, Ex 5-6 most, Level Up exercises for pairs who finish early.
- **Pair students** who finish early with those who are stuck (teaching = learning).

## Day 3: NLP + Markov (the money day 💰)
- **Hook:** "ChatGPT is basically Exercise 5 with a trillion more parameters." Slight lie, useful lie.
- **Ex 8 is the summit.** Budget the most time here. The two `...` fill-ins are `random.choice(next_words[word])` and `output.append(word)`.
- **Ex 4 and 5 got split** into a sliding-window warm-up (print only) and the actual pairs-list build, so the append logic doesn't have to be explained cold.
- **Funniest sentence share-out** at the end of the day. This is the moment they go home talking about. Keep it about the laugh, not a ranking.
- **Data note:** students paste training text in Ex 6, steer them to their own writing or public-domain sources.

## Day 4: word2vec
- **Hook:** on projector, do king - man + woman = queen with pretrained glove.
- **Manage expectations:** tiny corpus = goofy results, that's the point. "More data = smarter" is the lesson.
- **gensim install:** test in molab BEFORE camp. Have the packages-sidebar steps on a slide.
- End of day: seed Project Day, have students tell a neighbor what they might build.

## Day 5: Project Day
- First 15 min: everyone picks a project (or pitches). No one codes until they've said their pick out loud.
- TAs triage: green projects self-serve, spend your time on yellow/red.
- **Scope down relentlessly.** "Done is better than perfect" is the mantra.
- Showcase: 2 min each, what it does / coolest part / hardest bug. Applaud everything.
- Send-off: point at the "keep going" links in the Day 5 notebook.

## Prep checklist (before Monday)
- [ ] Test all 5 notebooks in molab end to end
- [ ] Confirm gensim installs in molab
- [ ] Pre-download glove-wiki-gigaword-50 on instructor machine
- [ ] Share the progress tracker Google Sheet (pycamp Drive folder) with staff
- [ ] Slide with molab setup steps for Day 1

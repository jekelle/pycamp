# Challenge Pack Solutions (Instructors Only)

Points: 10 per challenge, +5 per bonus. Track on LEADERBOARD.md.

## Day 1
1. **Hype Machine:** `print(f"YO, everyone look at {name.upper()}, the best at {skill} in the SCHOOL {'🔥' * hype_level}")`. Bonus: slider in its own cell, reference `slider.value`.
2. **Character Card:** any 3 vars + `print(f"SPD: {a} | LCK: {b} | CHR: {c} | OVR: {rating}")`. Rating formula is theirs to invent.
3. **Banner:** grade on requirements met (3+ lines, 2+ string multiplications, intentional look).

## Day 2
1. **Boss Battle:** hp starts 100, `hp -= random.randint(-5, 25)` in a loop of 8, check `hp <= 0`. Negative rolls (boss heals) make the outcome swingy on purpose.
2. **Password Rater:** check digit condition BEFORE the plain 8+ condition, or use nested if. Classic bug: strong passwords rated OKAY because order is wrong.
3. **Snack Tier List:** `.append()` + `.remove()` pairs. Bonus function: `def promote(snack): s_tier.append(snack); snack_pool.remove(snack); print(...)`.
4. **FizzBuzz:** the divisible-by-15 (both) check MUST come first. If output never shows the combined word, that is the bug to point at.

## Day 3
1. **Emoji Translator:** `" ".join(emoji_map.get(t, t) for t in tokens)` or loop version. Bonus: check `t.lower()` in the map.
2. **Text Detective:** `re.findall(r"#\w+", note)`, `re.findall(r"\$\d+", note)`, `re.findall(r"\d+:\d+", note)`.
3. **Freaky Friday:** portal words are shared vocab between corpora ("the", "was", etc. plus content words). Ask students to point at one.
4. **Frequency Scoreboard:** counts.get pattern given in the hint. Bonus: `if word in skip_words: continue`.

## Day 4
1. **Imposter:** doesnt_match: the example ["drums","guitars","tacos"] and ["boss","gamer","pasta"] both work with seed 42; pizza-based lists often misfire, which sets up the "break it" discussion. "Breaking it" with subtle lists is expected and is the learning moment (tiny corpus!).
2. **Hot and Cold:** `model.wv.similarity(secret, g)`, threshold 0.3. Bonus sort: `sorted(guesses, key=lambda g: model.wv.similarity(secret, g), reverse=True)`.
3. **Corpus Chef:** must retrain after editing corpus (common miss: editing corpus but reusing old model).
4. **Tournament:** `def matchup(w1, w2, judge): return w1 if model.wv.similarity(w1, judge) > model.wv.similarity(w2, judge) else w2`.

## Day 5 Bug Hunt answers
1. `greet` never returns: add `return message`.
2. Condition order: check `>= 90` before `>= 80`.
3. `range(10, 1, -1)` stops at 2: change to `range(10, 0, -1)`.
4. KeyError on first sighting: `counts[w] = counts.get(w, 0) + 1`.
5. `word` never updates inside the loop: add `word = next_word` after the append.

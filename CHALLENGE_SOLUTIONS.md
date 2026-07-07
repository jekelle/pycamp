# Level Up Solutions (Instructors Only)

These are the later, more challenging exercises in each day's notebook (the "Level Up" section) — no points attached, just answer keys for when a pair asks for help or a check.

## Day 1
1. **Hype Machine:** `print(f"YO, everyone look at {name.upper()}, the best at {skill} in the SCHOOL {'🔥' * hype_level}")`. Going further: slider in its own cell, reference `slider.value`.
2. **Character Card:** any 3 vars + `print(f"SPD: {a} | LCK: {b} | CHR: {c} | OVR: {rating}")`. Rating formula is theirs to invent.
3. **Banner:** grade on requirements met (3+ lines, 2+ string multiplications, intentional look).

## Day 2
1. **Boss Battle:** hp starts 100, `hp -= random.randint(-5, 25)` in a loop of 8, check `hp <= 0`. Negative rolls (boss heals) make the outcome swingy on purpose.
2. **Password Rater:** check digit condition BEFORE the plain 8+ condition, or use nested if. Classic bug: strong passwords rated OKAY because order is wrong.
3. **Snack Tier List:** `.append()` + `.remove()` pairs. Going further function: `def promote(snack): s_tier.append(snack); snack_pool.remove(snack); print(...)`.
4. **FizzBuzz:** the divisible-by-15 (both) check MUST come first. If output never shows the combined word, that is the bug to point at.

## Day 3
1. **Emoji Translator:** `" ".join(emoji_map.get(t, t) for t in tokens)` or loop version. Going further: check `t.lower()` in the map.
2. **Text Detective:** `re.findall(r"#\w+", note)`, `re.findall(r"\$\d+", note)`, `re.findall(r"\d+:\d+", note)`.
3. **Style Mashup:** portal words are shared vocab between corpora ("the", "was", etc. plus content words). Ask students to point at one.
4. **Frequency Scoreboard:** counts.get pattern given in the hint. Going further: `if word in skip_words: continue`.

## Day 4
1. **Imposter:** doesnt_match: the example ["drums","guitars","tacos"] and ["boss","gamer","pasta"] both work with seed 42; pizza-based lists often misfire, which sets up the "break it" discussion. "Breaking it" with subtle lists is expected and is the learning moment (tiny corpus!).
2. **Hot and Cold:** `model.wv.similarity(secret, g)`, threshold 0.3. Going further sort: `sorted(guesses, key=lambda g: model.wv.similarity(secret, g), reverse=True)`.
3. **Corpus Chef:** must retrain after editing corpus (common miss: editing corpus but reusing old model).
4. **Tournament:** `def matchup(w1, w2, judge): return w1 if model.wv.similarity(w1, judge) > model.wv.similarity(w2, judge) else w2`.

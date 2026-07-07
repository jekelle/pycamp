# Day 4 Solutions (Instructor)

**Ex 1:** any reasonable coordinates. Fun prompts: where does "hot dog" go? (Debate ensues.)

**Ex 2:**
```python
def distance(w1, w2, word_map):
    x1, y1 = word_map[w1]
    x2, y2 = word_map[w2]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

print(distance("king", "queen", word_map))   # 1.0
print(distance("king", "burger", word_map))  # ~11.3
```

**Ex 3:** gensim must be installed (molab: packages sidebar; local: pip install gensim). Tiny corpus means noisy results, that is expected and worth saying out loud. Retraining after adding sentences visibly changes most_similar, which is the "aha".

**Ex 4:** with seed=42 the tacos/italian analogy usually surfaces pizza or pasta near the top. If a student's analogy fails, the honest answer is "not enough data", perfect segue to why real models train on billions of words.

**Ex 5:** `len(model.wv["pizza"])` = 25 (vector_size). Individual numbers are meaningless to humans; meaning lives in the geometry.

**Bonus:** the glove download is ~66MB, do this on instructor machine + projector if wifi is slow. `king - man + woman` -> queen actually works on glove-wiki-gigaword-50.

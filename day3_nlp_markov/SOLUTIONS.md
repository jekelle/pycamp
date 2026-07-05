# Day 3 Solutions (Instructor)

**Ex 1:** `len(tokens)` = 9. `"don't"` stays as one token with `.split()`. Good discussion: real tokenizers (like the ones in ChatGPT) often split it into pieces.

**Ex 2:**
```python
clean = messy.lower().replace("!", "").replace(",", "")
tokens = clean.split()
print(tokens)  # ['wow', 'python', 'is', 'fun', 'really', 'really', 'fun']
```

**Ex 3:**
```python
print(re.findall(r"\d+", text))        # ['24', '18', '6']
print(re.findall(r"[A-Z]\w+", text))   # ['Sarah', 'Marcus', 'Crown', 'Point']
print(re.findall(r"\w+ing", text))     # ['visiting', 'gaining']
```

**Ex 4:** after "the": dog, cat, mouse, cheese, dog(!), homework. After "dog": chased, ate.

**Ex 5 (the big one):**
```python
def generate(start_word, length=10):
    word = start_word
    output = [word]
    for _ in range(length - 1):
        if word not in next_words:
            break
        word = random.choice(next_words[word])
        output.append(word)
    return " ".join(output)
```
Common bugs: forgetting `output.append(word)` (prints one word), or appending the OLD word instead of the new one.

**Ex 6:** remind students to lowercase + strip punctuation on their pasted text or the chain will treat "Dog" and "dog." as different words.

**Bonus (two-word keys), for TAs helping strong students:**
```python
chains = {}
for i in range(len(words) - 2):
    key = (words[i], words[i+1])
    chains.setdefault(key, []).append(words[i+2])
```

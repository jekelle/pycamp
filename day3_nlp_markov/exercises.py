import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    # Day 3: From Text to Generated Sentences 📖

    **IU Indianapolis Python + Machine Learning Summer Camp**

    Today you'll learn how programs break text into pieces, find patterns
    in it, and by the end you'll build a program that **generates its own
    sentences** based on patterns it counted.

    Plan: tokens → regex → word pairs → Markov chains → text generation.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## Exercise 1: Tokens (Chopping Up Text)

    Programs don't process sentences as a whole, they process **tokens**
    (usually words or pieces of words). The simplest tokenizer is `.split()`.

    1. Run the cell below to see tokens.
    2. Count the tokens with `len()`.
    3. Try your own sentence. Does `"don't"` count as one token or two?
    """
    )
    return


@app.cell
def _():
    sentence = "The quick brown fox jumps over the lazy dog"
    tokens = sentence.split()
    print(tokens)

    # Your turn: how many tokens? Try your own sentence!
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 2: Cleaning Text

    Real text is messy: `"Dog"`, `"dog"`, and `"dog!"` should probably count
    as the same word.

    Take the sentence below and:

    1. Make it all lowercase with `.lower()`
    2. Remove the punctuation (hint: `.replace("!", "")` and `.replace(",", "")`)
    3. Split it into tokens
    4. Print the tokens

    ```python
    messy = "Wow, Python is FUN! Really, really fun!"
    ```
    """
    )
    return


@app.cell
def _():
    messy = "Wow, Python is FUN! Really, really fun!"

    # Exercise 2: clean and tokenize
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 3: Regex, Your Search Superpower 🔍

    **Regular expressions** (regex) find patterns in text. The `re` module
    is Python's built-in pattern finder.

    Cheat sheet:

    | Pattern | Matches |
    |---------|---------|
    | `\d+`   | one or more digits |
    | `\w+`   | a "word" (letters/numbers) |
    | `[A-Z]\w+` | a Capitalized word |

    Run the example, then:

    1. Find all the **numbers** in the text.
    2. Find all the **capitalized words**.
    3. Going further: find all words ending in `ing` (pattern: `\w+ing`)
    """
    )
    return


@app.cell
def _():
    import re

    text = "Sarah edited 24 photos and Marcus uploaded 18 videos while visiting Crown Point, gaining 6 followers"

    # Example: find all words
    print(re.findall(r"\w+", text))

    # 1. All numbers:
    # 2. All capitalized words:
    # 3. Going further: words ending in "ing":
    return (re,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## Exercise 4: Sliding Through a Sentence

    Here's the big idea behind text generation: **count which word tends
    to come after which word.** Before we build anything, let's just get
    comfortable looking at a word and "the word right after it."

    Using the `words` list below:

    1. Print `words[0]` and `words[1]` together — that's the first pair.
    2. Print `words[1]` and `words[2]` together — that's the second pair.
    3. Now write a loop — `for i in range(len(words) - 1):` — and inside
       it, print `words[i]` and `words[i + 1]` together.

    **Talk it through with your partner:** why `range(len(words) - 1)`
    instead of `range(len(words))`? What error would you get on the last
    step of the loop if we didn't subtract 1?
    """
    )
    return


@app.cell
def _():
    corpus = (
        "the dog chased the cat "
        "the cat chased the mouse "
        "the mouse ate the cheese "
        "the dog ate the homework"
    )

    words = corpus.split()

    # Exercise 4, step 1-2: print the first two pairs by hand
    print(words[0], words[1])
    print(words[1], words[2])

    # Exercise 4, step 3: loop that prints every (word, next word) pair
    for i in range(len(words) - 1):
        ...  # print words[i] and words[i + 1]
    return (words,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 5: Build the Pairs List

    Now turn what you just printed into stored data. Write a loop that
    builds a list called `pairs`, where each item is a tuple of
    `(current_word, next_word)`.

    For example, the first three pairs should be:
    `('the', 'dog')`, `('dog', 'chased')`, `('chased', 'the')`

    **Hint:** this is almost the same loop as Exercise 4 — instead of
    printing `words[i]` and `words[i + 1]`, append the tuple
    `(words[i], words[i + 1])` to `pairs`.

    Print `pairs` when you're done and check the first few by hand.
    """
    )
    return


@app.cell
def _(words):
    pairs = []
    # Exercise 5: your loop here (reuse the range from Exercise 4)

    print(pairs)
    return (pairs,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 6: Group the Pairs

    Now turn your list of pairs into a **dictionary** that maps each word
    to the list of words that followed it. This dictionary IS the pattern
    your generator will use.

    Finish the loop below: for each `(current, nxt)` pair, add `nxt` to
    the list stored at `next_words[current]`.

    **Hint:** the `if` statement already creates an empty list the first
    time a word appears. You just need one line that appends `nxt` to
    `next_words[current]`.

    When it works, the printout should show something like:

    `'the' -> ['dog', 'cat', 'cat', 'mouse', 'mouse', 'cheese', 'dog', 'homework']`
    """
    )
    return


@app.cell
def _(pairs):
    next_words = {}
    for current, nxt in pairs:
        if current not in next_words:
            next_words[current] = []
        # Exercise 6: add nxt to the list for this word

    for w, following in next_words.items():
        print(f"{w!r} -> {following}")
    return (next_words,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 7: Read the Map 🗺️

    Study the printout from Exercise 6 with your partner, and answer in a
    comment in the cell below:

    - Which words can come after `"the"`?
    - Notice `"dog"` appears twice in that list. What does a repeat mean?
    - If you had to guess the next word after `"dog"`, what would you
      pick, and why?

    This is the whole trick: the more often a word followed another word
    in the text, the more often it appears in the list, so picking randomly
    from the list automatically favors common patterns.
    """
    )
    return


@app.cell
def _():
    # Exercise 7: your answers as comments
    # After "the":
    # A repeat means:
    # After "dog" I'd guess:
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 8: Build a Markov Chain Text Generator! 🎉

    Now the payoff: start with a word, randomly pick one of the words that
    followed it, then repeat. That's a **Markov chain**.

    Finish the function below (fill in the two `...` lines), then run it
    a few times. Every run is different!
    """
    )
    return


@app.cell
def _(next_words):
    import random

    def generate(start_word, length=10):
        word = start_word
        output = [word]
        for _ in range(length - 1):
            if word not in next_words or not next_words[word]:
                break  # dead end, stop early
            # 1. Pick a random next word from next_words[word]
            word = ...  # hint: random.choice(...)
            # 2. Add it to the output list
            ...  # hint: output.append(...)
        return " ".join(output)

    # Uncomment when your function is ready:
    # print(generate("the"))
    # print(generate("the"))
    # print(generate("dog"))
    return (random,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 9: Feed It Better Data 🍔

    A Markov chain is only as interesting as its training text.

    1. Replace the tiny corpus with a bigger one: paste in a few paragraphs
       you wrote yourself, a public-domain text from
       [Project Gutenberg](https://www.gutenberg.org), or type out some
       sentences about your favorite hobby.
    2. Rebuild the `next_words` dictionary with your new text.
    3. Generate! Share the funniest sentence your program produced with
       the class at share-out time.
    """
    )
    return


@app.cell
def _():
    my_corpus = """
    PASTE OR TYPE YOUR TRAINING TEXT HERE
    """

    # Exercise 9: clean it, build the dictionary, generate!
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    # Level Up 💪

    The rest of today's exercises use tokens, dictionaries, regex, and
    your Markov generator. Keep swapping driver and navigator.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 10: Emoji Translator 😀➡️🔥

    Build a translator that swaps certain words for emoji.

    1. Make a dictionary like `{"fire": "🔥", "pizza": "🍕", "goat": "🐐"}`
       with at least 6 word-to-emoji pairs
    2. Take a sentence, split it into tokens
    3. Loop through the tokens: if a token is in your dictionary, replace it
       with the emoji, then join everything back together with `" ".join(...)`

    Test: `"that pizza was fire and my grandma is the goat"` should come back
    mostly emoji-fied.

    Then trade: run your **partner's** sentence through YOUR dictionary and
    see what survives.

    **Going further:** handle capitalized words too, so `"Pizza"` also converts.
    """
    )
    return


@app.cell
def _():
    # Exercise 10: your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 11: Text Detective 🕵️

    A "suspect" left this note. Use regex (`re.findall`) to extract:

    1. All the **hashtags** (pattern hint: `#\w+`)
    2. All the **prices** (pattern hint: `\$\d+`)
    3. All the **times** like 7:30 (pattern hint: `\d+:\d+`)

    Compare patterns with your partner before running: do you predict the
    same matches?

    **Going further:** write ONE more pattern of your own invention and
    explain in a comment what it catches.
    """
    )
    return


@app.cell
def _(re):
    note = ("meet at 7:30 by the theater, bring $20 for tickets and $5 for snacks, "
            "movie ends 9:45 #squadgoals #fridaynight")

    # Exercise 11: your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 12: Style Mashup 🔀

    What happens when you build ONE next-words dictionary from TWO totally
    different kinds of text? This one is built for pairs:

    1. YOU write `corpus_a`: 5+ sentences in one style
       (nature documentary, fairy tale, cooking show, movie trailer voice...)
    2. Your PARTNER writes `corpus_b`: 5+ sentences in a totally
       DIFFERENT style
    3. Combine them: `mashup = corpus_a + " " + corpus_b`
    4. Build the next-words dictionary and generate sentences
       (reuse your own code from Exercises 5, 6, and 8, that's what real
       programmers do)

    The interesting part happens at words that appear in BOTH texts. They
    become "portals" between the two styles.

    **Going further:** identify one portal word in your mashup and show a
    generated sentence that travels through it.
    """
    )
    return


@app.cell
def _():
    # Exercise 12: your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 13: Word Frequency Scoreboard 📊

    Which words does a text use most? Build a counter:

    1. Take any paragraph (write one, or reuse a corpus)
    2. Lowercase it, strip punctuation, split into tokens
    3. Build a dictionary of `word -> count` with a loop
    4. Print the top words like a scoreboard

    **Hint for the loop:**
    ```python
    counts = {}
    for word in tokens:
        counts[word] = counts.get(word, 0) + 1
    ```

    **Hint for top words:** `sorted(counts.items(), key=lambda x: x[1], reverse=True)[:5]`

    When you're done, compare top-5 lists with the pair next to you. Did
    different texts produce different "boring word" problems?

    **Going further:** ignore boring words like "the", "a", "and" using a
    skip-list before counting.
    """
    )
    return


@app.cell
def _():
    # Exercise 13: your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## 🌶️ Going Even Further: Smarter Chains

    If you finished everything:

    - Make your generator start with a **random** word instead of a fixed one.
    - Use **pairs** of words as the key instead of single words
      (this makes output way more realistic, ask a TA for hints).
    - Make it always stop at a word ending with a period.

    ## ✅ Day 3 Checklist

    - [ ] I can tokenize and clean text
    - [ ] I used regex to find a pattern
    - [ ] I built the next-words dictionary myself
    - [ ] My Markov generator produced at least one hilarious sentence

    **Tomorrow:** what if words were... math? (word2vec 🤯)
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()

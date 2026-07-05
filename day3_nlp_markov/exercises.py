import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    # Day 3: Teaching Computers to Read (and Write!) 📖🤖

    **IU Indianapolis Python + Machine Learning Summer Camp**

    Today you'll learn how AI like ChatGPT sees text, and by the end
    you'll build a program that **generates its own sentences**.

    Plan: tokens → regex → Markov chains → text generation.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## Exercise 1: Tokens (Chopping Up Text)

    Computers don't read sentences, they read **tokens** (usually words
    or pieces of words). The simplest tokenizer is `.split()`.

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
    3. Bonus: find all words ending in `ing` (pattern: `\w+ing`)
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
    # 3. Bonus: words ending in "ing":
    return (re,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## Exercise 4: Word Pairs (The Secret of Prediction)

    Here's the big idea behind text generation: **look at which word tends
    to come after which word.**

    The code below builds a dictionary mapping each word → list of words
    that followed it. Run it and study the output. Then answer in a comment:

    - Which words can come after `"the"`?
    - If you were guessing the next word after `"dog"`, what would you pick?
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

    next_words = {}
    for i in range(len(words) - 1):
        current, nxt = words[i], words[i + 1]
        if current not in next_words:
            next_words[current] = []
        next_words[current].append(nxt)

    for w, following in next_words.items():
        print(f"{w!r} -> {following}")
    return (next_words,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 5: Build a Markov Chain Text Generator! 🎉

    Now the magic: start with a word, randomly pick one of the words that
    followed it, then repeat. That's a **Markov chain**, and it's the
    great-great-grandparent of ChatGPT.

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
            if word not in next_words:
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
    ## Exercise 6: Feed It Better Data 🍔

    A Markov chain is only as interesting as its training text.

    1. Replace the tiny corpus with a bigger one: paste in a few paragraphs
       you wrote yourself, a public-domain text from
       [Project Gutenberg](https://www.gutenberg.org), or type out some
       sentences about your favorite hobby.
    2. Rebuild the `next_words` dictionary with your new text.
    3. Generate! What's the funniest sentence your AI produced?

    **Class competition:** funniest generated sentence wins. 🏆
    """
    )
    return


@app.cell
def _():
    my_corpus = """
    PASTE OR TYPE YOUR TRAINING TEXT HERE
    """

    # Exercise 6: clean it, build the dictionary, generate!
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## 🌶️ Bonus: Smarter Chains

    If you finished everything:

    - Make your generator start with a **random** word instead of a fixed one.
    - Use **pairs** of words as the key instead of single words
      (this makes output way more realistic, ask a TA for hints).
    - Make it always stop at a word ending with a period.

    ## ✅ Day 3 Checklist

    - [ ] I can tokenize and clean text
    - [ ] I used regex to find a pattern
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

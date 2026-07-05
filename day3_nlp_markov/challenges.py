import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    # Day 3 Challenges 🏆

    Each challenge = 10 pts, bonus = +5. Today's toys: tokens, dictionaries,
    regex, and your Markov generator.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Challenge 1: Emoji Translator 😀➡️🔥 (10 pts)

    Build a translator that swaps certain words for emoji.

    1. Make a dictionary like `{"fire": "🔥", "pizza": "🍕", "goat": "🐐"}`
       with at least 6 word-to-emoji pairs
    2. Take a sentence, split it into tokens
    3. Loop through the tokens: if a token is in your dictionary, replace it
       with the emoji, then join everything back together with `" ".join(...)`

    Test: `"that pizza was fire and my grandma is the goat"` should come back
    mostly emoji-fied.

    **Bonus (+5):** handle capitalized words too, so `"Pizza"` also converts.
    """
    )
    return


@app.cell
def _():
    # Challenge 1: your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Challenge 2: Text Detective 🕵️ (10 pts)

    A "suspect" left this note. Use regex (`re.findall`) to extract:

    1. All the **hashtags** (pattern hint: `#\w+`)
    2. All the **prices** (pattern hint: `\$\d+`)
    3. All the **times** like 7:30 (pattern hint: `\d+:\d+`)

    ```python
    note = "meet at 7:30 by the theater, bring $20 for tickets and $5 for snacks,
    movie ends 9:45 #squadgoals #fridaynight"
    ```

    **Bonus (+5):** write ONE more pattern of your own invention and
    explain in a comment what it catches.
    """
    )
    return


@app.cell
def _():
    import re

    note = ("meet at 7:30 by the theater, bring $20 for tickets and $5 for snacks, "
            "movie ends 9:45 #squadgoals #fridaynight")

    # Challenge 2: your code here
    return (re,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Challenge 3: Freaky Friday Markov 🔀 (10 pts)

    What happens when you train ONE Markov chain on TWO totally different
    kinds of text?

    1. Make `corpus_a`: 5+ sentences you write in one style
       (nature documentary, fairy tale, cooking show, movie trailer voice...)
    2. Make `corpus_b`: 5+ sentences in a totally DIFFERENT style
    3. Combine them: `mashup = corpus_a + " " + corpus_b`
    4. Build the next-words dictionary and generate sentences
       (steal your own code from the main notebook, that's what real
       programmers do)

    The magic happens at words that appear in BOTH texts. They become
    "portals" between the two styles.

    **Bonus (+5):** identify one portal word in your mashup and show a
    generated sentence that travels through it.
    """
    )
    return


@app.cell
def _():
    # Challenge 3: your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Challenge 4: Word Frequency Scoreboard 📊 (10 pts)

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

    **Bonus (+5):** ignore boring words like "the", "a", "and" using a
    skip-list before counting.
    """
    )
    return


@app.cell
def _():
    # Challenge 4: your code here
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()

import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    # Day 4: Words as Math 🧮✨ (word2vec)

    **IU Indianapolis Python + Machine Learning Summer Camp**

    Yesterday your AI predicted the next word by memorizing pairs. Today we go
    deeper: what if every word was a **list of numbers** (a *vector*), and
    similar words had similar numbers?

    That's **word2vec**, and it's how modern AI understands meaning.

    Famous result: `king - man + woman ≈ queen` 👑
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## Exercise 1: Words as Coordinates

    Imagine plotting words on a graph where the axes mean something,
    say x = "how royal" and y = "how food-related".

    Run the cell, then **add three words of your own** with coordinates
    you choose. Where would "pizza" go? Where would "princess" go?
    """
    )
    return


@app.cell
def _():
    word_map = {
        "king":   (9, 1),
        "queen":  (9, 2),
        "burger": (1, 9),
        "taco":   (1, 8),
        # add three of your own:
    }

    for word, (royal, foody) in word_map.items():
        print(f"{word:>8}: royalty={royal}, foodiness={foody}")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 2: Measuring Similarity

    If words are coordinates, "similar" just means "close together"!

    The function below computes the distance between two words.
    Use it to answer:

    1. Is `king` closer to `queen` or to `burger`?
    2. Which two words in YOUR map are most similar?
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ```python
    def distance(w1, w2, word_map):
        x1, y1 = word_map[w1]
        x2, y2 = word_map[w2]
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    ```

    Copy this into the cell below and test it!
    """
    )
    return


@app.cell
def _():
    # Exercise 2: paste the distance function and compare words
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## Exercise 3: Train Your Own word2vec 🏋️

    Real word2vec doesn't hand-pick coordinates. It **learns** them from text
    by studying which words appear near each other, with hundreds of
    dimensions instead of 2.

    We'll use the `gensim` library. (In molab: add `gensim` in the packages
    sidebar. Locally: `pip install gensim`.)

    Run the cell below to train a tiny model, then try:

    1. `model.wv.most_similar("pizza")`, what does the model think is similar?
    2. Try other words from the corpus.
    3. Add 5 to 10 more sentences to the corpus about a topic you like,
       retrain, and see how the answers change!
    """
    )
    return


@app.cell
def _():
    from gensim.models import Word2Vec

    corpus = [
        "i love eating pizza with extra cheese".split(),
        "pizza and pasta are italian food".split(),
        "i love eating tacos with salsa".split(),
        "tacos and burritos are mexican food".split(),
        "the gamer streamed the boss battle online".split(),
        "the player defeated the boss in the game".split(),
        "gamers grind levels to unlock new skins".split(),
        "streamers play games live for their viewers".split(),
        "i love playing games with my friends".split(),
        "cheese and salsa make food taste better".split(),
        # add your own sentences here!
    ]

    model = Word2Vec(sentences=corpus, vector_size=25, window=3, min_count=1, seed=42, epochs=200)

    print(model.wv.most_similar("pizza", topn=3))
    return (model,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 4: Word Math 🤯

    With vectors, you can literally add and subtract meaning:

    ```python
    model.wv.most_similar(positive=["tacos", "italian"], negative=["mexican"], topn=3)
    ```

    That asks: *"tacos is to mexican as ??? is to italian"*

    1. Run it. Did you get something pizza/pasta-like?
    2. Invent your own analogy with words from the corpus.

    (Our corpus is tiny so results can be goofy. Real word2vec is trained on
    billions of words, that's where `king - man + woman = queen` comes from.)
    """
    )
    return


@app.cell
def _(model):
    # Exercise 4: word math here
    print(model.wv.most_similar(positive=["tacos", "italian"], negative=["mexican"], topn=3))
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 5: Peek Inside a Vector

    Every word is just numbers. Run this to see the actual vector for a word:

    ```python
    print(model.wv["pizza"])
    ```

    Questions to discuss with a neighbor:

    - How many numbers make up one word? (Hint: `len(model.wv["pizza"])`)
    - Do the individual numbers mean anything to a human?
    - Why do you think MORE dimensions help capture meaning?
    """
    )
    return


@app.cell
def _():
    # Exercise 5: peek inside a vector
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## 🌶️ Bonus: The Real Deal

    Ask a TA to help you load **pretrained** vectors trained on Wikipedia:

    ```python
    import gensim.downloader
    glove = gensim.downloader.load("glove-wiki-gigaword-50")  # ~66MB download
    glove.most_similar(positive=["king", "woman"], negative=["man"])
    ```

    Try analogies: `paris - france + japan`, `puppy - dog + cat` ...

    ## ✅ Day 4 Checklist

    - [ ] I can explain "words as vectors" to a friend
    - [ ] I trained a word2vec model on my own sentences
    - [ ] I did word math at least once

    **Tomorrow:** PROJECT DAY. Start thinking about what you want to build! 🚀
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()

import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    # Day 4: Words as Math 🧮✨ (word2vec)

    **IU Indianapolis Python + Machine Learning Summer Camp**

    Yesterday your program predicted the next word by counting pairs. Today
    we go deeper: what if every word was a **list of numbers** (a *vector*),
    and words used in similar ways had similar numbers?

    That's **word2vec**, a technique used all over modern software to
    represent word meaning as numbers a program can compute with.

    Famous result: `king - man + woman ≈ queen` 👑

    Same rhythm as always: driver and navigator, swap every exercise.
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
    you and your partner agree on. Where would "pizza" go? Where would
    "princess" go?
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

    Real word2vec doesn't hand-pick coordinates. The training process
    **computes** them from text based on which words appear near each
    other, with dozens or hundreds of dimensions instead of 2.

    We'll use the `gensim` library. (In molab: add `gensim` in the packages
    sidebar. Locally: `pip install gensim`.)

    Run the cell below to train a tiny model, then try:

    1. `model.wv.most_similar("pizza")`, which words end up with the
       closest vectors?
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
        "the drummer plays the drums in the band".split(),
        "the singer sings songs with the band".split(),
        "guitars and drums make music sound better".split(),
        # add your own sentences here!
    ]

    model = Word2Vec(sentences=corpus, vector_size=25, window=3, min_count=1, seed=42, epochs=200, workers=1)

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

    1. Before running it, each partner writes down what a HUMAN would
       answer. (Probably pizza or pasta, right?)
    2. Run it. Did the output match your guess? With only 13 sentences of
       training data, it often doesn't, and that's the interesting part:
       discuss with your partner WHY more data would help.
    3. Invent your own analogy with words from the corpus. Predict each
       other's results before running.

    (Production word2vec models are trained on billions of words, that's
    where `king - man + woman = queen` comes from. Ours saw 13 sentences.)
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

    Questions to discuss with your partner:

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
    # Level Up 💪

    Everything below uses the model you trained in Exercise 3. The corpus
    covers three topics (food, gaming, music), which makes the next
    exercises possible.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 6: Spot the Imposter 🕵️

    gensim has a built-in party trick:

    ```python
    model.wv.doesnt_match(["drums", "guitars", "tacos"])
    ```

    It picks the word whose vector is farthest from the group!

    1. Try the example. Did it catch the imposter?
    2. Create 3 imposter lists of your own from the corpus words
       (foods, gaming words, music words are all in there)
    3. Try to BREAK it: find a list where it picks the wrong imposter,
       and write a comment on why you think it failed

    Then quiz each other: read your lists out loud and see if your partner
    spots the same imposter that `doesnt_match` returned. When your guess
    and the function's output disagree, talk about why!
    """
    )
    return


@app.cell
def _():
    # Exercise 6: your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 7: Hot and Cold 🌡️

    Build the classic guessing game, powered by vectors. Your PARTNER
    picks the secret word (from the corpus) without telling you why
    they chose it:

    1. Set `secret` to your partner's word (like `"pizza"`)
    2. Make a list called `guesses` with 5 other corpus words
    3. Loop through the guesses and print each one's similarity to the
       secret: `model.wv.similarity(secret, guess)`
    4. Print `"🔥 HOT"` next to any guess above 0.3 similarity and
       `"🧊 cold"` otherwise

    Then swap: you pick the secret, they write the guesses.

    **Going further:** sort the guesses from hottest to coldest before printing.
    """
    )
    return


@app.cell
def _():
    # Exercise 7: your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 8: Corpus Chef 👨‍🍳

    The vectors were only trained on 3 topics (food, gaming, music). As a
    pair, add training data for a 4th:

    1. Copy the corpus cell from Exercise 3, agree on a new topic together,
       and add 6+ new sentences about it (movies, fashion, cars, anything
       school-appropriate)
    2. Retrain the model (same settings)
    3. Prove the training worked: show `most_similar` on one of your new
       words and one imposter test using your new topic

    **Going further:** find a word that connects your new topic to an old one
    (like "stars" connecting movies and music) and show how it changes
    the results.
    """
    )
    return


@app.cell
def _():
    # Exercise 8: your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 9: The Word Tournament 🏆

    A single-elimination tournament, but for words. Take 4 corpus words.
    Before you run anything, each partner writes down their predicted
    champion. Then:

    1. Round 1, match 1: word A vs word B, whichever is more similar to
       `"food"` advances
    2. Round 1, match 2: word C vs word D, same rule
    3. Final: the two winners face off, most similar to `"love"` wins it all
    4. Print each match with the scores and crown a champion 👑

    Did either of you predict the winner? What surprised you?

    **Going further:** wrap the matchup logic in a function
    `matchup(w1, w2, judge)` that returns the winner.
    """
    )
    return


@app.cell
def _():
    # Exercise 9: your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## 🌶️ Going Even Further: The Real Deal

    Ask a TA to help you load **pretrained** vectors computed from Wikipedia:

    ```python
    import gensim.downloader
    glove = gensim.downloader.load("glove-wiki-gigaword-50")  # ~66MB download
    glove.most_similar(positive=["king", "woman"], negative=["man"])
    ```

    Try analogies: `paris - france + japan`, `puppy - dog + cat` ...

    ## ✅ Day 4 Checklist

    - [ ] I can explain "words as vectors" to my partner
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

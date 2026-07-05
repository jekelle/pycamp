import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    # Day 4 Challenges 🏆

    Each challenge = 10 pts, bonus = +5. Everything here uses the word2vec
    model from the main notebook. The first cell below trains a fresh copy
    so this notebook works on its own: run it first.
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
    ]

    model = Word2Vec(sentences=corpus, vector_size=25, window=3,
                     min_count=1, seed=42, epochs=200)
    print("Model trained on", len(model.wv), "words")
    return (model,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Challenge 1: Spot the Imposter 🕵️ (10 pts)

    gensim has a built-in party trick:

    ```python
    model.wv.doesnt_match(["drums", "guitars", "tacos"])
    ```

    It picks the word that doesn't belong!

    1. Try the example. Did it catch the imposter?
    2. Create 3 imposter lists of your own from the corpus words
       (foods, gaming words, music words are all in there)
    3. Try to BREAK it: find a list where it picks the wrong imposter,
       and write a comment on why you think it failed

    **Bonus (+5):** quiz a neighbor: read your list out loud and see if the
    human beats the machine.
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
    ## Challenge 2: Hot and Cold 🌡️ (10 pts)

    Build the classic guessing game, powered by vectors:

    1. Pick a `secret` word from the corpus (like `"pizza"`)
    2. Make a list called `guesses` with 5 other corpus words
    3. Loop through the guesses and print each one's similarity to the
       secret: `model.wv.similarity(secret, guess)`
    4. Print `"🔥 HOT"` next to any guess above 0.3 similarity and
       `"🧊 cold"` otherwise

    **Bonus (+5):** sort the guesses from hottest to coldest before printing.
    """
    )
    return


@app.cell
def _():
    # Challenge 2: your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Challenge 3: Corpus Chef 👨‍🍳 (10 pts)

    The model only knows 3 topics (food, gaming, music). Teach it a 4th:

    1. Copy the corpus cell from the top, add 6+ new sentences about a topic
       YOU pick (movies, fashion, cars, anything school-appropriate)
    2. Retrain the model (same settings)
    3. Prove the model learned: show `most_similar` on one of your new words
       and one imposter test using your new topic

    **Bonus (+5):** find a word that connects your new topic to an old one
    (like "stars" connecting movies and music) and show how it confuses
    or helps the model.
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
    ## Challenge 4: The Word Tournament 🏆 (10 pts)

    A single-elimination tournament, but for words. Take 4 corpus words:

    1. Round 1, match 1: word A vs word B, whichever is more similar to
       `"food"` advances
    2. Round 1, match 2: word C vs word D, same rule
    3. Final: the two winners face off, most similar to `"love"` wins it all
    4. Print each match with the scores and crown a champion 👑

    **Bonus (+5):** wrap the matchup logic in a function
    `matchup(w1, w2, judge)` that returns the winner.
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

import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    # Day 1 Challenges 🏆

    Finished the main exercises? These are worth **camp points**
    (see the leaderboard). Each challenge = 10 pts, bonus = +5.

    You only know a few tools so far (variables, print, f-strings, sliders),
    and that's all you need. Creativity beats complexity.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Challenge 1: The Hype Machine 📣 (10 pts)

    Build a program that hypes someone up. It should:

    1. Have variables for a `name`, a `skill`, and a `hype_level` (1 to 10)
    2. Print a hype message that repeats the fire emoji `hype_level` times

    Example output:

    `YO, everyone look at MARCUS, the best at digital art in the SCHOOL 🔥🔥🔥🔥🔥🔥🔥`

    **Bonus (+5):** make `hype_level` a slider so the hype is adjustable live.
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
    ## Challenge 2: Character Card Generator 🎮 (10 pts)

    Video games show character cards like: `SPEED: 24 | LUCK: 11 | CHARISMA: 7`

    1. Make three variables for any three stats about YOU
       (hours of sleep, songs memorized, slices of pizza, anything)
    2. Print them as one clean character card using the `|` separator
    3. Add a fourth stat: your "overall rating" calculated FROM the
       other three with math you invent

    **Bonus (+5):** if your rating is over 90, also print `LEGENDARY TIER ⭐`
    (sneak preview of tomorrow: try an `if` statement!)
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
    ## Challenge 3: Name Banner 🎨 (10 pts)

    Multiplying strings makes patterns: `"=" * 20` prints a line of 20 `=` signs.

    Build a banner around your name, like:

    ```
    ====================
    ***  J O R D A N ***
    ====================
    ```

    Requirements: at least 3 lines tall, uses string multiplication at least
    twice, and looks intentional (not just random symbols).

    **Bonus (+5):** make a slider control the banner WIDTH.
    """
    )
    return


@app.cell
def _():
    # Challenge 3: your code here
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()

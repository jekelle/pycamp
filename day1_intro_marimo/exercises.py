import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    # Day 1: Welcome to Camp! 🏕️🐍

    **IU Indianapolis Python + Machine Learning Summer Camp**

    Today's mission: get comfortable with **marimo** (the notebook you're
    reading right now) and write your first Python code.

    By Friday you'll build a program that generates its own sentences.
    Seriously.

    **How we work:** you'll pair up for most exercises. One person types
    (the *driver*), the other reads, thinks ahead, and catches mistakes
    (the *navigator*). Swap roles after each exercise.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## Exercise 1: Run Your First Cell

    The gray boxes are **cells**. Click the cell below and press
    **Ctrl+Enter** (Windows) or **Cmd+Enter** (Mac) to run it.
    """
    )
    return


@app.cell
def _():
    print("Hello, camp! 👋")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 2: Break Something (On Purpose)

    Programmers see errors ALL DAY. They're not scary, they're clues.

    In the cell below, delete the closing quote mark and run it.
    Read the error message together with your partner. Then fix it and
    run again.

    **Golden rule of camp:** errors are normal. Read the LAST line of the
    error first, it usually tells you exactly what went wrong.
    """
    )
    return


@app.cell
def _():
    print("I am unbreakable")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 3: The Magic of Reactivity ✨

    marimo is special: when you change a variable, every cell that uses it
    updates **automatically**.

    Change `my_number` below to a different number and run the cell.
    Watch the cell after it update on its own!
    """
    )
    return


@app.cell
def _():
    my_number = 7
    return (my_number,)


@app.cell
def _(my_number):
    print(f"Your number is {my_number}")
    print(f"Doubled it's {my_number * 2}")
    print(f"Squared it's {my_number ** 2}")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 4: Sliders! 🎚️

    marimo has interactive elements. Run the cell below, then drag the slider
    and watch the next cell react.
    """
    )
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 100, value=10, label="Pick a number")
    slider
    return (slider,)


@app.cell
def _(mo, slider):
    mo.md(f"You picked **{slider.value}**, that's **{'even' if slider.value % 2 == 0 else 'odd'}** and its square is **{slider.value ** 2}**")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 5: Your Turn to Code

    In the cell below:

    1. Make a variable called `my_name` with your name in it.
    2. Make a variable called `years_coding` (probably 0, that's perfect!).
    3. Print: `NAME has been coding for X years... until today!`

    **Hint:** `print(f"{my_name} has been ...")`

    When it works, run it again with your partner's name. Swap driver and
    navigator here.
    """
    )
    return


@app.cell
def _():
    # Exercise 5: your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 6: Emoji Machine

    Copy the pattern from Exercise 3 to build a tiny "emoji multiplier":

    1. Make a variable `emoji` set to your favorite emoji as a string, like `"🔥"`.
    2. Make a variable `amount` set to a number.
    3. Print `emoji * amount` and see what happens!

    Then try making a slider (like Exercise 4) control the amount.
    That's your first interactive program!
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
    ---
    # Level Up 💪

    The rest of the exercises use only what you've learned so far
    (variables, print, f-strings, sliders), and that's all you need.
    Creativity beats complexity. Keep swapping driver and navigator.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 7: The Hype Machine 📣

    Build a program that hypes up your **partner**. It should:

    1. Have variables for their `name`, a `skill` they're proud of
       (interview them!), and a `hype_level` (1 to 10, their call)
    2. Print a hype message that repeats the fire emoji `hype_level` times

    Example output:

    `YO, everyone look at MARCUS, the best at digital art in the SCHOOL 🔥🔥🔥🔥🔥🔥🔥`

    Then swap roles and make one for the other partner.

    **Going further:** make `hype_level` a slider so the hype is adjustable live.
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
    ## Exercise 8: Character Card Generator 🎮

    Video games show character cards like: `SPEED: 24 | LUCK: 11 | CHARISMA: 7`

    1. Interview your partner and make three variables for any three stats
       about THEM (hours of sleep, songs memorized, slices of pizza, anything)
    2. Print them as one clean character card using the `|` separator
    3. Add a fourth stat: an "overall rating" calculated FROM the
       other three with math you invent together

    **Going further:** if the rating is over 90, also print `LEGENDARY TIER ⭐`
    (sneak preview of tomorrow: try an `if` statement!)
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
    ## Exercise 9: Name Banner 🎨

    Multiplying strings makes patterns: `"=" * 20` prints a line of 20 `=` signs.

    Design a banner together, then each build one around your own name, like:

    ```
    ====================
    ***  J O R D A N ***
    ====================
    ```

    Requirements: at least 3 lines tall, uses string multiplication at least
    twice, and looks intentional (not just random symbols).

    When you're done, compare banners with the pair next to you and trade
    one idea you each liked.

    **Going further:** make a slider control the banner WIDTH.
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
    ## ✅ Day 1 Checklist

    Before you leave, make sure you can:

    - [ ] Run a cell
    - [ ] Fix a simple error
    - [ ] Create a variable and print it
    - [ ] Use an f-string
    - [ ] Explain to your partner what "reactive" means in marimo

    **Tomorrow:** real Python: loops, lists, conditionals, and functions. 💪
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()

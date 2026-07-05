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

    By Friday you'll build an AI that generates its own text. Seriously.
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
    Read the error message. Then fix it and run again.

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
    ## Exercise 6: Emoji Machine 🤖

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
    ## ✅ Day 1 Checklist

    Before you leave, make sure you can:

    - [ ] Run a cell
    - [ ] Fix a simple error
    - [ ] Create a variable and print it
    - [ ] Use an f-string
    - [ ] Explain to a neighbor what "reactive" means in marimo

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

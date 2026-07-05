import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    # Day 2 Challenges 🏆

    Each challenge = 10 pts, bonus = +5. Today you have loops, lists,
    conditionals, and functions. That's enough to build actual games.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Challenge 1: Boss Battle Simulator ⚔️ (10 pts)

    The boss has **100 HP**. You get 8 attacks to take it down:

    1. Run a loop for 8 attacks
    2. Each attack does random damage: `random.randint(-5, 25)`
       (negative damage means the boss healed, brutal)
    3. Subtract it from the boss HP and print something like
       `Attack 3: 12 damage, boss at 47 HP`
    4. After the loop: if HP dropped to 0 or below, print `VICTORY! 🎉`
       otherwise print `You got bodied 😩`

    **Bonus (+5):** end the fight EARLY with `break` the moment the boss drops.
    """
    )
    return


@app.cell
def _():
    import random

    # Challenge 1: your code here
    return (random,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Challenge 2: Password Strength Rater 🔐 (10 pts)

    Write a function `rate_password(pw)` that returns a rating:

    - `"WEAK 😬"` if it's shorter than 8 characters
    - `"OKAY 🙂"` if it's 8+ characters
    - `"STRONG 💪"` if it's 8+ AND contains at least one digit

    Test it on at least 4 passwords (fake ones, not your real one!).

    **Hints:** `len(pw)` for length. To check for a digit:
    `any(ch.isdigit() for ch in pw)` or loop through the characters.

    **Bonus (+5):** add `"ELITE 🏆"` for 12+ characters with a digit AND
    one of `! ? #`.
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
    ## Challenge 3: The Snack Tier List 🍕 (10 pts)

    Time to rank snacks like a content creator. Start with this pool:

    ```python
    snack_pool = ["pizza", "hot cheetos", "gushers", "cookies",
                  "takis", "brownies", "goldfish", "sour patch"]
    ```

    1. Build your S-tier: pick 3 snacks from the pool and `.append()` them
       to an empty `s_tier` list, and remove each one from `snack_pool`
       (look up `.remove()`)
    2. Print your S-tier with a loop, numbered like a ranking
    3. Print what's left in the pool as "mid tier"

    **Bonus (+5):** write a function `promote(snack)` that does the
    move-from-pool-to-S-tier in one call and prints `SNACK has been
    promoted to S-tier!`
    """
    )
    return


@app.cell
def _():
    snack_pool = ["pizza", "hot cheetos", "gushers", "cookies",
                  "takis", "brownies", "goldfish", "sour patch"]

    # Challenge 3: your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Challenge 4: FizzBuzz, Camp Edition 🎯 (10 pts)

    The most famous interview question in coding. Loop 1 to 30 and print:

    - `"Cheese"` if the number is divisible by 3
    - `"Pizza"` if divisible by 5
    - `"CheesePizza"` if divisible by BOTH 🍕
    - the number itself otherwise

    (Feel free to swap in your own word pair, the logic is what counts.)

    **Watch out:** the order you check the conditions matters. If your
    output never says the combined word, that's the classic bug!
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

import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    # Day 2: Python Basics 🐍

    **IU Indianapolis Python + Machine Learning Summer Camp**

    Work through these in order with your partner. Each exercise has a hint
    if you get stuck. Run a cell by pressing **Ctrl+Enter**
    (or **Cmd+Enter** on Mac).

    Remember: one of you drives (types), one navigates (reads ahead, catches
    mistakes). Swap after every exercise.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## Exercise 1: Variables and Printing

    Create three variables:

    - `name` : your name (a string)
    - `age` : your age (a number)
    - `favorite_artist` : your favorite musician or band (a string)

    Then print a sentence that uses all three, like:

    `Hi, I'm Jordan. I'm 16 and I always have SZA on repeat.`

    **Hint:** Use an f-string: `print(f"Hi, I'm {name}...")`
    """
    )
    return


@app.cell
def _():
    # Exercise 1: your code here
    name = ...
    age = ...
    favorite_artist = ...

    # print your sentence below
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## Exercise 2: Math with Variables

    A streamer got **24, 31, 18, and 27** thousand views on their last four videos.

    1. Store the four view counts in four variables (or one list if you're feeling brave).
    2. Calculate the **total** views.
    3. Calculate the **average** views per video.
    4. Print both, like: `Total: 100 thousand | Average: 25.0 per video`

    **Hint:** Average = total divided by the number of videos.
    """
    )
    return


@app.cell
def _():
    # Exercise 2: your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## Exercise 3: Conditionals (if / elif / else)

    Write code that checks a variable called `temperature` and prints:

    - `"It's hot! 🥵"` if it's **90 or above**
    - `"Nice day 😎"` if it's between **60 and 89**
    - `"Bring a jacket 🧥"` if it's **below 60**

    Try changing `temperature` to different values and re-running the cell
    to make sure all three messages work.

    **Hint:** The order of your checks matters!
    """
    )
    return


@app.cell
def _():
    temperature = 75

    # Exercise 3: your if/elif/else here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## Exercise 4: Loops

    **Part A:** Use a `for` loop to print the numbers **1 through 10**.

    **Part B:** Now modify it so it only prints the **even** numbers.

    **Hint for Part B:** A number `n` is even if `n % 2 == 0`
    (the `%` symbol gives you the remainder after division).
    """
    )
    return


@app.cell
def _():
    # Exercise 4: your loop here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## Exercise 5: Lists

    Here's a list of songs on a playlist:

    ```python
    playlist = ["Levitating", "Blinding Lights", "Heat Waves", "As It Was"]
    ```

    1. Print the **first** song in the list.
    2. Print the **last** song (without counting by hand, Python has a trick for this).
    3. **Add** a song of your choice to the end of the list.
    4. Print how many songs are in the playlist now.
    5. Use a loop to print every song with its track number, like:
       `1. Levitating`

    **Hints:** `playlist[0]`, `playlist[-1]`, `.append()`, `len()`,
    and try `for i, song in enumerate(playlist, start=1):`
    """
    )
    return


@app.cell
def _():
    playlist = ["Levitating", "Blinding Lights", "Heat Waves", "As It Was"]

    # Exercise 5: your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## Exercise 6: Functions

    Write a function called `grade_quiz(score)` that takes a quiz score
    from 0 to 100 and **returns** a letter grade:

    | Score | Grade |
    |-------|-------|
    | 90+   | "A"   |
    | 80-89 | "B"   |
    | 70-79 | "C"   |
    | 60-69 | "D"   |
    | below 60 | "F" |

    Then test it by calling it with a few different scores:

    ```python
    print(grade_quiz(95))   # should print A
    print(grade_quiz(72))   # should print C
    print(grade_quiz(40))   # should print F
    ```
    """
    )
    return


@app.cell
def _():
    # Exercise 6: define grade_quiz here, then test it
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    # Level Up 💪

    You now have loops, lists, conditionals, and functions. That's enough
    to build actual games. Keep swapping driver and navigator, and when
    your pair finishes an exercise, compare your approach with the pair
    next to you: there's always more than one way.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 7: FizzBuzz, Camp Edition 🎯

    The most famous interview question in coding. Loop 1 to 30 and print:

    - `"Cheese"` if the number is divisible by 3
    - `"Pizza"` if divisible by 5
    - `"CheesePizza"` if divisible by BOTH 🍕
    - the number itself otherwise

    (Feel free to swap in your own word pair, the logic is what counts.)

    **Watch out:** the order you check the conditions matters. If your
    output never says the combined word, that's the classic bug! Talk it
    through with your navigator before you run it.
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
    ## Exercise 8: Find the Secret Number 🔍

    The computer has picked a secret number between 1 and 20 (see the cell below).
    Write a loop that checks every number from 1 to 20 and prints
    `"Found it! The number is X"` when it finds the secret number.

    **Going further:** Use `break` to stop the loop as soon as you find it,
    and count how many guesses it took.
    """
    )
    return


@app.cell
def _():
    import random

    secret_number = random.randint(1, 20)

    # Exercise 8: your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 9: Boss Battle Simulator ⚔️

    The boss has **100 HP**. You get 8 attacks to take it down:

    1. Run a loop for 8 attacks
    2. Each attack does random damage: `random.randint(-5, 25)`
       (negative damage means the boss healed, brutal)
    3. Subtract it from the boss HP and print something like
       `Attack 3: 12 damage, boss at 47 HP`
    4. After the loop: if HP dropped to 0 or below, print `VICTORY! 🎉`
       otherwise print `You got bodied 😩`

    Since the damage is random, every run is different. Run yours a few
    times, then compare with another pair: whose battle was closest?

    **Going further:** end the fight EARLY with `break` the moment the boss drops.
    """
    )
    return


@app.cell
def _():
    import random as random_boss

    # Exercise 9: your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Exercise 10: Password Strength Rater 🔐

    Write a function `rate_password(pw)` that returns a rating:

    - `"WEAK 😬"` if it's shorter than 8 characters
    - `"OKAY 🙂"` if it's 8+ characters
    - `"STRONG 💪"` if it's 8+ AND contains at least one digit

    Each partner writes 3 made-up test passwords (fake ones, not your
    real ones!) and predicts the rating. Then run them through the
    function: did the function agree with your predictions?

    **Hints:** `len(pw)` for length. To check for a digit:
    `any(ch.isdigit() for ch in pw)` or loop through the characters.

    **Going further:** add `"ELITE 🏆"` for 12+ characters with a digit AND
    one of `! ? #`.
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
    ## Exercise 11: The Snack Tier List 🍕

    Time to rank snacks. Start with this pool:

    ```python
    snack_pool = ["pizza", "hot cheetos", "gushers", "cookies",
                  "takis", "brownies", "goldfish", "sour patch"]
    ```

    1. Debate with your partner and agree on an S-tier: pick 3 snacks from
       the pool and `.append()` them to an empty `s_tier` list, and remove
       each one from `snack_pool` (look up `.remove()`)
    2. Print your S-tier with a loop, numbered like a ranking
    3. Print what's left in the pool as "mid tier"

    **Going further:** write a function `promote(snack)` that does the
    move-from-pool-to-S-tier in one call and prints `SNACK has been
    promoted to S-tier!`
    """
    )
    return


@app.cell
def _():
    snack_pool = ["pizza", "hot cheetos", "gushers", "cookies",
                  "takis", "brownies", "goldfish", "sour patch"]

    # Exercise 11: your code here
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## ✅ Done?

    Great work! Compare solutions with another pair, or help a pair
    that's stuck: explaining your code is the fastest way to make it
    stick. Tomorrow we start working with **real text data**.
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()

import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    # Day 1 Exercises: INSTRUCTOR SOLUTIONS 🔑

    Do not share with students until the end of the session.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Exercise 1: Variables and Printing""")
    return


@app.cell
def _():
    name = "Jordan"
    age = 16
    favorite_artist = "SZA"
    print(f"Hi, I'm {name}. I'm {age} and I always have {favorite_artist} on repeat.")
    return


@app.cell
def _(mo):
    mo.md(r"""## Exercise 2: Math with Variables""")
    return


@app.cell
def _():
    scores = [24, 31, 18, 27]
    total = sum(scores)
    average = total / len(scores)
    print(f"Total: {total} thousand | Average: {average} per video")
    return


@app.cell
def _(mo):
    mo.md(r"""## Exercise 3: Conditionals""")
    return


@app.cell
def _():
    temperature = 75

    if temperature >= 90:
        print("It's hot! 🥵")
    elif temperature >= 60:
        print("Nice day 😎")
    else:
        print("Bring a jacket 🧥")
    return


@app.cell
def _(mo):
    mo.md(r"""## Exercise 4: Loops""")
    return


@app.cell
def _():
    # Part A
    for n in range(1, 11):
        print(n)

    # Part B
    for m in range(1, 11):
        if m % 2 == 0:
            print(m)
    return


@app.cell
def _(mo):
    mo.md(r"""## Exercise 5: Lists""")
    return


@app.cell
def _():
    playlist = ["Levitating", "Blinding Lights", "Heat Waves", "As It Was"]

    print(playlist[0])       # first song
    print(playlist[-1])      # last song

    playlist.append("Espresso")
    print(len(playlist))     # 5

    for i, song in enumerate(playlist, start=1):
        print(f"{i}. {song}")
    return


@app.cell
def _(mo):
    mo.md(r"""## Exercise 6: Functions""")
    return


@app.cell
def _():
    def grade_quiz(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    print(grade_quiz(95))  # A
    print(grade_quiz(72))  # C
    print(grade_quiz(40))  # F
    return


@app.cell
def _(mo):
    mo.md(r"""## Bonus Challenge: Guess the Number""")
    return


@app.cell
def _():
    import random

    secret_number = random.randint(1, 20)

    guesses = 0
    for guess in range(1, 21):
        guesses += 1
        if guess == secret_number:
            print(f"Found it! The number is {guess} (took {guesses} guesses)")
            break
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()

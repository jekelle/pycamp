import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    # Day 5 Warm-Up: The Bug Hunt 🐛

    Before project time: 5 broken programs, each with ONE bug, using skills
    from this week.

    **How to hunt (in pairs):** for each bug, the navigator reads the code
    OUT LOUD and says what it *should* do, then you both predict the bug
    before touching the keyboard. Fix it, run it, swap roles, next bug.

    Rules: fix the bug, don't rewrite the program. Every bug here is one
    you (or your partner) probably hit this week. When your pair finishes
    all 5, go help another pair, but give hints, not answers!
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Bug 1: The Silent Greeting""")
    return


@app.cell
def _():
    # Should print a greeting... but prints nothing useful. Fix it!
    def greet(name):
        message = f"What's up, {name}!"

    greeting = greet("camper")
    print(greeting)
    return


@app.cell
def _(mo):
    mo.md(r"""## Bug 2: The Never-Ending B Student""")
    return


@app.cell
def _():
    # Every score comes back "B", even 95. Fix it!
    def grade(score):
        if score >= 80:
            return "B"
        elif score >= 90:
            return "A"
        else:
            return "C or below"

    print(grade(95))  # should be A
    print(grade(85))  # should be B
    return


@app.cell
def _(mo):
    mo.md(r"""## Bug 3: The Off-By-One Countdown""")
    return


@app.cell
def _():
    # Should count down 10, 9, 8 ... 1, LIFTOFF. Something's off. Fix it!
    for t in range(10, 1, -1):
        print(t)
    print("LIFTOFF 🚀")
    return


@app.cell
def _(mo):
    mo.md(r"""## Bug 4: The Broken Scoreboard""")
    return


@app.cell
def _():
    # Should count each word. Crashes instead. Fix it!
    words_list = "code eat code code sleep eat".split()

    counts = {}
    for w in words_list:
        counts[w] = counts[w] + 1

    print(counts)  # should be {'code': 3, 'eat': 2, 'sleep': 1}
    return


@app.cell
def _(mo):
    mo.md(r"""## Bug 5: The Stuck Markov Chain""")
    return


@app.cell
def _():
    # Should generate a wandering sentence. Prints the same word forever. Fix it!
    import random

    chain = {
        "the": ["dog", "cat"],
        "dog": ["ran", "barked"],
        "cat": ["slept", "ran"],
        "ran": ["home", "fast"],
    }

    word = "the"
    output = [word]
    for _ in range(6):
        if word not in chain:
            break
        next_word = random.choice(chain[word])
        output.append(next_word)

    print(" ".join(output))
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## Done?

    Walk another pair through ONE of your fixes (explaining a bug out loud
    is how it sticks), then get to your project. You just did what
    professional programmers do all day. 🐛✅
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()

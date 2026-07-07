import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    # Day 5: Project Day! 🚀

    **IU Indianapolis Python + Machine Learning Summer Camp**

    Today YOU are the developer. Build something using anything from this
    week, then show it off at the afternoon showcase.

    ## The Rules

    1. Work solo or in pairs.
    2. Pick a project below (or pitch your own to a TA).
    3. You have until showcase time. Done is better than perfect!
    4. Every project presents for about 2 minutes: what it does, coolest part,
       hardest part.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## 🟢 Starter Projects (pick one and make it yours)

    ### 1. Mad Libs Generator
    Ask the user for a noun, verb, adjective, etc. and drop them into a story
    template. *Uses: variables, f-strings, input widgets.*

    ### 2. Quiz Game
    A 5-question trivia quiz that keeps score and gives a final grade.
    *Uses: conditionals, loops, functions.*

    ### 3. Song Lyric Generator
    Type your own original verses as training text and let your Markov chain
    write the next hit single. *Uses: Day 3 skills.*

    ## 🟡 Level-Up Projects

    ### 4. Text Personality Analyzer
    Paste in text and report: word count, most common word, longest word,
    number of sentences, an "excitement score" (count the exclamation marks!).
    *Uses: tokenizing, regex, dictionaries.*

    ### 5. Fancy Markov: Two-Word Chains
    Upgrade Day 3's generator to use pairs of words as keys. Compare the
    output quality. *Uses: Day 3 + dictionaries with tuple keys.*

    ### 6. Word Similarity Game
    Using your word2vec model: the program picks a secret word, players guess,
    and it reports how "warm" (similar) each guess is. *Uses: Day 4 skills.*

    ## 🔴 Boss Level

    ### 7. Chatbot with Personality
    Combine regex (detect what the user asked about) with a Markov chain
    (generate a response) into a simple chatbot with sliders for
    "response length" and interactive marimo inputs.

    ### 8. Your Own Idea
    Pitch it to a TA first so we can help you scope it to one day!
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## Your Project Workspace

    Build below. Add as many cells as you need (click + between cells).

    **TA tip station:** stuck for more than 10 minutes? Flag us down.
    That's what we're here for.
    """
    )
    return


@app.cell
def _():
    # 🏗️ Project cell 1: start here!
    return


@app.cell
def _():
    # 🏗️ Project cell 2
    return


@app.cell
def _():
    # 🏗️ Project cell 3
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## 🎤 Showcase Checklist

    Before you present:

    - [ ] My program runs top to bottom without errors
    - [ ] I can demo it live in under 2 minutes
    - [ ] I can name the hardest bug I fixed
    - [ ] I know what I'd add with one more day

    ## 🎓 You Did It!

    In one week you went from "what's a variable?" to building programs
    that generate their own text. If you want to keep going:

    - **marimo:** [marimo.io](https://marimo.io), free, works in your browser
    - **Practice:** [exercism.org](https://exercism.org) Python track (free)
    - **The real stuff:** search "word2vec paper" when you're ready to see
      how deep the rabbit hole goes 🐇
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()

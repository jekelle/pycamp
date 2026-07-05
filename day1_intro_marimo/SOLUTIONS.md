# Day 1 Solutions (Instructor)

**Ex 1-4** are run-and-observe. Common issue: students hit Ctrl+Enter outside a cell. Have them click inside the gray box first.

**Ex 2:** deleting the quote gives `SyntaxError: unterminated string literal`. Point at the last line of the traceback.

**Ex 5:**
```python
my_name = "Jordan"
years_coding = 0
print(f"{my_name} has been coding for {years_coding} years... until today!")
```

**Ex 6:**
```python
emoji = "🔥"
amount = 5
print(emoji * amount)   # 🔥🔥🔥🔥🔥
```
Slider version:
```python
amount_slider = mo.ui.slider(1, 20, value=5)
amount_slider
# next cell:
print("🔥" * amount_slider.value)
```
Note: in marimo, a variable can only be defined in ONE cell. If a student gets a "multiple definitions" error, they defined the same name in two cells.

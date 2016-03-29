# Basic Exceptions and Print Debugging
You will make mistakes.
That's expected!
The computer will tell you what is wrong if you ask.

## Exceptions
**Exceptions** are errors.
They are **thrown** from a specific line of code when something is wrong.

They are so great!
They tell you the exact file, line, and what is wrong.

Look at the bottom of the error message:
```
Traceback (most recent call last):
  MORE FUNCTIONS...
  File "test.py", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects
```

* `NameError` -- No variable or function known by that name.
* `ValueError` -- A value you're using doesn't make sense in the context.
* `TypeError` -- You're using the wrong type.
* `SyntaxError` -- You're not writing Python correctly.

## Print Debugging
Because values are invisible while the program is running, it's hard to make sure your mental model matches what the computer is doing.
Print values out to double-check.

Can you spot the error?
```python
bill = 45.75
tip_pct = 20
tip = bill / tip_pct * 100
print(tip)
```
If you print out the value, it might be easier to see what you messed up.

Make sure to remove these debug prints when you're done.

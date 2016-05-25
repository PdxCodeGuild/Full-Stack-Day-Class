# Module Docstrings

Python puts documentation _inside_ the source code.
Each Python source file starts with a **module docstring**.
It should briefly describe what goes on in that file.

Docstrings are always in triple-double quotes.

```py
"""Greets a user."""
print('Your name?')
name = input()
print('Hi, ' + name + '!')
```

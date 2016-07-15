# Practice: Case Conversion

Save your solution in a Python file in `practice/` in a branch and make a GitHub pull request all named `case`.

Write a program that prompts the user for a word in `snake_case`, then converts and prints it out in `CamelCase`.
Also do the reverse conversion.

Useful hints:

* `str.replace` can be called in a loop.
* It can also be called to make the string longer: `'rubber'.replace('b', '1b')`

Write doctests for your functions.

## Advanced

* Write functions to handle `kebab-case` and `CONSTANT_CASE`.
* Write functions to auto-detect which case is input.
* Automatically print out all other cases on input.
* Come up with a original-case-agnostic intermediate representation.

# Doctests

Inline tests.
Look like an interactive session starting with >>>.

```py
def get_tens_digit(num):
    """Return the tens digit of a number.

    The number must be less than 100.

    >>> get_tens_digit(98)
    9
    """
    return num // 10
```

`python -m doctest -v PY_FILE` to run tests.

Will show which ones outputs don't match expected values in docstrings.

Write doctests for every function that's not input or main.

Try to come up with tests that use all of the lines of the function.
Realize if statements split up control flow.

Can make a PyCharm Python Test / Doctest run config and select the script you want to run.
Can run just specific test cases individually. Can debug!

Comparison is stupid, only compares printed versions.
Beware unordered containers and sort.
See [warnings section](https://docs.python.org/3.5/library/doctest.html) of doctest docs.

If you have multi-line input, use `...` on continuation lines.

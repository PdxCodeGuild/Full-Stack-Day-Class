# Function Docstrings

Each Python function body starts with a **function docstring**.
It should describe the behavior, inputs, outputs, and relevant types for that function.

For simple functions, put a one sentence description of the function.

```py
def square(x):
    """Square a number."""
    return x * x
```

For complicated functions, put a one sentence summary, then a blank line, then a longer description of the behavior.

```py
def lookup_phone(name):
    """Look up a user's phone number as a string by name.

    Only takes in a user name as a string.
    Throws a KeyError if no phone number found.
    """
    ...
```

Skim [PEP-257](https://www.python.org/dev/peps/pep-0257/) for proper docstring style.
I'm going to be anal about docstrings.
It's easy to do right and no professional code doesn't follow a style guide.

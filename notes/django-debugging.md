# Django Debugging

Debugging Django projects are just as easy as normal Python projects.

## Print

`print()` function calls still work!
They still print to the terminal.
Just make sure you hit the appropriate view that runs the code that prints.

## Tests

You can still write doctests for Django logic and model functions.
Do it!

Sometimes your logic or model functions will "not take arguments" because they're talking to the DB or some persistent data structure.
Split apart that function into two parts so you can test it;

1. Functional operation; explicit input and output
1. Stateful wrapper; get global input and delegate to functional functions

E.g. instead of:

```py
COUNTRIES = ...


def get_all_unique_countries():
    """Returns all unique countries previously added."""
    return set(COUNTRIES)
```

Do:

```py
def _uniq_countries(countries):
    """Return a set of all unique countries from a list of countries.

    >>> sorted(_uniq_countries(['USA', 'IN', 'IN']))
    ['IN', 'USA']
    """
    return set(countries)


def get_all_unique_countries():
  """Returns all unique countries previously added."""
  return _uniq_countries(COUNTRIES)
```

## Shell

Use the [Django shell](/notes/django-shell.md) to try out your app functions in a REPL and see if they behave as you expect.

## Routing

Double check that your routes are correct.
Sometimes something might be broken but only because a route was forgotten or the regexp was never hit.
Overview the [routing order](/notes/django-routes.md).

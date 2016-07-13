# List Comprehensions

If you have a list, and want to transform every element in that list by the same operation, use a **list comprehension**.
Use square brackets `[]`, then the expression you want, then `for`, then the variable name for each item in the list, then `in` then the source list.

```py
names = ['David', 'Helen', 'Anne']
lower_names = [name.lower() for name in names]
lower_names  #> ['david', 'helen', 'anne']
```

I think it's easier to always write them from back to front:

1. Pick your source list.
1. Pick the name you want to call each item.
1. Pick your item transformation.

The variable name after `for` actually _creates a new variable_ with that name, but it only exists within the brackets.

If you operation is kind of complex, write a function and call it in the list comprehension.

```py
def lookup_phone_number_by_name(name):
    """Return the phone number of a person."""
    ...


names = ['David', 'Helen', 'Anne']
phone_numbers = [lookup_phone_number_by_name(name) for name in names]
```

## If Clauses

Comprehensions also support filtering to only a _subset_ of the input data that matches an if statement.
After the source list, add an `if` then an expression that can use the item variable.

```py
years = [1995, 2000, 2004, 2011]
leap_years = [year for year in years if year % 4 == 0]
leap_years  #> [2000, 2004]
```

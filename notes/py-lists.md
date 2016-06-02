# Lists

Until now we've had values that represent _single_ facts.
A **list** is a value that is an ordered, 0-indexed, mutable, sequence of inner values.

They are written out literally using square brackets `[]` and a comma-separated list of values.

```py
['David', 'Helen', 'Mel']
[2, 4, 5]
[[1, -1], [2, -2]]
[]
```

A list with no inner values is called the **empty list**.
Any values, including other lists, can be inner values.

Any expressions can be used to construct a list literal.

```py
x = 5
[x, x, 3]  #> [5, 5, 3]
```

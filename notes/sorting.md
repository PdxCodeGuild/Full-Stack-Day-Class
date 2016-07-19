# Sorting

Often you want things in order.
Producing that order is called **sorting**.
Lists are the main data structure that preserves order, so the operations are focused around them.
`sorted()` returns a sorted list version of what you give it.

```py
sorted([3, 1, 2])  #> [1, 2, 3]
sorted([3, 1, 2], reverse=True)  #> [1, 2, 3]
```

Check out [the docs](https://docs.python.org/3/library/functions.html#sorted) for it.

If you want to find the biggest or smallest item in a list, don't sort it!
Instead [reduce](/notes/reducing.md).

## Key Sorting

Often you want to sort data on something _derived_ from the actual items.
This is called the **key**.

Let's say I want to sort a list of names by age:

```py
names_to_ages = {
  'Robyn': 38,
  'Al': 15,
  'Amanda': 90
}
names = ['Robyn', 'Amanda', 'Al']
```

If you can make a function that returns the value you want to sort by, that is a **key function**.

```py
def get_age(name):
  return names_to_ages[name]

# No ()s! Gives function as value.
sorted(names, key=get_age)  # ['Al', 'Robyn', 'Helen']
```

So this effectively does:

```py
# Input
[
  'Robyn',
  'Amanda',
  'Al'
]
# Transform to list of keys
[
  38,  # Is Robyn
  90,  # Is Amanda
  15,  # Is Al
]
# Sort list of keys
[
  15,  # Is Al
  38,  # Is Robyn
  90   # Is Amanda
]
# Transform back to initial values keeping sorted order
[
  'Al',
  'Robyn',
  'Amanda'
]
```

For dictionaries, instead of making that function, turns out you are given one already, `get`!

```py
# No () on get! Refers to function.
sorted(names, key=names_to_ages.get)  # ['Al', 'Robyn', 'Amanda']
```

You could imagine doing all sorts of fancy things, like sorting strings by length.

```py
sorted(names, key=len)  # ['Al', 'Robyn', 'Amanda']
```

Or sorting a list of two-tuples by the second element.

```py
items = [('apple', 0.99), ('candy', 0.25)]
def get_second(pair):
  return pair[2]
sorted(items, key=get_second)
```

## Nested Sorting

When sorting nested lists, the first value is what is sorted by.
Ties look to the second value to break them.
Just like sorting words and letters.

`sorted([[3, 2], [3, 1], [1, 9]])` -> `[[1, 9], [3, 1], [3, 1]]`

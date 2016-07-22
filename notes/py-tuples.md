# Tuples

Python has two ordered, 0-indexed, sequences of inner values: lists and tuples.

**Tuples** are like lists, but immutable.
Their literals are surrounded by parentheses `()`.

Single item tuples need a trailing comma to distinguish them from grouping parentheses.
Empty tuples are created using the `tuple()` cast function.

```py
('David', '503-555-9895')
(2016, 7, 13)
('Alice', )
tuple()
```

When do people use tuples vs. lists?
They're both ordered sequences!

Lists tend to be used for _homogenous_ data; each item is interpreted in exactly the same way.
Tuples tend to be used for "pairs", "triplets" or "n-tuples"; groupings of _heterogenous_ data that are interpreted _differently_.
E.g. A list of friends is a list because it doesn't matter exactly how many there are and all are names. A pair of address and phone number would be a tuple, since each is interpreted differently and if there was another item, it you wouldn't know what to do with it.

```py
friend_names = ['Kate', 'Al']
contact_info = ('123 Main St', '503-555-1234')
```

You can cast a sequence to a tuple with the `tuple()` function.

Tuples are immutable.
Trying to modify them is an exception.

```py
contact_info = ('123 Main St', '503-555-1234')
contact_info[0] = '456 Water Ave'  # Throws TypeError
```

Check out the [standard library docs for tuples](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) for an overview of all the things you can do.

Also, realize there are four different ways to use parentheses now:

1. Order of operations
1. Line continuations
1. Function calls
1. Tuple literals

```py
x = (4 + 3) * 6
x = (4 *
     3 *
     8)
min(5, 6)
('Al', 'Kate')
```

Be aware!

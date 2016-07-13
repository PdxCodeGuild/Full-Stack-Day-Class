# Sequence Functions

Python gives us lots of functions to conveniently work on sequences (e.g. lists, strings).
They're summarized on the [cheat sheet](/notes/mementopython3-english.pdf).

## Min / Max

Functions `min()` and `max()` return the smallest and largest item respectively.

```py
min([5, 1, 3])  #> 1
max(['Al', 'Zed', 'Helen'])  #> 'Zed'
max('Zebra')  #> 'Z'
```

## Length

The `len()` function returns the length of the input argument.
Realize it will not return the length of any _inner elements_.

```py
len(['apple', 'orange'])  #> 2
len('Alice')  #> 5
len([])  #> 0
```

## Range

The `range()` function returns a sequence from 0 to an end value, exclusive.
If two values are provided, the first is a start.

It returns a range object which is a sequence and not a list; I advise always casting to a list so it is easy to use.

```py
list(range(4))  #> [0, 1, 2, 3]
list(range(3, 6))  #> [3, 4, 5]
range(3, 6)  #> range(3, 6)
```

## Reversed

`reversed()` returns a reversed version of the input sequence.

It returns a reversed object which is a sequence and not a list; I advise always casting to a list so it is easy to use.

```py
list(reversed([5, 6, 1]))  #> [1, 6, 5]
list(reversed('Hi'))  #> ['i', 'H']
# Remember to cast to list for most operations
reversed([2, 5])  #> <reversed object at 0x107708ba8>
```

## Sorted

`sorted()` returns an ascending order copy of the input sequence.
It takes a `reverse` (note present tense) keyword argument to return in descending order.

```py
sorted([5, 6, 1])  #> [1, 5, 6]
sorted([5, 6, 1], reverse=True)  #> [1, 5, 6]
```

## Enumerate

`enumerate()` takes an ordered sequence and returns a version with 2-tuples of index and item.
It returns an enumerate object which is a sequence and not a list; I advise always casting to a list so it is easy to use.

```py
list(enumerate(['Helen', 'David']))  #> [(0, 'Helen'), (1, 'David')]
enumerate(['A', 'B'])  #> <enumerate object at 0x107706870>
```

## Zip

`zip()` takes a number of lists of the same length and creates tuples of interleaved items of the same index of each input list.

It returns a zip object which is a sequence and not a list; I advise always casting to a list so it is easy to use.

```py
list(zip(['A', 'B'], [9, 8]))  #> [('A', 9), ('B', 8)]
list(zip('AB', '12', '#$'))  #> [('A', '1', '#'), ('B', '2', '$')]
zip('AB', [1, 2])  #> <zip object at 0x107c2d248>
```

Zip and the **star operator** can be used together to transpose a matrix.
The star operator `*` **unpacks** a sequence into the positional arguments of the function.

```py
l = [2, 3]
pow(*l)  #> 8

board = [
    ['X', ' '],
    ['Y', ' '],
]
list(zip(*board))  #> [('X', 'Y'), (' ', ' ')]
```

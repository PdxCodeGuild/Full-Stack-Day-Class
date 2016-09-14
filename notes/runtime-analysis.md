# Runtime Analysis

**Computational complexity theory** is the academic study of "difficulty" of algorithmic problems.
There are a few different branches.

Perhaps the most practical branch is the analysis of how many steps an algorithm will take to complete, called **runtime analysis**.
There is an assumption that there are a small set of base operations that can be executed in one unit of time, usually allocation, math, assignment, lookup, equality of single values.
(This is actually not true, but a useful approximation.)
This is described as a function of **input length**, usually called _n_.

Let's say we want to increment a lot of numbers by one.

```py
nums = [1, 2, 5, 1, 22, 99]

nums_plus = [x + 1 for x in nums]
```

That list comprehension has to allocate an output list, then read, sum, and write once for each input number.
That means it takes _1 + 3n_ time to run.

**Big O** notation is a common way to write this out.
It ignores constants and specifies the _worst case_ runtime.
So the above would be written as _O(n)_.

What about finding if an value exists in a list?

```py
nums = [1, 2, 5, 1, 22, 99]
1 in nums  #> True
```

Well, turns out this is actually implemented more like:

```py
def in_list(y, l):
    for x in l:
        if x == y:
            return True
    return False
```

So this means you have to look through each element once, so _O(n)_.

Can we do better?
What if we pre-sorted the list?
(Let's ignore for now how hard that is.)
Then we can **binary search**!

The idea is that you keep halving the area you're looking in until the value is there or it isn't in a single item.
Check out [this visualization](https://www.cs.usfca.edu/~galles/visualization/Search.html).

```py
def in_sorted_list(y, l):
    low_index = 0
    high_index = len(l) - 1
    while low_index <= high_index:
        middle_of_low_high_index = (low_index + high_index) // 2
        if l[middle_of_low_high_index] > y:
            high_index = middle_of_low_high_index - 1
        elif l[middle_of_low_high_index] < y:
            low_index = middle_of_low_high_index + 1
        else:
            return True
    return False
```

So this, at worst, has to look the number of times you can halve the length of the list until you get zero.
That is _O(log(n, 2))_.

Can we do even better?
Sort of, but we can't use a list.

If we use a set, we can.

```py
nums = {1, 2, 5, 22, 99}
1 in nums  #> True
```

Sets have different underlying structure; they are **hash tables**.
A hash table is a list that is "indexed" by the value being put into it.
It has to be (much) bigger than the number of items in it.
The index in the list is determined by running a **hash function** on the value.

```py
def hash_str(s):
    """Shitty hash function."""
    return sum(ord(c) for c in s)


def add_str_to_set(s, l):
    index = hash_str(s) % len(l)
    l[index] = s


def is_str_in_set(s, l):
    index = hash_str(s) % len(l)
    return l[index] == s
```

Check out [this visualization](http://cs.usfca.edu/~galles/visualization/OpenHash.html).
Since running the hash function is the same no matter how many items are in the set, adding and searching is _O(1)_ (mostly, there are a lot of caveats due to collisions).

That's cool.
Different algorithms for doing the same thing can take different amounts of time!
For small numbers of _n_ this stuff doesn't matter.
But when _n_ does get big, [differences are huge](https://en.wikipedia.org/wiki/Analysis_of_algorithms#/media/File:Comparison_computational_complexity.svg)!

This same kind of Big O analysis can be used for memory consumption.

You can read up on lots of different data structures that have different tradeoffs and performance characteristics: dequeue, linked lists, binary search trees, bloom filters, etc.

**Don't worry about this stuff until you know you have to worry about this stuff.**

> Premature optimization is the root of all evil.

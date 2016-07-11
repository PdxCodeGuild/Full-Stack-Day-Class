# Practice: Last Join

Python gives you a string function `str.join(seq)`.

```py
'-'.join(['one', 'two', 'three'])  #> 'one-two-three'
```

This is useful, but often we want to write out nice English lists.

Write a program that asks the user for a list of space separated words.
It then joins them by `, `, ` and `, and `, and ` depending if there are two or more than two words in the list.
Count the number of original words and print out the new joined version like the examples below.

> Words? one two three four
>
> 4 words: one, two, three, and four
>
> Words? one two three
>
> 3 words: one, two, and three
>
> Words? one two
>
> 2 words: one and two
>
> Words? one
>
> 1 words: one

## Advanced

Ask the user for the "joiner", "pair joiner", and "last joiner" and use those.

## Super Advanced

* Put this behavior in a function named `last_join(seq, joiner, pair_joiner, last_joiner)` that returns the joined string.
* Use [doctests](https://docs.python.org/3/library/doctest.html) to test it's behavior.

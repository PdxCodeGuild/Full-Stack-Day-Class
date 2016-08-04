# Practice: Sum Pairs

Write a function named `find_sum_pairs`.
It takes two arguments:

1. A list of ints to search
1. A sum to find

Go through the search list and find all pairs of numbers that would add together to the sum.

Example output:

```py
>>> find_sum_pairs([-1, 0, 1, 2], 3)
[[1, 2]]
>>> find_sum_pairs([-1, 0, 1, 2], 1)
[[-1, 2], [0, 1]]
>>> find_sum_pairs([2, -1, 2], 1)
[[2, -1], [-1, 2]]
>>> find_sum_pairs([-1, 1, 2, 2], 3)
[[1, 2], [1, 2]]
```

Write doctests for this function.

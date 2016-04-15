# Practice: Sum Pairs
Write a function named `find_sum_pairs`.
It takes two arguments:
a list of ints to search, and a sum to find.

Go through the search list and find all pairs of numbers that would add together to the sum.

Example output:
```python
>>> find_sum_pairs([-1, 0, 1, 2], 3)
[[1, 2]]
>>> find_sum_pairs([-1, 1, 2, 2], 3)
[[1, 2], [1, 2]]
>>> find_sum_pairs([-1, 0, 1, 2], 1)
[[-1, 2], [0, 1]]
>>> find_sum_pairs([2, -1, 2], 1)
[[2, -1], [-1, 2]]
```

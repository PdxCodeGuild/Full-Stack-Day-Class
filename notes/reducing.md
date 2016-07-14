# Reducing

**Reducing** is walking through a collection and updating a _summary value_ with each item.

E.g. Summing a list of ages.
Finding the average height of a list.
Returning if any of a list of items is a kind of orange.

The most common cases are best done with _special purpose functions_, but the general case of using a _for loop_ and _aggregating values_ works.

* `sum()`
* `any()`
* `all()`
* `statistics` module

```py
ages = [6, 19, 3, 45]
ages_sum = sum(ages)

heights = [50.6, 30.2, 55.1]

import statistics
mean_height = statistics.mean(heights)

grocery_list = ['apple', 'blood orange']
contains_kind_of_orange = any(['orange' in item for item in grocery_list])
```

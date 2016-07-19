# Reducing

**Reducing** is walking through a collection creating a _single summary value_ from all of the items.
It's like "boiling down" a list of data.

E.g. Summing a list of ages.
Finding the average height of a list.
Finding the minimum price drink.
Returning if any of a list of items is a kind of orange.

The most common cases are best done with _special purpose functions_.

* [sum()](https://docs.python.org/3/library/functions.html#sum) / [str.join()](https://docs.python.org/3/library/stdtypes.html#str.join) / [itertools.chain()](https://docs.python.org/3/library/itertools.html#itertools.chain)
* [min()](https://docs.python.org/3/library/functions.html#min) / [max()](https://docs.python.org/3/library/functions.html#max) take a `key` keyword argument like [sorted()](/notes/sorting.md)
* [any()](https://docs.python.org/3/library/functions.html#any) / [all()](https://docs.python.org/3/library/functions.html#all)
* [statistics](https://docs.python.org/3/library/statistics.html) module

```py
ages = [6, 19, 3, 45]
ages_sum = sum(ages)

digits = ['1', '2', '3']
''.join(digits)  #> '123'

from itertools import chain
friend_names = ['David', 'Helen']
enemy_names = ['Fido', 'Otis']
all_names = list(chain(friend_names, enemy_names))
chain(*list_of_lists)
all_names  #> ['David', 'Helen', 'Fido', 'Otis']

import statistics
heights = [50.6, 30.2, 55.1]
mean_height = statistics.mean(heights)

soda_to_price = {'Coke': 0.99, 'Pepsi': 0.89, 'Tab': 0.79}
cheapest_soda = min(soda_to_price.keys(), key=soda_to_price.get)

grocery_list = ['apple', 'blood orange']
contains_kind_of_orange = any(['orange' in item for item in grocery_list])
```

The general case of using a _for loop_ and **aggregating value** works.
The aggregating is a working "total" that you update with new information from each item.

1. Determine what your input list or sequence is.
1. Come up with a good name to call each individual item.
1. Decide the initial aggregating value.
1. Write a function or expression that combines the current working aggregating value with each item.

```py
# 3. Initial Aggregating Value
total = 0
# 1. Input Items
# 2. Name Each Item
for cost in costs:
    # 4. Update Aggregating Value
    total += cost
```

Turns out this is such a common pattern, there is a [reduce()](https://docs.python.org/3/library/functools.html#functools.reduce) that facilitates this.

```py
from functools import reduce

def update_total(total, cost):
    """Updates a running total with a new cost by summing.

    >>> update_total(5, 6)
    11
    """
    return total + cost

total = reduce(update_total, costs, 0)
```

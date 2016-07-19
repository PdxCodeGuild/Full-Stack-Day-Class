# Filtering

**Filtering** is taking a collection and getting a subset of the items that _match some criteria_.

E.g. Taking a list of names and returning a list of just the names with the letter `i` in them.
Take a list of years and return just the ones that are leap years.

This is best done with _if-clause comprehensions_.

I find it easiest to work through the comprehensions _backwards_:

1. Determine what your input list or sequence is.
1. Come up with a good name to call each individual item.
1. Write a function or expression that decides if you want to _keep_ an item and returns a boolean.
1. Call it in the comprehension after an `if`.

You can combine [mapping](/notes/mapping.md) and filtering by having both an if-clause and a function call at the beginning of the comprehension.

```py
names = ['David', 'Mel', 'Erin']

# 3. Decide to Keep Item
def contains_i(s):
    """Return if a string contains the letter 'i'.

    >>> contains_i('hi')
    True
    >>> contains_i('bye')
    False
    """
    return 'i' in s

i_containing_names = [
    name
    # 2. Name Each Item
    for name
    # 1. Input Items
    in names
    # 4. Call Keeping Function
    if contains_i(name)
]

product_to_prices = {'apple': 1.50, 'gold bar': 800.0}
expensive_product_to_prices = {
    product: price
    for product, price
    in product_to_prices.items()
    if price > 150.0
}
```

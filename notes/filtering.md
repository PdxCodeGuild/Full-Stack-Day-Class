# Filtering

**Filtering** is taking a collection and getting a subset of the items that _match some criteria_.

E.g. Taking a list of names and returning a list of just the names with the letter `i` in them.
Take a list of years and return just the ones that are leap years.

This is best done with _if clause comprehensions_.

```py
names = ['David', 'Mel', 'Erin']
i_containing_names = [name for name in names if 'i' in name]

product_to_prices = {'apple': 1.50, 'gold bar': 800.0}
expensive_product_to_prices = {
    product: price
    for product, price
    in product_to_prices.items()
    if price > 150.0
}
```

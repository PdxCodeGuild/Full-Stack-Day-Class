# Mapping

**Mapping** is taking a collection and doing _a single same thing to each item_.

E.g. Turning a list of `YYYY-MM-DD` dates into a list of `YYYY` years.
Turn a mapping of ages into birth years.

This is best done with _comprehensions_.

I find it easiest to work through the comprehensions _backwards_:

1. Determine what your input list or sequence is.
1. Come up with a good name to call each individual item.
1. Write a function or come up with an expression that converts just one item.
1. Call it in the comprehension.

```py
dates = ['2016-02-04', '1987-05-09']

# 3. Convert Item
def extract_year(date):
    """Convert a whole date in YYYY-MM-DD format to just YYYY.

    >>> extract_year('2016-02-04')
    '2016'
    """
    return date.split('-')[0]

years = [
    # 4. Call Converter for Item
    extract_year(date)
    # 2. Name Each Item
    for date
    # 1. Input Items
    in dates
]

name_to_age = {'Mel': 45, 'Robert': 39}
current_year = 2016
name_to_birth_year = {
    name: current_year - age
    for name, age
    in name_to_age.items()
}
```

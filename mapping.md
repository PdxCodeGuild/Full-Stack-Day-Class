## Mapping
**Mapping** is taking a collection and doing _a single thing to each item_.

E.g. Turning a list of `YYYY-MM-DD` dates into a list of `YYYY` years.
Turn a mapping of ages into birth years.

This is best done with _comprehensions_.
```python
dates = ['2016-02-04', '1987-05-09']
years = [date.split('-')[0] for date in dates]

name_to_age = {'Mel': 45, 'Robert': 39}
current_year = 2016
name_to_birth_year = {
    name: current_year - age
    for name, age
    in name_to_age.items()
}
```

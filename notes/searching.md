# Searching

Min / max. Supply Key.

```py
heaviest_pumpkin = max(pumpkin_weights)
min_age = min(names, key=names_to_ages.get)
```

Make function that for loops and return on found.

```py
def find_david(names):
    for name in names:
        if name == 'David':
            return name
```

Consider dict if always single answer.

```py
names_and_ages = [('Al', 15), ('Alice', 90)]
def find_age(search_name, names_and_ages):
    for name, age in names_and_ages:
        if name == search_name:
            return age

name_to_age = dict(names_and_ages)
names_to_ages[search_name]
```

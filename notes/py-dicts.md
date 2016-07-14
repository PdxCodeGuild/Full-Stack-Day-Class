# Dicts

**Dictionaries** provide an _unordered_, mutable, sequence mapping between unique **keys** to arbitrary **values**.

```py
{'David': 100}
{}
```

Any immutable object can be a key.

Use same getter operators, but with keys.

```py
names_to_ages['David']
names_to_ages[192]  #> Throws KeyError
```

.keys(), .values(), .items().
Always use one of these, avoid iterating throug bare dictionary because you'll forget it's just keys. You probably want items.

Use sorted if you want consisten ordering.

items() and dict() are inverses.

There are dict comprehensions.

```py
{name: age / 2 for name, age in names_to_ages.items()}
```

# Dicts

**Dictionaries** provide an _unordered_, mutable, sequence mapping between unique **keys** to arbitrary **values**.

They are written out literally using curled braces `{}` and a comma-separated list of inner key, then colon `:`, then values.

```py
{'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
{'David': ['day'], 'Sheri': ['day', 'night']}
{}
```

Any _immutable_ value can be a key, thus lists and other dicts can't be keys.
Any value can be a value.

The bread and butter of a dictionary is looking up the value for a specific key.
Use the same square bracket `[]` operator like accessing a specific index in a list.
You can not look up keys by value.

```py
product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
product_to_price['apple']  #> 1.0
product_to_price['grapes']  #> 0.75
product_to_price['banana']  # Throws KeyError
product_to_price[1.0]  # Throws KeyError
```

Values can be added or updated by using the set operator, similar to assigning to a specific list element index.

```py
product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
product_to_price['apple'] = 2.0
product_to_price  #> {'apple': 2.0, 'pear': 1.5, 'grapes': 0.75}
product_to_price['banana'] = 0.25
product_to_price  #> {'apple': 1.0, 'pear': 1.5, 'banana': 0.25, 'grapes': 0.75}
```

To combine two dictionaries, use the `.update()` type method.
Note that it mutates in place.

```py
product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
product_to_price.update({'banana': 0.25})
product_to_price  #> {'apple': 1.0, 'pear': 1.5, 'banana': 0.25, 'grapes': 0.75}
```

There are a few type methods that allow you to view different parts of the dictionary.
All produce sequences and not proper lists, so cast them to a list to use them normally.
**Dictionaries are unordered; there is no guarantee the same order will come out at each call!**

```py
list(product_to_price.keys())  #> ['pear', 'apple', 'grapes']
list(product_to_price.values())  #> [0.75, 1.0, 1.5]
list(product_to_price.items())  #> [('grapes', 0.75), ('apple', 1.0), ('pear', 1.5)]
```

Call `sorted()` on the results if you need a stable order.

```py
sorted(product_to_price.keys())  #> ['apple', 'grapes', 'pear']
```

A bare dictionary is also a sequence _of just it's keys_.
Avoid using it like this, though, as it's easy to forget.

```py
sorted(product_to_price)  #> ['apple', 'grapes', 'pear']
[x for x in product_to_price]  #> ['pear', 'apple', 'grapes']
for x in product_to_price:
    print(x)
```

Instead explicitly call `.keys()` to remind the reader what you want.

```py
sorted(product_to_price.keys())  #> ['apple', 'grapes', 'pear']
[x for x in product_to_price.keys()]  #> ['pear', 'apple', 'grapes']
for x in product_to_price.keys():
    print(x)
```

You can cast a sequences of two-tuples to a dictionary using `dict()`.
This means `.items()` and `dict()` are inverses.

```py
names_and_fav_colors = [('Alice', 'red'), ('David', 'green')]
dict(names_and_fav_colors)  #> {'Alice': 'red', 'David': 'green'}
dict(product_to_price.items()) == product_to_price  #> True
```

Check out the [standard library docs for dicts](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) for an overview of all the things you can do.

## Dict Comprehensions

Dict comprehensions look like list comprehensions, but with curly braces and colons.
Remember, you probably want to modify both keys and values, so you need to iterate over `.items()`.

```py
names_to_ages = {'Amanda': 90, 'David': 50}
{name: age / 2 for name, age in names_to_ages.items()}  #> {'Amanda': 45, 'David': 25}
```

# Structured Data

Thus far most of our data structures have contained _homogenous data_.
Each item is meant to be interpreted in the same way.

```py
names = ['David', 'Helen', 'Meg']
city_to_mayor = {'Portland': 'Charlie Hales', 'New York': 'Bill de Blasio'}
```

We've seen a little bit of **heterogenous data** with the standard use of tuples.
Each entry is meant to be interpreted differently.

```py
enum_item = (4, 'David')
contact_info = ('503-555-9895', '123 Main St.')
```

For tuples, this requires you to remember what the zeroth index is, the first index, etc.
No fun.
That requires a lot of coordination and implicit communication between parts of the code.

Another common way of structuring heterogenous data is using dictionaries, with the key being the field name.

```py
contact_info = {
    'phone': '503-555-9895',
    'address': '123 Main St.',
}
contact_info['phone'] ...
```

This is slightly better, but there's nothing enforcing that all of the keys exist in every instance and are spelled correctly.
That sucks, but you'll see lots of existing code like this.
Avoid this.

```py
my_contact_info = {
    'phone': '503-555-9895',
    'address': '123 Main St.',
}
helen_contact_info = {
    # Missing 'phone' key. Is that okay? Bug? Allowed?
    'addy': '123 Main St.',  # Alternative key? Bug?
}
```

A much better way is a [named tuple](/notes/py-tuples-named.md) (or a [class](/notes/py-classes-basic.md), but we'll deal with that later).

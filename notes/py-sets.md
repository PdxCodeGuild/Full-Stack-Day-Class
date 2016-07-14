# Sets

**Sets** are an _unordered_, mutable, unique, sequence of inner values.
They are like the sets you might have thought about in math class.

They are written out literally using curled braces `{}` and a comma-separated list of inner values.
Except for the empty set, it is `set()` as to not conflict with the empty dict.

```py
{2, 4, 6, 8}
set()
```

Any _immutable_ value can be inside, thus lists and other dicts can't be inner values.

If there are duplicate values, they are collapsed into a single one.

```py
{2, 2, 2}  #> {2}
```

You can cast a sequence to a set using the `set()` function.

```py
set([1, 2, 2, 4, 4])  #> {1, 2, 4}
```

## Operators

All of the "mathy" set operators Python gives you.

* In `in`
* Union `|`
* Intersection `&`
* Difference `-`

```py
2 in {1, 2, 4}  #> True
{1, 2, 3} | {3, 4}  #> {1, 2, 3, 4}
{1, 2, 3} & {3, 4}  #> {3}
{1, 2, 3} - {3, 4}  #> {1, 2}
```

Check out the [standard library docs for sets](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset) for an overview of all the things you can do.

## Comprehensions

Set comprehensions look like list comprehensions, but with curly braces.

```py
even_nums = {x * 2 for x in range(4)}
even_nums  #> {0, 2, 4}
```

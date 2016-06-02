# Boolean Operators

There are some operators that only work on booleans.

* `not x` returns the "opposite value"
* `a and b` returns `True` only if _both_ are `True`
* `a or b` returns `True` if _either or both_ are `True`

```py
not True  #> False
True and True  #> True
False and True  #> True
```

They are often chained together.
Use parentheses `()` so that only one operation happens at a time.
Without parentheses, you might not get the same behavior!

```py
a = True
b = False
c = True
(a and b) or c  #> False
a and (b or c)  #> True
```

These operators do not modify the behavior of other operators!
If you want to check for multiple kinds of equality, you need multiple equals operators.

```py
if x == 3 or 4:  # Will not work as expected!
    ...
if x == 3 or x == 4:  # This is correct.
    ...
```

Remember, all operators are just expressions and can be used anywhere a value is needed.

```py
if a or b:
    print('Hi')
x = b and c
print(not a)
```

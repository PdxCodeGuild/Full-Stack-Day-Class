# For Loops

A **for loop** gives you a _generic_ way to perform a block of code once for _each item_ in a list.
That code can do anything!
It doesn't have to make a new list.

```py
receipt = [3.00, 2.50, 10.75]
total = 0
for cost in receipt:
    total += cost
```

Think carefully before using them, though.
90% of the things you want to do with a for loop, you already have functions to do.
The above would be better written using `sum()`, though.

```py
receipt = [3.00, 2.50, 10.75]
total = sum(receipt)
```

# Evaluation Order
Python evaluates files from top to bottom, one line at a time, then each line from left to right.

To communicate values between lines, you _have to_ save them in variables and reference them later.

Whenever Python is expecting a value, it reads from left to right until it finds a complete one, evaluating things deeper along the way if necessary.

```python
x = max(4 * 2, abs(-4 * 3)
#       ----- First evaluates
#                  ----- Second evaluates
#              ----------- Third evaluates
#   ----------------- Fourth evaluates
y = x / (2 + x)
#            - First evaluates
#        ----- Second evaluates
#   ----------- Third evaluates
```

Remember, **all things that evaluate to values are equivalent**.
You can use
* a literal to specify a value
* a variable to refer to the value within
* an operator to use the return value
* a function call to use the return value

# Advanced Function Calling
## Passing by Position
Thus far, we've been passing arguments functions **by position**.
The values at the call site are bound to the variables in the function signature _in order_.

```python
def subtract(a, b):
  return a - b

subtract(5, 8)  #> -3
# a = 5; b = 8
```

Most positional arguments are like above, **required arguments**.
It's also possible to have functions that take **optional arguments**.
If they are specified at the function call, then the caller's value is used.
Otherwise, the default value from the function definition is used.

```python
def subtract(a, b=1):
  return a - b

subtract(5)  #> 4
# a = 5; b = 1
subtract(5, 8)  #> -3
# a = 5; b = 8
```

## Passing by Keyword
_Only optional_ arguments may also be passed **by keyword** in _any_ order.

```python
def subtract(a, b=1, c=0):
  return a - b - c

subtract(5, b=8)  #> -3
# a = 5; b = 8; c = 1
subtract(5, c=9)  #> -5
# a = 5; b = 1; c = 9
subtract(5, c=9, b=8)  #> -12
# a = 5; b = 8; c = 9
```

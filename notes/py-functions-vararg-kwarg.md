# Vararg and Kwarg Functions

Python functions can take variable number of arguments.

An argument in the function definition which is prefixed by a star `*` will contain a list of all unknown positional arguments.
There can only be a single star prefixed argument.

```py
def f_args(a, b, *args):
    ...

f_args(1, 2, 3)  # a = 1, b = 2, args = [3]
f_args(1, 2)  # a = 1, b = 2, args = []
f_args(1, 2, 3, 4)  # a = 1, b = 2, args = [3, 4]
f_args(1)  # Throws TypeError
```

An argument in the function definition prefixed by a double star `**` will contain a dictionary of all unknown keyword arguments.

```py
def f_kwargs(a, b, **kwargs):
    ...

f_kwargs(1, 2, x=3)  # a = 1, b = 2, kwargs = {'x': 3}
f_kwargs(1, 2)  # a = 1, b = 2, kwargs = {}
f_kwargs(1, 2, x=3, y=4)  # a = 1, b = 2, kwargs = {'x': 3, 'y': 4}
# Remember, positional arguments _can_ be passed by keyword.
f_kwargs(b=1, a=2, x=3, y=4)  # a = 2, b = 1, kwargs = {'x': 3, 'y': 4}
```

When calling a function, all positional arguments must come before all keyword arguments at the call site.
Otherwise the meaning is ambiguous.

Stars `*` and double stars `**` can also be used to **unpack** arguments upon function calling.

```py
x = [1, 2, 3]
f_args(*x)  # a = 1, b = 2, args = [3]
x = [1, 2, 3]
f_args(4, *x)  # a = 4, b = 1, args = [2, 3]
# Equivalent to f_args(4, 1, 2, 3)
d = {'a': 1, 'b': 2, 'x': 3}
f_kwargs(**d)  # a = 1, b = 2, kwargs = {'x': 3}
d = {'b': 2, 'x': 3}
f_kwargs(4, **d)  # a = 4, b = 2, kwargs = {'x': 3}
# Equivalen to f_kwargs(4, b=2, x=3)
```

A common pattern is making a **pass-through function**.
It allows a function to take any signature and pass that on to another function.

```py
def time_g(*args, **kwargs):
    start = now()
    g(*args, **kwargs)
    end = now()
    print(end - start)
```

The inner call to `g` will fail with `TypeError` if `g` doesn't take that signature.

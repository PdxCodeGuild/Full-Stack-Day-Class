# Function Signatures

A function **signature** is a written description of a way of calling a function.
It's a short description of all of the different number and order of arguments the function could take; any one is valid, although sometimes they have slightly different meanings.

```
name()
name(required, required)
```

Optional arguments are in square brackets `[]`, they can be nested.

```
name(required[, optional1[, optional2]])
```

Arguments with defaults have an equals after the name `=` are passed in by keyword and can have default values overridden.

```
name(required[, optional], default=10)
```

Arguments preceded by a splat `*` mean that they can take _any number_ of positional arguments in the slot.

```
name(*many_optional)
```

E.g. The `max` built-in function has [a signature](https://docs.python.org/3/library/functions.html#max) that will return the max of any number of arguments.

Sometimes optional and default arguments must either be passed only by position or only by keyword.
Unfortunately the function signature doesn't distinguish between that, but you'll get a `TypeError` that says that.

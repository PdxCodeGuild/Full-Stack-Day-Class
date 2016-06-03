# Function Signatures

A function **signature** is a written description of a way of calling a function.
It's a short description of all of the different number and order of arguments the function could take.

Optional arguments are in square brackets `[]`, they can be nested.
Arguments with defaults have an equals after the name `=` and can be overridden.
Sometimes there are multiple signatures for the same function name; any one is valid, although sometimes they have slightly different meanings.

```
name(required[, optional], default=10)
name(required, required)
name(required[, optional1[, optional2]])
name()
```

Sometimes optional and default arguments must either be passed only by position or only by keyword.
Unfortunately the function signature doesn't distinguish between that, but you'll get a `TypeError` that says that.

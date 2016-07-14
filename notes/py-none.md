# None

Python has a special single value called **none**.
It is a value that represents the _absence of a value_.
It's literal is uppercase none.

```py
None
```

**Avoid using none.**
Basically any time you think about None, you could probably be using a better "empty value".

* Empty list
* Empty string
* False

## Existing Code

You'll see it used in a few different situations:

Functions that don't explicitly return a value implicitly return none.

```py
def print_hi():
    print('hi')

x = print_hi()
x  #> None
```

Default function arguments are sometimes set to none to indicate they're unused.

```py
def print_hi(name=None):
    if name is None:
        print('hi')
    else:
        print('hi, ' + name)
```

But in that case, I'd suggest the default being empty string `''`.

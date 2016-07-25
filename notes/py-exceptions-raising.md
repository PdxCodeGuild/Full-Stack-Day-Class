# Raising Exceptions

You can have your own functions **raise** exceptions.
Be very sparing in using this power.
It's a way to signal that something un-recoverable has gone wrong.
Use the `raise` keyword, then instantiate a new exception by its name and a message describing what went wrong.

```py
def parse_phone(phone_str):
    """Parse a phone number separated by dashes into its component parts.

    >>> parse_phone('503-555-1234')
    ['503', '555', '1234']
    >>> parse_phone('Hi')
    Traceback (most recent call last):
        ...
    ValueError: phone number is not in proper format
    """
    if '-' not in phone_str:
        raise ValueError('phone number is not in proper format')
    return '-'.split(phone_str)
```

**Only raise an exception if there is no reasonable return value.**
Remember, [None](/notes/py-none.md) is usually not a reasonable return value.
Try to pick an [already-existing exception type](https://docs.python.org/3/library/exceptions.html#concrete-exceptions) that matches the meaning of the error.

Also, if you're mutating values, throw all exceptions up front.
The implicit agreement of a function is that it either completes fully and returns a value, or throws an exception and does nothing.
If you throw an exception part of the way through your process, you might have half-baked values.

If you use immutable types, this isn't a worry.

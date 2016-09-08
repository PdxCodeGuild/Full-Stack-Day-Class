# Raising Exceptions

You can have your own functions **raise** exceptions.
Be very sparing in using this power.
It's a way to signal that something un-recoverable has gone wrong.
Use the `raise` keyword, then instantiate a new exception by its name and a message describing what went wrong.

```py
def parse_area_code(phone_str):
    """Parse a phone number separated by dashes into its area code.

    >>> parse_area_code('503-555-1234')
    '503'
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

Whenever you raise an exception, you make all of the function call sites more complicated.
So only do this if necessary.

Try to pick an [already-existing exception type](https://docs.python.org/3/library/exceptions.html#concrete-exceptions) that matches the meaning of the error.
Avoid "casting" exceptions to a different type unless the originating exception is misleading.
Whenever you raise a new exception, you lose the traceback of the original one, which can make it harder to understand problems.

```py
try:
    name = contact_info['name']
    phone = contact_info['phone']
# Which line above went wrong? That information is lost.
except KeyError:
    raise ValueError('invalid contact info')
```

Also, if you're mutating values, throw all exceptions up front.
The implicit agreement of a function is that it either completes fully and returns a value, or throws an exception and does nothing.
If you throw an exception part of the way through your process, you might have half-baked values.

If you use immutable types, this isn't a worry.

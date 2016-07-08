# Booleans

A **boolean** is a data type that represents "yes" / "true" or "no" / "false".
Those are the _only_ two values is has.

Their literals are capitalized and have no quotes.

```py
True
False
```

## Avoid Fake Booleans

Why don't we just use ints `1` and `0` or strings `'Yes'` and `'No'` to store this information?
They have _too much flexibility_.

There are so many strings or ints that could mean "true", and your code won't let you know when you make a mistake.

```py
# This code won't work because the author wasn't consistent about string values.
keep_running = 'True'
while keep_running == 'Yes':
    do_something()
```

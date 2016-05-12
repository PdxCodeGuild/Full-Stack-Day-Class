# Exceptions
Exceptions are signals that something went wrong in the code that's currently running.

## Catching
You can **catch** exceptions using a try-except block.
The code in the except block is only run if an exception is thrown.
Any code below where the exception is thrown is skipped over.
```py
try:
    x = int('hi')
    # This is skipped.
    x = 5
except ValueError:
    print("error happend!")
    x = 0
x  #> 0
```

Program flow continues after the except block in every case.

### Code Structure
Often you can prevent an exception from being thrown in the first place.
This technique is called **LBYL** or **Look Before You Leap**.
```py
word_to_count = {}
for word in words:
    if word not in counts:
        word_to_count[word] = 0
    word_to_count[word] += 1
```

You can also structure code that just handles the exception.
This technique is called **EAFP** or **Easier to Ask for Forgiveness than Permission**.
```py
word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
```

I find EAFP code harder to understand, in general.
I would err on the side of finding a LBYL version.

## Raising
You can also **raise** your own exceptions.
Be very sparing in using this power.
It's a way to signal that something un-recoverable has gone wrong.

You can make a new exception by calling its name and giving it an error message.

```py
def convert_css_color_to_hex(css_color_string):
    if not css_color_string.startswith('rgb('):
        raise ValueError("can't convert malformed CSS color: {!r}".format(css_color_string))
    ...
```

_Only_ raise an exception if there isn't a reasonable return value.

Try to pick an [already-existing exception type](https://docs.python.org/3/library/exceptions.html#concrete-exceptions) that matches the meaning of the error.

# Using Python 2

Much of the code you find when googling for Python problems is written in Python 2.
There were some breaking changes.
Here is an overview of them.
See the [Python docs](https://docs.python.org/release/3.1.2/whatsnew/3.0.html#common-stumbling-blocks) for a more complete list.

If you see things like `print hi` or `raw_input()` or `iteritems()` or `xrange()`, you'll have to follow these changes.

## Changes

### Print is a Function

Python 2

```py
print 'Hi', name
```

Python 3

```py
print('Hi', name)
```

### Input was Renamed

Python 2

```py
name = raw_input()
```

Python 3

```py
name = input()
```

### Dict Iterating Functions Renamed

Python 2

```py
d.iteritems()
d.iterkeys()
d.itervalues()
```

Python 3

```py
d.items()
d.keys()
d.values()
```

### XRange

Python 2

```py
xrange(4)
```

Python 3

```py
range(4)
```

### Integer Division Truncation

Python 2

```py
3 / 1  #> 0
```

Python 3

```py
3 / 1  #> 0.333
```

## Running Bigger Python 2 Programs

If you come across a complete Python 2 program you want to run, you have a few options.

If you just care about running the program and not modifying it, just run it using `python2`.
All of you probably already have a Python 2 interpreter installed.

If you care about modifying the program, you could run the _source code_ through [a tool](https://docs.python.org/3/library/2to3.html) called `2to3` which does the above transformations for you.

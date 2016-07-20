# Modules

You can write your own modules to structure your own code.
Conveniently, every Python file is already a module!

If your project looks like

```
project/
    main.py
    logic.py
```

If `logic.py` is

```py
def think_hard():
    return 42

class Bandit:
    def __init__(self):
        self.name = 'David'
```

Then in `main.py` you can import any Python files in the same directory with the other file name _without the `.py`_.

```py
import logic

answer = logic.think_hard()
robber = logic.Bandit()

print(answer)
print(robber.name)
```

Only files in _the same directory_ as the importing file can be imported.

Be careful about **circular dependencies**.
If `a.py` imports `b.py` which imports `a.py` will throw `NameError`s.

Python style requires that files that are going to be imported as modules to be in `snake_case`.
It's actually a little bit more than style, you _can't_ import files with any symbols other than underscore.

## Nested Modules

You can also introduce more structure by using directories as modules.

If your project looks like

```
project/
    main.py
    logic/
        __init__.py
        thinking.py
        bandits.py
```

Where `__init__.py` is a blank file that marks the directory as a module.

Then from `main.py` you can then import those inner Python files

```py
import logic.thinking
answer = logic.thinking.think_hard()
```

You _can not do_

```py
import logic
answer = logic.thinking.think_hard()
```

Only individual _files_ can be imported.

## Importing is Executing

When you import a module, Python has to run that file to create all of the values.
That means if you have a main function call at the bottom, it will run it _on import_!

If you have an `a.py` that looks like

```py
print("I'm in A")
```

And a `b.py` that looks like

```py
import a

print("I'm in B")
```

Then running `b.py` will print out

> I'm in A
>
> I'm in B

This is why we have been using a [gated main](/notes/py-functions-main.md#gatedmain).

```py
if __name__ == '__main__':
    main()
```

That code will _not execute upon import_ but will run if you call the Python file directly.
This is important during testing.

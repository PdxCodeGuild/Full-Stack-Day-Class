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
```python
def think_hard():
    return 42

class Bandit:
    def __init__(self):
        self.name = 'David'
```

Then in `main.py` you can import any _top level_ item using the name of the Python file _without the `.py`_.
```python
import logic

answer = logic.think_hard()
robber = logic.Bandit()

print(answer)
print(robber.name)
```

Only files in _the same directory_ as the importing file can be imported.

Be careful about **circular dependencies**.
If `a.py` imports `b.py` which imports `a.py` will throw `NameError`s.

## Sub Modules
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
```python
import logic.thinking
```

You _can not do_
```python
import logic
logic.thinking.think_hard()
```
Only individual _files_ can be imported.

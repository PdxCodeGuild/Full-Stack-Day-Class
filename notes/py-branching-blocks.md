# Branching and Blocks

Programs need to make decisions to do the work we want the to.
**If statements** let us selectively execute code paths.

```py
if is_raining:
  wear_jacket = True
  mood = 'sad'
else:
  wear_jacket = False
  mood = 'happy'
wear_shoes = True
wear_pants = True
```

An if statement takes a _boolean expression_ and only executes a following **block** if the expression is `True`.

## Blocks

A block is a group of statements to be run together in order.
All statements in a block are _indented_ four spaces more than before.

Indentation is important!
**Only use 4 spaces.**
Double check that your editor is actually inserting spaces and not tabs.
Atom has "Toggle Invisibles" which shows shaded dots wherever you have spaces and double chevrons when you have a tab.

There are two blocks in the above example.

```py
wear_jacket = True
mood = 'sad'
```

and

```py
wear_jacket = False
mood = 'happy'
```

Blank lines have nothing to do with whether code is included in a block.
The following is identical to above.

```py
if is_raining:
  wear_jacket = True

  mood = 'sad'
else:
  wear_jacket = False
  mood = 'happy'

wear_shoes = True
wear_pants = True
```

Blocks can be **nested**.
Just indent four more spaces.

```py
if is_raining:
  if is_warm:
    wear_jacket = False
  else:
    wear_jacket = True
  mood = 'sad'
```

Blocks only come after a colon, `:`.
If you see a colon, you need an indented block on the next line, and vice versa.

## If Structure

An if statement is made up of one `if` **branch**, any number (including zero) of `elif` branches, and maybe one `else` branch.
Each `if` and `elif` branch has a proceeding boolean expression.

The boolean expressions are evaluated from _top to bottom_ and the first one to evaluate to `True` is run.
If none evaluate to `True`, the `else` branch is run.
_Only one_ branch is run.

```py
if num_legs < 2:
  print('snake')
elif num_legs < 3:
  print('human')
elif num_legs < 5:
  print('dog')
else:
  print('octopus')
```

In this example, only one animal will be printed.

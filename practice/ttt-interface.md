# Practice: Tic-Tac-Toe Interface

Save your solution in a directory in `practice/` in a branch and make a GitHub pull request all named `tic-tac-toe`.

You and I are working together on a tic-tac-toe game.
I'm writing the user interface and you're working on the board data structure.

We've decided on an interface for the board class.
The functions in each board class are:

* `place_token(x, y, token)` Place a token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.

```py
board.place_token(1, 2, 'X')
```

* `calc_winner()` What token character string has won or `None` if no one has.

```py
board.calc_winner()  #> 'X'
```

* `__str__()` Return a pretty-printed picture of the board.

```
X| |
 |X|O
 | |
```

I've already written out [some board test code](/practice/ttt-interface/boards_test.py).
Save it as `boards_test.py` in your solution directory.

I'd like you to prototype out three different _implementations_ of the board data structure that pass those tests.

1. Stored as a row-first list of lists of of tokens, `ListTTTBoard` in a module `list_board`

```py
_rows = [
    [None, None, 'x'],
    ['', 'X', ''],
    [' ', ' ', 'O'],
]
```

You'll have to consider how empty board spaces are represented.
They could be `None` or empty string `''` or a `' '` or something else.

2. Stored as a dict of coordinates to tokens, `DictTTTBoard` in a module `dict_board`

```py
_coord_to_token = {
    (0, 0): 'X',
    'a1': 'O',
    '02': None,
}
```

You'll have to consider how coordinates are encoded and empty board spaces are represented.
Coordinates could be two-tuples of `x` and `y` or an encoded string of some sort.
Empty spaces could have a key, or just be missing from the dict.

3. Stored as a list of coordinate token three-tuples, `CoordsTTTBoard` in a module `coords_board`

```py
_token_coords = [
    (1, 1, 'X'),
    (0, 1, 'O'),
]
```

Empty spaces should not be represented in this list.

Finish implementing all three of those classes so the `main()` tests successfully runs on all three versions.
Either run `py.test` from the `ttt-interface` directory, or setup a PyCharm test Run Configuration.

You should still write doctests for your functions that test internal implementation.

Once you're done with all three, look at how the implementations of the different functions varied.
Note how some operations were very easy with one data structure and much more tedious with a different one.
See how that matches up with your expectations and my [data structure problem solving](/notes/problem-solving-data-structures.md) notes.
This should show you how important it is to pick the right data structure that fits your problem!

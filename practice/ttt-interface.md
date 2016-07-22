# Practice: Tic-Tac-Toe Interface

Save your solution in a directory in `practice/` in a branch and make a GitHub pull request all named `tic-tac-toe`.

We're working together on a tic-tac-toe game.
I'm writing the user interface and you're working on the board data structure.

We've decided on an interface for the board class.
The functions in each board class are:

* `place_token(x, y)` Place a token at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position
* `calc_winner()` What user, if any, has won
* `__str__()` Return a pretty-printed picture of the board

```
X| |
 |X|O
 | |
```

I've already written out [some board test code](/practice/ttt-interface/boards_test.py).
Save it as `boards_test.py` in your solution directory.

I'd like you to prototype out three different _implementations_ of the board data structure that pass those tests.

* Stored as a row-first list of lists of of tokens, `ListTTTBoard` in a module `list_board`
* Stored as a dict of coordinates to tokens, `DictTTTBoard` in a module `dict_board`
* Stored as a list of coordinate token three-tuples, `CoordsTTTBoard` in a module `coords_board`

Finish implementing all three of those classes so the `main()` tests successfully runs on all three versions.
Either run `py.test` from the `ttt-interface` directory, or setup a PyCharm test Run Configuration.

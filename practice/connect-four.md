# Practice: Connect Four

Save your solution in a Python file in `practice/` in a branch and make a GitHub pull request all named `connect-four`.

[Connect Four](https://en.wikipedia.org/wiki/Connect_Four) is a board game.
Players take turns placing tokens of their color into a vertical grid.
They drop to the bottom, and if anyone has four of their color in a straight line, they've won!

Create a program that simulates the _just playing moves_ of an existing Connect Four game.
Do not concern yourself with figuring out who has won.

It will read a file that contains a history of the moves in a game.
Assume the playing board is made of columns numbered 1 through 7.
The file will have one line for each move (players alternate).
The number in that line is the column the current player placed a token in.

Use the following [example move file](/practice/connect-four-moves.txt).
Save it in something like `connect-four-moves.txt`
This moves file recreates [this game](https://en.wikipedia.org/wiki/File:Connect_Four.gif).

*   Think about how to figure out how far that token will fall in a given column.

*   Think about how to place a token in a column.

*   Think about how to concisely store the tokens that have been dropped in the board.

*   Read in moves from the file.

*   After each move, print out a representation of the board.
    You can use `R` and `Y` to represent the pieces.

## Advanced

* Once all moves are done, also print out what player, if any, won.

# Practice: Connect Four
[Connect Four](https://en.wikipedia.org/wiki/Connect_Four) is a board game.
Players take turns placing tokens of their color into a vertical grid.
They drop to the bottom, and if anyone has four of their color in a straight line, they've won!

Create a program that simulates the moves of an existing Connect Four game.

It will read a file that contains a history of the moves in a game.
Assume the playing board is made of columns numbered 1 through 7.
The file will have one line for each move (players alternate).
The number in that line is the column the current player placed a token in.

You board should be represented as a class.
Think about how to concisely store the tokens that have been dropped in the board.

Use the following example move file.
Save it in something like `4-moves.txt`
```
4
3
5
6
4
4
5
3
6
2
7
7
3
7
4
5
6
5
```
This moves file recreates [this game](https://en.wikipedia.org/wiki/File:Connect_Four.gif).

After each move, print out a representation of the board.
You can use `R` and `Y` to represent the pieces.

## Advanced
* Once all moves are done, also print out what player, if any, won.

# Practice: Writing to Interface
We're working together on a tic-tac-toe game.
I'm writing the user interface and you're working on the board data structure.

We've decided on an interface for the board class.
* Allows a user to place a token at a given coordinate (top-left is 0, 0)
* Can be asked to figure out what user, if any, has won
* Can return a pretty-printed picture of the board

I've already written out [some board test code](interface.py) and I'd like you to prototype out three different _implementations_ of the board data structure.
* Stored as a list of rows of tokens, `ListListTTTBoard`
* Stored as a dict of coordinates to tokens, `DictTTTBoard`
* Stored as a list of coordinate token three-tuples, `CoordsTTTBoard`

Finish implementing all three of those classes so the `main()` tests successfully runs on all three versions.

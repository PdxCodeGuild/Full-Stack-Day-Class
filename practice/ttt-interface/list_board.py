"""Module containing a list of lists tic-tac-toe board implementation."""


class ListListTTTBoard:
    """Tic-Tac-Toe board that implements storage as a list
    of rows, each with three slots.

    The following board results in the following data structure.
    X| |
     |X|O
     | |

    [
        ['X', ' ', ' '],
        [' ', 'X', 'O'],
        [' ', ' ', ' '],
    ]
    """

    def __init__(self):
        """Initialize an empty board."""
        self.rows = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]

    def place_token(self, x, y, player):
        """Place a token on the board at some given coordinates.

        x is horizontal position, y is vertical position.
        0, 0 is the top-left.
        `player` is either 'X' or 'O'
        """
        pass

    def calc_winner(self):
        """Return which token type won ('X' or 'O') or None if no one
        has won yet.
        """
        pass

    def __str__(self):
        """Return a string representation of the board.

        Should be three rows with each cell separated by a '|'.

        X| |
         |X|O
         | |
        """
        pass

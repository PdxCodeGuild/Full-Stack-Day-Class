"""Module containing a dictionary tic-tac-toe board implementation."""


class DictTTTBoard:
    """Tic-Tac-Toe board that implements storage as a flat
    dictionary of slots.

    The following board results in the following data structure.
    X| |
     |X|O
     | |

    {
        'a1': 'X', 'b1': ' ', 'c1': ' ',
        'a2': ' ', 'b2': 'X', 'c2': 'O',
        'a3': ' ', 'b3': ' ', 'c3': ' ',
    }
    """

    def __init__(self):
        """Initialize an empty board."""
        self.pos_to_token = {
            'a1': ' ', 'b1': ' ', 'c1': ' ',
            'a2': ' ', 'b2': ' ', 'c2': ' ',
            'a3': ' ', 'b3': ' ', 'c3': ' ',
        }

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

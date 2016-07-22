"""Module containing a coordinates tic-tac-toe board implementation."""


class CoordsTTTBoard:
    """Tic-Tac-Toe board that implements storage as a list of x, y, token triplets.

    An empty board is an empty list.
    Each token that is on the board adds one item to the triplet list.

    The following board results in the following data structure.
    X| |
     |X|O
     | |

    [(0, 0, 'X'), (1, 1, 'X'), (2, 1, 'O')]
    """

    def __init__(self):
        """Initalize an empty board."""
        self.x_y_token_triplets = []

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

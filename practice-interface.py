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
        """Initializes an empty board."""
        self.rows = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]

    def place(self, x, y, player):
        """Places a token on the board at some given coordinates.

        0, 0 is the top-left.
        `player` is either 'X' or 'O'
        """
        pass

    def won(self):
        """Return which token type won ('X' or 'O') or None if no one
        has won yet."""
        pass

    def __str__(self):
        """Returns a string representation of the board.

        Should be three rows with each cell separated by a '|'.

        X| |
         |X|O
         | |
        """
        pass


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
        """Initializes an empty board."""
        self.pos_to_token = {
            'a1': ' ', 'b1': ' ', 'c1': ' ',
            'a2': ' ', 'b2': ' ', 'c2': ' ',
            'a3': ' ', 'b3': ' ', 'c3': ' ',
        }

    def place(self, x, y, token):
        """Places a token on the board at some given coordinates.

        0, 0 is the top-left.
        `player` is either 'X' or 'O'
        """
        pass

    def won(self):
        """Return which token type won ('X' or 'O') or None if no one
        has won yet."""
        pass

    def __str__(self):
        """Returns a string representation of the board.

        Should be three rows with each cell separated by a '|'.

        X| |
         |X|O
         | |
        """
        pass


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
        """Initalizes an empty board."""
        self.x_y_token_triplets = []

    def place(self, x, y, player):
        """Places a token on the board at some given coordinates.

        0, 0 is the top-left.
        `player` is either 'X' or 'O'
        """
        pass

    def won(self):
        """Return which token type won ('X' or 'O') or None if no one
        has won yet."""
        pass

    def __str__(self):
        """Returns a string representation of the board.

        Should be three rows with each cell separated by a '|'.

        X| |
         |X|O
         | |
        """
        pass


def play(board):
    """Plays a test game on an empty board.

    Asserts that the board is working properly.
    """
    board.place(1, 1, 'X')
    print(board)
    board.place(0, 0, 'O')
    print(board)
    board.place(1, 0, 'X')
    assert str(board) == "O|X| \n |X| \n | | \n"
    print(board)
    board.place(0, 2, 'O')
    print(board)
    assert board.won() is None
    board.place(1, 2, 'X')
    print(board)
    assert board.won() == 'X'


def main():
    board1 = DictTTTBoard()
    play(board1)
    board2 = ListListTTTBoard()
    play(board2)
    board3 = CoordsTTTBoard()
    play(board3)


main()

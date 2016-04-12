class DictTTTBoard:
    def __init__(self):
        self.pos_to_token = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': 'X', 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def place(self, x, y, player):
        ...

    def won(self):
        ...

    def __str__(self):
        ...


class ListListTTTBoard:
    def __init__(self):
        self.rows = [
            [None, None, None],
            [None, 'X', None],
            [None, None, None],
        ]

    def place(self, x, y, player):
        ...

    def won(self):
        ...

    def __str__(self):
        ...


class CoordsTTTBoard:
    def __init__(self):
        self.x_y_token_triplets = [
            (1, 1, 'X'),
        ]

    def place(self, x, y, player):
        ...

    def won(self):
        ...

    def __str__(self):
        ...


def play(board):
    board.place(0, 0, 'O')
    print(board)
    board.place(1, 0, 'X')
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

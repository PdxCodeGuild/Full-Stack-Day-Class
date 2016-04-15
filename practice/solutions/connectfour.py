class Board:
    def __init__(self):
        self.cols_from_bottom = [[] for _ in range(7)]

    def put_token_in(self, col, token):
        self.cols_from_bottom[col].append(token)

    def as_pretty(self):
        print(self.cols_from_bottom)
        cols_filled_from_bottom = [
            col + [' ' for i in range(6 - len(col))]
            for col
            in self.cols_from_bottom
        ]
        print(cols_filled_from_bottom)
        filled_reverse_rows = list(zip(*cols_filled_from_bottom))
        print(filled_reverse_rows)
        filled_rows = reversed(filled_reverse_rows)
        row_strings = [
            '|{}|'.format('|'.join(row))
            for row
            in filled_rows
        ]
        return '\n'.join(row_strings)

    def __repr__(self):
        return 'Board({!r})'.format(self.cols_from_bottom)


MOVE_FILE = """4
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
5""".split()


def main():
    the_board = Board()
    for move_num, line in enumerate(MOVE_FILE):
        row_to_play = int(line.strip()) - 1
        player = 'Y' if move_num % 2 != 0 else 'R'
        the_board.put_token_in(row_to_play, player)
        print(the_board.as_pretty())
        print()


main()

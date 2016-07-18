"""Reads in a text file, which is a matrix of words, then pretty prints them so each column is of equal width with
borders.
"""


def read_file_into_rows(filename):
    """Read a given file and parse each line into space separated rows.

    The return value will be a list of rows of cells.

    [['row1item1', 'row1item2'], ['row2item1', 'row2item2']]
    """
    with open(filename) as f:
        return parse_lines_into_rows(f)


def parse_lines_into_rows(lines):
    r"""Convert a list of lines into a list of rows of cells.

    Remove blank lines.

    >>> parse_lines_into_rows(['how now\n', 'brown\n', '\n'])
    [['how', 'now'], ['brown']]
    """
    return [
        line.strip().split()
        for line
        in lines
        if line.strip() != ''
    ]


def transpose(matrix):
    """Transpose a list of lists.

    >>> transpose([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]
    """
    return [list(x) for x in zip(*matrix)]


def pad_cols(cols):
    """Pad a list of columns with spaces to the longest cell in each column.

    >>> pad_cols([['a', 'aa'], ['bbb', 'b']])
    [['a ', 'aa'], ['bbb', 'b  ']]
    """
    return [pad(col) for col in cols]


def calc_max_len(l):
    """Calculate the longest length in a list.

    >>> calc_max_len(['', 'a', 'aa'])
    2
    """
    return max([len(cell) for cell in l])


def pad(col):
    """Pad a list so all strings are the length of the longest.

    >>> pad(['a', 'aa', 'aaa'])
    ['a  ', 'aa ', 'aaa']
    """
    max_len = calc_max_len(col)
    return [cell.ljust(max_len) for cell in col]


def border_cols(cols):
    """Adds border line entries to each column.

    >>> border_cols([['aa', 'a'], ['bbb', 'b']])
    [['--', 'aa', 'a', '--'], ['---', 'bbb', 'b', '---']]
    """
    return [border_col(col) for col in cols]


def border_col(col):
    """Add a beginning and ending border of dashes to a list of cells.

    The border will be as long as the longest cell.

    >>> border_col(['aa', 'a'])
    ['--', 'aa', 'a', '--']
    """
    border_str = '-' * calc_max_len(col)
    return [border_str] + col + [border_str]


def print_rows(bordered_rows):
    """Given a list of rows (which is a matrix), print it out with pipes between each cell.

    >>> print_rows([['a', 'b'], ['c', 'd']])
    |a|b|
    |c|d|
    """
    for row in bordered_rows:
        joinable_row = [''] + row + ['']
        print('|'.join(joinable_row))


def pretty_print_table(rows):
    """Pretty an entire table with left justified columns.

    >>> pretty_print_table([['a', 'aa'], ['bbb', 'b']])
    |---|--|
    |a  |aa|
    |bbb|b |
    |---|--|
    """
    cols = transpose(rows)
    padded_cols = pad_cols(cols)
    bordered_padded_cols = border_cols(padded_cols)
    bordered_padded_rows = transpose(bordered_padded_cols)
    print_rows(bordered_padded_rows)


def main():
    """Read in a table file and pretty print it."""
    rows = read_file_into_rows('test-table.txt')
    pretty_print_table(rows)


if __name__ == '__main__':
    main()

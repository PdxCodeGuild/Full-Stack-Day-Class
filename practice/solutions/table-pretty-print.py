header_to_rows = {
  'Fruits': ['apple', 'orange', 'pineapple'],
  'Names': ['Alice', 'Bob'],
  'Animals': ['Dog', 'Cat', 'Ferret', 'Hamster']
}


def find_fit_width(row, header):
    lens = [len(cell) for cell in row + [header]]
    return max(lens)


def pad_row_width(row, width):
    return [cell.ljust(width) for cell in row]


def find_fit_height(rows):
    lens = [len(row) for row in rows]
    return max(lens)


def pad_row_height(row, length):
    needed_rows = length - len(row)
    return row + ['' for _ in range(needed_rows)]


def pad_table(header_to_rows):
    fit_height = find_fit_height(header_to_rows.values())
    vert_padded_table = {
        header: pad_row_height(row, fit_height)
        for header, row
        in header_to_rows.items()
    }
    padded_table = {
        header.ljust(find_fit_width(row, header)): pad_row_width(row, find_fit_width(row, header))
        for header, row
        in vert_padded_table.items()
    }
    return padded_table


def print_padded_rect_table(padded_header_to_rows):
    header_row_pairs = padded_header_to_rows.items()
    headers = [header for header, row in header_row_pairs]
    table_header = ' '.join(headers)
    print(table_header)
    rows = [row for header, row in header_row_pairs]
    for cells_across in zip(*rows):
        table_row = ' '.join(cells_across)
        print(table_row)


def pretty_print_table(header_to_rows):
    print_padded_rect_table(pad_table(header_to_rows))


if __name__ == '__main__':
    pretty_print_table(header_to_rows)

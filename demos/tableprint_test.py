import unittest
import tableprint


class TablePrintTest(unittest.TestCase):
    def test_find_fit_width(self):
        found = tableprint.find_fit_width(['1', '22', '333'], '1')
        assert found == 3

    def test_pad_row_width(self):
        found = tableprint.pad_row_width(['1', '22', '333'], 3)
        expected = ['1  ', '22 ', '333']
        assert found == expected

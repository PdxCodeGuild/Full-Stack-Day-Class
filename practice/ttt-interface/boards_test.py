"""Tests for all three board implementations."""


from coords_board import CoordsTTTBoard

from dict_board import DictTTTBoard

from list_board import ListTTTBoard


class BaseBoardTest:
    """Test class that will test a board.

    Store the class to be tested in a board_class class variable.
    """

    def test_str(self):
        """Test that the magic string method on a full board works."""
        board = self.board_class()
        board.place_token(1, 1, 'X')
        board.place_token(0, 0, 'O')
        board.place_token(1, 0, 'X')
        assert str(board) == 'O|X| \n |X| \n | | \n'

    def test_calc_winner_none(self):
        """Test that calculating a winner returns None when no winner."""
        board = self.board_class()
        board.place_token(1, 1, 'X')
        board.place_token(0, 0, 'O')
        board.place_token(1, 0, 'X')
        board.place_token(0, 2, 'O')
        assert board.calc_winner() is None

    def test_winner_won(self):
        """Test that calculating a winner returns the winner."""
        board = self.board_class()
        board.place_token(1, 1, 'X')
        board.place_token(0, 0, 'O')
        board.place_token(1, 0, 'X')
        board.place_token(0, 2, 'O')
        board.place_token(1, 2, 'X')
        assert board.calc_winner() == 'X'


class TestCoordsTTTBoard(BaseBoardTest):
    """Tests CoordsTTTBoard using BaseBoardTest test methods."""
    board_class = CoordsTTTBoard


class TestDictTTTBoard(BaseBoardTest):
    """Tests DictTTTBoard using BaseBoardTest test methods."""
    board_class = DictTTTBoard


class TestListListTTTBoard(BaseBoardTest):
    """Tests ListListTTTBoard using BaseBoardTest test methods."""
    board_class = ListTTTBoard

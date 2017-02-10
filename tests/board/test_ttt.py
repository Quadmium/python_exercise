import unittest

from modular_ttt.board.ttt import Board


class TestTTT(unittest.TestCase):
    def test_squares_attribute_in_board_is_a_list_of_nine_elements(self):
        board = Board()

        self.assertEqual(9, len(board.get_squares()))

    def test_getting_empty_positions(self):
        squares = ['X', '-', '-', 'X', '-', '-', 'O', '-', '-']
        board = Board()
        board.set_all_squares(squares)

        expected_empty_squares = [1, 2, 4, 5, 7, 8]

        self.assertEqual(expected_empty_squares, board.get_empty_square_positions())

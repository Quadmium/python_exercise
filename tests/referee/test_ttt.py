import unittest

from modular_ttt.referee.ttt import Referee
from modular_ttt.board.ttt import Board


class TestTTT(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.referee = Referee()

    def test_X_is_winner_in_first_horizontal(self):
        current_turn_token = 'X'
        squares = [
            'X', 'X', 'X',
            'O', 'O', '-',
            '-', '-', '-'
        ]
        self.board.set_all_squares(squares)

        self.assertTrue(self.referee.is_winner(self.board, current_turn_token))

    def test_O_is_winner_in_second_horizontal(self):
        current_turn_token = 'O'
        squares = [
            'X', 'X', '-',
            'O', 'O', 'O',
            '-', '-', '-'
        ]
        self.board.set_all_squares(squares)

        self.assertTrue(self.referee.is_winner(self.board, current_turn_token))

    def test_O_is_winner_in_first_vertical(self):
        current_turn_token = 'O'
        squares = [
            'O', 'X', '-',
            'O', 'X', '-',
            'O', '-', '-'
        ]
        self.board.set_all_squares(squares)

        self.assertTrue(self.referee.is_winner(self.board, current_turn_token))

import unittest
from unittest.mock import patch
from io import StringIO
import sys

from modular_ttt.game import Game
import itertools

class TestTTT(unittest.TestCase):
    @patch('modular_ttt.players.random.sleep', return_value=0)
    @patch('modular_ttt.input.move_handler.SimpleStdIn.choose')
    def test_random_vs_random(self, mock_choose, patched_time_sleep):
        # Mock the sleep function to make the gameplay instantly happen
        # Mock the side_effect such that input for choosing players will choose 0 then 0, (rand, rand)
        mock_choose.side_effect = [0, 0]
        # Take away stdout so game doesnt print to testing console
        originalOut = sys.stdout
        out = StringIO()
        sys.stdout = out
        game = Game()
        game.run()
        sys.stdout = originalOut
        # Check if game ended with congrats or tie
        self.assertTrue('Congrats' in out.getvalue() or 'tie' in out.getvalue())

    @patch('modular_ttt.players.random.sleep', return_value=0)
    @patch('modular_ttt.players.interactive.sleep', return_value=0)
    @patch('builtins.input')
    @patch('modular_ttt.input.move_handler.SimpleStdIn.choose')
    def test_random_vs_interactive(self, mock_choose, mock_play, patched_time_sleep1, patched_time_sleep2):
        # Mock the sleep function to make the gameplay instantly happen
        # Mock the side_effect such that input for choosing players will choose 0 then 1 (rand, interactive)
        mock_choose.side_effect = [0, 1]
        # Mock the interactive player input to an array from 1-9, so it will eventually find a correct location
        mock_play.side_effect = itertools.cycle([1, 2, 3, 4, 5, 6, 7, 8, 9])
        # Take away stdout so game doesnt print to testing console
        originalOut = sys.stdout
        out = StringIO()
        sys.stdout = out
        game = Game()
        game.run()
        sys.stdout = originalOut
        # Check if game ended with congrats or tie
        self.assertTrue('Congrats' in out.getvalue() or 'tie' in out.getvalue())

    @patch('modular_ttt.players.interactive.sleep', return_value=0)
    @patch('builtins.input')
    @patch('modular_ttt.input.move_handler.SimpleStdIn.choose')
    def test_interactive_vs_interactive(self, mock_choose, mock_play, patched_time_sleep):
        # Mock the sleep function to make the gameplay instantly happen
        # Mock the side_effect such that input for choosing players will choose 1 then 1 (interactive, interactive)
        mock_choose.side_effect = [1, 1]
        # Mock the interactive player input to an array from 1-9, so it will eventually find a correct location
        mock_play.side_effect = itertools.cycle([1, 2, 3, 4, 5, 6, 7, 8, 9])
        # Take away stdout so game doesnt print to testing console
        originalOut = sys.stdout
        out = StringIO()
        sys.stdout = out
        game = Game()
        game.run()
        sys.stdout = originalOut
        # Check if game ended with o winning, since the 1-9 choosing will lead to O getting a right diagonal
        self.assertTrue('Player O won' in out.getvalue())



    @patch('modular_ttt.players.random.sleep', return_value=0)
    @patch('modular_ttt.players.minimax.sleep', return_value=0)
    @patch('modular_ttt.input.move_handler.SimpleStdIn.choose')
    def test_minimax_vs_random(self, mock_choose, patched_time_sleep1, patched_time_sleep2):
        # Mock the sleep function to make the gameplay instantly happen
        # Mock the side_effect such that input for choosing players will choose 0 then 2, (rand, minimax)
        mock_choose.side_effect = [0, 2]
        # Take away stdout so game doesnt print to testing console
        originalOut = sys.stdout
        out = StringIO()
        sys.stdout = out
        game = Game()
        game.run()
        sys.stdout = originalOut
        # Check if game ended with at least a tie for minimax
        self.assertTrue('tie' in out.getvalue() or 'Player X won' in out.getvalue())

    @patch('modular_ttt.players.minimax.sleep', return_value=0)
    @patch('modular_ttt.players.interactive.sleep', return_value=0)
    @patch('builtins.input')
    @patch('modular_ttt.input.move_handler.SimpleStdIn.choose')
    def test_minimax_vs_interactive(self, mock_choose, mock_play, patched_time_sleep1, patched_time_sleep2):
        # Mock the sleep function to make the gameplay instantly happen
        # Mock the side_effect such that input for choosing players will choose 1 then 2 (interactive, minimax)
        mock_choose.side_effect = [1, 2]
        # Mock the interactive player input to an array from 1-9, so it will eventually find a correct location
        mock_play.side_effect = itertools.cycle([1, 2, 3, 4, 5, 6, 7, 8, 9])
        # Take away stdout so game doesnt print to testing console
        originalOut = sys.stdout
        out = StringIO()
        sys.stdout = out
        game = Game()
        game.run()
        sys.stdout = originalOut
        # Check if game ended with a win for minimax, since the 1-9 choosing will never win
        self.assertTrue('Player X won' in out.getvalue())

    @patch('modular_ttt.players.minimax.sleep', return_value=0)
    @patch('modular_ttt.input.move_handler.SimpleStdIn.choose')
    def test_minimax_vs_minimax(self, mock_choose, patched_time_sleep):
        # Mock the sleep function to make the gameplay instantly happen
        # Mock the side_effect such that input for choosing players will choose 2 then 2 (minimax, minimax)
        mock_choose.side_effect = [2, 2]
        # Take away stdout so game doesnt print to testing console
        originalOut = sys.stdout
        out = StringIO()
        sys.stdout = out
        game = Game()
        game.run()
        sys.stdout = originalOut
        # Check if game ended with a tie, since minimax can only tie each other
        self.assertTrue('tie' in out.getvalue())

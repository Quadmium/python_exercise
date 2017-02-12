from random import randint
from time import sleep


class RandomPlayer:
    def __init__(self, token):
        self.token = token

    def play(self, board):
        empty_squares = board.get_empty_square_positions()
        move_position = randint(0, len(empty_squares) - 1)
        board.set_square(empty_squares[move_position], self.token)
        sleep(0.5)

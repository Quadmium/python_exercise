from random import randint
from time import sleep
from modular_ttt.input.move_handler import SimpleStdIn


class InteractivePlayer:
    def __init__(self, token):
        self.token = token

    def play(self, board):
        playerInput = SimpleStdIn()
        targetMove = -1
        while targetMove == -1:
            targetMove = playerInput.play(board)
            print(" ")

        board.set_square(targetMove, self.token)
        sleep(0.5)

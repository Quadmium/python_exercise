from time import sleep
from modular_ttt.input.move_handler import SimpleStdIn
from modular_ttt.referee.ttt import Referee
from modular_ttt.constants import O_TOKEN, X_TOKEN, EMPTY_SQUARE
from modular_ttt.board.ttt import Board

class MinimaxPlayer:
    def __init__(self, token):
        self.token = token
        self.ref = Referee()

    def play(self, board):
        # Skip first move if given it, because it takes a long time to generate
        if board.is_board_empty():
            board.set_square(0, self.token)
            return

        tempBoard = Board()
        tempBoard.set_all_squares(board.squares[:])
        self.board = tempBoard
        board.set_square(self.minimax(True, True), self.token)
        sleep(0.5)

    def minimax(self, isMyTurn, returnMove = False):
        # Returns 5 if you win, 0 draw, -5 tie
        hasXWon = self.ref.is_winner(self.board, X_TOKEN)
        hasOWon = self.ref.is_winner(self.board, O_TOKEN)

        if hasXWon:
            return ((self.token == X_TOKEN) * 2 - 1) * 5
        elif hasOWon:
            return ((self.token == X_TOKEN) * 2 - 1) * -5
        elif self.board.is_board_full():
            return 0

        if isMyTurn:
            bestScore = -1000
            bestMove = -1
            for move in self.board.get_empty_square_positions():
                self.board.set_square(move, self.token)
                newBoardScore = self.minimax(False)
                self.board.set_square(move, EMPTY_SQUARE)
                if newBoardScore > bestScore:
                    bestMove = move
                bestScore = max(bestScore, newBoardScore)
            return bestScore if not returnMove else bestMove
        else:
            bestScore = 1000
            for move in self.board.get_empty_square_positions():
                self.board.set_square(move, X_TOKEN if self.token == O_TOKEN else O_TOKEN)
                newBoardScore = self.minimax(True)
                self.board.set_square(move, EMPTY_SQUARE)
                bestScore = min(bestScore, newBoardScore)
            return bestScore
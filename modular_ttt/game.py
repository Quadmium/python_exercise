from modular_ttt.board.ttt import Board
from modular_ttt.players.random import RandomPlayer
from modular_ttt.referee.ttt import Referee
from modular_ttt.output.simple_stdout import SimpleStdOut
from modular_ttt.constants import O_TOKEN, X_TOKEN


class Game:
    def __init__(self):
        self.board = Board()
        self.out = SimpleStdOut()
        self.playerO = RandomPlayer(O_TOKEN)
        # In random against random, player 'O' moves first
        self.current_turn_token = O_TOKEN
        self.playerX = RandomPlayer(X_TOKEN)
        self.referee = Referee()
        self.round = None

    def switch_turns(self):
        if self.current_turn_token == O_TOKEN:
            self.current_turn_token = X_TOKEN
            return
        self.current_turn_token = O_TOKEN

    def is_game_over(self):
        return self.referee.is_winner(self.board, self.current_turn_token) or \
            self.board.is_board_full()

    def annouce_result(self):
        if self.referee.is_winner(self.board, self.current_turn_token):
            self.out.display_winner_announcement(self.current_turn_token)
        elif self.board.is_board_full():
            self.out.display_tie_annoucement()

    def run(self):
        try:
            self.out.display_greetings_and_game_info()
            self.out.current_game_header()
            self.out.announce_player(
                type(self.playerO).__name__,
                O_TOKEN
            )
            self.out.announce_player(
                type(self.playerX).__name__,
                X_TOKEN
            )
            self.out.announce_who_moves_first(O_TOKEN)
            self.round = 0

            while True:
                self.playerO.play(self.board)
                self.out.display_board(self.board.get_squares(), self.round)
                if self.is_game_over():
                    break
                self.round += 1
                self.switch_turns()
                self.playerX.play(self.board)
                self.out.display_board(self.board.get_squares(), self.round)
                if self.is_game_over():
                    break
                self.round += 1
                self.switch_turns()

            self.annouce_result()

        except KeyboardInterrupt:
            print("Bye.")

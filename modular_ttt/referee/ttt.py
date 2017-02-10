class Referee:
    def __init__(self):
        self.squares = None
        self.token_to_check = None

    def is_winner(self, board, token_to_check):
        self.squares = board.get_squares()
        self.token_to_check = token_to_check
        is_winner = self.is_winner_in_horizontals() or \
            self.is_winner_in_verticals()
        return is_winner

    def is_winner_in_horizontals(self):
        is_winner = False
        first_position_in_horizontals = [0, 1, 2]
        for i in first_position_in_horizontals:
            k = i * 3
            if self.squares[k] == self.token_to_check and \
                    self.squares[k + 1] == self.token_to_check and \
                    self.squares[k + 2] == self.token_to_check:
                is_winner = True
                break
        return is_winner

    def is_winner_in_verticals(self):
        is_winner = False
        first_position_in_verticals = [0, 1, 2]
        for i in first_position_in_verticals:
            if self.squares[i] == self.token_to_check and \
                    self.squares[i + 3] == self.token_to_check and \
                    self.squares[i + 6] == self.token_to_check:
                is_winner = True
                break
        return is_winner

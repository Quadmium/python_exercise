class Referee:
    def __init__(self):
        self.squares = None
        self.token_to_check = None

    def is_winner(self, board, token_to_check):
        self.squares = board.get_squares()
        self.token_to_check = token_to_check
        is_winner = self.is_winner_in_horizontals() or \
            self.is_winner_in_verticals() or \
            self.is_winner_in_diagonals()
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

    # Checks for diagonal wins using a mask
    def is_winner_in_diagonals(self):
        is_winner = True
        left_diagonal_mask  = [1, 0, 0, 0, 1, 0, 0, 0, 1]
        right_diagonal_mask = [0, 0, 1, 0, 1, 0, 1, 0, 0]
        for i in range(0, len(left_diagonal_mask)):
            if left_diagonal_mask[i] == 1 and \
                self.squares[i] != self.token_to_check:
                is_winner = False
                break

        # If is_winner stays true after left loop, then dont check right
        if not is_winner:
            is_winner = True
            for i in range(0, len(right_diagonal_mask)):
                if right_diagonal_mask[i] == 1 and \
                    self.squares[i] != self.token_to_check:
                    is_winner = False
                    break

        return is_winner
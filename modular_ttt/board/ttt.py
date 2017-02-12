from modular_ttt.constants import EMPTY_SQUARE, O_TOKEN, X_TOKEN

class Board:
    def __init__(self):
        self.squares = [
            EMPTY_SQUARE,
            EMPTY_SQUARE,
            EMPTY_SQUARE,
            EMPTY_SQUARE,
            EMPTY_SQUARE,
            EMPTY_SQUARE,
            EMPTY_SQUARE,
            EMPTY_SQUARE,
            EMPTY_SQUARE
        ]

    def get_squares(self):
        return self.squares

    def set_square(self, position, token):
        self.squares[position] = token

    def set_all_squares(self, squares):
        self.squares = squares

    def get_empty_square_positions(self):
        empty_squares = []
        for index, value in enumerate(self.squares):
            if value == EMPTY_SQUARE:
                empty_squares.append(index)
        return empty_squares

    def is_board_full(self):
        return len(self.get_empty_square_positions()) == 0

    def is_board_empty(self):
        return len(self.get_empty_square_positions()) == 9

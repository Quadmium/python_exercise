from modular_ttt.constants import EMPTY_SQUARE

class SimpleStdIn:

    def __init__(self):
        pass

    def choose(self, numChoices):
        try:
            choice = int(input("Please choose (1-{}): \n".format(numChoices))) - 1

            if choice < 0 or choice > numChoices - 1:
                print("Choice out of bounds, please try again")
                choice = -1

            return choice
        except ValueError:
            print("Wrong choice, please try again")
            return -1

    def play(self, board):
        try:
            next_move = int(input("Please enter your next move (1-9): \n")) - 1

            if next_move < 0 or next_move > board.get_number_of_squares() - 1:
                print("Square not within (1-9), please try again")
                next_move = -1

            if board.squares[next_move] != EMPTY_SQUARE:
                print("Square already taken, please try again")
                next_move = -1

            return next_move
        except ValueError:
            print("Wrong move, please try again")
            return -1

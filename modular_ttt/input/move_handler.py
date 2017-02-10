def play(self, board):
    try:
        next_move = int(input("Please enter your next move: \n"))

        return board
    except ValueError:
        print("Wrong move, please try again")
        return board

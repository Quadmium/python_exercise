class SimpleStdOut:
    def __init__(self):
        pass

    def display_board(self, squares, round):
        print("Round {}: ".format(round), end=" ")
        print(squares, end=" ")
        print("")
        print("")

    def game_gretings(self):
        print("Welcome to Modular Tic Tac Toe")
        print("------------------")

    def display_greetings_and_game_info(self):
        self.game_gretings()
        self.general_info()

    def general_info_header(self):
        print("GENERAL INFO")
        print("------------------")

    def general_info(self):
        self.general_info_header()
        print("Until further development the traditional TTT board: ")
        print("__________________")
        print("|  1  |  2  |  3  |")
        print("|  4  |  5  |  6  |")
        print("|  7  |  8  |  9  |")
        print("__________________")
        print("")
        print("will be displayed like shown below during the game: ")
        print("")
        print("['1', '2', '3', '4', '5', '6', '7', '8', '9']")
        print("")
        print("")

    def display_winner_announcement(self, winner_token):
        print("Player {} won. Congrats.".format(winner_token))
        print("")

    def display_tie_annoucement(self):
        print("It was a tie. Well played.")
        print("")

    def current_game_header(self):
        print("------------------")
        print("CURRENT GAME")
        print("------------------")

    def announce_player(self, player_type, token):
        print("Player {} plays with {}.".format(player_type, token))

    def announce_who_moves_first(self, token_that_moves_first):
        print("Player {} moves first.".format(token_that_moves_first))
        print("")

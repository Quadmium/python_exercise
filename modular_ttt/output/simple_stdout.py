class SimpleStdOut:
    def __init__(self):
        pass

    def display_board(self, squares, round):
        print("Round {}: ".format(round))
        print("-------------------")
        print("|  {0}  |  {1}  |  {2}  |".format(squares[0], squares[1], squares[2]))
        print("|  {0}  |  {1}  |  {2}  |".format(squares[3], squares[4], squares[5]))
        print("|  {0}  |  {1}  |  {2}  |".format(squares[6], squares[7], squares[8]))
        print("-------------------")
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
        print("The TTT board will be shown as: ")
        print("-------------------")
        print("|  1  |  2  |  3  |")
        print("|  4  |  5  |  6  |")
        print("|  7  |  8  |  9  |")
        print("-------------------")
        print("")
        print("")

    def display_choose_prompt(self, player):
        print("Choose player {}".format(player))

    def display_player_choices(self):
        print("1. Random")
        print("2. Interactive")
        print("3. Minimax")

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

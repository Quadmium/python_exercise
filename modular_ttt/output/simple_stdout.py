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
        return "{}\n{}\n".format(
            "Welcome to Modular Tic Tac Toe",
            "------------------"
        )

    def display_greetings_and_game_info(self):
        return "{}{}".format(
            self.game_gretings(),
            self.general_info()
        )

    def general_info_header(self):
        return "{}\n{}".format(
            "GENERAL INFO",
            "------------------"
        )

    def general_info(self):
        return "{}\n{}\n{}\n{}\n{}\n{}\n{}\n\n".format(
            self.general_info_header(),
            "The TTT board will be shown as:",
            "-------------------",
            "|  1  |  2  |  3  |",
            "|  4  |  5  |  6  |",
            "|  7  |  8  |  9  |",
            "-------------------"
        )

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

class WebOut:
    def __init__(self):
        pass

    def display_board(self, squares, round):
        return "Round {}: ".format(round) + "<br>" + \
        "|  {0}  |  {1}  |  {2}  |".format(squares[0], squares[1], squares[2]) + "<br>" + \
        "|  {0}  |  {1}  |  {2}  |".format(squares[3], squares[4], squares[5]) + "<br>" + \
        "|  {0}  |  {1}  |  {2}  |".format(squares[6], squares[7], squares[8]) + "<br>"

    def game_gretings(self):
        return "{}\n{}\n".format(
            "Welcome to Modular Tic Tac Toe",
            "------------------".replace("\n", "<br>")
        )

    def display_greetings_and_game_info(self):
        return "{}{}".format(
            self.game_gretings(),
            self.general_info().replace("\n", "<br>")
        )

    def general_info_header(self):
        return "{}\n{}".format(
            "GENERAL INFO",
            "------------------".replace("\n", "<br>")
        )

    def general_info(self):
        return "{}\n{}\n{}\n{}\n{}\n\n\n".format(
            self.general_info_header(),
            "The TTT board will be shown as:",
            "|  1  |  2  |  3  |",
            "|  4  |  5  |  6  |",
            "|  7  |  8  |  9  |").replace("\n", "<br>")


'''
    def display_choose_prompt(self, player):
        "Choose player {}".format(player))

    def display_player_choices(self):
        "1. Random")
        "2. Interactive")
        "3. Minimax")

    def display_winner_announcement(self, winner_token):
        "Player {} won. Congrats.".format(winner_token))
        "")

    def display_tie_annoucement(self):
        "It was a tie. Well played.")
        "")

    def current_game_header(self):
        "------------------")
        "CURRENT GAME")
        "------------------")

    def announce_player(self, player_type, token):
        "Player {} plays with {}.".format(player_type, token))

    def announce_who_moves_first(self, token_that_moves_first):
        "Player {} moves first.".format(token_that_moves_first))
        "")
'''
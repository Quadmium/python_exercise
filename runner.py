from modular_ttt.game import Game
from modular_ttt.game_over_network import app
from modular_ttt.input.move_handler import SimpleStdIn


if __name__ == '__main__':
    print("Choose UI mode:")
    print("1. CLI")
    print("2. Over network")
    print("")
    ui_mode_input = SimpleStdIn()
    ui_mode = -1
    while ui_mode == -1:
        ui_mode = ui_mode_input.choose(2)

    if ui_mode == 0:
        game = Game()
        game.run()

    if ui_mode == 1:
        app.run(host='0.0.0.0')

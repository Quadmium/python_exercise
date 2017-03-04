from flask import Flask, make_response, request
import sqlite3
import json
import traceback

from modular_ttt.board.ttt import Board
from modular_ttt.players.random import RandomPlayer
from modular_ttt.players.interactive import InteractivePlayer
from modular_ttt.players.minimax import MinimaxPlayer
from modular_ttt.referee.ttt import Referee
from modular_ttt.output.webout import WebOut
from modular_ttt.input.move_handler import SimpleStdIn
from modular_ttt.constants import O_TOKEN, X_TOKEN

app = Flask(__name__)


@app.route('/', methods=['GET'])
def provide_game_info():
    try:
        out = WebOut()
        resp_string = out.display_greetings_and_game_info().replace("\n", "<br>")
        
        conn = sqlite3.connect('game.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM game_state")
        game_data = cur.fetchone()

        current_turn_squares = list(game_data[4])

        board = Board()
        board.set_all_squares(current_turn_squares)

        resp_string += "<br>" + \
                       out.display_board(board.squares, 9 - len(board.get_empty_square_positions())).replace("\n", "<br>")

        resp = make_response(resp_string, 200)

        return resp
    except Exception as e:
        print(e)
    finally:
        conn.close()


@app.route('/move', methods=['POST'])
def handle_move():
    conn = sqlite3.connect('game.db')
    cur = conn.cursor()
    try:
        # {'token': 'O', 'square': '3'}
        data_dict = request.get_json()

        if 'reset' in data_dict:
            cur.execute("UPDATE game_state SET current_turn_token='O', current_board_squares='---------'")
            conn.commit()
            return 'Board reset'

        token = data_dict['token']
        square = int(data_dict['square'])

        # INITIAL GAME STATE
        # sqlite> select * from game_state;
        # game_id     player_one_token  player_two_token  current_turn_token  current_board_squares
        # ----------  ----------------  ----------------  ------------------  ---------------------
        # 1           O                 X                 O                   ---------
        cur.execute("SELECT * FROM game_state")
        game_data = cur.fetchone()
        current_turn_token = game_data[3]

        if token != current_turn_token:
            return 'Not your turn yet'

        opponent_token = X_TOKEN if token == O_TOKEN else O_TOKEN
        current_turn_squares = list(game_data[4])

        board = Board()
        board.set_all_squares(current_turn_squares)
        if square not in board.get_empty_square_positions():
            return 'Square taken'

        referee = Referee()
        if referee.is_winner(board, token) or referee.is_winner(board, opponent_token):
            return 'Game over, send reset'

        current_turn_squares[square] = token

        # can add WHERE game_id=1
        cur.execute("UPDATE game_state SET current_board_squares='" + ''.join(current_turn_squares) + "'")
        cur.execute("UPDATE game_state SET current_turn_token='" + opponent_token+ "'")
        
        conn.commit()
        return 'Move accepted'
    except Exception as e:
        traceback.print_exc()
    finally:
        conn.close()

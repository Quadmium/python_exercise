from flask import Flask, make_response, request
import sqlite3
import json
import traceback

from modular_ttt.board.ttt import Board
from modular_ttt.players.random import RandomPlayer
from modular_ttt.players.interactive import InteractivePlayer
from modular_ttt.players.minimax import MinimaxPlayer
from modular_ttt.referee.ttt import Referee
from modular_ttt.output.simple_stdout import SimpleStdOut
from modular_ttt.input.move_handler import SimpleStdIn
from modular_ttt.constants import O_TOKEN, X_TOKEN

app = Flask(__name__)


@app.route('/', methods=['GET'])
def provide_game_info():
    try:
        out = SimpleStdOut()
        resp_string = out.display_greetings_and_game_info()
        # ...
        resp = make_response(resp_string, 200)

        return resp
    except Exception as e:
        print(e)


@app.route('/move', methods=['POST'])
def handle_move():
    conn = sqlite3.connect('game.db')
    cur = conn.cursor()
    try:
        # {'token': 'O', 'square': '3'}
        data_dict = request.get_json()
        token = data_dict['token']
        square = int(data_dict['square'])

        # INITIAL GAME STATE
        # sqlite> select * from game_state;
        # game_id     player_one_token  player_two_token  current_turn_token  current_board_squares
        # ----------  ----------------  ----------------  ------------------  ---------------------
        # 1           O                 X                 O                   ---------
        cur.execute("SELECT * FROM game_state")
        current_turn_token = cur.fetchone()[3]

        if token != current_turn_token:
            return 'Not your turn yet'

        #...

        return 'Finish handling move'
    except Exception as e:
        traceback.print_exc()
    finally:
        conn.close()

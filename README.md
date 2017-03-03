Python tic tac toe scenarios

Useful docs:

http://flask.pocoo.org/docs/0.12/quickstart/

https://docs.python.org/2/library/sqlite3.html

CREATE TABLE game_state(game_id integer primary key,player_one_token text not null,player_two_token text not null,current_turn_token text not null, current_board_squares);

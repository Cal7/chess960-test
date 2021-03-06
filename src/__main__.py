from simulation import Simulation
from db_functions import *
import config
import chess.uci
import sqlite3
import sys

if not db_exists():
    create_db()

con = sqlite3.connect(get_db_path())

if len(sys.argv) >= 2: #if it has been specified which starting id to start looping from
    current_start_position_id = int(sys.argv[1])
else:
    current_start_position_id = 0

while True:
    simulation = Simulation(chess.uci.popen_engine(config.engine_path), current_start_position_id, config.time_limit, config.time_increment)
    simulation.run()
    simulation.save_to_db(con)

    if current_start_position_id == 959:
        current_start_position_id = 0
    else:
        current_start_position_id += 1
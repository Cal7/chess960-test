import sqlite3
import os.path

def create_db():
    con = sqlite3.connect("../db/db.sqlite")
    cur = con.cursor()
    cur.execute("CREATE TABLE `games` ( `id` INTEGER PRIMARY KEY AUTOINCREMENT, `start_position_id` INTEGER, `time_limit` INTEGER, `time_increment` INTEGER, `result` INTEGER, `move_history` TEXT )")

def db_exists():
    return os.path.isfile(os.path.join(os.path.dirname(__file__), "../db/db.sqlite"))
import sqlite3
import os.path

def create_db():
    con = sqlite3.connect(get_db_path())
    cur = con.cursor()
    cur.execute("CREATE TABLE `games` ( `id` INTEGER PRIMARY KEY AUTOINCREMENT, `start_position_id` INTEGER, `time_limit` INTEGER, `time_increment` INTEGER, `result` INTEGER, `move_history` TEXT )")

def get_db_path():
    return os.path.join(os.path.dirname(__file__), "../db/db.sqlite")

def db_exists():
    return os.path.isfile(get_db_path())
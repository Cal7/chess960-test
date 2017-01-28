import sqlite3
from os.path import isfile

def create_db():
    con = sqlite3.connect("../db/db.sqlite")
    cur = con.cursor()
    cur.execute("CREATE TABLE `games` ( `id` INTEGER PRIMARY KEY AUTOINCREMENT, `start_postion_id` INTEGER, `time_limit` INTEGER, `time_increment` INTEGER, `result` INTEGER, `move_history` TEXT )")

def db_exists():
    return isfile("db.sqlite")

create_db()
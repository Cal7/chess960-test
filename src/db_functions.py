import sqlite3
from os.path import isfile

def create_db():
    con = sqlite3.connect("../db/db.sqlite")
    cur = con.cursor()
    cur.execute("CREATE TABLE `games` ( `id` INTEGER PRIMARY KEY AUTOINCREMENT, `starting_id` INTEGER NOT NULL, `time_limit` INTEGER NOT NULL, `result` TEXT )")
    cur.execute("CREATE TABLE `moves` ( `id` INTEGER PRIMARY KEY AUTOINCREMENT, `number` INTEGER, `move` TEXT, `game_id` INTEGER )")

def db_exists():
    return isfile("db.sqlite")

create_db()
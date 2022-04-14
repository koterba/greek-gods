import sqlite3
import random

conn = sqlite3.connect("gods.db")
curr = conn.cursor()

all_data = curr.execute("SELECT god, description FROM gods").fetchall()

def get_god():
	return random.choice(all_data)

god, desc = get_god()
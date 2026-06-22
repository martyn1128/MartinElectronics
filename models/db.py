import os
import sqlite3

class DB:
    def __init__(self):

        self.db_path = os.path.join(os.getenv('APPDATA'),'Martin Electronics/data/me.db')

    def connect(self):
        return sqlite3.connect(self.db_path)
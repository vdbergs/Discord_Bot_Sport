import sqlite3
import os

class Database:
    def __init__(self):
        db_path = os.path.join('storage', 'data', 'sports.db')
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fixtures (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sport TEXT,
                date TEXT,
                teams TEXT,
                competition TEXT
            )
        ''')
        self.conn.commit()

    def store_fixtures(self, sport, fixtures):
        cursor = self.conn.cursor()
        cursor.executemany(
            'INSERT INTO fixtures (sport, date, teams, competition) VALUES (?, ?, ?, ?)',
            [(sport, f['date'], f['teams'], f['competition']) for f in fixtures]
        )
        self.conn.commit()

    def __del__(self):
        self.conn.close()
import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('education_counseling.db', check_same_thread=False)

    def create_log_table(self):
        c = self.conn.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS user_interactions (
            id INTEGER PRIMARY KEY,
            timestamp TEXT,
            user_input TEXT,
            bot_response TEXT
        )
        ''')
        self.conn.commit()

    def create_courses_table(self):
        c = self.conn.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY,
            name TEXT,
            details TEXT
        )
        ''')
        self.conn.commit()

    def log_interaction(self, timestamp, user_input, bot_response):
        c = self.conn.cursor()
        c.execute('''
        INSERT INTO user_interactions (timestamp, user_input, bot_response) 
        VALUES (?, ?, ?)
        ''', (timestamp, user_input, bot_response))
        self.conn.commit()

    def get_courses(self):
        c = self.conn.cursor()
        c.execute("SELECT name, details FROM courses")
        return c.fetchall()

    def get_prices(self):
        c = self.conn.cursor()
        c.execute("SELECT name, price FROM courses")
        return c.fetchall()

    def insert_course(self, name, details):
        c = self.conn.cursor()
        c.execute('''
        INSERT INTO courses (name, details) VALUES (?, ?)
        ''', (name, details))
        self.conn.commit()

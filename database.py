import sqlite3


def init_db():
    with sqlite3.connect("expense_tracker.db") as conn:
        cursor = conn.cursor()

        # Create users table
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          username TEXT UNIQUE NOT NULL,
                          email TEXT UNIQUE NOT NULL,
                          password_hash TEXT NOT NULL)''')

        # Create expenses table
        cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          user_id INTEGER NOT NULL,
                          date TEXT NOT NULL,
                          category TEXT NOT NULL,
                          description TEXT,
                          amount REAL NOT NULL,
                          FOREIGN KEY (user_id) REFERENCES users(id))''')

        conn.commit()


if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")

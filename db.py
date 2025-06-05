import sqlite3
from config import DB_NAME

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE,
            full_name TEXT,
            phone TEXT UNIQUE
        )''')
    conn.commit()
    conn.close()

def is_user_registered(telegram_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE telegram_id = ?', (telegram_id,))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def register_user(telegram_id, full_name, phone):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (telegram_id, full_name, phone) VALUES (?, ?, ?)',
                       (telegram_id, full_name, phone))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"User with telegram_id {telegram_id} or phone {phone} already exists.")
    finally:
        conn.close()
import sqlite3

def init_db():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER UNIQUE,
                name TEXT,
                password PASSWORD,
                phone TEXT UNIQUE
                )
''')
    conn.commit()
    conn.close()

def is_user_registered(telegram_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("select * from users where telegram_id = ?", (telegram_id))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def register_user(telegram_id, name, password, phone):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute("insert into users(telegram_id, name, password, phone) values (?,?,?,?)", (telegram_id, name, password, phone))
        conn.commit()
    except sqlite3.InterruptedError:
        print(f"user with telegram_id {telegram_id} or phone {phone} elreade exists")
    finally:
        conn.close()
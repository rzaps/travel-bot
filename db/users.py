# === ФАЙЛ: db/users.py ===
import sqlite3

def init_db():
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tg_id INTEGER UNIQUE,
                full_name TEXT,
                city TEXT
            )
        ''')
        conn.commit()

def save_user(tg_id: int, full_name: str, city: str):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO users (tg_id, full_name, city)
            VALUES (?, ?, ?)
        ''', (tg_id, full_name, city))
        conn.commit()

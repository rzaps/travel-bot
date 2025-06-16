# === ФАЙЛ: db/users.py ===
import sqlite3

# Функция инициализации БД
def init_db():
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tg_id INTEGER UNIQUE,
                name TEXT,
                city TEXT,
                category1 TEXT,
                category2 TEXT,
                category3 TEXT,
                expenses1 REAL,
                expenses2 REAL,
                expenses3 REAL
            )
        ''')
        conn.commit()


# Функция сохранения данных о пользователе
def save_user(tg_id: int, name: str, city: str):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO users (tg_id, name, city)
            VALUES (?, ?, ?)
        ''', (tg_id, name, city))
        conn.commit()


# Функция получения данных о пользователе
def get_user(tg_id: int):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE tg_id = ?', (tg_id,))
        return cursor.fetchone()


# Функция обновления финансовых данных
def update_finance(tg_id: int, data: dict):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE users
            SET category1 = ?, category2 = ?, category3 = ?,
                expenses1 = ?, expenses2 = ?, expenses3 = ?
            WHERE tg_id = ?
        ''', (
            data.get('category1'),
            data.get('category2'),
            data.get('category3'),
            data.get('expenses1'),
            data.get('expenses2'),
            data.get('expenses3'),
            tg_id
        ))
        conn.commit()


# Функция получения финансовых данных с расчетом статистики
def get_finance_data(tg_id: int):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT category1, category2, category3, expenses1, expenses2, expenses3
            FROM users WHERE tg_id = ?
        ''', (tg_id,))
        result = cursor.fetchone()
        
        if not result:
            return None
            
        categories = [result[0], result[1], result[2]]
        expenses = [result[3] or 0, result[4] or 0, result[5] or 0]
        
        # Фильтруем только заполненные категории
        valid_data = [(cat, exp) for cat, exp in zip(categories, expenses) if cat and exp > 0]
        
        if not valid_data:
            return None
            
        total = sum(exp for _, exp in valid_data)
        
        # Рассчитываем проценты
        percentages = []
        for cat, exp in valid_data:
            percentage = (exp / total * 100) if total > 0 else 0
            percentages.append((cat, exp, percentage))
            
        return {
            'total': total,
            'breakdown': percentages
        }

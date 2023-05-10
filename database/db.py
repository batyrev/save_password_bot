import sqlite3

from database.db_config import DB_FILE


def create_table():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (
                            user_id INTEGER,
                            service TEXT,
                            password TEXT,
                            PRIMARY KEY (user_id, service)
                        )''')
        conn.commit()


def set_password(user_id, service, password):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT OR REPLACE INTO passwords \
                       (user_id, service, password) VALUES (?, ?, ?)',
                       (user_id, service, password))
        conn.commit()


def get_password(user_id, service):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT password FROM passwords \
                       WHERE user_id = ? AND service = ?',
                       (user_id, service))
        return cursor.fetchone()


def delete_password(user_id, service):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM passwords \
                       WHERE user_id = ? AND service = ?',
                       (user_id, service))
        conn.commit()

import sqlite3

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
user_id INTEGER PRIMARY KEY,
username TEXT,
balance INTEGER DEFAULT 0
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS history(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
type TEXT,
prompt TEXT,
result TEXT
)
""")

conn.commit()


def create_user(user_id, username):

    cursor.execute(
        "INSERT OR IGNORE INTO users(user_id,username) VALUES(?,?)",
        (user_id,username)
    )

    conn.commit()


def get_balance(user_id):

    cursor.execute(
        "SELECT balance FROM users WHERE user_id=?",
        (user_id,)
    )

    return cursor.fetchone()[0]


def add_balance(user_id, amount):

    cursor.execute(
        "UPDATE users SET balance = balance + ? WHERE user_id=?",
        (amount,user_id)
    )

    conn.commit()


def deduct_balance(user_id, amount):

    cursor.execute(
        "UPDATE users SET balance = balance - ? WHERE user_id=?",
        (amount,user_id)
    )

    conn.commit()


def save_history(user_id,type_,prompt,result):

    cursor.execute(
        "INSERT INTO history(user_id,type,prompt,result) VALUES(?,?,?,?)",
        (user_id,type_,prompt,result)
    )

    conn.commit()


def get_history(user_id):

    cursor.execute(
        "SELECT type,prompt,result FROM history WHERE user_id=? ORDER BY id DESC"
        ,(user_id,)
    )

    return cursor.fetchall()
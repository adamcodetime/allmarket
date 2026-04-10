import sqlite3

conn = sqlite3.connect("db.sqlite3")
conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT
    )
"""
)
conn.commit()
conn.close()

print("Database created.")

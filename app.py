from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "db.sqlite3")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    conn = get_db()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return render_template("index.html", users=users)


@app.route("/submit", methods=["POST"])
def submit():
    username = request.form["username"]

    conn = sqlite3.connect("db.sqlite3")
    conn.execute("INSERT INTO users (username) VALUES (?)", (username,))
    conn.commit()
    conn.close()

    return "Saved to DB: " + username


if __name__ == "__main__":
    app.run()

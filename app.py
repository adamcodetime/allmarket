from flask import Flask, render_template, request, redirect, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "supersecret123"

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
    username = request.form["username"].strip()

    try:
        with sqlite3.connect("db.sqlite3") as conn:
            conn.execute(
                "INSERT INTO users (username) VALUES (?)",
                (username,)
            ) 

    except sqlite3.IntegrityError:
        pass

    except sqlite3.OperationalError:
        pass

    return redirect("/")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

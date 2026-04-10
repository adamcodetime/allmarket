from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("db.sqlite3")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

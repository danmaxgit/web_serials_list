from flask import Flask, render_template, jsonify

import sqlite3
from pathlib import Path
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods=['GET'])
def main():
	return render_template("index.html")

@app.route("/api", methods=['GET'])
def get():
    path = Path("/mnt/home_nas/scripts")
    path = path / "db"
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    sql = "SELECT * FROM serials ORDER BY time ASC"
    cursor.execute(sql)
    db = cursor.fetchall()
    conn.close()
    res = []
    for i in db:
         res.append({
              "name" : i[0],
              "watched" : i[1],
              "date" : datetime.fromtimestamp(i[2])
         })
    return jsonify(res)

if __name__ == "__main__":
    app.run()
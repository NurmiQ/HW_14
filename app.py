from flask import Flask, request
from functions import get_db
import sqlite3


app = Flask(__name__)


@app.route("/")
def page_index():
    data = read_json(POST_PATH)
    return render_template('index.html', tags=get_hash(data))








@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)



if __name__ == "__main__":
    app.run()




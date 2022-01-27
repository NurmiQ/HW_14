import json

from flask import Flask, request, jsonify
from functions import get_db
import sqlite3

app = Flask(__name__)


@app.route('/movie/title')
def search_movie():
    if request.method == 'GET':
        response = {}
        title = request.args.get('title')
        if title:
            sqlite_query = f"""
            select
                   title,
                   country,
                   listed_in,
                   release_year,
                   description
            from netflix
            where title = '{title}'
            order by release_year DESC 
            LIMIT 1
            """
            result = get_db('netflix.db', sqlite_query)
            if len(result):
                response = {
                    "title": result[0][0],
                    "country" : result[0][1],
                    "listed_in" : result[0][2],
                    "release_year" : result[0][3],
                    "description" : result[0][4],
                }
        return jsonify(response)


if __name__ == "__main__":
    app.run()

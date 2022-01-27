import json

from flask import Flask, request, jsonify
from functions import get_db, sort_rating
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


@app.route('/movie/year/')
def search_year():
    if request.method == 'GET':
        response = []
        f_year = request.args.get('f_year')
        s_year = request.args.get('s_year')
        if f_year and s_year:
            sqlite_query = f"""
            select title, release_year
            from netflix
            where release_year between {f_year} and {s_year}
            order by release_year DESC limit 100
            """
            result = get_db('netflix.db', sqlite_query)       # [(title, year), (title, year)]
            for line in result:
                line_dict = {
                    'title': line[0],
                    'release_year': line[1],
                }
                response.append(line_dict)
        return jsonify(response)


@app.route('/rating/children')
def rating_children():
    response = sort_rating(['G'])
    return jsonify(response)


@app.route('/rating/family')
def rating_family():
    response = sort_rating(['G', 'PG', 'PG-13'])
    return jsonify(response)


@app.route('/rating/adult')
def rating_adult():
    response = sort_rating(['R', 'NC-17'])
    return jsonify(response)


if __name__ == "__main__":
    app.run()

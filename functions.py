import sqlite3


def get_db(db, sqlite_query):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(sqlite_query)
    result = cur.fetchall()
    con.close()
    return result


def sort_rating(rating):
    response = []
    if len(rating) > 1:
        str_rating = "','".join(rating)
    else:
        str_rating = "".join(rating)
    sqlite_query = f"""
    select title, rating, description
     from netflix where rating in ('{str_rating}')
     """
    result = get_db('netflix.db', sqlite_query)
    for line in result:
        line_dict = {
            "title": line[0],
            "rating": line[1],
            "description": line[2],
        }
        response.append(line_dict)
    return response


def get_movie_by_genre(genre):
    response = []
    sqlite_query = f"""
    select title, description
    from netflix where listed_in like '%{genre}%'
    order by release_year DESC limit 10"""
    result = get_db('netflix.db', sqlite_query)
    for line in result:
        line_dict = {
            "title": line[0],
            "description": line[1],
        }
        response.append(line_dict)
    return response



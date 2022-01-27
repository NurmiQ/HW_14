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

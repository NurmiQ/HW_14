import sqlite3


def get_db(sqlite_query):
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    cur.execute(sqlite_query)
    result = cur.fetchall()
    con.close()
    return result


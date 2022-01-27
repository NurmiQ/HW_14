import sqlite3


def get_db(db, sqlite_query):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(sqlite_query)
    result = cur.fetchall()
    con.close()
    return result




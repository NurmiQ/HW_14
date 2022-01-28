import sqlite3
from collections import Counter


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


def search_actors(actor_1, actor_2):
    sqlite_query = f"""
    select \"cast\" from netflix
    where \"cast\" like '%{actor_1}%' and \"cast\" like '%{actor_2}%' """
    result = get_db('netflix.db', sqlite_query)  # [('Steve Carell, Anne Hathaway, Dwayne Johnson, Alan Arkin, Terence Stamp, Terry Crews, David Koechner, James Caan, Masi Oka, Nate Torrence, Bill Murray',), ('Dwayne Johnson, AnnaSophia Robb, Alexander Ludwig, Carla Gugino, Ciarán Hinds, Tom Everett Scott, Chris Marquette, Billy Brown, Christine Lakin, Tom Woodruff Jr., John Kassir, Garry Marshall, John Duff, Ted Hartley, Dave Engfer, Bob Clendenin, Shengyi Huang, Robert Torti, Kim Richards, Brandon Miller, Paul Darnell, Omar Dorsey, Dennis Hayden, Suzanne Krull, Steve Rosenbaum, Andrew Shaifer, Bryan Fogel, Bob Koherr, Sam Wolfson, Beth Kennedy, Corri English, Jonathan Slavin, Kevin Christy, Meredith Salenger',)]
    result_list = []
    for line in result:
        list_line = line[0].split(',')  # ['Steve Carell', ' Anne Hathaway', ' Dwayne Johnson', ' Alan Arkin', ' Terence Stamp', ' Terry Crews', ' David Koechner', ' James Caan', ' Masi Oka', ' Nate Torrence', ' Bill Murray']
        result_list += list_line
    counter = Counter(result_list)  # Counter({'Steve Carell': 1, ' Anne Hathaway': 1, ' Dwayne Johnson': 1, ' Alan Arkin': 1, ' Terence Stamp': 1, ' Terry Crews': 1, ' David Koechner': 1, ' James Caan': 1, ' Masi Oka': 1, ' Nate Torrence': 1, ' Bill Murray': 1, 'Dwayne Johnson': 1, ' AnnaSophia Robb': 1, ' Alexander Ludwig': 1, ' Carla Gugino': 1, ' Ciarán Hinds': 1, ' Tom Everett Scott': 1, ' Chris Marquette': 1, ' Billy Brown': 1, ' Christine Lakin': 1, ' Tom Woodruff Jr.': 1, ' John Kassir': 1, ' Garry Marshall': 1, ' John Duff': 1, ' Ted Hartley': 1, ' Dave Engfer': 1, ' Bob Clendenin': 1, ' Shengyi Huang': 1, ' Robert Torti': 1, ' Kim Richards': 1, ' Brandon Miller': 1, ' Paul Darnell': 1, ' Omar Dorsey': 1, ' Dennis Hayden': 1, ' Suzanne Krull': 1, ' Steve Rosenbaum': 1, ' Andrew Shaifer': 1, ' Bryan Fogel': 1, ' Bob Koherr': 1, ' Sam Wolfson': 1, ' Beth Kennedy': 1, ' Corri English': 1, ' Jonathan Slavin': 1, ' Kevin Christy': 1, ' Meredith Salenger': 1})
    actors_list = []
    for key, value in counter.items():
        if value > 2 and key.strip() not in [actor_1, actor_2]:
            actors_list.append(key)
    return actors_list


print(search_actors('Jack Black', 'Dustin Hoffman'))


def list_movies(type, release_year, listed_in):
    response = []
    sqlite_query = f"""
    select title, description from netflix
    where type like '%{type}%'
    and release_year = '{release_year}'
    and listed_in like '%{listed_in}%' """
    result = get_db('netflix.db', sqlite_query)
    for line in result:
        line_dict = {
            "title": line[0],
            "description": line[1],
        }
        response.append(line_dict)
    return response



print(list_movies('Movie', 1984, 'Dramas'))
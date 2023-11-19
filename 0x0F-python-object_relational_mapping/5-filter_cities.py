#!/usr/bin/python3
"""takes name of state as argument and lists
all cities of that state"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    host = 'localhost'
    port = 3306
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host=host, port=port, user=username,
                         passwd=password, db=dbname)

    cur = db.cursor()
    query = "SELECT cities.name\
        FROM cities LEFT OUTER JOIN states ON\
        states.id = cities.state_id\
        WHERE states.name = %s\
        ORDER by cities.id ASC"
    cur.execute(query, (state,))
    rows = cur.fetchall()
    cities_list = ', '.join(row[0] for row in rows)
    print(cities_list)
    cur.close()
    db.close()

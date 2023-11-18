#!/usr/bin/python3
"""displays states according to the user input
while protecting against sql injection"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    host = 'localhost'
    port = 3306
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(host=host, port=port, user=username,
                         passwd=password, db=dbname)

    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name\
        FROM cities LEFT OUTER JOIN states ON\
        states.id = cities.state_id\
        ORDER by cities.id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

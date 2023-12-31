#!/usr/bin/python3
"""displays states according to the user input"""


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
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}'\
        ORDER by states.id ASC".format(state)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

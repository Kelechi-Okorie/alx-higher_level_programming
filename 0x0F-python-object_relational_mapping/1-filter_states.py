#!/usr/bin/python3
"""lists all states starting with letter N from db hbtn_0e_0_usa"""


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

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cur = db.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

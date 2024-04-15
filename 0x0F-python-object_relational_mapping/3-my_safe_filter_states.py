#!/usr/bin/python3
"""
Script takes arguments and displays all values in
table  where name matches the argument, safe from MySQL
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY states.id ASC", (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

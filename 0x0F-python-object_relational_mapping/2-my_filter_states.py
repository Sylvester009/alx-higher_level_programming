#!/usr/bin/python3
"""
Script takes  argument and displays all values in
table where name matches the argument
"""

if __name__ == '__main__':

    import MySQLdb
    import sys
    db = MySQLdb.connect(host='localhost', port=3306,
                         username=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                ORDER BY states.id ASC".format(sys.argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

#!/usr/bin/python3
""" takes name of a state as an argument and lists all cities"""

import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8")

    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities \
                    INNER JOIN states ON \
                    cities.state_id=states.id \
                    WHERE states.name=%s", (sys.argv[4],))
    row = cursor.fetchall()
    print(", ".join(city[0] for city in rows))

    cur.close()
    db.close()

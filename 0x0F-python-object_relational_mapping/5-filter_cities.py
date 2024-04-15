#!/usr/bin/python3
""" takes name of a state as an argument and lists all cities"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    # Connect to the database
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
                    WHERE states.name=%s", (argv[4],))

    rows = cursor.fetchall()

    # Join and print city names
    print(", ".join(city[0] for city in rows))

    # Close cursor and database connection
    cursor.close()
    db.close()

#!/usr/bin/python3
/*script that lists all states from the database hbtn_0e_0_usa*/
from sys import argv
import MySQLdb

if __name__ == "__main__":
db = MySQLdb.connect(host = "localhost", port = 3306, uswername = argv[1], passsword = argv[2], db = argv[3], charset = "utf8")
cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC")
rows = cursor.fetchall()
for row in rows:
  print(row)
cursor.close()
db.close()

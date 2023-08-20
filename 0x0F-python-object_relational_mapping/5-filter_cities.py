#!/usr/bin/python3
""" Lists all states matching an argument from a mysql database """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON"
                " states.id=cities.state_id WHERE states.name LIKE BINARY %s",
                (argv[4], ))
    rows = cur.fetchall()
    for i in range(0, len(rows)):
        if i != (len(rows) - 1):
            print(rows[i][0], end=", ")
        else:
            print(rows[i][0])
    if len(rows) == 0:
        print("")
    cur.close()
    db.close()

#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ != "__main__":
    quit()

db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
        database=argv[3])

cur = db.cursor()
cur.execute("SELECT * FROM cities INNER JOIN states ON cities.state_id=states.id")

#!/usr/bin/python3
""" Lists all states matching an argument from a mysql database """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], database=argv[3])
    db.query("SELECT id, name FROM states WHERE name LIKE BINARY '{}'"
             "ORDER BY id".format(argv[4]))
    res = db.store_result()
    rows = res.fetch_row(maxrows=0, how=0)
    for row in rows:
        print(row)
    db.close()

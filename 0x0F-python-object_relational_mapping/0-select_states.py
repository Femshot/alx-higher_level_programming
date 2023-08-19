#!/usr/bin/python3
"""Lists all states from a mysql database passed as an argument"""
import MySQLdb
from sys import argv


db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                     password=argv[2], database=argv[3])
db.query("SELECT id, name FROM states ORDER BY id")
res = db.store_result()
rows = res.fetch_row(maxrows=0, how=0)
for row in rows:
    print(row)

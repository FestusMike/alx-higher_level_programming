#!/usr/bin/python3
"""
4-cities_by_state: lists all cities in database table
"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
      host="localhost",
      user=sys.argv[1],
      passwd=sys.argv[2],
      database=sys.argv[3],
      port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
        LEFT JOIN states ON cities.state_id = states.id ORDER BY cities.id")
    results = cur.fetchall()
    for result in results:
        print(result)
    cur.close()

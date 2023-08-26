#!/usr/bin/python3
"""
5-filter_cities: safely select cities of states matching argument
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
    cur.execute("SELECT * FROM cities RIGHT JOIN states ON cities.state_id =\
        states.id WHERE states.name = '{}'".format(sys.argv[4]))
    results = cur.fetchall()
    print(", ".join([result[2] for result in results]))
    cur.close()

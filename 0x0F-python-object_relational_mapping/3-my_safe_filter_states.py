#!/usr/bin/python3
"""
3-my_safe_filter_states: safely select states matching argument
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
    cur.execute("SELECT * FROM states WHERE name LIKE \
        %s ORDER BY id", sys.argv[4])
    results = cur.fetchall()
    for result in results:
        print(result)
    cur.close()

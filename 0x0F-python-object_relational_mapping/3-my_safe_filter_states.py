#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the argument (safe from MySQL injection).
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("Need 4 arguments!")

    myDataBase = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = myDataBase.cursor()

    state_name = sys.argv[4]

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id"
    cursor.execute(query, (state_name,))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    myDataBase.close()

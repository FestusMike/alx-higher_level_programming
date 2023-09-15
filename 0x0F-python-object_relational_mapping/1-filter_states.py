#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise Exception("Need 3 arguments!")

    myDataBase = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = myDataBase.cursor()

    # Modify the query to filter states with names starting with "N"
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

    for row in cursor.fetchall():
        if row[1][0] == 'N':
            print(row)

    cursor.close()
    myDataBase.close()

#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
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
        db=sys.argv[3]  # Changed myDataBase to db
    )

    cursor = myDataBase.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    myDataBase.close()

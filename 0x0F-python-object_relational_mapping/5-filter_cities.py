#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
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

    # Use execute() once to fetch all cities of the given state
    query = "SELECT cities.name FROM states \
             JOIN cities ON states.id = cities.state_id \
             WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))

    cities = cursor.fetchall()
    cities_list = [city[0] for city in cities]
    cities_string = ", ".join(cities_list)
    print(cities_string)

    cursor.close()
    myDataBase.close()

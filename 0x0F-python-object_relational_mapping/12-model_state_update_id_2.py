#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise Exception("Need 3 arguments!")

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    # Create an engine
    URL = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(URL.format(user, passwd, db))

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get the State object with id = 2
    state_to_update = session.query(State).get(2)

    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
    else:
        print("State not found")

    # Close the session
    session.close()

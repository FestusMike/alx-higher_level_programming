#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
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

    # Get the State objects with names containing the letter 'a'
    states_to_delete = session.query(State)\
        .filter(State.name.like('%a%')).all()

    if states_to_delete:
        for state in states_to_delete:
            session.delete(state)
        session.commit()
    else:
        print("No states with 'a' in their names found")

    # Close the session
    session.close()

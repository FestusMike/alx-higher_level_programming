#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    if len(sys.argv) != 5:
        raise Exception("Need 4 arguments!")

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    search_name = sys.argv[4]

    # Create an engine
    URL = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(URL.format(user, passwd, db))

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == search_name)\
        .order_by(State.id)
    if states is not None and states.count() > 0:
        for state in states:
            print('{}'.format(state.id))
    else:
        print('Not found')

    # Close the session
    session.close()

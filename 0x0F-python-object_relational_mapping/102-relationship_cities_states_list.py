#!/usr/bin/python3
""" lists all City objects from the database hbtn_0e_101_usa """

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise Exception("Need 3 arguments!")

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    URL = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(URL.format(user, passwd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    for state in session.query(State).order_by(State.id).all():
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))

    session.close()

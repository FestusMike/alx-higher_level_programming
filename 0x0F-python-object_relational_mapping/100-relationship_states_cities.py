#!/usr/bin/python3
""" Start link class to table in database. """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    URL = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(URL.format(user, passwd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)  # Establish the relationship
    session.add(new_state)
    session.commit()

    session.close()

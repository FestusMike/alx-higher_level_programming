#!/usr/bin/python3
"""
7-model_state_fetch_all: lists all State objects from database
"""


from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    for result in session.query(State):
        print("{}: {}".format(result.id, result.name))

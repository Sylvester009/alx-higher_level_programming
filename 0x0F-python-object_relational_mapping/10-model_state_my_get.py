#!/usr/bin/python3
"""
prints the State object with the name
passed as argument from the database
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python script.py <username> <password>"
              "<database_name> <state_name>")
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create the database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session
    session = Session(engine)
    state = session.query(State).filter(State.name == sys.argv[4]).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()

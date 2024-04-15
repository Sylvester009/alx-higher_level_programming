#!/usr/bin/python3
"""
lists all State objects that contain the letter a from the database
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    
    # Create a session to interact with the database
    session = Session(engine)
    for state in session.query(State)\
                        .filter(State.name.like('%a%'))\
                        .order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()

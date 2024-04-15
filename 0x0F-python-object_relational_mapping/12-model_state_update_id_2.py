#!/usr/bin/python3
"""
changes the name of a State object from the database
"""

if __name__ == '__main__':
    from sys import argv, exit
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                           '{}'.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    session = Session(engine)
    Base.metadata.create_all(engine)

    stateUpdate = session.query(State).filter_by(id=2).first()
    if stateUpdate:
        stateUpdate.name = 'New Mexico'
    session.commit()
    session.close()

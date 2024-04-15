#!/usr/bin/python3
"""
lists all State objects from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: {} <username> <password> <dbname>"
              .format(sys.argv[0]))
        sys.exit(1)

    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}',
        pool_pre_ping=True)

    with Session(engine) as session:
        for state in session.query(State).order_by(State.id).all():
            print(f"{state.id}: {state.name}")

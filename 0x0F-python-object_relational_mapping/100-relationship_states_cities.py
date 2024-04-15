#!/usr/bin/python3
"""
Script that creates the State “California” with the City
“San Francisco” from the database
"""

if __name__ == '__main__':

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from relationship_state import Base, State
    from relationship_city import City

    # Ensure command-line arguments are sufficient
    if len(argv) < 4:
        print("Usage: {} <user> <pass> <dbname>".format(argv[0]))
        exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1],argv[2], argv[3]),
                           echo=True, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)

    session.add(new_state)
    session.commit()
    session.close()

#!/usr/bin/python3
"""
script that creates the State “California” with the City
“San Francisco” from the database
"""

if __name__ == '__main__':

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from relationship_state import Base, State
    from relationship_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                           '{}'.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    session = Session(engine)
    Base.metadata.create_all(engine)

    new_state = State(name='California')
    new_state2 = City(name='San Francisco', state_id=new_state.id)
    new_state.cities.append(new_state2)
    session.add_all([new_state, new_state2])
    session.commit()
    session.close()

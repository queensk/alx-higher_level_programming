#!/usr/bin/python3
"""
script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa:
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    """
    connect to database and transact
    """
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name='California')
    city = City(name='San Francisco')
    state.cities.append(city)

    session.add(state)
    session.commit()
    session.close()

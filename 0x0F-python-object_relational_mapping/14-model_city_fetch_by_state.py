#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

import sqlalchemy
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    Session.configure(bind=eng)
    session = Session()
    values = session.query(State, City).filter(City.state_id == State.id).\
             order_by(City.id)
    for state, city in values:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()

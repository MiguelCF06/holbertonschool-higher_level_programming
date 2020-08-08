#!/usr/bin/python3
"""
script that deletes all State objects with a name containing the letter a from
the database hbtn_0e_6_usa
"""

import sqlalchemy
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    Session.configure(bind=eng)
    session = Session()
    session.query(State).filter(State.name.like('%a%')).\
        delete(synchronize_session='fetch')
    session.commit()
    session.close()

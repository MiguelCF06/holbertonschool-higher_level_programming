#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa
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
    update_user = session.query(State).filter_by(id=2).first()
    update_user.name = "New Mexico"
    session.commit()
    session.close()

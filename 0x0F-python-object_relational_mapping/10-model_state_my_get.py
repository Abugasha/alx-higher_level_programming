#!/usr/bin/python3
"""
This file prints all states from the database
"""

import sys
import sqlalchemy
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    This file use a mysql search from python
    """
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(db_user, db_password,
                                   db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = None
    for state in session.query(State).filter(State.name.like(state_name)):
        print("{}".format(state.id))
    if (not state):
        print("Not found")
    session.close()

if __name__ == '__main__':
    main()

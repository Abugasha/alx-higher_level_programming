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

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(db_user, db_password,
                                   db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).filter(
                    State.name.like("%a%")):
        print("{}: {}".format(state.id, state.name))
    session.close()

if __name__ == '__main__':
    main()

#!/usr/bin/python3
"""
Deletes all State objects with the letter 'a' in their names.
Usage: ./13-model_state_delete_a.py <username> <password> <database_name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <username> <password> <database_name>")
        exit()

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        session.delete(state)

    session.commit()

    session.close()

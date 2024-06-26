#!/usr/bin/python3
"""This script prints the first State object
    from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    state_name = argv[4]
    connection = 'mysql://{}:{}@localhost:3306/{}'.format(username,
                                                          password,
                                                          dbname)
    engine = create_engine(connection)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State) \
                   .filter(State.name == state_name) \
                   .order_by(State.id) \
                   .one_or_none()
    if state:
        print('{}'.format(state.id))
    else:
        print('Not found')
    session.close()

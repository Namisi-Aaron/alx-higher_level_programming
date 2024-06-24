#!/usr/bin/python3
"""This script lists all State objects
    that contain the letter a
    from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    connection = 'mysql://{}:{}@localhost:3306/{}'.format(username,
                                                          password,
                                                          dbname)
    engine = create_engine(connection)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State) \
                    .filter(State.name.like('%a%')) \
                    .order_by(State.id).all()
    for s in states:
        print('{}: {}'.format(s.id, s.name))
    session.close()

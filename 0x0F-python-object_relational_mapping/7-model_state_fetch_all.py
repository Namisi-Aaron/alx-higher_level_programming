#!/usr/bin/python3
"""This module contains the class definition of State"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

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

states = session.query(State).order_by(State.id).all()
for s in states:
    print('{}: {}'.format(s.id, s.name))
session.close()

#!/usr/bin/python3
"""This module contains the class definition of State"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class State(Base):
    """This is the class State definition"""

    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement=True,
                primary_key=True,
                nullable=False)

    name = Column(String(128), nullable=False)

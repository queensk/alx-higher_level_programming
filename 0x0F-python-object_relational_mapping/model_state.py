#!/usr/bin/python3
"""
contains the class definition of a,
State and an instance Base = declarative_base():
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    state definition
    Attributes:
        __tablename__: str name of the table
        id: State Id
        name: str name of the state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

#!/usr/bin/python3
"""
contains the class definition of a,
State and an instance Base = declarative_base():
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
    City definition
    Attributes:
        __tablename__: str name of the table
        id: City Id
        name: str name of the City
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

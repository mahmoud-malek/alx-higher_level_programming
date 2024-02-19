#!/usr/bin/python3

""" a mudule that contains the class definition of a City """

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):

    """ This is a city class """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

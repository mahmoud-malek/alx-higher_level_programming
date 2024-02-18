#!/usr/bin/python3

""" a mudule that contains the class definition of a City """

from model_state import Base, Column, Integer, String, State
from sqlalchemy import ForeignKey


class City(Base):
    """ This is city class """

    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, nullable=False,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)

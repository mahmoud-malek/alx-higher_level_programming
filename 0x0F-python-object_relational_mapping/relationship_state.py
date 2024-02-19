#!/usr/bin/python3
""" a python file that contains the class definition
 of a State and an instance Base = declarative_base(): """

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

data = MetaData()
Base = declarative_base(metadata=data)


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

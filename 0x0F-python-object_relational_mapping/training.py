#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickkname = Column(String)

    def __reper__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)

    def __init__(self, name, fullname, nickname):
        self.name = name
        self.fullname = fullname
        self.nickname = nickname


user1 = User("ed", "Ed Jones", "eddie")
user2 = User("wendy", "Wendy Williams", "windy")
user3 = User("mary", "Mary Contrary", "mary")

print(user1.fullname)

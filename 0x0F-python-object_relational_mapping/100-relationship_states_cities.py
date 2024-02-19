#!/usr/bin/python3

""" a script that creates the State “California”
 with the City “San Francisco” from the database hbtn_0e_100_usa """

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    if len(argv) == 4:
        usrname, passwd, db_name = argv[1], argv[2], argv[3]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(usrname, passwd, db_name),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        new_state = State(name="California")
        new_city = City(name="San Francisco", state=new_state)
        new_state.cities.append(new_city)

        session.add(new_state)
        session.add(new_city)
        session.commit()
        session.close()
    else:
        print("Usage: {} username password database".format(argv[0]))

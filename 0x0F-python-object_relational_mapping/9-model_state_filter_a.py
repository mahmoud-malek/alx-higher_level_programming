#!/usr/bin/python3

""" a script that lists all State objects that
 contain the letter a from the database hbtn_0e_6_usa """


if __name__ == "__main__":

    from sqlalchemy import create_engine
    from model_state import Base, State
    from sys import argv
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Sesssion = sessionmaker(bind=engine)
    session = Sesssion()

    for state in session.query(State).order_by(State.id).filter(
            State.name.like('%a%')):
        print("{}: {}".format(state.id, state.name))

    session.close()

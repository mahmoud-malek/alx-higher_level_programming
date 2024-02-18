#!/usr/bin/python3

"""  a script that prints the State object with the name passed
 as argument from the database hbtn_0e_6_usa"""


if __name__ == "__main__":

    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # create the connection to the database
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    target = argv[4]
    port = 3306

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:{}/{}".format(
        username, password, port, db_name))
    Base.metadata.create_all(engine)

    # create the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query the database
    state = session.query(State).filter(State.name == target)
    print(state[0].id if state.first() else "Not found")

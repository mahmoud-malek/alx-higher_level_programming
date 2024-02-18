#!/usr/bin/python3

""" a script that adds the State object
 “Louisiana” to the database hbtn_0e_6_usa"""


if __name__ == "__main__":

    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # create the connection to the database
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    port = 3306

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:{}/{}".format(
        username, password, port, db_name))

    Base.metadata.create_all(engine)

    # create the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query the database
    session.add(State(name="Louisiana"))
    session.commit()
    print(session.query(State).filter(State.name == "Louisiana").first().id)
    session.close()

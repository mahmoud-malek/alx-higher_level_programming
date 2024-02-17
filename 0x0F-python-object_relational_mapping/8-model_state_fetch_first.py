#!/usr/bin/python3

""" a script that prints the first State object
 from the database hbtn_0e_6_usa """


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    port = 3306

    connect = "mysql+mysqldb://{}:{}@localhost:{}/{}".format(
        username, password, port, db_name)
    engine = create_engine(connect)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    running = Session()

    first = running.query(State)[0]
    print(f"{first.id}: {first.name}")

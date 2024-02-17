#!/usr/bin/python3

"""" a script that lists all State objects from the
database hbtn_0e_6_usa """


if __name__ == "__main__":
    from model_state import State, Base
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, db_name))

    Base.metadata.create_all(engine)

    Sesstion = sessionmaker(bind=engine)
    session = Sesstion()

    for s in session.query(State).order_by(State.id):
        print(f"{s.id}: {s.name}")

    session.close()

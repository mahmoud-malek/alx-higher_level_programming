#!/usr/bin/python3

""" a script 14-model_city_fetch_by_state.py
 that prints all City objects from the database hbtn_0e_14_usa: """


if __name__ == "__main__":
    from model_city import City
    from model_state import State, Base

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    port = 3306

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
        username, password, port, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    for (city, state) in session.query(City, State).join(State) \
        .order_by(City.id).filter(City.state_id == State.id)\
            .order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
    engine.dispose()

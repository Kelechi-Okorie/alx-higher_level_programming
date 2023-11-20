#!/usr/bin/python3
"""prints all City objects from the hbtn_0e_14_usa db"""


if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from model_city import City

    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    con_string = f'mysql+mysqldb://{username}:{password}@localhost/{db}'
    engine = create_engine(con_string)
    Base.metadata.create_all(engine)

    session = Session(engine)
    query = session.query(State, City).filter(State.id == City.state_id)\
        .order_by(City.id).all()
    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()

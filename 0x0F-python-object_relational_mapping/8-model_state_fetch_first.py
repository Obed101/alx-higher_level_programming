#!/usr/bin/python3
"""
This module uses sqlalchemy to print table
"""
import sys
import MySQLdb as sql
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker


if __name__ = '__main__':
    """Making it unexecuted on import"""
    host = "localhost"
    port = 3306
    username = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
        username, passwd, host, port, database),
                           pool_pre_ping=True, poolclass=NullPool)
    Session = sessionmaker(bind=engine)
    new_session = Session()
    states = new_session.query(State).order_by(State.id).first()
    new_session.close()
    if states:
        first1 = states.id + ": " + states.name
    else:
        first1 = "Nothing"
    print(first1)

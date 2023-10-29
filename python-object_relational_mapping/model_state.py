"""
State class represents a table in the database called 'states'.

Attributes:
    id (Column): Primary key column of type Integer with auto-increment and non-null constraints.
    name (Column): Column of type String with a length of 128 characters and non-null constraint.

Methods:
    __init__(self, name): Initializes a State object with a given name.

"""
#!/usr/bin/python3
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    __tablename__: Defines the name of the table in the db

    __init__: initializes the State object

    name(string(128)): a column name in the db
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    from sqlalchemy import create_engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

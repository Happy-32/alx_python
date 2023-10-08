from sqlalchemy import create_engine, Column, Integer, String
import sys
from sqlalchemy.orm import declarative_base

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Please provide 3 arguments: MySQL username, MySQL password, database name")
        sys.exit(1)
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

path = "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, database)

database = create_engine(path)
Connection = database.connect()

Base = declarative_base()

"""
State defines a state class used to create a states table in
the database
"""

class State(Base):

    """
    __tablename__: Defines the name of the table in the db

    __init__: initializes the State object

    name(string(128)): a column name in the db
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name
Base.metadata.create_all(bind=database)
# State("Arizona")
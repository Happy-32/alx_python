"""
This script demonstrates how to interact with a MySQL database using SQLAlchemy.

The script expects three command-line arguments: MySQL username, MySQL password, and database name.

Usage: python script.py <username> <password> <database>

"""
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
State class represents a table in the database called 'states'.

Attributes:
    id (Column): Primary key column of type Integer with auto-increment and non-null constraints.
    name (Column): Column of type String with a length of 128 characters and non-null constraint.

Methods:
    __init__(self, name): Initializes a State object with a given name.

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







import sys
import MySQLdb

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 5:
        print("Please provide 4 arguments: MySQL username, MySQL password, database name, and state")
        sys.exit(1)

    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]


    # print("{}, {}, {}".format(username,password,database))

    def select_state(username, password, database, state):
        database = MySQLdb.connect(host="localhost", port=3306,
                                   user=username, passwd=password, db=database)
        cursor = database.cursor()
        
        query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """

        cursor.execute(query, (state,))
        rows = cursor.fetchall()

        city_names = set(row[0] for row in rows)
        city_names_str = ', '.join(city_names)
        print(city_names_str)

        # city_names = ', '.join(row[0] for row in rows)
        # print(city_names)
        
        # for row in rows:
            # print(row[0])

        cursor.close()
        database.close()

    
    select_state(username, password, database, state)
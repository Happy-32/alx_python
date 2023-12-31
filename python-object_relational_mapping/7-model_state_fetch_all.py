import sys
from sqlalchemy import create_engine
from model_state import Base, State
if len(sys.argv) != 4:
    print("Insufficient number of arguments, please provide 'username', 'password' and 'database name' to procede")
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
port = 3306

path = "mysql+mysqldb://{}:{}@localhost:{}/{}".format(username, password, port, database)
database = create_engine(path)
Base.metadata.bind = database
# Base.metadata.create_all(bind=database)
connection = database.connect()

states = connection.execute(State.__table__.select().order_by(State.id))

for state in states:
    print("{}: {}".format(state.id, state.name))

connection.close()


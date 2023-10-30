import sys
from sqlalchemy import create_engine, select
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

state = connection.execute(select(State).order_by(State.id)).fetchone()

if state:
    print("{}: {}".format(state.id, state.name))
else:
    print("Nothing")
print(end="")

connection.close()


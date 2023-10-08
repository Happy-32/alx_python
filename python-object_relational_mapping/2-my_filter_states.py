import sys
import MySQLdb

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 5:
        print("Please provide 4 arguments: MySQL username, MySQL password, database name and state")
        sys.exit(1)

    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]


    def select_state(username, password, database, state):
        # print("{}, {}, {}, {}".format(username,password,database, state))
        
        database = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = database.cursor()
        cursor.execute("SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC", (state,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        database.close()


    select_state(username, password, database, state)
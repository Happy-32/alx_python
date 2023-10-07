import sys
import MySQLdb

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Please provide 3 arguments: MySQL username, MySQL password, database name, and state")
        sys.exit(1)

    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # print("{}, {}, {}".format(username,password,database))

    def select_state(username, password, database):
        database = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = database.cursor()
        query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        database.close()

    
    select_state(username, password, database)
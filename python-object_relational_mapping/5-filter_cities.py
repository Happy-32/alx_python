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

    def alphanumeric_sort(s):
        return ''.join(c for c in s if c.isalnum())
    
    def select_state(username, password, database, state):
        database = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
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

        city_names = [row[0] for row in rows]
        print(*city_names, sep=", ")

        cursor.close()
        database.close()

    
    select_state(username, password, database, state)
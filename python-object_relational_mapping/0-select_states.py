import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Please provide all 3 arguments: MySQL username, MySQL password, and database name")
        sys.exit(1)

    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # print("{}, {}, {}".format(username,password,database))

    def select_state(username, password, database):
        database = MySQLdb.connect(host="localhost",port=3306, user=username, passwd=password, db=database)
        cursor = database.cursor()
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        database.close()

    
    select_state(username, password, database)
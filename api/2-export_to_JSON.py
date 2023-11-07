"""
This module exports the response to a json file
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("Enter an id")
        sys.exit(1)

    try:
        employeeId = int(sys.argv[1])
    except ValueError:
        print("emplpyee id must be an integer")
        sys.exit(1)


def employeeID(employeeId):

    todoItemsUrl = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    employeeUrl = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

    todoResponse = requests.get(todoItemsUrl)
    employeeResponse = requests.get(employeeUrl)
    todo = todoResponse.json()
    employee = employeeResponse.json()

    employeeId = employee.get('id')
    employeeName = employee.get('username')


    employee_json_data = {
        "USER_ID": {
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": employeeName
            }
            for task in todo
        }
    }

    # Write JSON data to a file
    json_filename = f'{employeeId}.json'
    with open(json_filename, 'w') as json_file:
        json.dump(employee_json_data, json_file, indent=4)

employeeID(id)


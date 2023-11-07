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
        id = int(sys.argv[1])
    except ValueError:
        print("emplpyee id must be an integer")
        sys.exit(1)

todoItemsUrl = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
employeeUrl = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

todoResponse = requests.get(todoItemsUrl)
employeeResponse = requests.get(employeeUrl)
todo = todoResponse.json()
employee = employeeResponse.json()

employeeId = employee.get('id')
employeeName = employee.get('username')

tasks = []

# Create a dictionary for each task
for task in todo:
    taskId = task['id']
    taskTitle = task['title']
    taskCompleted = task['completed']
    
    taskDict = {
        'task': taskTitle,
        'completed': taskCompleted,
        'username': employeeName
    }
    
    tasks.append(taskDict)

# Create a dictionary for the employee's tasks
employeeTasks = {
    'USER_ID': tasks
}

# Create a JSON file with the employee ID as the filename
filename = '{}.json'.format(employeeId)

# Write the employee tasks dictionary to a JSON file
with open(filename, 'w') as jsonfile:
    json.dump(employeeTasks, jsonfile)


import csv
import json
import requests
import sys

id = sys.argv[1]

def getTodo(id):
    todoItemsUrl = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    employeeUrl = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

    todoResponse = requests.get(todoItemsUrl)
    employeeResponse = requests.get(employeeUrl)
    todo = todoResponse.json()
    employee = employeeResponse.json()
    employeeName = employee['username']
    totalTasks = len(todo)

    csv_filename = "{}.csv".format(id)

    with open(csv_filename, mode="w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo:
            tasks_completed = "Completed" if task["completed"] else "Not Completed"
            csv_writer.writerow([id, employeeName, tasks_completed, task["title"]])

    with open(csv_filename, 'r') as f:
        pass

getTodo(id)

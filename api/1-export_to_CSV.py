import csv
import json
import requests
import sys

id = sys.argv[1]



def csvExport(id):
    todoItemsUrl = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    employeeUrl = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

    todoResponse = requests.get(todoItemsUrl)
    employeeResponse = requests.get(employeeUrl)
    todo = todoResponse.json()
    employee = employeeResponse.json()

    employeeId = employee.get('id')
    employeeID = f"{employeeId}"
    employeeName = employee.get("username", "unknown employee")
    employeename = f"{employeeName}"


    filename = '{}.csv'.format(employeeId)

    # Open the CSV file in write mode
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        
        
        # Write each task as a row in the CSV file
        for task in todo:
            taskId = task['id']
            taskTitle = task['title']
            taskCompleted = str(task['completed'])
            writer.writerow([id, employeename, taskCompleted, taskTitle])

    print("Data exported to {}".format(filename))

csvExport(id)

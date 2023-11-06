import csv
import json
import requests
import sys

id = sys.argv[1]

todoItemsUrl = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
employeeUrl = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

todoResponse = requests.get(todoItemsUrl)
employeeResponse = requests.get(employeeUrl)
todo = todoResponse.json()
employee = employeeResponse.json()

employeeId = employee['id']
employeeName = employee['username']

# Create a CSV file with the employee ID as the filename
filename = '{}.csv'.format(employeeId)

# Open the CSV file in write mode
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the header row
    writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
    
    # Write each task as a row in the CSV file
    for task in todo:
        taskId = task['id']
        taskTitle = task['title']
        taskCompleted = task['completed']
        
        # Write the task details as a row in the CSV file
        writer.writerow([employeeId, employeeName, taskCompleted, taskTitle])
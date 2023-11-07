import json
import requests

# API endpoint URLs
todoItemsUrl = 'https://jsonplaceholder.typicode.com/todos'
employeeUrl = 'https://jsonplaceholder.typicode.com/users'

# Retrieve tasks and employee data from the API
todoResponse = requests.get(todoItemsUrl)
employeeResponse = requests.get(employeeUrl)
todos = todoResponse.json()
employees = employeeResponse.json()

# Create a dictionary to store tasks for each employee
tasks = {}

# Iterate over each employee
for employee in employees:
    employeeId = employee['id']
    # employeeName = employee['name']
    userName = employee['username']
    
    # Filter tasks for the current employee
    employeeTasks = [task for task in todos if task['userId'] == employeeId]
    
    taskList = []
    # Iterate over each task for the current employee
    for task in employeeTasks:
        taskId = task['id']
        taskTitle = task['title']
        taskCompleted = task['completed']
        
        # Create a dictionary for each task
        taskDict = {
            'username': userName,
            'task': taskTitle,
            'completed': taskCompleted
        }
        
        # Add the task dictionary to the taskList
        taskList.append(taskDict)
    
    # Add the taskList to the tasks dictionary, using the employeeId as the key
    tasks[employeeId] = taskList

# Create a dictionary to store tasks for all employees
allEmployeeTasks = tasks

# Specify the filename for the JSON output
filename = 'todo_all_employees.json'

# Write the allEmployeeTasks dictionary to a JSON file
with open(filename, 'w') as jsonfile:
    json.dump(allEmployeeTasks, jsonfile)

# Print a message indicating the location of the exported JSON file
print("Data exported to {}".format(filename))

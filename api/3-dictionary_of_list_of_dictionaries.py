import json
import requests

todoItemsUrl = 'https://jsonplaceholder.typicode.com/todos'
employeeUrl = 'https://jsonplaceholder.typicode.com/users'

todoResponse = requests.get(todoItemsUrl)
employeeResponse = requests.get(employeeUrl)
todos = todoResponse.json()
employees = employeeResponse.json()

tasks = {}

# Create a dictionary of tasks for each employee
for employee in employees:
    employeeId = employees.get('id')
    employeeName = employees.get('username')
    
    # Filter tasks for the current employee
    employeeTasks = [task for task in todos if task['userId'] == employeeId]
    
    taskList = []
    for task in employeeTasks:
        taskId = task['id']
        taskTitle = task['title']
        taskCompleted = task['completed']
        
        taskDict = {
            'username': employeeName,
            'task': taskTitle,
            'completed': taskCompleted
        }
        
        taskList.append(taskDict)
    
    tasks[employeeId] = taskList

# Create a dictionary for all employees' tasks
allEmployeeTasks = {
    'tasks': tasks
}

# Create a JSON file named "todo_all_employees.json"
filename = 'todo_all_employees.json'

# Write the allEmployeeTasks dictionary to a JSON file
with open(filename, 'w') as jsonfile:
    json.dump(allEmployeeTasks, jsonfile)

print("Data exported to {}".format(filename))

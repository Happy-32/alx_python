import json
import requests

# API endpoint URLs
todoItemsUrl = 'https://jsonplaceholder.typicode.com/todos'
employeeUrl = 'https://jsonplaceholder.typicode.com/users'

todoResponse = requests.get(todoItemsUrl)
employeeResponse = requests.get(employeeUrl)
todos = todoResponse.json()
employees = employeeResponse.json()

tasks = {}

for employee in employees:
    employeeId = employee['id']
    userName = employee['username']
    
    employeeTasks = [task for task in todos if task['userId'] == employeeId]
    
    taskList = []
    for task in employeeTasks:
        taskId = task['id']
        taskTitle = task['title']
        taskCompleted = task['completed']
        
        taskDict = {
            'username': userName,
            'task': taskTitle,
            'completed': taskCompleted
        }
        
        taskList.append(taskDict)
    
    tasks[employeeId] = taskList

allEmployeeTasks = tasks

filename = 'todo_all_employees.json'

with open(filename, 'w') as jsonfile:
    json.dump(allEmployeeTasks, jsonfile)

print("Data exported to {}".format(filename))

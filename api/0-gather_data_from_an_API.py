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

employeeName = employee['name']
totalTasks = len(todo)
taskCompleted = sum(1 for i in todo if i['completed'])

print('Emplyee {} is done with tasks ({}/{}):'.format(employeeName, taskCompleted, totalTasks))
for i in todo:
    if i['completed']:
        print('\t',i['title'])


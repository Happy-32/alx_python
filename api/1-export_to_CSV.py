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
    taskCompleted = sum(1 for i in todo if i['completed'])

    csvFile = []
    csvFile.append(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
    for i in todo:
        csvFile.append([id,employeeName, str(i['completed']), i['title']])
    

    with open('USER_ID.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csvFile)


    # print('Emplyee {} is done with tasks ({}/{})'.format(employeeName, taskCompleted, totalTasks))
    # for i in todo:
    #     if i['completed']:
    #         print('\t',i['title'])

getTodo(id)


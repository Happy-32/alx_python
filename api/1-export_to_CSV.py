import csv
import requests
import sys

if len(sys.argv) != 2:
    sys.exit(1)

id = sys.argv[1]


def getTodo(id):
    employeeURL = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todoURL = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    employeeResponse = requests.get(employeeURL)
    todoResponse = requests.get(todoURL)
    employee = employeeResponse.json()
    todo = todoResponse.json()

    username = employee['username']

    csv_filename = "{}.csv".format(id)

    with open(csv_filename, "w", newline="") as file:
        csv_writer = csv.writer(file)

        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo:
            task_completed_status = "Completed" if task["completed"] else "Not Completed"
            # csv_writer.writerow([id, username, task_completed_status, task["title"]])
            # csv_writer.writerow('"' + str(task['userId']) + '","' + employee[0]['username'] + '","' + str(task['completed']) + '","' + task['title'] + '"')
            # csv_writer.writerow([task['userId'], username, task_completed_status, task['title']])
            csv_writer.writerow(['"' + str(task['userId']) + '"', '"' + username + '"', '"' + task_completed_status + '"', '"' + task['title'] + '"'])


getTodo(id)
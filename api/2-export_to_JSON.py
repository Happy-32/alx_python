"""
This module exports data in the JSON format.
"""

import json
import requests
import sys

def get_employee_info(employee_id):
    # Define the API endpoints
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Fetch employee information
    user_response = requests.get(user_url)
    user_data = user_response.json()

    if 'id' not in user_data:
        print(f"USER_ID {employee_id} is not valid.")
        return

    employee_id = user_data.get('id')
    employee_name = user_data.get('username')

    # Fetch employee's TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Create a JSON data structure
    employee_json_data = {
        "USER_ID": [
            {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": employee_name
            }
            for todo in todos_data
        ]
    }

    # Write JSON data to a file
    json_filename = f'{employee_id}.json'
    with open(json_filename, 'w') as json_file:
        json.dump(employee_json_data, json_file, indent=4)

    print(f"Data has been exported to {json_filename}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_info(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
#!/usr/bin/python3
""" 2. Fetch employee ID and output info as JSON file. """

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_info = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    user_todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id))

    user_data = user_info.json()
    todos_data = user_todos.json()

    task_list = []
    for task in todos_data:
        task_dict = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user_data.get('username')
        }
        task_list.append(task_dict)

    user_tasks = {user_id: task_list}

    with open('{}.json'.format(user_id), 'w') as json_file:
        json.dump(user_tasks, json_file)

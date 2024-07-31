#!/usr/bin/python3
""" 0. Fetch employee ID and output their todo list via API. """

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_info = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    user_todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id))

    user_data = user_info.json()
    todos_data = user_todos.json()

    user_name = user_data.get('name')
    total_tasks = len(todos_data)

    completed_tasks = 0
    for todo in todos_data:
        if todo.get('completed'):
            completed_tasks += 1

    print('Employee {} is done with tasks({}/{}):'.format(user_name, completed_tasks, total_tasks))
    for todo in todos_data:
        if todo.get('completed'):
            print("\t {}".format(todo.get('title')))

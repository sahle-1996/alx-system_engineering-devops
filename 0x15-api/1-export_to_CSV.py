#!/usr/bin/python3
""" 1. Fetch employee ID and output info to CSV file. """

import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_info = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    user_todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id))

    user_data = user_info.json()
    todos_data = user_todos.json()

    username = user_data.get('username')

    with open('{}.csv'.format(user_id), 'w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([user_id, username, task.get('completed'), task.get('title')])

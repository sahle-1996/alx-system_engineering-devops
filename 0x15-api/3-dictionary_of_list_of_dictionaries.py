#!/usr/bin/python3
""" 3. Fetch data for all users and output to JSON file. """

import json
import requests

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    all_users_data = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos', params={'userId': user_id}).json()
        
        tasks = []
        for todo in todos:
            task_dict = {
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": username
            }
            tasks.append(task_dict)
        
        all_users_data[user_id] = tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_users_data, json_file)

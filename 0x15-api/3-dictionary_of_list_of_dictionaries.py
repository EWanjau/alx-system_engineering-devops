#!/usr/bin/python3
"""this module gets data from REST API and represents it in JSON
"""


import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    response_users = requests.get(url)
    users = {}

    for user in response_users.json():
        userid = str(user['id'])
        response_tasks = requests.get(url + userid + '/todos/')
        tasks_lists = []
        for tasks in response_tasks.json():
            tasks_lists.append({"username": user['username'],
                               "task": tasks['title'],
                                "completed": tasks['completed']})

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(tasks_lists, json_file)

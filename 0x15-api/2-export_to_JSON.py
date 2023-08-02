#!/usr/bin/python3
"""this module gets data from REST API and represents it in JSON
"""


import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    response_user = requests.get(url + argv[1])
    username = response_user.json()['name']

    response_todos = requests.get(url + argv[1] + '/todos')
    task_list = []
    for items in response_todos.json():
        task_list.append({"task": items['title'],
                          "completed": items['completed'],
                          "username": username})

    with open(argv[1] + ".json", 'w') as json_file:
        json.dump({argv[1]: task_list}, json_file)

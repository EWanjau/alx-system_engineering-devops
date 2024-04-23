#!/usr/bin/python3
"""this module gets data from REST API
"""


import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    response_user = requests.get(url + argv[1])
    employee_name = response_user.json()['name']

    response_todos = requests.get(url + argv[1] + '/todos')
    total_tasks = response_todos.json()
    done_tasks = []
    for task in total_tasks:
        done_tasks.append([task["userId"], employee_name,
                           task['completed'], task['title']])

    with open(str(done_tasks[0][0]) + '.csv', 'w') as file:
        write = csv.writer(file, quoting=csv.QUOTE_ALL)
        write.writerows(done_tasks)

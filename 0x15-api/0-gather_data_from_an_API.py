#!/usr/bin/python3
"""this module gets data from REST API
"""


from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    response_user = requests.get(url + argv[1])
    employee_name = response_user.json()['name']

    response_todos = requests.get(url + argv[1] + '/todos')
    total_tasks = response_todos.json()
    done_tasks = []
    for task in total_tasks:
        if task['completed']:
            done_tasks.append(task['title'])

    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, len(done_tasks), len(total_tasks)))
    for tasks in done_tasks:
        print('\t', tasks)

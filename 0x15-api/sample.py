#!/usr/bin/python3

import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos')
answer = response.json()
print(answer)

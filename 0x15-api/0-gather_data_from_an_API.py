#!/usr/bin/python3

"""Accessing a REST API for todo lists of employees"""

import requests
from sys import argv


def fetch_data(id):
    req = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(id))
    user = req.json()
    info = "Employee {} is done with tasks".format(user["name"])

    req = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                       .format(id))
    todos = req.json()
    info += "({}/{}):".format(
                        sum(1 for todo in todos if todo["completed"]),
                        len(todos))
    for todo in todos:
        if todo["completed"]:
            info += "\n\t {}".format(todo["title"])
    print(info)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
    else:
        fetch_data(argv[1])

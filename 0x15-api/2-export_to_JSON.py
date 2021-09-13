#!/usr/bin/python3
""" Export JSON API """
import json
from requests import get
from sys import argv


def tasks_list(employee_id=None):
    """ Return employee info TODO list """

    filename = employee_id + ".json"
    API = "https://jsonplaceholder.typicode.com/"

    try:
        employee_id = int(employee_id)
    except:
        return "No valid employee id"

    employee = get(API + "users/{}". format(employee_id)).json()
    todos = get(API + "todos?userId={}".format(employee_id)).json()

    _id = int(employee_id)
    username = employee.get("username")

    struct = {employee_id: []}
    for task in todos:
        task_title = task.get("title")
        task_status = task.get("completed")
        struct[employee_id].append({"task": task_title,
                                    "completed": task_status,
                                    "username": username})

    with open(filename, "w") as f:
        json.dump(struct, f)


if __name__ == "__main__":
    tasks_list(argv[1])

#!/usr/bin/python3
""" Export JSON ALL API """
import json
from requests import get


def all_tasks():
    """ Return employee info TODO list """

    filename = "todo_all_employees.json"
    API = "https://jsonplaceholder.typicode.com/"

    employees = get(API + "users/").json()
    todos = get(API + "todos/").json()

    struct = {}
    for employe in employees:
        one_id = employe.get("id")
        struct[one_id] = []
        for one in todos:
            if one.get("userId") == one_id:
                one_username = employe.get("username")
                one_task_status = one.get("completed")
                one_task_title = one.get("title")

                struct[one_id].append({"username": one_username,
                                       "task": one_task_title,
                                       "completed": one_task_status})

    with open(filename, "w") as f:
        json.dump(struct, f)


if __name__ == "__main__":
    all_tasks()

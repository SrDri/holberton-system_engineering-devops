#!/usr/bin/python3
""" Use API REST https://jsonplaceholder.typicode.com"""

from requests import get
from sys import argv


def tasks_list(employee_id=None):
    """ Return employee info TODO list """

    API = "https://jsonplaceholder.typicode.com/"

    try:
        employee_id = int(employee_id)
    except:
        return "No valid employee id"

    employee = get(API + "users/{}". format(employee_id)).json()
    todos = get(API + "todos?userId={}".format(employee_id)).json()

    name = employee.get("name")
    tasks_total = len(todos)
    tasks_done = 0
    titles_tasks = []

    for task in todos:
        if task.get("completed") is True:
            titles_tasks.append(task.get("title"))
            tasks_done = tasks_done + 1

    del todos, employee

    print("Employee {:s} is done with tasks({:d}/{:d}):".
          format(name, tasks_done, tasks_total))

    for task in titles_tasks:
        print('\t', task)


if __name__ == "__main__":
    tasks_list(argv[1])

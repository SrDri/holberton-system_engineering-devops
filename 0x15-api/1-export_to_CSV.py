#!/usr/bin/python3
""" Export CSV API """
import csv
from requests import get
from sys import argv


def tasks_list(employee_id=None):
    """ Return employee info TODO list """

    filename = employee_id + ".csv"
    API = "https://jsonplaceholder.typicode.com/"

    try:
        employee_id = int(employee_id)
    except:
        return "No valid employee id"

    employee = get(API + "users/{}". format(employee_id)).json()
    todos = get(API + "todos?userId={}".format(employee_id)).json()

    _id = int(employee_id)
    username = employee.get("username")

    with open(filename, "w") as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            task_status = task.get("completed")
            task_title = task.get("title")
            wr.writerow([_id, username, task_status, task_title])


if __name__ == "__main__":
    tasks_list(argv[1])

#!/usr/bin/python3
"""uses jsonplaceholder api to print info"""


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) != 2:
        sys.exit()
    else:
        employee_id = sys.argv[1]
        base_url = "https://jsonplaceholder.typicode.com"
        user_url = f"{base_url}/users/{employee_id}"
        todo_url = f"{base_url}/users/{employee_id}/todos"

        user_info = requests.get(user_url)
        user_info = user_info.json()
        user_name = user_info.get("name")

        user_todo = requests.get(todo_url)
        user_todo = user_todo.json()
        total_todo = len(user_todo)
        done_todo = [task for task in user_todo if task.get("completed")]
        lendone = len(done_todo)

        print("Employee {} is done with tasks ({}/{})".format(
            user_name, lendone, total_todo))
        for task in done_todo:
            task_done = task.get("title")
            print("\t {}".format(task_done))

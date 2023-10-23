#!/usr/bin/python3
"""uses jsonplaceholder api to print info"""


if __name__ == "__main__":
    import requests
    import sys
    import csv

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
        user_id = user_todo[int(sys.argv[1])].get("userId")
        csv_file = sys.argv[1] + ".csv"
        with open(csv_file, mode="w", newline='\n') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for task in user_todo:
                task_done = task.get("title")
                task_status = task.get("completed")
                
                writer.writerow([str(user_id),str(user_name),str(task_status),str(task_done)])

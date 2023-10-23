#!/usr/bin/python3
"""uses jsonplaceholder api to print info"""


if __name__ == "__main__":
    import requests
    import sys
    import json

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
    
        tasks_json = {
            str(user_id): [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": user_name
                }
                for task in user_todo
            ]
        }

    # Define the file name
        file_name = f"{user_id}.json"

    # Save the JSON data to the file
        with open(file_name, "w") as json_file:
            json.dump(tasks_json, json_file)

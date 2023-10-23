import requests
import json

# Base URL of the JSONPlaceholder API
base_url = "https://jsonplaceholder.typicode.com"
user_url = f"{base_url}/users"
user_data = requests.get(user_url).json()
total_employees = len(user_data)

# Create a dictionary to store tasks for all employees
all_tasks = {}

# Iterate through employee IDs (assuming employee IDs start from 1 and are sequential)
for employee_id in range(1, total_employees + 1):
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/users/{employee_id}/todos"

    user_info = requests.get(user_url)
    user_info = user_info.json()
    user_name = user_info.get("name")

    user_todo = requests.get(todo_url)
    user_todo = user_todo.json()
    user_id = user_todo[0].get("userId")

    # Create a list to store tasks for the current employee
    tasks = [
        {
            "username": user_name,
            "task": task.get("title"),
            "completed": task.get("completed")
        }
        for task in user_todo
    ]

    # Add the tasks to the all_tasks dictionary
    all_tasks[str(user_id)] = tasks

# Define the file name
file_name = "todo_all_employees.json"

# Save the JSON data to the file
with open(file_name, "w") as json_file:
    json.dump(all_tasks, json_file)

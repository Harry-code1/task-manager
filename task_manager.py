import json
from random import choice

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task["title"]}")

def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Exit")

        choice = input("Choose and option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")





main()

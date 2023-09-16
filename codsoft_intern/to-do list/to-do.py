import json
import os

# Function to load tasks from a JSON file
def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            return json.load(file)
    else:
        return []

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

# Function to display the list of tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to add a new task
def add_task(tasks, new_task):
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully!")

# Function to update a task
def update_task(tasks, task_index, new_task):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1] = new_task
        save_tasks(tasks)
        print("Task updated successfully!")
    else:
        print("Invalid task index.")

# Function to delete a task
def delete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"Task '{deleted_task}' deleted successfully!")
    else:
        print("Invalid task index.")

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            new_task = input("Enter the task: ")
            add_task(tasks, new_task)
        elif choice == '3':
            task_index = int(input("Enter the task index to update: "))
            new_task = input("Enter the new task: ")
            update_task(tasks, task_index, new_task)
        elif choice == '4':
            task_index = int(input("Enter the task index to delete: "))
            delete_task(tasks, task_index)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

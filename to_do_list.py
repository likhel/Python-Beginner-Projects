import json


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{i + 1}. [{status}] {task['task']}")


def mark_completed(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print(f"Task '{tasks[index]['task']}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            print(f"Task '{deleted_task['task']}' deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
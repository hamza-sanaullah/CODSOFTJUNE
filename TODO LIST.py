import json


def load_tasks():
    try:

        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks


def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date: ")
    task = {"title1": title, "description": description, "due_date": due_date, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


def list_tasks(tasks):
    for idx, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{idx}. [{status}] {task['title']} - Due: {task['due_date']}")


def mark_completed(tasks, task_index):
    tasks[task_index]["completed"] = True
    save_tasks(tasks)
    print("Task marked as completed.")


def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            list_tasks(tasks)
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            mark_completed(tasks, task_index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()

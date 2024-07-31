def add_task(todo_list, task):
    todo_list.append({'task': task, 'status': 'Pending'})

def list_tasks(todo_list):
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("Tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task['task']} ({task['status']})")

def mark_task_completed(todo_list):
    if not todo_list:
        print("No tasks to mark as completed.")
        return

    print("Select the task to mark as completed:")
    list_tasks(todo_list)

    try:
        task_number = int(input("Enter the task number: "))
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number - 1]['status'] = 'Completed'
            print(f"Task '{todo_list[task_number - 1]['task']}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_in_progress(todo_list):
    if not todo_list:
        print("No tasks to mark as in progress.")
        return

    print("Select the task to mark as in progress:")
    list_tasks(todo_list)

    try:
        task_number = int(input("Enter the task number: "))
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number - 1]['status'] = 'In Progress'
            print(f"Task '{todo_list[task_number - 1]['task']}' marked as in progress.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def clear_tasks(todo_list):
    todo_list.clear()

def main():
    todo_list = []
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Mark a task as in progress")
        print("5. Clear the entire to-do list")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(todo_list, task)
            print(f"Task '{task}' added.")
        elif choice == '2':
            list_tasks(todo_list)
        elif choice == '3':
            mark_task_completed(todo_list)
        elif choice == '4':
            mark_task_in_progress(todo_list)
        elif choice == '5':
            clear_tasks(todo_list)
            print("All tasks cleared.")
        elif choice == '6':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
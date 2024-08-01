todo_list = []

def add_task(todo_list, task):
    todo_list.append({'task': task, 'status': 'Pending'})

def list_tasks(todo_list):
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("Tasks:")
        for task in todo_list:
            print(f"{task['task']} ({task['status']})")

def mark_task_completed(todo_list, task_name):
    for task in todo_list:
        if task['task'] == task_name:
            task['status'] = 'Completed'
            break

def mark_task_in_progress(todo_list, task_name):
    for task in todo_list:
        if task['task'] == task_name:
            task['status'] = 'In progress'
            break

def clear_tasks(todo_list):
    todo_list.clear()

def main():
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
            task_name = input("Enter the task to mark as completed: ")
            mark_task_completed(todo_list, task_name)
            print(f"Task '{task_name}' marked as completed.")
        elif choice == '4':
            task_name = input("Enter the task to mark as in progress: ")
            mark_task_in_progress(todo_list, task_name)
            print(f"Task '{task_name}' marked as in progress.")
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
from collections import defaultdict

def add_task(todo_list, task, day):
    todo_list[day].append({'task': task, 'status': 'Pending'})

def list_tasks(todo_list):
    if not any(todo_list.values()):
        print("No tasks in the to-do list.")
    else:
        for day, tasks in todo_list.items():
            print(f"\nTasks for {day.capitalize()}:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task['task']} ({task['status']})")

def mark_task_completed(todo_list, day):
    if not todo_list[day]:
        print(f"No tasks to mark as completed for {day}.")
        return

    print(f"Select the task to mark as completed for {day}:")
    list_tasks({day: todo_list[day]})

    try:
        task_number = int(input("Enter the task number: "))
        if 1 <= task_number <= len(todo_list[day]):
            todo_list[task_number - 1]['status'] = 'Completed'
            print(f"Task '{todo_list[day][task_number - 1]['task']}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def clear_tasks(todo_list):
    for day in todo_list:
        todo_list[day].clear()

def main():
    todo_list = defaultdict(list)
    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Clear the entire to-do list")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task to add: ")
            day = input(f"Enter the day of the week ({', '.join(days_of_week)}): ").strip().lower()
            if day in days_of_week:
                add_task(todo_list, task, day)
                print(f"Task '{task}' added for {day}.")
            else:
                print("Invalid day of the week.")
        elif choice == '2':
            list_tasks(todo_list)
        elif choice == '3':
            day = input(f"Enter the day of the week ({', '.join(days_of_week)}): ").strip().lower()
            if day in days_of_week:
                mark_task_completed(todo_list, day)
            else:
                print("Invalid day of the week.")
        elif choice == '4':
            clear_tasks(todo_list)
            print("All tasks cleared.")
        elif choice == '5':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
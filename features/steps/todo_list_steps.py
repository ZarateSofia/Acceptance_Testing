import todo_list
import behave

@given('the to-do list is empty')
def step_impl(context):
    context.todo_list = []
@when('the user adds the task Buy food')
def step_impl(context):
    todo_list.add_task(context.todo_list, "Buy food")
@then('the to-do list should contain Buy food (Pending)')
def step_impl(context):
    tasks = [t for t in context.todo_list if t['task'] == "Buy food" and t['status'] == "Pending"]
    assert len(tasks) == 1, "Task 'Buy food' with status 'Pending' not found in the to-do list"


@given('the to-do list contains "Buy food (Pending)" and "Pay bills (Pending)"')
def step_impl(context):
    context.todo_list = [
        {'task': 'Buy food', 'status': 'Pending'},
        {'task': 'Pay bills', 'status': 'Pending'}
    ]

@when('the user lists all tasks')
def step_impl(context):
    context.listed_tasks = [f"{task['task']} ({task['status']})" for task in context.todo_list]

@then('the output should contain "Buy food (Pending)" and "Pay bills (Pending)"')
def step_impl(context):
    expected_tasks = {"Buy food (Pending)", "Pay bills (Pending)"}
    listed_tasks_set = set(context.listed_tasks)
    assert expected_tasks == listed_tasks_set, f"Expected tasks {expected_tasks} but got {listed_tasks_set}"


@when('the user marks task "Buy food" as completed')
def step_impl(context):
    todo_list.mark_task_completed(context.todo_list, "Buy food")

@then('the to-do list should show task "Buy food" as completed')
def step_impl(context):
    tasks = [t for t in context.todo_list if t['task'] == "Buy food"]
    assert len(tasks) == 1 and tasks[0]['status'] == 'Completed', "Task 'Buy food' was not marked as completed"


@when('the user clears the to-do list')
def step_impl(context):
    todo_list.clear_tasks(context.todo_list)

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo_list) == 0, "The to-do list should be empty"


@when('the user marks task "Buy food" as in progress')
def step_impl(context):
    todo_list.mark_task_in_progress(context.todo_list, "Buy food")

@then('the to-do list should show task "Buy food" as in progress')
def step_impl(context):
    tasks = [t for t in context.todo_list if t['task'] == "Buy food"]
    assert len(tasks) == 1 and tasks[0]['status'] == 'In progress', "Task 'Buy food' was not marked as in progress"



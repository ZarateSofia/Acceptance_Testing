import todo_list
import behave

to_do_list = []

@given('the to-do list is empty')
def step_impl(context):
    global to_do_list
    to_do_list = []
@when('the user adds the task "{task}"')
def step_impl(context, task):
    global to_do_list
    todo_list.add_task(to_do_list, task)
@then('the to-do list should contain 1. "{task}" (Pending)')
def step_impl(context, task):
    global to_do_list
    todo_list.list_tasks(todo_list)
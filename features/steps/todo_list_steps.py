import todo_list
import behave

to_do_list = []

@given('the to-do list is empty')
def step_impl(context):
    global to_do_list
    to_do_list = []
@when('the user adds the task Buy food')
def step_impl(context):
    global to_do_list
    todo_list.add_task(to_do_list,"Buy food")
@then('the to-do list should contain Buy food (Pending)')
def step_impl(context):
    global to_do_list
    todo_list.list_tasks(todo_list)
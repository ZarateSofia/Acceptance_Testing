# language: en
Feature: Manage the list

    @manageTheList
    Scenario: Add a task to the to-do list
        Given the to-do list is empty
        When the user adds the task Buy food
        Then the to-do list should contain Buy food (Pending)

    @manageTheList
    Scenario: List all tasks in the to-do list
        Given the to-do list contains "Buy food (Pending)" and "Pay bills (Pending)"
        When the user lists all tasks
        Then the output should contain "Buy food (Pending)" and "Pay bills (Pending)"

    @manageTheList
    Scenario: Mark a task as completed
        Given the to-do list contains "Buy food (Pending)" and "Pay bills (Pending)"
        When the user marks task "Buy food" as completed
        Then the to-do list should show task "Buy food" as completed

    @manageTheList
    Scenario: Clear the entire to-do list
        Given the to-do list contains "Buy food (Pending)" and "Pay bills (Pending)"
        When the user clears the to-do list
        Then the to-do list should be empty

    @manageTheList
        Scenario: Mark a task as in progress
        Given the to-do list contains "Buy food (Pending)" and "Pay bills (Pending)"
        When the user marks task "Buy food" as in progress
        Then the to-do list should show task "Buy food" as in progress


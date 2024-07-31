# language: en
Feature: Manage the list

    @manageTheList
    Scenario: Add a task to the to-do list
        Given the to-do list is empty
        When the user adds the task Buy food
        Then the to-do list should contain Buy food (Pending)

    @manageTheList
    Scenario: List all tasks in the to-do list


    @manageTheList
    Scenario: Mark a task as completed

    @manageTheList
    Scenario: Clear the entire to-do list

    @manageTheList
    Scenario: Mark a task as “In progress” 
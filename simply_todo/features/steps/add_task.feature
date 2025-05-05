Feature: Add a new task
  As a user
  I want to add a task
  So that I can track my to-do items

  Scenario: User adds a new task successfully
    Given I am on the "Add Task" page
    When I fill in "Title" with "Buy groceries"
    And I fill in "Due Date" with "2025-05-10"
    And I press "Add Task"
    Then I should see "Buy groceries" in the task list

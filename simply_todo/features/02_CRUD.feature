Feature: Task Management (CRUD)
  As a user
  I want to manage my tasks
  So that I can stay productive and organized

  Background:
    Given a user "taskuser" with password "taskpass" exists
    And I am logged in as "taskuser"
    And I am on the task dashboard

  Scenario: Add a new task
    When I click the "Add Task" button
    And I fill the form with:
      | title       | Learn Cucumber   |
      | description | Study test cases |
      | category    | Study            |
      | due_date    | 2025-05-10       |
      | priority    | High             |
    And I submit the task form
    Then I should see "Learn Cucumber" in the task list

  Scenario: Update an existing task
    Given I have a task titled "Learn Django"
    When I click the edit button for "Learn Django"
    And I update the title to "Master Django"
    And I save the changes
    Then I should see "Master Django" in the task list

  Scenario: Delete a task
    Given I have a task titled "Temp Task"
    When I click the delete button for "Temp Task"
    And I confirm the deletion
    Then I should not see "Temp Task" in the task list

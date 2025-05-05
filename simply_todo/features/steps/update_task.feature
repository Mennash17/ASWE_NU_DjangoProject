Feature: Update a task
  As a user
  I want to update a task
  So that I can modify its details

  Scenario: User updates a task successfully
    Given I have a task titled "Write report"
    When I update the task titled "Write report" to "Write final report"
    Then I should see "Write final report" in the task list

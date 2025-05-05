Feature: Delete a task
  As a user
  I want to delete a task
  So that I can remove tasks I no longer need

  Scenario: User deletes a task successfully
    Given I have a task titled "Clean desk"
    When I delete the task titled "Clean desk"
    Then I should not see "Clean desk" in the task list

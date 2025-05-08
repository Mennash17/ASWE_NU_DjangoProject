Feature: Task Export
  Scenario: Export as Excel
    Given a user "taskuser" with password "taskpass" exists
    And I am logged in as "taskuser"
    And I have a task titled "Export Test Task"
    And I am on the task dashboard
    When I click the "Export" button
    Then a file named "tasks_export.xlsx" should be downloaded

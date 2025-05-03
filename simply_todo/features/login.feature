Feature: User Login

  Scenario: User logs in with valid credentials
    Given I am on the login page
    When I enter a valid username and password
    And I press the login button
    Then I should see the dashboard

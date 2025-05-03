Feature: User Account Management
  As a user
  I want to be able to register and log in
  So I can manage my tasks securely

  Scenario: New user registration
    Given I am on the login page and I click register
    When I enter valid user details and submit
    Then I should be redirected to the login page

  Scenario: Successful login
    Given I am on the login page
    When I enter a valid username and password
    And I press the login button
    Then I should see my task dashboard

  Scenario: Failed login with invalid credentials
    Given I am on the login page
    When I enter an incorrect username or password
    And I press the login button
    Then I should see an error message

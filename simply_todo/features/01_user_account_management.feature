Feature: User Account Management
  As a user
  I want to register and log in securely
  So that I can manage my personal tasks

  Background:
    Given I open the application

  Scenario: Navigate to registration page
    Given I am on the login page
    When I click the "Register" link
    Then I should be redirected to the registration form

  Scenario: Successful registration with valid details
    Given I am on the registration form
    When I fill in a unique username and matching passwords
    And I submit the registration form
    Then I should be redirected to the login page
    And I should see a message "Registration successful"

  Scenario: Registration with mismatched passwords
    Given I am on the registration form
    When I fill in a unique username and mismatched passwords
    And I submit the registration form
    Then I should see an error message "Passwords do not match"

  Scenario: Registration with an existing username
    Given a user "menna" already exists
    And I am on the registration form
    When I fill in the username "menna" with valid passwords
    And I submit the registration form
    Then I should see an error message "Username already taken"

  Scenario: Successful login
    Given a user "testuser" with password "testpass" exists
    And I am on the login page
    When I enter "testuser" and "testpass"
    And I press the login button
    Then I should be redirected to the dashboard
    And I should see a welcome message

  Scenario: Failed login with invalid credentials
    Given I am on the login page
    When I enter "wronguser" and "wrongpass"
    And I press the login button
    Then I should see an error message "Invalid username or password"

  Scenario: Logout
    Given I am logged in as "testuser"
    When I click the "Logout" button
    Then I should be redirected to the login page
    And I should see a message "You have been logged out"

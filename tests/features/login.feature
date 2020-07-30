Feature: Login
  https://www.saucedemo.com/

  Scenario: Upon login user sees the products page
    Given I am on the login page
    When I enter a valid username and password
    And I login
    Then I should see the products page

  Scenario: Username is required at login
    Given I am on the login page
    When I login
    Then I should get a message "Username is required"
    And I should see the login page

  Scenario: Password is required at login
    Given I am on the login page
    When I enter a username
    And I login
    Then I should get a message "Password is required"
    And I should see the login page

  Scenario: Locked out user is unable to login
    Given I am on the login page
    When I enter a locked out username and password
    And I login
    Then I should get a message "Sorry, this user has been locked out."
    And I should see the login page
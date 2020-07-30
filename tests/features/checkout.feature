Feature: Cart
  https://www.saucedemo.com/cart.html

  Scenario: User is able to add one item to a cart
    Given I am on the login page
    When I enter a valid username and password
    And I login
    When I add an <item> to the cart
    Then I should see the <item> in the cart

  Examples:
  | item    |
  | Sauce Labs Bike Light   |
  | Sauce Labs Bolt T-Shirt    |

  Scenario: User is able to remove items from the cart
    Given I am on the login page
    When I enter a valid username and password
    And I login
    And I have an <item> in the cart
    When I remove an item from the cart
    Then I no longer see any items in the cart

  Examples:
  | item    |
  | Sauce Labs Bike Light   |
  | Sauce Labs Bolt T-Shirt    |

  Scenario: User is able to add multiple items to a cart
    Given I am on the login page
    When I enter a valid username and password
    And I login
    When I add multiple items to a cart
    Then I should see the items in the cart

  Scenario: User able to continue shopping from the cart
    Given I am on the login page
    When I enter a valid username and password
    And I login
    When I go to the cart page
    And I choose to continue shopping
    Then I should see the products page

  Scenario: User should be able to check out
    Given I am on the login page
    When I enter a valid username and password
    And I login
    When I go to the cart page
    And I choose to checkout
    Then I should see the your information page

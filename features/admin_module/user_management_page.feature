Feature: User management

  Scenario: Open Add User page
    Given I am on the dashboard page
    When I open the Admin module
    And I click Add user
    Then I should see the Add User page


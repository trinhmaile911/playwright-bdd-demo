Feature: Adding User

  @smoke
  Scenario Outline: Successfully add a user
    Given I am on the dashboard page
    When I open the Admin module
    And I click Add user
    And I select user role <user_role>
    And I select status <status>
    And I enter employee name as <employee_name>
    And I enter username <username>
    And I enter password <password>
    And I confirm <password>
    And I save the data

    Examples:
      | user_role | status  | employee_name | username | password   |  |
      | ESS       | Enabled | Trinh Le      | trinh_le | Trinhle123 |  |

  Scenario: Cancel adding user
    Given I am on the dashboard page
    When I open the Admin module
    And I click Add user
    And I cancel adding user
    Then I should see the System Users page
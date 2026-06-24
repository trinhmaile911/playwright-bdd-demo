Feature: Assign Leave

  @smoke
  Scenario Outline: Successfully add a user
    Given I am on the assign leave page
    When I select an employee name
    And I select leave type 'CAN - Personal'
    And I select start date as 5 days from now
    And I select end date as 6 days from now
    And I select Partial days option as 'Start Day Only'
    And I select Duration option as 'Half Day - Morning'
    And I leave a comment 'Personal reason'
    Then I should see a confirm dialog

    When I click on the confirm button
    Then I should see a toast message



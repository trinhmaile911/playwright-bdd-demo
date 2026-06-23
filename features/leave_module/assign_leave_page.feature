Feature: Assign Leave

  @smoke
  Scenario Outline: Successfully add a user
    Given I am on the assign leave page
    When I select start date as 5 days from now
    And I select end date as 6 days from now

Feature: Edit Personal Details

  @smoke
  Scenario Outline: Successfully edit personal details
    Given I am on the personal details page
    When I fill data in the First Name textbox
    And I fill data in the Middle Name textbox
    And I fill data in the Last Name textbox
    And I select license expiry date
    And I select gender

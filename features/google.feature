Feature: search keyword in google
  Scenario: Search for selenium
    Given I open google
    When I search for "selenium"
    Then I should see "Selenium" in search result

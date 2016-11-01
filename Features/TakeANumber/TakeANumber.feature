Feature: Ticketing
  As a business owner, I want to effectively manage customers waiting to be served in a "first come, first served" manner.

  @wip
  Scenario: Start_Machine
    Given Machine is off
    When  Machine is started
    Then  Machine is on
    And   Display shows 1
    And   Ticket is 1

  Scenario: Stop_Machine
    Given Machine is on
    When  Machine is stopped
    Then  Machine is off
    And   Display shows 0

  Scenario: Customer_Takes_Ticket
    Given Machine is on
    When  Customer takes <ticket>
    Then  <ticket> should be less than or equal to the display

  Scenario: Serve
    Given Machine is on
    And   Display is less than <ticket>
    When  A customer is called
    Then  Display should increase by 1

  Scenario: Reset_Machine
    Given Machine is on
    When  Machine is reset
    Then  Display shows 1
    And   Ticket is 1


Feature: Ticketing
  As a business owner, I want to allow my employees to efficiently and effectively manage customers waiting to be served.

  The system will maintain an ordering of customers based on their arrival times, and allocate them to wickets where they are served.

  A customer will not be allocated to a closed wicket, and one only customer can be assigned to a wicket at any given time.

  @wip
  Scenario: Start Machine
    Given Machine is off
    When  Machine is started
    Then  Machine is on
    And   Display should show 1

  @wip
  Scenario: Stop Machine
    Given Machine is on
    When  Machine is stopped
    Then  Machine is off
    And   Display should be empty

  Scenario: Customer Takes Ticket
    Given Machine is on
    When  A ticket is dispensed
    Then  The ticket should be less than the displayed number

  Scenario: Wicket Serves Customer
    Given Machine is on
    And   Wicket <wicket> is open
    When  Wicket <wicket> serves a customer with ticket <ticket>
    Then  The "Now Serving" display should show <wicket> is serving <ticket>

  Scenario: Wicket Closes With Customers
    Given Wicket <wicket> is open
    And   There are customers left to serve
    When  Wicket <wicket> is closed
    Then  Wicket <wicket> is shown as closed.
    And   Another wicket should be open

  Scenario: Wicket Closes
    Given Wicket <wicket> is open
    And   There are no customers left to serve
    When  Wicket <wicket> is closed
    Then  Wicket <wicket> is shown as closed.


Feature: Ticketing
  As a business owner, I want to allow my employees to efficiently and effectively manage customers waiting to be served.

  Scenario: Start Machine
  """
    This is some text.
    """
    Given Machine is off
    """
    running = FALSE
    """
    When  Machine is started
    """
    running := TRUE
    """
    Then  Machine is on

  Scenario: Customer Takes Ticket
    Given Machine is on
    When  A ticket is dispensed
    Then  The ticket should be less than the displayed number

  Scenario: Wicket Serves Customer
    Given Machine is on
    And   Wicket <wicket> is open
    When  Wicket <wicket> serves a customer with ticket <ticket>
    Then  The "Now Serving" display should show <wicket> is serving <ticket>

  Scenario: Wicket Closes
    Given Machine is on
    And   Wicket <wicket> is open
    When  Wicket <wicket> is closed
    Then  The "Now Serving" display should now show <wicket>

  Scenario: Stop Machine
    Given Machine is on
    When  Machine is stopped
    Then  Machine is off
    And   The "Now Serving" display should be blank


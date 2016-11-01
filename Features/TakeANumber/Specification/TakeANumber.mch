MACHINE           NowServing(max_display)

CONSTRAINTS       max_display : INT & max_display > 0 & max_display < 100

VARIABLES         running, display, next_ticket

INVARIANT         running : BOOL & display : NAT & next_ticket : NAT1 & display < max_display

INITIALISATION    running := FALSE || display := 0 || next_ticket := 1

OPERATIONS

  Start_Machine =
  PRE running = FALSE
  THEN running := TRUE || display := 1
  END;

  Stop_Machine =
  PRE running = TRUE
  THEN running := FALSE || display := 0
  END;

  Customer_Takes_Ticket =
  PRE running = TRUE
  THEN next_ticket := next_ticket + 1
  END;

  Reset_Machine =
  PRE running = TRUE
  THEN display := 1 || next_ticket := 1
  END;

  Serve =
  PRE running = TRUE & display < next_ticket
  THEN display := display + 1
  END

END

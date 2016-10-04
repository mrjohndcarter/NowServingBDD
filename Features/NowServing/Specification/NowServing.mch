MACHINE           NowServing(max_ticket)

CONSTRAINTS       max_ticket : NAT1 & max_ticket <= 10

VARIABLES         running, display

INVARIANT         running : BOOL & display : INT 

INITIALISATION    running := FALSE || display := 0

OPERATIONS

  Start_Machine =
  PRE running = FALSE
  THEN running := TRUE || display := 1
  END

END

MACHINE           NowServing(max_ticket)

CONSTRAINTS       max_ticket : NAT1 & max_ticket <= 10

SETS              WICKET; NOT_DEFERRED = {a, b}

CONSTANTS         closed_sentinel

PROPERTIES        closed_sentinel : NAT & closed_sentinel = 0

VARIABLES         next_ticket, current, serving, running

INVARIANT         running : BOOL & next_ticket : NAT & current : NAT & serving : WICKET --> NAT & current < next_ticket

INITIALISATION    current := 0 || next_ticket := 1 || serving := WICKET * {closed_sentinel} || running := FALSE

OPERATIONS

  Start_Machine =
  PRE running = FALSE
  THEN running := TRUE
  END;
  
  reset =
  current := 0 || next_ticket := 1 || serving := WICKET * {closed_sentinel};

  serve(ww) =
  PRE ww : WICKET & (current + 1) < next_ticket & current <= max_ticket
  THEN serving(ww) := current + 1 || current := current + 1
  END;

  ticket <-- take_ticket =
  PRE next_ticket <= max_ticket
  THEN ticket := next_ticket || next_ticket := next_ticket + 1
  END;
  
  close(ww) =
  PRE ww: WICKET & serving(ww) /= closed_sentinel
  THEN serving(ww) := closed_sentinel
  END

END

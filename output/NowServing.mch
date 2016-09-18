MACHINE				NowServing(max_ticket)

CONSTRAINTS				max_ticket : NAT1 & max_ticket <= 10

SETS				NOT_DEFERRED = {a,b}; WICKET

CONSTANTS				closed_sentinel

PROPERTIES				closed_sentinel : NAT & closed_sentinel = 0

VARIABLES				current, next_ticket, running, serving

INVARIANT				current : NAT & next_ticket : NAT & running : BOOL & serving : WICKET --> NAT

INITIALISATION				current := 0 || next_ticket := 1 || running := FALSE || serving := WICKET * {closed_sentinel}

OPERATIONS

Start_Machine = 
PRE running = FALSE
THEN running := TRUE
END
END
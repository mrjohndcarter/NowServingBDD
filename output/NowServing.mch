MACHINE				NowServing(max_ticket)

CONSTRAINTS				max_ticket : NAT1 & max_ticket <= 10

VARIABLES				running

INVARIANT				running : BOOL

INITIALISATION				running := FALSE

OPERATIONS

Start_Machine = 
PRE running = FALSE
THEN running := TRUE
END
END

class TicketingModel:
    def __init__(self):
        self._display = 0
        self._is_running = False
        self._ticket = 0

    # model properties
    def __get_display(self):
        return self._display

    def __set_display(self, display):
        self._display = display

    def __get_ticket(self):
        return self._ticket

    def __set_ticket(self, ticket):
        self._ticket = ticket

    def __get_running_state(self):
        return self._is_running

    def __set_running_state(self, running_state):
        self._is_running = running_state

    display = property(__get_display, __set_display)
    ticket = property(__get_ticket, __set_ticket)
    running = property(__get_running_state, __set_running_state)

    # model operations
    def start(self):
        self.running = True
        self.reset()

    def stop(self):
        self.running = False
        self.display = 0

    def reset(self):
        self.display = 0
        self.ticket = 1

    def take_ticket(self):
        if not self.running:
            return None
        current = self.ticket
        self.ticket = (self.ticket + 1)
        return current

    def serve_customer(self):
        if self.ticket - 1 == self.display:
            return None
        self.display += 1
        return self.display

import unittest

class TestTicketingModel(unittest.TestCase):
    def setUp(self):
        self.model = TicketingModel()

    def tearDown(self):
        pass

    def testConstruction(self):
        assert not self.model.running
        assert self.model.display == 0

    def testReset(self):
        self.model.reset()
        assert self.model.ticket == 1
        assert self.model.display == 0

    def testStart(self):
        self.model.start()
        assert self.model.running
        assert self.model.ticket == 1
        assert self.model.display == 0

    def testStop(self):
        self.model.stop()
        assert not self.model.running

    def testTakeTicket(self):
        assert self.model.take_ticket() is None
        self.model.start()
        assert self.model.take_ticket() == 1
        assert self.model.take_ticket() == 2

    def testServeCustomer(self):
        assert self.model.display == 0
        self.model.start()
        self.model.take_ticket()
        assert self.model.serve_customer() == 1
        assert self.model.display == 1
        self.model.take_ticket()
        self.model.take_ticket()
        assert self.model.serve_customer() == 2
        assert self.model.serve_customer() == 3
        assert self.model.display == 3
        assert self.model.ticket == 4
        assert self.model.serve_customer() is None

if __name__ == '__main__':
    unittest.main()

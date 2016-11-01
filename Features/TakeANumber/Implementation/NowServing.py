from enum import Enum


class NowServing:
    class Status(Enum):
        off = 0
        on = 1

    def __init__(self):
        self.status = NowServing.Status.off
        self.display = ''

    def start(self):
        self.status = NowServing.Status.on

    def take_ticket(self):
        return 1

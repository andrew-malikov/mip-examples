from random import random

from packages.bas_models.src.bus_state import BusState


class Bus:
    def __init__(self, breakage: [float]):
        self.state = BusState.FULLY_FUNCTIONAL
        self.flights = 0
        self.breakage = breakage

    def crack(self):
        if self.state == BusState.FULLY_FUNCTIONAL:
            if random() < self.breakage[0]:
                self.state = BusState.PARTIALLY_DEFECTIVE
        elif self.state == BusState.PARTIALLY_DEFECTIVE:
            if random() < self.breakage[1]:
                self.state = BusState.FULLY_DEFECTIVE

    def repair(self):
        self.state = BusState.FULLY_FUNCTIONAL

    def can_ride(self):
        return self.state != BusState.FULLY_DEFECTIVE

    def done(self):
        self.flights += 1

    def reset(self):
        self.flights = 0
        self.repair()

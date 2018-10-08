from packages.bas_models.src.model import Model
from packages.bas_models.src.bus import Bus
from packages.bas_models.src.bus_state import BusState


class RepairModel(Model):
    def __init__(self, buses: [Bus]):
        return super().__init__(buses)

    def run(self, flights: int):
        for i in range(0, flights):
            for bus in self.buses:

                bus.crack()

                if bus.state == BusState.PARTIALLY_DEFECTIVE:
                    bus.repair()
                else:
                    bus.done()

        return self.buses

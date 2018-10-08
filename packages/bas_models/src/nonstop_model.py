from packages.bas_models.src.model import Model
from packages.bas_models.src.bus import Bus


class NonstopModel(Model):
    def __init__(self, buses: [Bus]):
        super().__init__(buses)

    def run(self, flights: int):
        for i in range(0, flights):
            for bus in self.buses:

                bus.crack()

                if bus.can_ride():
                    bus.done()

        return self.buses

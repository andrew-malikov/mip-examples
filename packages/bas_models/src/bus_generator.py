from packages.bas_models.src.bus import Bus


class BusGenerator:
    def __init__(self, breakages: [float]):
        self.breakages = breakages

    def generate(self, count):
        buses = []

        for i in range(0, count):
            buses.append(Bus(self.breakages))

        return buses

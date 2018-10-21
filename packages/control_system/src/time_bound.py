from packages.random.src.uniform import UniformRandom


class TimeBound:
    def __init__(self, bounds: (float, float)):
        self.bounds = bounds
        self.random = UniformRandom()

    def next(self):
        return round(self.random.next(self.bounds))

from packages.random.src.uniform import UniformRandom


class UniformRandomGenerator:
    def __init__(self, bounds: (int, int), precision: int):
        self.bounds = bounds
        self.precision = precision

        self.random = UniformRandom()

    def generate(self, count: int):
        return [
            round(self.random.next(self.bounds), self.precision)
            for x in range(0, count)
        ]

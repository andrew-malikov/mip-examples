from packages.random.src.exponential import ExponentialRandom


class ExponentialRandomGenerator:
    def __init__(self, rate: float, precision: int):
        self.rate = rate
        self.precision = precision

        self.random = ExponentialRandom()

    def generate(self, count: int):
        return [
            round(self.random.next(self.rate), self.precision)
            for x in range(0, count)
        ]

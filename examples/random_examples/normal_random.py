from packages.random.src.normal import NormalRandom


class NormalRandomGenerator:
    def __init__(self, mu: float, sigma: float, precision: int):
        self.mu = mu
        self.sigma = sigma
        self.precision = precision

        self.random = NormalRandom()

    def generate(self, count: int):
        return [
            round(self.random.next(self.mu, self.sigma), self.precision)
            for x in range(0, count)
        ]

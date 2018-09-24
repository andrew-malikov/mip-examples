from random import random
from math import sqrt


class NormalRandom:
    def next(self, mu: int, sigma: int, randomness=12) -> float:
        body = sum([random() - randomness / 2 for n in range(1, randomness)])
        return mu + (sigma / sqrt(randomness)) * body

from random import random


class UniformRandom():
    def next(self, bounds: (float, float)) -> float:
        return bounds[0] + random() * (bounds[1] - bounds[0])

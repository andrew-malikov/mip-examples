from random import random
from math import log


class ExponentialRandom:
    def next(self, rate: float) -> float:
        return (-1 / rate) * log(random())

from math import factorial


class ErlangModel:
    def __init__(self, produce: float, control: float):
        self.flow_power = produce / control

    def arrange_stats(self, channels: int):
        return 1 - self._compute_free_prob(
            channels) * self.flow_power**channels / factorial(channels)

    def _compute_free_prob(self, channels: int) -> float:
        return 1 / sum([
            self.flow_power**i / factorial(i) for i in range(0, channels + 1)
        ])

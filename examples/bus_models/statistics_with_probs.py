from packages.bas_models.src.model import Model
from packages.bas_models.src.bus_generator import BusGenerator


class StatisticsWithProbs:
    def __init__(self, model: Model, days: int, flights: int):
        self.model = model
        self.days = days
        self.flights = flights

    def arrange_statistics(self, probs):
        stats = dict()

        for prob in probs:
            generator = BusGenerator(prob)
            buses = generator.generate(1)

            self.model.buses = buses

            stats[self._get_key(prob)] = self._get_statistics(prob)

        return stats

    def _get_key(self, prob: [float]) -> str:
        return "{0}/{1}".format(prob[0], prob[1])

    def _get_statistics(self, prob) -> int:
        result = 0

        for day in range(0, self.days):
            buses = self.model.run(self.flights)

            result += sum(list(map(lambda x: x.flights, buses)))

            self.model.reset_buses()

        return result / self.days

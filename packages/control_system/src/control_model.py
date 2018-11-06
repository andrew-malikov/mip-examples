from packages.control_system.src.time_bound import TimeBound
from packages.control_system.src.channel_manager import ChannelManager
from packages.control_system.src.model_stats import ModelStats


class ControlModel:
    def __init__(self, manager, produce: TimeBound, control: TimeBound):
        self.manager: ChannelManager = manager
        self.produce = produce
        self.control = control

    def arrange_stats(self, sample: int) -> ModelStats:
        stats = ModelStats(sample, len(self.manager.channels))

        time = 0

        for i in range(0, sample):
            produce_time = self.produce.next()

            time += produce_time

            is_missed = True

            for i in range(0, len(self.manager.channels)):
                if self.manager.channels[i] < time:
                    self.manager.channels[i] = time + self.control.next()

                    is_missed = False
                    break

            if is_missed:
                stats.missed += 1

        self.reset()

        return stats

    def reset(self):
        self.manager.reset()

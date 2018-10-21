class ModelStats:
    def __init__(self, sample: int, channels: int):
        self.sample = sample
        self.missed = 0
        self.channels = channels

    @property
    def ratio(self):
        return 1 - self.missed / self.sample

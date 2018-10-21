class ChannelManager:
    def __init__(self, count: int):
        self.channels = get_channels(count)

    def reset(self):
        for i in range(0, len(self.channels)):
            self.channels[i] = 0

    def add(self, count: int = 1):
        self.channels.extend(get_channels(count))


def get_channels(count: int):
    return [0 for i in range(0, count)]

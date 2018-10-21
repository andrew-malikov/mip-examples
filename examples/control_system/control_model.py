from packages.control_system.src.control_model import ControlModel
from packages.control_system.src.model_stats import ModelStats


def analyze(model: ControlModel, sample: int, ratio: float) -> ModelStats:
    stats = model.arrange_stats(sample)

    while stats.ratio < ratio:
        model.manager.add()
        stats = model.arrange_stats(sample)

    return stats

from packages.random.src.expected_value import expected_value


def dispersion(sample: [float]) -> float:
    expectation = expected_value(sample)

    body = sum([(n - expectation)**2 for n in sample])
    return (1 / (len(sample) - 1)) * body

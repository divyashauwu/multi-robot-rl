import random


class StochasticBlockages:
    def __init__(self, blockage_probability: float = 0.2):
        self.blockage_probability = blockage_probability

    def is_blocked(self) -> bool:
        return random.random() < self.blockage_probability

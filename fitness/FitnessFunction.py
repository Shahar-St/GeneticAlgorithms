from abc import abstractmethod


class FitnessFunction:

    def __init__(self, targetVal):
        self.targetVal = targetVal

    @abstractmethod
    def calculate(self, stringVal):
        raise NotImplementedError
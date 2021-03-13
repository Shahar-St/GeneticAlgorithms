from abc import abstractmethod


class FitnessFunction:

    def __init__(self, targetVal):
        self._targetVal = targetVal

    @abstractmethod
    def calculate(self, vector):
        raise NotImplementedError
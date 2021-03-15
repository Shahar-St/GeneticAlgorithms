import importlib
from abc import abstractmethod


class FitnessFunction:

    def __init__(self, targetVal):
        self._targetVal = targetVal

    @abstractmethod
    def calculate(self, vector):
        raise NotImplementedError

    @staticmethod
    def factory(fitnessName, targetVal):
        module = importlib.import_module('fitness.' + fitnessName)
        fitness = getattr(module, fitnessName)
        return fitness(targetVal)
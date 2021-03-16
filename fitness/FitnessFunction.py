import importlib
from abc import abstractmethod


class FitnessFunction:

    @abstractmethod
    def calculate(self, problem, vector):
        raise NotImplementedError

    @staticmethod
    def factory(fitnessName):
        module = importlib.import_module('fitness.' + fitnessName)
        fitness = getattr(module, fitnessName)
        return fitness()
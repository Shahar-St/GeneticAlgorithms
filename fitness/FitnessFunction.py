import importlib
from abc import abstractmethod


class FitnessFunction:

    def __init__(self, problem):
        self._problem = problem

    @abstractmethod
    def calculate(self, vector):
        raise NotImplementedError

    @staticmethod
    def factory(fitnessName, problem):
        module = importlib.import_module('fitness.' + fitnessName)
        fitness = getattr(module, fitnessName)
        return fitness(problem)
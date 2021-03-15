import importlib
from abc import ABC, abstractmethod


class Algorithm(ABC):

    def __init__(self, target, fitnessFunction, popSize):
        self._popSize = popSize
        self._fitnessFunction = fitnessFunction
        self._target = target

    @abstractmethod
    def findSolution(self, maxIter):
        raise NotImplementedError

    @staticmethod
    def factory(AlgoName, target, fitnessFunction, popSize, eliteRate, crossoverFunc, mutationRate):
        module = importlib.import_module('algorithms.' + AlgoName)

        algo = getattr(module, AlgoName)

        if AlgoName == 'PSO':
            return algo(target, fitnessFunction, popSize)

        if AlgoName == 'GeneticAlgorithm':
            return algo(target, fitnessFunction, popSize, eliteRate, crossoverFunc, mutationRate)
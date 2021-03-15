import importlib
from abc import ABC, abstractmethod


class Algorithm(ABC):

    def __init__(self, targetSize, fitnessFunction, popSize):
        self._popSize = popSize
        self._fitnessFunction = fitnessFunction
        self._targetSize = targetSize

    def getPopSize(self):
        return self._popSize

    @abstractmethod
    def findSolution(self, maxIter):
        raise NotImplementedError

    @staticmethod
    def factory(AlgoName, targetSize, fitnessFunction, popSize, eliteRate, crossoverFunc, mutationRate,
                parentSelectionFunction):
        module = importlib.import_module('algorithms.' + AlgoName)

        algo = getattr(module, AlgoName)

        if AlgoName == 'PSO':
            return algo(targetSize, fitnessFunction, popSize)

        if AlgoName == 'GeneticAlgorithm':
            return algo(targetSize, fitnessFunction, popSize, eliteRate, crossoverFunc, mutationRate,
                        parentSelectionFunction)

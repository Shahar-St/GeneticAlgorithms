from abc import ABC, abstractmethod


class Algorithm(ABC):

    def __init__(self, target, fitnessFunction, popSize):
        self._popSize = popSize
        self._fitnessFunction = fitnessFunction
        self._target = target

    @abstractmethod
    def findSolution(self, maxIter):
        raise NotImplementedError
import importlib
from abc import ABC, abstractmethod

import numpy as np


class Problem(ABC):

    def __init__(self, fitnessFunction, targetSize):
        self._targetSize = targetSize
        self._fitnessFunction = fitnessFunction

    def getTargetSize(self):
        return self._targetSize

    @abstractmethod
    def translateVec(self, vec):
        raise NotImplementedError

    @abstractmethod
    def generateRandomVec(self):
        raise NotImplementedError

    def calculateFitness(self, newVec):
        return self._fitnessFunction(self, newVec)

    @staticmethod
    def factory(problemName, fitnessFunction, targetSize, targetVal=None):
        module = importlib.import_module('problems.' + problemName)
        problem = getattr(module, problemName)

        if problemName == 'StringMatching':
            return problem(fitnessFunction, targetSize, targetVal)

        if problemName == 'NQueens':
            return problem(fitnessFunction, targetSize)

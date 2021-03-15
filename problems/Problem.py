import importlib
from abc import ABC, abstractmethod

import numpy as np


class Problem(ABC):

    def __init__(self, targetVal, fitnessFunction):
        self._targetVal = targetVal
        self._targetVec = self._setTargetVec()
        self._fitnessFunction = fitnessFunction


    @abstractmethod
    def _setTargetVec(self):
        raise NotImplementedError

    @abstractmethod
    def translateVec(self, vec):
        raise NotImplementedError

    @abstractmethod
    def generateRandomVec(self):
        raise NotImplementedError

    def getTargetVec(self):
        return np.copy(self._targetVec)

    def calculateFitness(self, newVec):
        return self._fitnessFunction(self._targetVec, newVec)

    @staticmethod
    def factory(problemName, targetVal, fitnessFunction):
        module = importlib.import_module('problems.' + problemName)
        problem = getattr(module, problemName)
        return problem(targetVal, fitnessFunction)
import importlib
from abc import ABC, abstractmethod

import numpy as np


class Problem(ABC):

    def __init__(self, targetVal):
        self._targetVal = targetVal
        self._targetVec = self._setTargetVec()

    @abstractmethod
    def _setTargetVec(self):
        raise NotImplementedError

    def getTargetVec(self):
        return np.copy(self._targetVec)

    @staticmethod
    def factory(problemName, targetVal):
        module = importlib.import_module('problems.' + problemName)
        problem = getattr(module, problemName)
        return problem(targetVal)
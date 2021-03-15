import importlib
from abc import abstractmethod, ABC


class Crossover(ABC):

    def __init__(self, targetWord):
        self._targetWord = targetWord

    @abstractmethod
    def makeNewChild(self, parent1, parent2):
        raise NotImplementedError

    @staticmethod
    def factory(CrossName, targetVal):
        module = importlib.import_module('entities.crossovers.' + CrossName)
        cross = getattr(module, CrossName)
        return cross(targetVal)
import importlib
from abc import abstractmethod, ABC


class Crossover(ABC):

    @abstractmethod
    def makeNewChild(self, parent1, parent2):
        raise NotImplementedError

    @staticmethod
    def factory(crossName):
        module = importlib.import_module('entities.crossovers.' + crossName)
        cross = getattr(module, crossName)
        return cross()
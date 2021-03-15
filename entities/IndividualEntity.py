from abc import ABC, abstractmethod


class IndividualEntity(ABC):

    def __init__(self, stringVal):
        self._stringVal = stringVal
        self._fitness = 0
        self._vec = None

    def getFitness(self):
        return self._fitness

    def setFitness(self, fitness):
        self._fitness = fitness

    def getStr(self):
        return self._stringVal

    @abstractmethod
    def getVec(self):
        raise NotImplementedError

    def __lt__(self, other):
        return self._fitness < other.getFitness()


from abc import abstractmethod

class Crossover:

    def __init__(self, targetWord):
        self.targetWord = targetWord

    @abstractmethod
    def makeNewChild(self, parent1, parent2):
        raise NotImplementedError
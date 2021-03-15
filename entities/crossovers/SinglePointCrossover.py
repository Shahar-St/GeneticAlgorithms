import random

from entities.crossovers.Crossover import Crossover
from entities.GeneticEntity import GeneticEntity


class SinglePointCrossover(Crossover):

    def makeNewChild(self, parent1, parent2):
        matingIndex = random.randrange(len(self._targetWord))

        childStr = parent1.getStr()[:matingIndex] + parent2.getStr()[matingIndex:]
        return GeneticEntity(childStr)

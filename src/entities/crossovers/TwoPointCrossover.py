import random

from entities.crossovers.Crossover import Crossover
from entities.GeneticEntity import GeneticEntity


class TwoPointCrossover(Crossover):

    def makeNewChild(self, parent1, parent2):
        matingIndex1 = random.randrange(len(self._targetWord))
        # ensure index1 != index2
        matingIndex2 = random.choice([i for i in range(len(self._targetWord)) if i != matingIndex1])

        # ensure index1 < index2
        if matingIndex1 > matingIndex2:
            temp = matingIndex1
            matingIndex1 = matingIndex2
            matingIndex2 = temp

        childStr = parent1.getStr()[:matingIndex1] + parent2.getStr()[matingIndex1:matingIndex2] + parent1.getStr()[
                                                                                                   matingIndex2:]
        return GeneticEntity(childStr)

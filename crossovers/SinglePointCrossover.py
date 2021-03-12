import random

from crossovers.Crossover import Crossover
from geneticentities.Entity import Entity


class SinglePointCrossover(Crossover):

    def makeNewChild(self, parent1, parent2):
        matingIndex = random.randrange(len(self.targetWord))

        childStr = parent1.getStr()[:matingIndex] + parent2.getStr()[matingIndex:]
        return Entity(childStr)

import random

from crossovers.Crossover import Crossover
from geneticentities.Entity import Entity


class UniformCrossover(Crossover):

    def makeNewChild(self, parent1, parent2):
        childStr = ''.join([parent1.getStr()[i] if random.random() < 0.5 else parent2.getStr()[i]
                            for i in range(len(self.targetWord))])

        return Entity(childStr)

import random

from entities.crossovers.Crossover import Crossover
from entities.GeneticEntity import GeneticEntity


class UniformCrossover(Crossover):

    def makeNewChild(self, parent1, parent2):
        childStr = ''.join([parent1.getStr()[i] if random.random() < 0.5 else parent2.getStr()[i]
                            for i in range(len(self._targetWord))])

        return GeneticEntity(childStr)

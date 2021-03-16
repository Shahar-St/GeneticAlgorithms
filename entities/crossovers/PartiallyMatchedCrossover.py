import random

import numpy as np

from entities.GeneticEntity import GeneticEntity
from entities.crossovers.Crossover import Crossover


class PartiallyMatchedCrossover(Crossover):

    def makeNewChild(self, parent1, parent2):
        parent1vec = parent1.getVec()
        parent2vec = parent2.getVec()

        size = len(parent1vec)

        newChildVec = np.copy(parent1vec)

        indexes = [i for i in range(size)]
        i = 0
        while len(indexes) > 1 and 1 / (i + 1) < random.random():
            index = random.choice(indexes)
            indexes.pop(index)
            indexes.pop(np.where(parent1vec == parent2vec[index])[0])

            newChildVec[index] = parent2vec[index]
            newChildVec[np.where(parent1vec == parent2vec[index])] = parent1vec[index]

        return GeneticEntity(newChildVec)

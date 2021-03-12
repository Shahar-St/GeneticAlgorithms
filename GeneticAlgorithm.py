import random

import numpy as np

from geneticentities.Entity import Entity
from util.Consts import BEST

class GeneticAlgorithm:

    def __init__(self, targetWord, population, fitnessFunction, eliteRate, mutationRate, maxIter):
        self._targetWord = targetWord
        self._population = population
        self._fitnessFunction = fitnessFunction
        self._popSize = len(self._population.getCitizens())
        self._eliteRate = eliteRate
        self._mutationRate = mutationRate
        self._maxIter = maxIter

    def findSolution(self):
        self._population.updateFitness()
        best = self._population.getCitizenAtIndex(BEST)

        # iterative improvement
        iterCounter = 0
        while best.getFitness() != 0 and iterCounter < self._maxIter:
            print(f'Best: {best.getStr()} ({best.getFitness()}). Mean: {self._population.getMean():.2f},'
                  f' STD: {self._population.getStd():.2f}')

            self._mate()

            self._population.updateFitness()
            best = self._population.getCitizenAtIndex(BEST)
            iterCounter += 1
        print(f'Best: {best.getStr()} ({best.getFitness()})')


    def _mate(self):
        eliteSize = int(self._popSize * self._eliteRate)
        citizens = self._population.getCitizens()

        tempPopulation = []
        for i in range(eliteSize):
            tempPopulation.append(citizens[i])

        for i in range(eliteSize, self._popSize):

            parent1 = random.randrange(int(self._popSize / 2))
            parent2 = random.randrange(int(self._popSize / 2))
            matingIndex = random.randrange(len(self._targetWord))
            childStr = citizens[parent1].getStr()[:matingIndex] + citizens[parent2].getStr()[matingIndex:]
            newChild = Entity(childStr)

            if random.random() < self._mutationRate:
                newChild.mutate()

            tempPopulation.append(newChild)

        self._population.setCitizens(np.array(tempPopulation))

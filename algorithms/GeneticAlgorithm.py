import random
import time

import numpy as np

from algorithms.Algorithm import Algorithm
from entities.GeneticEntity import GeneticEntity
from entities.parentselection.RandomParentSelection import RandomParentSelection

from util.Consts import ALLOWED_CHARS, BEST, CLOCK_RATE


class GeneticAlgorithm(Algorithm):

    def __init__(self, targetSize, fitnessFunction, popSize, eliteRate, crossoverFunc, mutationRate,
                 parentSelectionFunction):
        super().__init__(targetSize, fitnessFunction, popSize)

        self._citizens = np.array(
            [GeneticEntity(''.join(random.choice(ALLOWED_CHARS) for _ in range(targetSize))) for _ in
             range(popSize)])

        self._mean = None
        self._standardDeviation = None
        self._eliteRate = eliteRate
        self._crossoverFunc = crossoverFunc
        self._mutationRate = mutationRate
        self._parentSelectionFunction = parentSelectionFunction

    def findSolution(self, maxIter):
        startTime = time.time()
        self.updateFitness()

        best = self._citizens[BEST]

        # iterative improvement
        iterCounter = 0
        while best.getFitness() != 0 and iterCounter < maxIter:

            print(f'Best: {best.getStr()} ({best.getFitness()}). Mean: {self._mean:.2f},'
                  f' STD: {self._standardDeviation:.2f}')

            endTime = time.time()
            elapsedTime = endTime - startTime
            print("This generation took", elapsedTime * CLOCK_RATE, "clock ticks")

            startTime = time.time()

            self._mate()

            self.updateFitness()
            best = self._citizens[BEST]
            iterCounter += 1

        print(f'Best: {best.getStr()} ({best.getFitness()}). Mean: {self._mean:.2f},'
              f' STD: {self._standardDeviation:.2f}')

        endTime = time.time()
        elapsedTime = endTime - startTime
        print(f'This generation took {elapsedTime * CLOCK_RATE} clock ticks \n')

        print(f'Number of iterations: {iterCounter}\n')

        return best.getVec()

    def _mate(self):
        eliteSize = int(self._popSize * self._eliteRate)

        tempPopulation = []
        for i in range(eliteSize):
            tempPopulation.append(self._citizens[i])

        for i in range(eliteSize, self._popSize):

            parent1, parent2 = self._parentSelectionFunction.getParents(self._citizens)

            newChild = self._crossoverFunc(parent1, parent2)

            if random.random() < self._mutationRate:
                newChild.mutate()

            tempPopulation.append(newChild)

        self._citizens = np.array(tempPopulation)

    def updateFitness(self):
        fitnessValues = []
        for citizen in self._citizens:
            fitnessVal = self._fitnessFunction(citizen.getVec())
            citizen.setFitness(fitnessVal)
            fitnessValues.append(fitnessVal)

        self._citizens.sort()
        self._mean = np.mean(fitnessValues)
        self._standardDeviation = np.std(fitnessValues)
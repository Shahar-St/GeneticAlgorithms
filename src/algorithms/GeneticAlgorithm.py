import random

import numpy as np

from algorithms.Algorithm import Algorithm
from entities.GeneticEntity import GeneticEntity
from util.Consts import ALLOWED_CHARS, BEST, GA_CONTINUATION_RATE


class GeneticAlgorithm(Algorithm):

    def __init__(self, target, fitnessFunction, popSize, eliteRate, crossoverFunc, mutationRate):
        super().__init__(target, fitnessFunction, popSize)

        stringSize = len(target)
        self._citizens = np.array(
            [GeneticEntity(''.join(random.choice(ALLOWED_CHARS) for _ in range(stringSize))) for _ in
             range(popSize)])

        self._mean = None
        self._standardDeviation = None
        self._eliteRate = eliteRate
        self._crossoverFunc = crossoverFunc
        self._mutationRate = mutationRate

    def findSolution(self, maxIter):
        self.updateFitness()
        best = self._citizens[BEST]

        # iterative improvement
        iterCounter = 0
        while best.getFitness() != 0 and iterCounter < maxIter:
            print(f'Best: {best.getStr()} ({best.getFitness()}). Mean: {self._mean:.2f},'
                  f' STD: {self._standardDeviation:.2f}')

            self._mate()

            self.updateFitness()
            best = self._citizens[BEST]
            iterCounter += 1
        print(f'Best: {best.getStr()} ({best.getFitness()})')

    def _mate(self):
        eliteSize = int(self._popSize * self._eliteRate)

        tempPopulation = []
        for i in range(eliteSize):
            tempPopulation.append(self._citizens[i])

        for i in range(eliteSize, self._popSize):

            parent1 = self._citizens[random.randrange(int(self._popSize * GA_CONTINUATION_RATE))]
            parent2 = self._citizens[random.randrange(int(self._popSize * GA_CONTINUATION_RATE))]

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
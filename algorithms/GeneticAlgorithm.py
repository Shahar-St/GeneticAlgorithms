import random
import time

import numpy as np

from algorithms.Algorithm import Algorithm
from entities.GeneticEntity import GeneticEntity

from util.Consts import BEST, CLOCK_RATE


class GeneticAlgorithm(Algorithm):

    def __init__(self, problem, popSize, eliteRate, crossoverFunc, mutationRate,
                 mutationFunction, parentSelectionFunction, continuationRuleFunction):
        super().__init__(problem, popSize)

        self._citizens = np.array(
            [GeneticEntity(problem.generateRandomVec()) for _ in
             range(popSize)])

        self._mean = None
        self._standardDeviation = None
        self._eliteRate = eliteRate
        self._crossoverFunc = crossoverFunc
        self._mutationFunction = mutationFunction
        self._mutationRate = mutationRate
        self._parentSelectionFunction = parentSelectionFunction
        self._continuationRuleFunction = continuationRuleFunction
        self._problem = problem

    def findSolution(self, maxIter):
        startTime = time.time()
        self.updateFitness()

        best = self._citizens[BEST]

        # iterative improvement
        iterCounter = 0
        while best.getFitness() != 0 and iterCounter < maxIter:

            print(f'Best: {self._problem.translateVec(best.getVec())} ({best.getFitness()}). Mean: {self._mean:.2f},'
                  f' STD: {self._standardDeviation:.2f}')

            endTime = time.time()
            elapsedTime = endTime - startTime
            print("This generation took", elapsedTime * CLOCK_RATE, "clock ticks")

            startTime = time.time()

            self._mate()

            self.updateFitness()
            best = self._citizens[BEST]
            iterCounter += 1

        print(f'Best: {self._problem.translateVec(best.getVec())} ({best.getFitness()}). Mean: {self._mean:.2f},'
              f' STD: {self._standardDeviation:.2f}')

        endTime = time.time()
        elapsedTime = endTime - startTime
        print(f'This generation took {elapsedTime * CLOCK_RATE} clock ticks \n')

        print(f'Number of iterations: {iterCounter}\n')

        return best.getVec()

    def _mate(self):

        tempPopulation, secList = self._continuationRuleFunction(self._citizens, self._eliteRate)

        candidates = self._parentSelectionFunction(secList)
        candidatesSize = len(candidates)

        while len(tempPopulation) < self._popSize:
            parent1 = candidates[random.randrange(candidatesSize)]
            parent2 = candidates[random.randrange(candidatesSize)]
            newChild = self._crossoverFunc(parent1, parent2)

            if random.random() < self._mutationRate:
                newChild.setVec(self._mutationFunction(newChild.getVec()))

            tempPopulation.append(newChild)

        self._citizens = np.array(tempPopulation)

    def updateFitness(self):
        fitnessValues = []
        for citizen in self._citizens:
            fitnessVal = self._problem.calculateFitness(citizen.getVec())
            citizen.setFitness(fitnessVal)
            fitnessValues.append(fitnessVal)

        self._citizens.sort()
        self._mean = np.mean(fitnessValues)
        self._standardDeviation = np.std(fitnessValues)
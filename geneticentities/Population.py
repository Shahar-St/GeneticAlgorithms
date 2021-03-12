import random
import string

import numpy as np

from geneticentities.Entity import Entity


class Population:

    def __init__(self, target, fitnessFunction, popSize):
        self._target = target

        stringSize = len(target)

        self._citizens = np.array(
            [Entity(''.join(random.choice(string.printable) for _ in range(stringSize))) for _ in range(popSize)])

        self._fitnessFunction = fitnessFunction
        self._mean = None
        self._standardDeviation = None

    def updateFitness(self):
        fitnessValues = []
        for citizen in self._citizens:
            fitnessVal = self._fitnessFunction(citizen.getStr())
            citizen.setFitness(fitnessVal)
            fitnessValues.append(fitnessVal)

        self._citizens.sort()
        self._mean = np.mean(fitnessValues)
        self._standardDeviation = np.std(fitnessValues)

    def getCitizenAtIndex(self, index):
        return self._citizens[index]

    def getCitizens(self):
        return self._citizens

    def setCitizens(self, citizens):
        self._citizens = citizens

    def getMean(self):
        return self._mean

    def getStd(self):
        return self._standardDeviation

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

    def updateFitness(self):
        for citizen in self._citizens:
            citizen.setFitness(self._fitnessFunction(citizen.getStr()))

        self._citizens.sort()

    def getCitizenAtIndex(self, index):
        return self._citizens[index]

    def getCitizens(self):
        return self._citizens

    def setCitizens(self, citizens):
        self._citizens = citizens

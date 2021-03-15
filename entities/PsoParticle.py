import random

import numpy as np

from entities.IndividualEntity import IndividualEntity
from util.Consts import LOWER_BOUND, UPPER_BOUND


class PsoParticle(IndividualEntity):

    def __init__(self, stringVal):
        super().__init__(stringVal)

        self._positionVector = np.array([ord(char) for char in stringVal])
        self._pBestVec = np.copy(self._positionVector)
        self._velocity = np.array(
            [random.randint(-abs(LOWER_BOUND - UPPER_BOUND), abs(LOWER_BOUND - UPPER_BOUND)) for _ in
             stringVal])

    def getStr(self):
        return ''.join(chr(i) if LOWER_BOUND <= i <= UPPER_BOUND else i for i in self._positionVector)

    def getVec(self):
        return self._positionVector

    def getVelocity(self):
        return self._velocity

    def getPBestVec(self):
        return self._pBestVec

    def updatePosition(self, newVelocity):
        # update velocity
        self._velocity = newVelocity

        # updatePosition
        self._positionVector += newVelocity.astype(int)

    def updateFitness(self, fitness):
        if fitness < self._fitness:
            self._pBestVec = np.copy(self._positionVector)

        self.setFitness(fitness)

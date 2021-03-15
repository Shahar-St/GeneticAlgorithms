import random

import numpy as np

from entities.IndividualEntity import IndividualEntity
from util.Consts import ALLOWED_CHARS


class GeneticEntity(IndividualEntity):

    def __init__(self, stringVal):
        super().__init__(stringVal)

        self._age = 0

    def increaseAge(self):
        self._age += 1

    def getAge(self):
        return self._age

    def setAge(self, age):
        self._age = age

    def getVec(self):
        vec = np.array([ord(c) for c in self.getStr()])
        return vec

    def mutate(self):
        indexToMutate = random.randrange(len(self._stringVal))
        mutation = random.choice(ALLOWED_CHARS)
        self._stringVal = self._stringVal[:indexToMutate] + mutation + self._stringVal[indexToMutate + 1:]
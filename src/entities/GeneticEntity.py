import random

import numpy as np

from entities.IndividualEntity import IndividualEntity
from util.Consts import ALLOWED_CHARS


class GeneticEntity(IndividualEntity):

    def getVec(self):
        vec = np.array([ord(c) for c in self.getStr()])
        return vec

    def mutate(self):
        indexToMutate = random.randrange(len(self._stringVal))
        mutation = random.choice(ALLOWED_CHARS)
        self._stringVal = self._stringVal[:indexToMutate] + mutation + self._stringVal[indexToMutate + 1:]


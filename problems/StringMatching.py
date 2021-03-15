import random

import numpy as np

from problems.Problem import Problem
from util.Consts import ALLOWED_CHARS


class StringMatching(Problem):

    def generateRandomVec(self):
        randomString = ''.join(random.choice(ALLOWED_CHARS) for _ in range(len(self._targetVec)))
        return np.array([ord(c) for c in randomString])

    def translateVec(self, vec):
        return ''.join([chr(c) for c in vec])

    def _setTargetVec(self):
        return np.array([ord(c) for c in self._targetVal])

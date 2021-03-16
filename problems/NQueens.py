import numpy as np

from problems.Problem import Problem


class NQueens(Problem):

    def getTargetSize(self):
        return self._target

    def translateVec(self, vec):
        return vec

    def generateRandomVec(self):
        return np.random.permutation(self._target)

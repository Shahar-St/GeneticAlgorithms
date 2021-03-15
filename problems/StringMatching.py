import numpy as np

from problems.Problem import Problem


class StringMatching(Problem):

    def __init__(self, targetVal):
        super().__init__(targetVal)
        self._targetVec = np.array([ord(c) for c in self._targetVal])

    def _setTargetVec(self):
        return np.array([ord(c) for c in self._targetVal])


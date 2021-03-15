import numpy as np

from problems.Problem import Problem


class NQueens(Problem):

    def _setTargetVec(self):
        return np.copy(self._targetVal)
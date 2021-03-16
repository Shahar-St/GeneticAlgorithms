import itertools
import random

import numpy as np

from algorithms.Algorithm import Algorithm


class MinimalConflict(Algorithm):

    def __init__(self, problem, popSize):
        super().__init__(problem, popSize)

        size = self._problem.getTargetSize()
        queensPositions = []
        # self._board = np.full((size, size), False)

        availPos = [[i, j] for i, j in itertools.product(range(size), range(size))]
        for i in range(size):
            pos = random.choice(availPos)
            queensPositions.append(pos)
            # self._board[pos[0]][pos[1]] = True
            availPos.remove(pos)

        self._queensPositions = queensPositions

    def findSolution(self, maxIter):

        size = self._problem.getTargetSize()
        iterCounter = 0
        while not self._solutionFound() and iterCounter < maxIter:
            minAttacks = size + 1

            pickedQueenIndex = random.randrange(size)
            positions = self._availablePositions(pickedQueenIndex)
            minConflictPosition = (-1, -1)

            for pos in positions:

                # move queen to pos
                priorPosition = self._queensPositions[pickedQueenIndex]
                self._queensPositions[pickedQueenIndex] = pos

                newNumberOfConflicts = self._specificQueenConflicts(pos)
                if newNumberOfConflicts < minAttacks:
                    minConflictPosition = pos
                    minAttacks = newNumberOfConflicts

                # return the queen to prev place
                self._queensPositions[pickedQueenIndex] = priorPosition

            self._queensPositions[pickedQueenIndex] = minConflictPosition
            iterCounter += 1

        solution = np.zeros(size, dtype=int)
        for pos in self._queensPositions:
            solution[pos[0]] = pos[1]

        return solution

    def _solutionFound(self):

        tempQueensPos = np.array(self._queensPositions)
        rows = tempQueensPos[:, 0]
        cols = tempQueensPos[:, 1]

        if len(rows) != len(set(rows)) or len(cols) != len(set(cols)):
            return False

        size = self._problem.getTargetSize()

        i = 0
        while i < size:
            j = i + 1
            while j < size:
                if abs(rows[i] - rows[j]) == abs(cols[i] - cols[j]):
                    return False
                j += 1
            i += 1

        return True

    def _availablePositions(self, pickedQueen):
        pass


    def _specificQueenConflicts(self, pos):

        conflicts = 0

        tempQueensPos = np.copy(self._queensPositions)
        rows = tempQueensPos[:, 0]
        cols = tempQueensPos[:, 1]

        # row conflicts
        num, count = np.unique(rows, return_counts=True)
        for i in range(len(num)):
            conflicts += count[pos[0]] - 1

        # col conflicts
        num, count = np.unique(cols, return_counts=True)
        for i in range(len(num)):
            if num[i] == pos[1]:
                conflicts += count[i] - 1

        # dia conflicts
        for queenPos in tempQueensPos:
            if (queenPos[0] != pos[0] or queenPos[1] != pos[1]) and abs(queenPos[0] - pos[0]) == abs(
                    queenPos[1] - pos[1]):
                conflicts += 1

        return conflicts

from fitness.FitnessFunction import FitnessFunction


class BullsAndCows(FitnessFunction):

    def __init__(self, targetVal):
        super().__init__(targetVal)

    def calculate(self, vector):

        fitness = 0
        tempVec = vector.tolist()
        targetVec = [ord(c) for c in self._targetVal]

        i = 0
        while i < len(targetVec):
            if tempVec[i] == targetVec[i]:
                tempVec.pop(i)
                targetVec.pop(i)
            else:
                i += 1

        i = 0
        while i < len(tempVec):
            if tempVec[i] in targetVec:
                fitness += 1
                targetIndex = targetVec.index(tempVec[i])
                targetVec.pop(targetIndex)

            i += 1

        fitness += len(targetVec) * 2

        return fitness

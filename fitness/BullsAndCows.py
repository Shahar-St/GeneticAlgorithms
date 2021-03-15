from fitness.FitnessFunction import FitnessFunction


class BullsAndCows(FitnessFunction):


    def calculate(self, targetVec, vector):

        fitness = 0
        tempTargetVec = targetVec.tolist()
        tempVec = vector.tolist()

        i = 0
        while i < len(tempTargetVec):
            if tempVec[i] == tempTargetVec[i]:
                tempVec.pop(i)
                tempTargetVec.pop(i)
            else:
                i += 1

        i = 0
        while i < len(tempVec):
            if tempVec[i] in tempTargetVec:
                fitness += 1
                targetIndex = tempTargetVec.index(tempVec[i])
                tempTargetVec.pop(targetIndex)

            i += 1

        fitness += len(tempTargetVec) * 2

        return fitness

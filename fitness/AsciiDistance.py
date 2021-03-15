from fitness.FitnessFunction import FitnessFunction


class AsciiDistance(FitnessFunction):

    def __init__(self, problem):
        super().__init__(problem)

    def calculate(self, vector):

        targetVec = self._problem.getTargetVec()

        fitness = 0
        for newVal, targetElement in zip(vector, targetVec):
            fitness += abs(newVal - targetElement)

        return fitness

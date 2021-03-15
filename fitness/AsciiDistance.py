from fitness.FitnessFunction import FitnessFunction


class AsciiDistance(FitnessFunction):

    def __init__(self, targetVal):
        super().__init__(targetVal)

    def calculate(self, vector):

        fitness = 0
        for newVal, targetChar in zip(vector, self._targetVal):
            fitness += abs(newVal - ord(targetChar))

        return fitness

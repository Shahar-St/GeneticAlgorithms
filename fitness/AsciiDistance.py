from fitness.FitnessFunction import FitnessFunction


class AsciiDistance(FitnessFunction):


    def calculate(self, targetVec, vector):

        fitness = 0
        for newVal, targetElement in zip(vector, targetVec):
            fitness += abs(newVal - targetElement)

        return fitness

from fitness.FitnessFunction import FitnessFunction



class EuclideanDistance(FitnessFunction):

    def __init__(self, targetVal):
        super().__init__(targetVal)
        self.targetAsciiVal = sum(map(ord, targetVal))

    def calculate(self, stringVal):


        fitness = 0
        for originChar, targetChar in zip(stringVal, self.targetVal):
            fitness += abs(ord(originChar) - ord(targetChar))

        return fitness

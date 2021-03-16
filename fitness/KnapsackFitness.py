import numpy as np

from fitness.FitnessFunction import FitnessFunction


class KnapsackFitness(FitnessFunction):

    def calculate(self, problem, vector):

        gain = problem.calculateGain(vector)
        if problem.getWeight(vector) > problem.getC():
            return problem.getOptimalCost()

        return problem.getOptimalCost() - gain
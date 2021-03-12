from GeneticAlgorithm import GeneticAlgorithm
from fitness.EuclideanDistance import EuclideanDistance
from geneticentities.Population import Population
from util.Consts import GA_TARGET, GA_POP_SIZE, GA_ELITE_RATE, GA_MUTATION_RATE, GA_MAX_ITER


def main():
    fitnessFunction = EuclideanDistance(GA_TARGET).calculate
    population = Population(GA_TARGET, fitnessFunction, GA_POP_SIZE)

    algo = GeneticAlgorithm(GA_TARGET, population, fitnessFunction, GA_ELITE_RATE, GA_MUTATION_RATE, GA_MAX_ITER)
    algo.findSolution()


if __name__ == '__main__':
    main()

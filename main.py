from GeneticAlgorithm import GeneticAlgorithm
from crossovers.SinglePointCrossover import SinglePointCrossover
from crossovers.TwoPointCrossover import TwoPointCrossover
from crossovers.UniformCrossover import UniformCrossover
from fitness.EuclideanDistance import EuclideanDistance
from geneticentities.Population import Population
from util.Consts import GA_TARGET, GA_POP_SIZE, GA_ELITE_RATE, GA_MUTATION_RATE, GA_MAX_ITER


def main():
    fitnessFunction = EuclideanDistance(GA_TARGET).calculate
    population = Population(GA_TARGET, fitnessFunction, GA_POP_SIZE)
    crossover = UniformCrossover(GA_TARGET)

    algo = GeneticAlgorithm(GA_TARGET, population, fitnessFunction, GA_ELITE_RATE,
                            GA_MUTATION_RATE, GA_MAX_ITER, crossover.makeNewChild)
    algo.findSolution()


if __name__ == '__main__':
    main()

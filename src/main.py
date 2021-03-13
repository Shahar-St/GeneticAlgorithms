from algorithms.PSO import PSO
from entities.crossovers.UniformCrossover import UniformCrossover
from fitness.AsciiDistance import AsciiDistance
from algorithms.GeneticAlgorithm import GeneticAlgorithm
from util.Consts import GA_TARGET, GA_POP_SIZE, GA_ELITE_RATE, GA_MUTATION_RATE, GA_MAX_ITER


def main():

    fitnessFunction = AsciiDistance(GA_TARGET).calculate
    crossoverFunc = UniformCrossover(GA_TARGET).makeNewChild

    pso = PSO(GA_TARGET, fitnessFunction, GA_POP_SIZE)
    solVec = pso.findSolution(GA_MAX_ITER)
    print(''.join([chr(i) for i in solVec]))

    geneticAlgo = GeneticAlgorithm(GA_TARGET, fitnessFunction, GA_POP_SIZE, GA_ELITE_RATE, crossoverFunc, GA_MUTATION_RATE)
    geneticAlgo.findSolution(GA_MAX_ITER)


if __name__ == '__main__':
    main()

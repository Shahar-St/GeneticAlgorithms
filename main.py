import time

import argparse
from algorithms.Algorithm import Algorithm
from entities.crossovers.Crossover import Crossover
from fitness.FitnessFunction import FitnessFunction
from util.Consts import GA_TARGET, GA_POP_SIZE, GA_ELITE_RATE, GA_MUTATION_RATE, GA_MAX_ITER


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-a', '--algo', default='GeneticAlgorithm', help='the algo will be process')
    parser.add_argument('-c', '--cross', default='SinglePointCrossover', help='the cross will be process')
    parser.add_argument('-f', '--fitness', default='AsciiDistance', help='the fitness will be process')
    args = parser.parse_args()

    fitnessName = args.fitness
    fitnessFunction = FitnessFunction.factory(fitnessName, GA_TARGET).calculate

    crossoverName = args.cross
    crossoverFunction = Crossover.factory(crossoverName, GA_TARGET).makeNewChild

    algoName = args.algo
    algo = Algorithm.factory(algoName, GA_TARGET, fitnessFunction, GA_POP_SIZE, GA_ELITE_RATE, crossoverFunction,
                             GA_MUTATION_RATE)

    startTime = time.time()

    solVec = algo.findSolution(GA_MAX_ITER)
    print('Solution = ' + ''.join([chr(i) for i in solVec]))

    endTime = time.time()

    print("Elapsed time in seconds:", endTime - startTime)


if __name__ == '__main__':
    main()

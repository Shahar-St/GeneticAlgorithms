import time

import argparse
from algorithms.Algorithm import Algorithm
from entities.crossovers.Crossover import Crossover
from entities.parentselection.ParentSelection import ParentSelection
from fitness.FitnessFunction import FitnessFunction
from problems.Problem import Problem
from util.Consts import GA_TARGET, GA_POP_SIZE, GA_ELITE_RATE, GA_MUTATION_RATE, GA_MAX_ITER, ALLOWED_ALGO_NAMES, \
    ALLOWED_FITNESS_NAMES, ALLOWED_CROSS_NAMES, CLOCK_RATE, DEFAULT_FITNESS, DEFAULT_CROSSOVER, DEFAULT_ALGORITHM, \
    DEFAULT_PROBLEM, ALLOWED_PROBLEM_NAMES, DEFAULT_PARENT_SELECTION_FUNC, ALLOWED_PARENT_SELECTION_FUNC_NAMES


def main():
    startTime = time.time()

    parser = argparse.ArgumentParser()

    parser.add_argument('-a', '--algo', default=DEFAULT_ALGORITHM, help='the algo will be process')
    parser.add_argument('-c', '--cross', default=DEFAULT_CROSSOVER, help='the cross will be process')
    parser.add_argument('-f', '--fitness', default=DEFAULT_FITNESS, help='the fitness will be process')
    parser.add_argument('-p', '--problem', default=DEFAULT_PROBLEM, help='Problem to be solved')
    parser.add_argument('-s', '--parentSelection', default=DEFAULT_PARENT_SELECTION_FUNC, help='Problem to be solved')
    args = parser.parse_args()

    if args.algo not in ALLOWED_ALGO_NAMES:
        print("invalid algo! \n")
        return
    if args.cross not in ALLOWED_CROSS_NAMES:
        print("invalid cross function! \n")
        return
    if args.fitness not in ALLOWED_FITNESS_NAMES:
        print("invalid fitness function! \n")
        return
    if args.problem not in ALLOWED_PROBLEM_NAMES:
        print("invalid problem! \n")
        return
    if args.parentSelection not in ALLOWED_PARENT_SELECTION_FUNC_NAMES:
        print("invalid parent selection function! \n")
        return

    problem = Problem.factory(args.problem, GA_TARGET)
    fitnessFunction = FitnessFunction.factory(args.fitness, problem).calculate
    crossoverFunction = Crossover.factory(args.cross, GA_TARGET).makeNewChild
    parentSelectionFunction = ParentSelection.factory(args.parentSelection)
    algo = Algorithm.factory(args.algo, len(GA_TARGET), fitnessFunction, GA_POP_SIZE, GA_ELITE_RATE, crossoverFunction,
                             GA_MUTATION_RATE, parentSelectionFunction)

    solVec = algo.findSolution(GA_MAX_ITER)
    print('Solution = ' + ''.join([chr(i) for i in solVec]) + '\n')

    endTime = time.time()

    elapsedTime = endTime - startTime

    print(f'Elapsed time in seconds: {elapsedTime}')
    print(f'This process took {elapsedTime * CLOCK_RATE} clock ticks')


if __name__ == '__main__':
    main()

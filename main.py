import time

import argparse
import traceback

from algorithms.Algorithm import Algorithm
from entities.crossovers.Crossover import Crossover
from entities.mutations.Mutation import Mutation
from entities.parentselection.ParentSelection import ParentSelection
from fitness.FitnessFunction import FitnessFunction
from problems.Problem import Problem
from util.Consts import *


def main():
    startTime = time.time()

    parser = argparse.ArgumentParser()

    parser.add_argument('-a', '--algo', default=DEFAULT_ALGORITHM, help='the algo will be process')
    parser.add_argument('-c', '--cross', default=DEFAULT_CROSSOVER, help='the cross will be process')
    parser.add_argument('-f', '--fitness', default=DEFAULT_FITNESS, help='the fitness will be process')
    parser.add_argument('-p', '--problem', default=DEFAULT_PROBLEM, help='Problem to be solved')
    parser.add_argument('-s', '--parentSelection', default=DEFAULT_PARENT_SELECTION_FUNC, help='Problem to be solved')
    parser.add_argument('-m', '--mutation', default=DEFAULT_MUTATION, help='Mutation method to be used')
    parser.add_argument('-t', '--target', default=DEFAULT_TARGET, help='Target to find')
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
    if args.mutation not in ALLOWED_MUTATION_NAMES:
        return

    fitnessFunction = FitnessFunction.factory(args.fitness).calculate
    problem = Problem.factory(args.problem, fitnessFunction, len(args.target), args.target)

    crossoverFunction = Crossover.factory(args.cross).makeNewChild
    parentSelectionFunction = ParentSelection.factory(args.parentSelection)
    mutationFunction = Mutation.factory(args.mutation).mutate

    algo = Algorithm.factory(algoName=args.algo,
                             popSize=GA_POP_SIZE,
                             eliteRate=GA_ELITE_RATE,
                             crossoverFunc=crossoverFunction,
                             mutationRate=GA_MUTATION_RATE,
                             mutationFunction=mutationFunction,
                             parentSelectionFunction=parentSelectionFunction,
                             problem=problem
                             )

    solVec = algo.findSolution(GA_MAX_ITER)
    print(f'Solution = {problem.translateVec(solVec)}\n')

    endTime = time.time()

    elapsedTime = endTime - startTime

    print(f'Elapsed time in seconds: {elapsedTime}')
    print(f'This process took {elapsedTime * CLOCK_RATE} clock ticks')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        traceback.print_exc()

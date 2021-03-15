import importlib
from abc import ABC, abstractmethod


class Algorithm(ABC):

    def __init__(self, problem, popSize):
        self._popSize = popSize
        self._problem = problem

    @abstractmethod
    def findSolution(self, maxIter):
        raise NotImplementedError

    @staticmethod
    def factory(algoName, popSize, eliteRate, crossoverFunc, mutationRate,
                mutationFunction, parentSelectionFunction, problem):
        module = importlib.import_module('algorithms.' + algoName)

        algo = getattr(module, algoName)

        if algoName == 'PSO':
            return algo(problem=problem,
                        popSize=popSize
                        )

        if algoName == 'GeneticAlgorithm':
            return algo(problem=problem,
                        popSize=popSize,
                        eliteRate=eliteRate,
                        crossoverFunc=crossoverFunc,
                        mutationRate=mutationRate,
                        mutationFunction=mutationFunction,
                        parentSelectionFunction=parentSelectionFunction
                        )

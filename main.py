import random

import numpy as np

from fitness.EuclideanDistance import EuclideanDistance
from geneticentities.Entity import Entity
from geneticentities.Population import Population
from util.Consts import GA_TARGET, GA_POP_SIZE, GA_ELITE_RATE, GA_MUTATION_RATE, BEST, GA_MAX_ITER



def mate(population):
    eliteSize = int(GA_POP_SIZE * GA_ELITE_RATE)
    citizens = population.getCitizens()

    tempPopulation = []
    for i in range(eliteSize):
        tempPopulation.append(citizens[i])

    for i in range(eliteSize, GA_POP_SIZE):

        parent1 = random.randrange(GA_POP_SIZE / 2)
        parent2 = random.randrange(GA_POP_SIZE / 2)
        matingIndex = random.randrange(len(GA_TARGET))
        childStr = citizens[parent1].getStr()[:matingIndex] + citizens[parent2].getStr()[matingIndex:]
        newChild = Entity(childStr)

        if random.random() < GA_MUTATION_RATE:
            newChild.mutate()

        tempPopulation.append(newChild)

    population.setCitizens(np.array(tempPopulation))


def main():
    fitnessFunction = EuclideanDistance(GA_TARGET).calculate
    population = Population(GA_TARGET, fitnessFunction, GA_POP_SIZE)

    population.updateFitness()
    best = population.getCitizenAtIndex(BEST)

    # iterative improvement
    iterCounter = 0
    while best.getFitness() != 0 and iterCounter < GA_MAX_ITER:
        print(f'Best: {best.getStr()} ({best.getFitness()})')

        mate(population)

        population.updateFitness()
        best = population.getCitizenAtIndex(BEST)
        iterCounter += 1
    print(f'Best: {best.getStr()} ({best.getFitness()})')


if __name__ == '__main__':
    main()

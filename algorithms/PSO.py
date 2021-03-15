import random

import numpy as np

from algorithms.Algorithm import Algorithm
from entities.PsoParticle import PsoParticle
from util.Consts import COGNITIVE_WEIGHT, SOCIAL_WEIGHT


class PSO(Algorithm):

    def __init__(self, problem, popSize):
        super().__init__(problem, popSize)
        self._swarm = np.array(
            [PsoParticle(problem.generateRandomVec()) for _ in
             range(popSize)])
        self._gBestVal = np.inf
        self._gBestVec = None
        self._solutionFound = False
        self._solutionParticle = None
        self._problem = problem

        for particle in self._swarm:

            fitness = self._problem.calculateFitness(particle.getVec())
            particle.setFitness(fitness)
            if fitness < self._gBestVal:
                self._gBestVal = fitness
                self._gBestVec = np.copy(particle.getVec())
                if fitness == 0:
                    self._solutionFound = True

    def findSolution(self, maxIter):

        inertiaArr = np.linspace(0.4, 0.9, num=maxIter)

        i = 0
        while not self._solutionFound and i < maxIter:
            j = 0
            while j < len(self._swarm):
                particle = self._swarm[j]

                cognitiveRand = random.random()
                socialRand = random.random()

                newInertia = inertiaArr[i] * particle.getVelocity()
                newCognitiveComp = COGNITIVE_WEIGHT * cognitiveRand * (particle.getPBestVec() - particle.getVec())
                newSocialComp = SOCIAL_WEIGHT * socialRand * (self._gBestVec - particle.getVec())
                newVelocity = newInertia + newCognitiveComp + newSocialComp

                particle.updatePosition(newVelocity)
                newFitness = self._problem.calculateFitness(particle.getVec())
                particle.updateFitness(newFitness)

                if newFitness < self._gBestVal:
                    self._gBestVal = newFitness
                    self._gBestVec = np.copy(particle.getVec())
                    if newFitness == 0:
                        self._solutionFound = True
                        return particle.getVec()
                j += 1
            i += 1

        return self._gBestVec

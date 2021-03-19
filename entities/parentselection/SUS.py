import math
import random
import numpy as np
from entities.parentselection.ParentSelection import ParentSelection


class SUS(ParentSelection):

    def getCandidates(self, citizens):

        candidates = []
        fitnessSum = 0
        for i in range(len(citizens)):
            fitnessSum += math.sqrt(citizens[i].getFitness())                              # scaling with sqrt

        fitnessRate = []

        for i in range(len(citizens)):
            fitnessRate.append(math.sqrt(citizens[i].getFitness()) / fitnessSum)   # scaling with sqrt

        cumFitnessRate = list(np.cumsum(np.flip(fitnessRate)))

        r = random.random()
        for i in range(len(cumFitnessRate)):

            i = 0
            found = False
            while i < len(cumFitnessRate) and not found:
                if r < cumFitnessRate[i]:
                    candidates.append(citizens[i])
                    found = True
                i += 1

            r += (1/len(citizens))
            if r >= 1:
                r = r - 1

        return np.array(candidates)
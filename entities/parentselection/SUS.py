import math
import random
import numpy as np
from entities.parentselection.ParentSelection import ParentSelection


class SUS(ParentSelection):

    def getCandidates(self, citizens):

        candidates = []
        sumFitness = 0
        for i in range(len(citizens)):
            sumFitness += math.sqrt(citizens[i].getFitness())                              # scaling with sqrt

        rateFitnessCitizens = []

        for i in range(len(citizens)):
            rateFitnessCitizens.append(math.sqrt(citizens[i].getFitness()) / sumFitness)   # scaling with sqrt

        rev = np.flip(rateFitnessCitizens)
        cum_rateFitness = list(np.cumsum(rev))

        r = random.random()
        for i in range(len(cum_rateFitness)):
            i = 0
            while r > cum_rateFitness[i]:
                i += 1
            candidates.append(citizens[i])
            r += (1/len(citizens))
            if r >= 1:
                r = r - 1

        return np.array(candidates)
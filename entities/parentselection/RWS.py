import math
import random
import numpy as np
from entities.parentselection.ParentSelection import ParentSelection




class RWS(ParentSelection):

    def getCandidates(self, citizens):

        candidates = []
        sumFitness = 0
        for i in range(len(citizens)):
            sumFitness += math.sqrt(citizens[i].getFitness())                               # scaling with sqrt

        rateFitnessCitizens = []
        
        for i in range(len(citizens)):
            rateFitnessCitizens.append(math.sqrt(citizens[i].getFitness()) / sumFitness)    # scaling with sqrt

        rev = np.flip(rateFitnessCitizens)

        cum_rateFitness = list(np.cumsum(rev))

        for j in range(len(cum_rateFitness)):
            r = random.random()

            i = 0
            found = False
            while i < len(cum_rateFitness) and not found:
                if r < cum_rateFitness[i]:
                    candidates.append(citizens[i])
                    found = True
                i += 1

        return np.array(candidates)
import random
from math import sqrt
import numpy as np
from entities.parentselection.ParentSelection import ParentSelection


class StochasticTournament(ParentSelection):

    def getCandidates(self, citizens):

        candidates = []
        citizensSize = len(citizens)

        for j in range(citizensSize):

            k = random.randrange(1, int(sqrt(citizensSize)))
            participantsTournament = []

            for i in range(k):
                participantsTournament.append((citizens[random.randrange(len(citizens))]))
            participantsTournament.sort()

            sumFitness = 0
            for i in range(len(participantsTournament)):
                sumFitness += participantsTournament[i].getFitness()

            rateFitnessCitizens = []

            for i in range(len(participantsTournament)):
                rateFitnessCitizens.append(participantsTournament[i].getFitness() / sumFitness)

            rev = np.flip(rateFitnessCitizens)

            cum_rateFitness = list(np.cumsum(rev))

            r = random.random()
            i = 0
            found = False
            while i < len(cum_rateFitness) and not found:
                if r < cum_rateFitness[i]:
                    candidates.append(participantsTournament[i])
                    found = True
                i += 1

        return np.array(candidates)

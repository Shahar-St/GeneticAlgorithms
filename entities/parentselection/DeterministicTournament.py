import random
from math import sqrt

import numpy as np

from entities.GeneticEntity import GeneticEntity
from entities.parentselection.ParentSelection import ParentSelection
from util.Consts import BEST


class DeterministicTournament(ParentSelection):

    def getCandidates(self, citizens):

        candidates = []
        citizensSize = len(citizens)

        for j in range(citizensSize):
            k = random.randrange(1, int(sqrt(citizensSize)))
            participantsTournament = []

            for i in range(k):
                participantsTournament.append((citizens[random.randrange(len(citizens))]))

            winner = min(participantsTournament)
            candidates.append(winner)

        return np.array(candidates)
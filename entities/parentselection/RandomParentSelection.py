from entities.parentselection.ParentSelection import ParentSelection
from util.Consts import GA_CONTINUATION_RATE

import random


class RandomParentSelection(ParentSelection):

    def getParents(self, candidates):
        size = len(candidates)

        parent1 = candidates[random.randrange(int(size * GA_CONTINUATION_RATE))]
        parent2 = candidates[random.randrange(int(size * GA_CONTINUATION_RATE))]

        return parent1, parent2

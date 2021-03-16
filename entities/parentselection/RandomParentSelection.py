import numpy as np

from entities.parentselection.ParentSelection import ParentSelection




class RandomParentSelection(ParentSelection):

    def getCandidates(self, citizens):

        sizeCitizens = len(citizens)
        candidates = []

        for i in range(int(sizeCitizens / 2)):
            candidates.append(citizens[i])

        return np.array(candidates)

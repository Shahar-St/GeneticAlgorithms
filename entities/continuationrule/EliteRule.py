from abc import ABC

import numpy as np

from entities.continuationrule.ContinuationRule import ContinuationRule


class EliteRule(ContinuationRule, ABC):

    def getNextGenAndPotentialParents(self, citizens, eliteRate):

        firstList = []
        secList = citizens

        eliteSize = int(len(citizens) * eliteRate)

        for i in range(eliteSize):
            citizens[i].increaseAge()
            firstList.append(citizens[i])


        return firstList, np.array(secList)
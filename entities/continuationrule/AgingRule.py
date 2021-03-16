from abc import ABC

import numpy as np

from entities.continuationrule.ContinuationRule import ContinuationRule
from util.Consts import AGE_DIE, AGE_MIN_TO_BE_PARENT


class AgingRule(ContinuationRule, ABC):

    def getNextGenAndPotentialParents(self, citizens, eliteRate):

        firstList = []
        secList = []

        for i in range(len(citizens)):
            citizens[i].increaseAge()
            if (citizens[i].getAge()) >= AGE_DIE:
                citizens.pop(i)

        firstList = citizens

        for i in range(len(citizens)):
            if (citizens[i].getAge()) >= AGE_MIN_TO_BE_PARENT:
                secList.append(citizens[i])

        return firstList, np.array(secList)


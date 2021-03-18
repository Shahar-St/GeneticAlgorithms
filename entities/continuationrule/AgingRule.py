from abc import ABC

import numpy as np

from entities.continuationrule.ContinuationRule import ContinuationRule
from util.Consts import AGE_DIE, AGE_MIN_TO_BE_PARENT


class AgingRule(ContinuationRule, ABC):

    def getNextGenAndPotentialParents(self, citizens, _):

        tempCitizens = []
        secList = []

        for i in range(len(citizens)):
            citizens[i].increaseAge()
            if (citizens[i].getAge()) < AGE_DIE:
                tempCitizens.append(citizens[i])


        for i in range(len(citizens)):
            if (citizens[i].getAge()) >= AGE_MIN_TO_BE_PARENT:
                secList.append(citizens[i])

        return tempCitizens, np.array(secList)


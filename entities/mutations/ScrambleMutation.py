import random

from entities.mutations.Mutation import Mutation
from util.Util import getValidIndexes


class ScrambleMutation(Mutation):

    def mutate(self, vec):
        vecSize = len(vec)
        index1, index2 = getValidIndexes(vecSize)

        elementsToShuffle = vec[index1:index2 + 1]
        random.shuffle(elementsToShuffle)

        return vec[:index1] + elementsToShuffle + vec[index2 + 1:]
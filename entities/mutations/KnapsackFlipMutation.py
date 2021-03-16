import random

from entities.mutations.Mutation import Mutation


class KnapsackFlipMutation(Mutation):

    def mutate(self, vec):
        indexToMutate = random.randrange(len(vec))
        if vec[indexToMutate] == 1:
            vec[indexToMutate] = 0
        else:
            vec[indexToMutate] = 1

        return vec
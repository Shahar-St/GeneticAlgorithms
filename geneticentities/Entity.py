import random
import string


class Entity:

    def __init__(self, stringVal):
        self._stringVal = stringVal
        self._fitness = 0

    def getFitness(self):
        return self._fitness

    def setFitness(self, fitness):
        self._fitness = fitness

    def getStr(self):
        return self._stringVal

    def mutate(self):
        indexToMutate = random.randrange(len(self._stringVal))
        mutation = random.choice(string.printable)
        self._stringVal = self._stringVal[:indexToMutate] + mutation + self._stringVal[indexToMutate + 1:]

    def __lt__(self, other):
        return self.getFitness() < other.getFitness()

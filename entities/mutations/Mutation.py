import importlib
from abc import ABC, abstractmethod


class Mutation(ABC):

    @abstractmethod
    def mutate(self, vec):
        raise NotImplementedError

    @staticmethod
    def factory(mutationName):
        module = importlib.import_module('entities.mutations.' + mutationName)
        cross = getattr(module, mutationName)
        return cross()

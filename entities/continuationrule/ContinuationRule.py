import importlib
from abc import ABC, abstractmethod


class ContinuationRule(ABC):
    
    # def __init__(self):
    #     pass
    
    @abstractmethod
    def getNextGenAndPotentialParents(self, citizens, eliteRate):
        raise NotImplementedError
    
    @staticmethod
    def factory(continuationRuleName):
        module = importlib.import_module('entities.continuationrule.' + continuationRuleName)
        continuationRule = getattr(module, continuationRuleName)
        return continuationRule()
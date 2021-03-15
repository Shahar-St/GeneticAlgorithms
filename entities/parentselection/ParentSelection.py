import importlib
from abc import ABC, abstractmethod


class ParentSelection(ABC):

    @abstractmethod
    def getParents(self, candidates):
        raise NotImplementedError

    @staticmethod
    def factory(parentSelectionName):
        module = importlib.import_module('entities.parentselection.' + parentSelectionName)
        parentSelection = getattr(module, parentSelectionName)
        return parentSelection()

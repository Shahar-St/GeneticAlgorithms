from entities.IndividualEntity import IndividualEntity


class GeneticEntity(IndividualEntity):

    def __init__(self, stringVal):
        super().__init__(stringVal)

        self._age = 0

    def increaseAge(self):
        self._age += 1

    def getAge(self):
        return self._age


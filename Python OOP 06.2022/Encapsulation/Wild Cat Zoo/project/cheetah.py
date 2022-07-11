from project.animal import Animal


class Cheetah(Animal):

    MONEY_FOR_CARE = 60

    def __init__(self, name, gender, age):
        Animal.__init__(self, name, gender, age, self.MONEY_FOR_CARE)

from project.food.main_dish import MainDish


class Salmon(MainDish):

    GRAMS = 22

    def __init__(self, name, price):
        MainDish.__init__(self, name, price, self.GRAMS)

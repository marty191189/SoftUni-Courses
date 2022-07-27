from project.cat import Cat


class Kitten(Cat):

    def __init__(self, name, age):
        super().__init__(name, age, "Female")

    def make_sound(self):
        return f"Meow"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

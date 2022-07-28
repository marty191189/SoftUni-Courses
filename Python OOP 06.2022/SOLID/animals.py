from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):

    def make_sound(self):
        return "Meow"


class Dog(Animal):

    def make_sound(self):
        return "Woof"


def animal_sound(animals_list: list):

    for animal in animals_list:
        print(animal.make_sound())


animals = [Cat(), Dog()]
animal_sound(animals)

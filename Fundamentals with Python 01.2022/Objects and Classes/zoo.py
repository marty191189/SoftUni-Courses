class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):

        if species == "mammal":
            self.mammals.append(name)

        elif species == "fish":
            self.fish.append(name)

        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):

        result = ""

        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}"

        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fish)}"

        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}"

        result += f"\nTotal animals: {Zoo.__animals}"

        return result
        

name_of_zoo = input()
zoo = Zoo(name_of_zoo)
number_of_lines = int(input())

for line in range(number_of_lines):
    info = input().split(" ")
    species = info[0]
    type_of_animal = info[1]
    zoo.add_animal(species, type_of_animal)

additional_info = input()
print(zoo.get_info(additional_info))

# втори начин
#
# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def get_animals_count(self):
#         return self.__animals
#
#     def add_animal(self, species, name):
#         if species == "mammal":
#             self.mammals.append(name)
#         elif species == "fish":
#             self.fishes.append(name)
#         elif species == "bird":
#             self.birds.append(name)
#
#         self.__animals += 1
#
#     def get_info(self, species):
#         if species == "mammal":
#             return f"Mammals in {self.name}: {', '.join(self.mammals)}"
#         elif species == "fish":
#             return f"Fishes in {self.name}: {', '.join(self.fishes)}"
#         elif species == "bird":
#             return f"Birds in {self.name}: {', '.join(self.birds)}"
#
#
# name = input()
# n = int(input())
# zoo = Zoo(name)
#
# for num in range(n):
#     species, name = input().split()
#     zoo.add_animal(species, name)
#
# searched_species = input()
# print(zoo.get_info(searched_species))
# print(f"Total animals: {zoo.get_animals_count()}")

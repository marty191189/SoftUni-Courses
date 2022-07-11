class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):

        if price <= self.__budget and 0 < self.__animal_capacity:
            self.__budget -= price
            self.__animal_capacity -= 1
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif price > self.__budget and 0 < self.__animal_capacity:
            return "Not enough budget"

        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):

        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):

        for worker in self.workers:

            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):

        salaries_to_pay = sum([worker.salary for worker in self.workers])

        if self.__budget < salaries_to_pay:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries_to_pay
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):

        total_price_animal_food = sum([animal.money_for_care for animal in self.animals])

        if self.__budget < total_price_animal_food:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= total_price_animal_food
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):

        result = f"You have {len(self.animals)} animals\n"

        lions_list = [0]
        tigers_list = [0]
        cheetahs_list = [0]

        for animal in self.animals:

            if animal.__class__.__name__ == "Lion":
                lions_list[0] += 1
                lions_list.append(animal)

            elif animal.__class__.__name__ == "Tiger":
                tigers_list[0] += 1
                tigers_list.append(animal)

            elif animal.__class__.__name__ == "Cheetah":
                cheetahs_list[0] += 1
                cheetahs_list.append(animal)

        result += f"----- {lions_list[0]} Lions:\n"
        lions_list.pop(0)
        result += "\n".join([animal.__repr__() for animal in lions_list]) + "\n"

        result += f"----- {tigers_list[0]} Tigers:\n"
        tigers_list.pop(0)
        result += "\n".join([animal.__repr__() for animal in tigers_list]) + "\n"

        result += f"----- {cheetahs_list[0]} Cheetahs:\n"
        cheetahs_list.pop(0)
        result += "\n".join([animal.__repr__() for animal in cheetahs_list]) + "\n"

        return result.strip()

    def workers_status(self):

        result = f"You have {len(self.workers)} workers\n"

        keepers_list = [0]
        caretakers_list = [0]
        vets_list = [0]

        for worker in self.workers:

            if worker.__class__.__name__ == "Keeper":
                keepers_list[0] += 1
                keepers_list.append(worker)

            elif worker.__class__.__name__ == "Caretaker":
                caretakers_list[0] += 1
                caretakers_list.append(worker)

            elif worker.__class__.__name__ == "Vet":
                vets_list[0] += 1
                vets_list.append(worker)

        result += f"----- {keepers_list[0]} Keepers:\n"
        keepers_list.pop(0)
        result += "\n".join([worker.__repr__() for worker in keepers_list]) + "\n"

        result += f"----- {caretakers_list[0]} Caretakers:\n"
        caretakers_list.pop(0)
        result += "\n".join([worker.__repr__() for worker in caretakers_list]) + "\n"

        result += f"----- {vets_list[0]} Vets:\n"
        vets_list.pop(0)
        result += "\n".join([worker.__repr__() for worker in vets_list]) + "\n"

        return result.strip()

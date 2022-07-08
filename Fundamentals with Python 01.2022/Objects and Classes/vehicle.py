class Vehicle:

    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if money >= self.price and self.owner is None:
            self.owner = owner
            change = money - self.price
            text = f"Successfully bought a {self.type}. Change: {change:.2f}"
            return text

        elif self.price > money:
            text = "Sorry, not enough money"
            return text

        else:
            text = "Car already sold"
            return text

    def sell(self):
        if self.owner is not None:
            self.owner = None

        else:
            text = "Vehicle has no owner"
            return text

    def __repr__(self):
        if self.owner is not None:
            text = f"{self.model} {self.type} is owned by: {self.owner}"
            return text

        else:
            text = f"{self.model} {self.type} is on sale: {self.price}"
            return text


# code to test the class
#
# vehicle_type = "car"
# model = "BMW"
# price = 30000
# vehicle = Vehicle(vehicle_type, model, price)
# print(vehicle.buy(15000, "Peter"))
# print(vehicle.buy(35000, "George"))
# print(vehicle)
# vehicle.sell()
# print(vehicle)

class Cup:

    def __init__(self, size: int, quantity: int):
        self.size = int(size)
        self.quantity = int(quantity)

    def fill(self, quantity: int):
        if self.quantity + int(quantity) <= self.size:
            self.quantity += int(quantity)

    def status(self):
        result = self.size - self.quantity
        return result


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())

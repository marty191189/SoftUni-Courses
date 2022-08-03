import copy


class Person:

    def __init__(self, position):
        self.position = position


class Prisoner(Person):

    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super(Prisoner, self).__init__(copy.copy(self.PRISON_LOCATION))


prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")

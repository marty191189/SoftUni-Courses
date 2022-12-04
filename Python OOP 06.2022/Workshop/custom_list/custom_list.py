class CustomList:

    def __init__(self):
        self.__values = []

    def append(self, val):
        self.__values.append(val)

    def remove(self, index):

        try:
            element = self.__values.pop(index)
            return element

        except IndexError:
            raise IndexError("Invalid index.")

        except TypeError:
            raise ValueError("Index is not a valid integer. Please pass a integer number.")

    def get(self, index):
        pass

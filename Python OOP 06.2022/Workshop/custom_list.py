from copy import deepcopy

from errors import NoSuchValueError, NoElementsInTheListError

class CustomIntList:

    def __init__(self):
        self.__values = []

    def append(self, values):
        if not isinstance(values, int):
            raise ValueError("Only integers are accepted!")

        self.__values.append(values)

    def remove(self, index):

        try:
            element = self.__values.pop(index)
            return element

        except IndexError:
            raise IndexError("Invalid index.")

        except TypeError:
            raise ValueError("Index is not a valid integer. Please pass a integer number.")

    def get(self, index):

        try:
            return self.__values[index]

        except IndexError:
            raise IndexError("Invalid index.")

    def extend(self, values):

        try:

            for el in values:
                if not isinstance(el, int):
                    raise ValueError("Only integers are accepted!")

            self.__values.extend(values)
            return deepcopy(self.__values)

        except TypeError:
            raise ValueError("Extend method only works with iterable objects.")

    def insert(self, index, value):

        try:
            if index < 0 or len(self.__values) <= index:
                raise IndexError

            self.__values.insert(index, value)

            return self.__values

        except IndexError:
            raise IndexError("Invalid index.")

        except TypeError:
            raise ValueError("Index is not a valid integer. Please pass a integer number.")

    def pop(self):

        if not self.__values:
            raise NoElementsInTheListError("No elements in the list.")

        return self.__values.pop()

    def clear(self):
        self.__values.clear()

    def index_left(self, value):

        try:
            return self.__values.index(value)

        except ValueError:
            raise NoSuchValueError("No such value in the list.")

    def index_right(self, value):

        for index in range(len(self.__values) - 1, -1, -1):

            if self.__values[index] == value:
                return index

        raise NoSuchValueError("No such value in the list.")

    def count(self, value):
        return self.__values.count(value)

    def reverse(self):
        return self.__values[::-1]

    def copy(self):
        return deepcopy(self.__values)

    def size(self):
        return len(self.__values)

    def add_first(self, value):

        if not isinstance(value, int):
            raise ValueError("Only integers are accepted!")

        self.__values.insert(0, value)

    def dictionize(self):

        result = {}

        for index in range(0, len(self.__values), 2):

            key = self.__values[index]

            try:
                value = self.__values[index + 1]

            except IndexError:
                value = " "

            result[key] = value

        return result

    def move(self, amount):
        self.__values = self.__values[amount:] + self.__values[:amount]
        return self.__values

    def sum(self):
        return sum(self.__values)

    def overbound(self):
        return max(self.__values)

    def underbound(self):
        return min(self.__values)

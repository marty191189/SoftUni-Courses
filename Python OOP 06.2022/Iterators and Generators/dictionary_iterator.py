class dictionary_iter:

    def __init__(self, numbers_dict):
        self.items = list(numbers_dict.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index == len(self.items):
            raise StopIteration

        current_el = self.items[self.index]
        self.index += 1
        return current_el


result = dictionary_iter({1: "1", 2: "2"})

for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})

for x in result:
    print(x)

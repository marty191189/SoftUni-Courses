def fibonacci():

    first_number = 0
    second_number = 1

    yield first_number
    yield second_number

    while True:
        result = first_number + second_number
        first_number, second_number = second_number, result
        yield result


generator = fibonacci()

for i in range(5):
    print(next(generator))

print()

generator = fibonacci()

for i in range(1):
    print(next(generator))

def store_results(function):

    def wrapper(*args):

        result = function(*args)

        with open("./results.txt", "a") as file:
            file.write(f"Function '{function.__name__}' was called. Result: {result}")
            file.write("\n")

        return result

    return wrapper


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


print(add(2, 2))
print(mult(6, 4))

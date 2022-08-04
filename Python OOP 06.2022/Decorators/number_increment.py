def number_increment(numbers):

    def increase():

        result_list = [number + 1 for number in numbers]

        return result_list

    return increase()


print(number_increment([1, 2, 3]))

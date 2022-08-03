def is_prime(num):

    if num <= 1:
        return False

    counter = 0

    for n in range(1, num + 1):
        if num % n == 0:
            counter += 1

    if counter > 2:
        condition = False

    else:
        condition = True

    return condition


def get_primes(numbers_list):

    for number in numbers_list:
        if is_prime(number):
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

print()

print(list(get_primes([-2, 0, 0, 1, 1, 0])))

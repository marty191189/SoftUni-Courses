def squares(num):

    i = 1

    while i <= num:
        yield i ** 2
        i += 1


print(list(squares(5)))

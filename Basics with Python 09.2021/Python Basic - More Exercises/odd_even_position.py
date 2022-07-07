import sys

n = int(input())

odd_numbers_sum = 0
even_numbers_sum = 0
even_max = -sys.maxsize
even_min = sys.maxsize
odd_max = -sys.maxsize
odd_min = sys.maxsize


if n == 1:
    for number in range(1, n + 1):
        num1 = float(input())

        if number % 2 == 0:
            even_numbers_sum += num1

            if num1 > even_max:
                even_max = num1

            if num1 < even_min:
                even_min = num1

        elif number % 2 != 0:
            odd_numbers_sum += num1

            if num1 > odd_max:
                odd_max = num1

            if num1 < odd_min:
                odd_min = num1

    print(f"OddSum={odd_numbers_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_numbers_sum:.2f},")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")

elif n == 0:
    for number in range(1, n + 1):
        num1 = float(input())

        if number % 2 == 0:
            even_numbers_sum += num1

            if num1 > even_max:
                even_max = num1

            if num1 < even_min:
                even_min = num1

        elif number % 2 != 0:
            odd_numbers_sum += num1

            if num1 > odd_max:
                odd_max = num1

            if num1 < odd_min:
                odd_min = num1

    print(f"OddSum={odd_numbers_sum:.2f},")
    print(f"OddMin=No,")
    print(f"OddMax=No,")
    print(f"EvenSum={even_numbers_sum:.2f},")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")

else:
    for number in range(1, n+1):
        num1 = float(input())

        if number % 2 == 0:
            even_numbers_sum += num1

            if num1 > even_max:
                even_max = num1

            if num1 < even_min:
                even_min = num1

        elif number % 2 != 0:
            odd_numbers_sum += num1

            if num1 > odd_max:
                odd_max = num1

            if num1 < odd_min:
                odd_min = num1

    print(f"OddSum={odd_numbers_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_numbers_sum:.2f},")
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")

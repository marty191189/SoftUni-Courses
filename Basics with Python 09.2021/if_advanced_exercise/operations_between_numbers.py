N1 = int(input())
N2 = int(input())
operator1 = input()

remainder = 0
result = 0

if operator1 == "+":
    result = N1 + N2

    if result % 2 == 0:
        print(f"{N1} {operator1} {N2} = {result} - even")
    else:
        print(f"{N1} {operator1} {N2} = {result} - odd")

elif operator1 == "-":
    result = N1 - N2

    if result % 2 == 0:
        print(f"{N1} {operator1} {N2} = {result} - even")
    else:
        print(f"{N1} {operator1} {N2} = {result} - odd")

elif operator1 == "*":
    result = N1 * N2

    if result % 2 == 0:
        print(f"{N1} {operator1} {N2} = {result} - even")
    else:
        print(f"{N1} {operator1} {N2} = {result} - odd")

elif operator1 == "/" and N2 != 0:
    result = N1 / N2
    print(f"{N1} / {N2} = {result:.2f}")

elif operator1 == "%" and N2 != 0:
    remainder = N1 % N2
    print(f"{N1} % {N2} = {remainder}")

elif (operator1 == "/" or operator1 == "%") and N2 == 0:
    print(f"Cannot divide {N1} by zero")

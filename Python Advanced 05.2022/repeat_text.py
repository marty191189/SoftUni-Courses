try:
    text = input()
    number = int(input())

    result = text * number

    print(result)

except ValueError:
    print("Variable times must be an integer")

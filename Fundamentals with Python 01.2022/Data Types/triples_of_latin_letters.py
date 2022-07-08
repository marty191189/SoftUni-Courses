num1 = int(input())

for i in range(0, num1):
    for j in range(0, num1):
        for k in range(0, num1):
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")

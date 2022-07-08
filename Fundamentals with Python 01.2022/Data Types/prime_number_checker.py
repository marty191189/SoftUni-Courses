number = int(input())

counter = 0

for n in range(1, number + 1):
    if number % n == 0:
        counter += 1

if counter > 2:
    print("False")

else:
    print("True")

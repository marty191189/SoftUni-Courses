import sys

count_of_numbers = int(input())

sum_of_all_numbers = 0
max_number = -sys.maxsize

for number in range(1, count_of_numbers + 1):
    current_number = int(input())
    sum_of_all_numbers += current_number

    if current_number > max_number:
        max_number = current_number

if max_number == (sum_of_all_numbers - max_number):
    print("Yes")
    print(f"Sum = {max_number}")
else:
    diff = abs(max_number - (sum_of_all_numbers - max_number))
    print("No")
    print(f"Diff = {diff}")

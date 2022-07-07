upper_border_first_number = int(input())
upper_border_second_number = int(input())
upper_border_third_number = int(input())

for num1 in range(1, upper_border_first_number + 1):
    for num2 in range(1, upper_border_second_number + 1):
        for num3 in range(1, upper_border_third_number + 1):
            if num1 % 2 == 0 and num3 % 2 == 0 and num2 in (2, 3, 5, 7):
                print(f"{num1} {num2} {num3}")

# Втори вариант:
#
# upper_border_first_number = int(input())
# upper_border_second_number = int(input())
# upper_border_third_number = int(input())
#
# for num1 in range(1, upper_border_first_number + 1):
#     for num2 in range(2, upper_border_second_number + 1):
#         for num3 in range(1, upper_border_third_number + 1):
#             if num1 % 2 == 0 and num3 % 2 == 0:
#
#                 counter = 0
#
#                 for n in range(1, num2 + 1):
#                     if num2 % n == 0:
#                         counter += 1
#
#                 if counter <= 2:
#                     print(f"{num1} {num2} {num3}")

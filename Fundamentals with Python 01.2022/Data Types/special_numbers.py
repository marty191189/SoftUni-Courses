number_1 = int(input())

for n in range(1, number_1 + 1):
    working_number = n
    digit_sum = 0
    while working_number > 0:
        # 1234 % 10 = 4 => digit_sum += 4
        digit_sum += (working_number % 10)
        # 1234 / 10 = 123.4 , но трябва да е цяло число затова int() = 123
        working_number = int(working_number / 10)

    # булева променлива, която проверява дали условието е изпълнено
    # ако едно от тях е изпълнено, значи числото е специално и го принтира
    is_special = digit_sum == 5 or digit_sum == 7 or digit_sum == 11
    print(f"{n} -> {is_special}")

# втори начин на Инес

# n = int(input())

# for num in range(1, n + 1):
#     nums_as_string = str(num)
#     result = 0
#
#     for symbol in nums_as_string:
#         result += int(symbol)
#
#     if result == 5 or result == 7 or result == 11:
#         print(f"{num} -> True")
#     else:
#         print(f"{num} -> False")

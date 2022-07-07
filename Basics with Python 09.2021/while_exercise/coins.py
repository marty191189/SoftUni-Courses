# sum1 = float(input())
# sum1 = int(sum1 * 100)
# coins_counter = 0
#
# coins_counter += sum1 // 200
# sum1 = sum1 % 200
#
# coins_counter += sum1 // 100
# sum1 = sum1 % 100
#
# coins_counter += sum1 // 50
# sum1 = sum1 % 50
#
# coins_counter += sum1 // 20
# sum1 = sum1 % 20
#
# coins_counter += sum1 // 10
# sum1 = sum1 % 10
#
# coins_counter += sum1 // 5
# sum1 = sum1 % 5
#
# coins_counter += sum1 // 2
# sum1 = sum1 % 2
#
# coins_counter += sum1 // 1
# sum1 = sum1 % 1
#
# print(coins_counter)

sum1 = float(input())
sum1 = int(sum1 * 100)
coins_counter = 0

while sum1 > 0:
    if sum1 - 200 >= 0:
        coins_counter += 1
        sum1 -= 200
        continue

    elif sum1 - 100 >= 0:
        coins_counter += 1
        sum1 -= 100
        continue

    elif sum1 - 50 >= 0:
        coins_counter += 1
        sum1 -= 50
        continue

    elif sum1 - 20 >= 0:
        coins_counter += 1
        sum1 -= 20
        continue

    elif sum1 - 10 >= 0:
        coins_counter += 1
        sum1 -= 10
        continue

    elif sum1 - 5 >= 0:
        coins_counter += 1
        sum1 -= 5
        continue

    elif sum1 - 2 >= 0:
        coins_counter += 1
        sum1 -= 2
        continue

    elif sum1 - 1 >= 0:
        coins_counter += 1
        sum1 -= 1
        continue

print(coins_counter)

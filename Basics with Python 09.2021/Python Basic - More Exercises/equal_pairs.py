number = int(input())

diff = 0
max_diff = 0
value = 0

for num in range(number):
    current_number_one = int(input())
    current_number_two = int(input())
    current_sum = current_number_one + current_number_two

    if num == 0:
        value = current_sum

    else:
        diff = abs(value - current_sum)
        value = current_sum

    if diff > max_diff:
        max_diff = diff

if max_diff == 0:
    print(f"Yes, value={value}")

else:
    print(f"No, maxdiff={max_diff}")

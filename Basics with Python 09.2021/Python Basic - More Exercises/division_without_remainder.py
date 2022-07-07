n = int(input())

counter_d_2 = 0
counter_d_3 = 0
counter_d_4 = 0

for number in range(n):

    current_number = int(input())

    if current_number % 2 == 0:
        counter_d_2 += 1

    if current_number % 3 == 0:
        counter_d_3 += 1

    if current_number % 4 == 0:
        counter_d_4 += 1

percent_divided_by_2 = (counter_d_2 / n) * 100
percent_divided_by_3 = (counter_d_3 / n) * 100
percent_divided_by_4 = (counter_d_4 / n) * 100

print(f"{percent_divided_by_2:.2f}%")
print(f"{percent_divided_by_3:.2f}%")
print(f"{percent_divided_by_4:.2f}%")

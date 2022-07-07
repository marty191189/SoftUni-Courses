number_days_of_tournament = int(input())

counter_day_win = 0
counter_day_lose = 0
counter_all_win = 0
counter_all_lose = 0
current_sum = 0
total_sum = 0

for day in range(1, number_days_of_tournament + 1):

    sport = input()
    result = input()

    while True:

        if sport == "Finish":
            break

        if result == "win":
            current_sum += 20
            counter_day_win += 1
            counter_all_win += 1

        elif result == "lose":
            counter_day_lose += 1
            counter_all_lose += 1

        sport = input()

        if sport == "Finish":
            break

        result = input()

    if counter_day_win > counter_day_lose:
        current_sum = current_sum + ((10/100) * current_sum)

    counter_day_win = 0
    counter_day_lose = 0

    total_sum += current_sum
    current_sum = 0

if counter_all_win > counter_all_lose:
    total_sum = total_sum + ((20/100) * total_sum)
    print(f"You won the tournament! Total raised money: {total_sum:.2f}")

else:
    print(f"You lost the tournament! Total raised money: {total_sum:.2f}")

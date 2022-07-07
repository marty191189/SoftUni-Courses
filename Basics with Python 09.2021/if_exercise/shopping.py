budget = float(input())
number_video_cards = int(input())
number_cpu = int(input())
number_ram = int(input())
final_sum = 0

video_cards = 250

sum_video_cards = video_cards * number_video_cards

cpu = 0.35 * sum_video_cards

ram = 0.1 * sum_video_cards

total_sum = (video_cards * number_video_cards) + (cpu * number_cpu) + (ram * number_ram)

if number_video_cards > number_cpu:
    total_sum = total_sum - ((15 / 100) * total_sum)

diff = abs(total_sum - budget)

if total_sum <= budget:
    print(f"You have {diff:.2f} leva left!")

else:
    print(f"Not enough money! You need {diff:.2f} leva more!")

name_of_actor = input()
points_from_academy = float(input())
number_of_judges = int(input())

final_points_from_judge = 0
points_from_all_judges = 0
total_sum = 0

for judge in range(1, number_of_judges + 1):

    name_of_judge = input()

    points_from_judge = float(input())

    final_points_from_judge = (len(name_of_judge) * points_from_judge) / 2

    points_from_all_judges += final_points_from_judge

    total_sum = points_from_academy + points_from_all_judges

    if total_sum >= 1250.5:
        print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_sum:.1f}!")
        break

diff = abs(total_sum - 1250.5)

if total_sum < 1250.5:
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")

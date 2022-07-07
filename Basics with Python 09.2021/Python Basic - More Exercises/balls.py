import math

number_of_balls = int(input())

total_points = 0

counter_red_balls = 0
counter_orange_balls = 0
counter_yellow_balls = 0
counter_white_balls = 0
counter_other_balls = 0
counter_black_balls = 0

for number in range(number_of_balls):
    colour_of_ball = input()

    if colour_of_ball == "red":
        counter_red_balls += 1
        total_points += 5

    elif colour_of_ball == "orange":
        counter_orange_balls += 1
        total_points += 10

    elif colour_of_ball == "yellow":
        counter_yellow_balls += 1
        total_points += 15

    elif colour_of_ball == "white":
        counter_white_balls += 1
        total_points += 20

    elif colour_of_ball == "black":
        counter_black_balls += 1
        total_points = math.floor(total_points / 2)

    else:
        counter_other_balls += 1

print(f"Total points: {total_points}")
print(f"Red balls: {counter_red_balls}")
print(f"Orange balls: {counter_orange_balls}")
print(f"Yellow balls: {counter_yellow_balls}")
print(f"White balls: {counter_white_balls}")
print(f"Other colors picked: {counter_other_balls}")
print(f"Divides from black balls: {counter_black_balls}")

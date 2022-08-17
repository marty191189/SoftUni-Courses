number = 6

counter_throws = 3

matrix = [input().split() for i in range(number)]

total_points = 0

for throw in range(counter_throws):

    row, col = [int(el) for el in eval(input())]

    try:
        if matrix[row][col] == "B":
            total_points += sum([int(matrix[row_index][col]) for row_index in range(number) if matrix[row_index][col].isdigit()])
            matrix[row][col] = "0"

    except IndexError:
        continue

if total_points < 100:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")

elif 100 <= total_points < 200:
    print(f"Good job! You scored {total_points} points, and you've won Football.")

elif 200 <= total_points < 300:
    print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")

else:
    print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")

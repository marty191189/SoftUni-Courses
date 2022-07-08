def get_next_pos(row_1, col_1, dir_1, steps_1):

    r = 0
    c = 0

    if dir_1 == "up":
        r = row_1 - steps_1
        c = col_1

    elif dir_1 == "down":
        r = row_1 + steps_1
        c = col_1

    elif dir_1 == "left":
        r = row_1
        c = col_1 - steps_1

    elif dir_1 == "right":
        r = row_1
        c = col_1 + steps_1

    return r, c


def is_inside(new_row, new_col, matrix_size):

    condition = False

    if 0 <= new_row < matrix_size and 0 <= new_col < matrix_size:
        condition = True

    return condition


size = 5

matrix = []

hit_targets = []

player_row = 0
player_col = 0

bullet_row = 0
bullet_col = 0

targets = 0

for row in range(0, size):

    row_elements = input().split()

    for col in range(0, size):

        if row_elements[col] == "A":
            player_row = row
            player_col = col

        elif row_elements[col] == "x":
            targets += 1

    matrix.append(row_elements)

matrix[player_row][player_col] = "."

number_of_commands = int(input())

for num in range(0, number_of_commands):
    command_parts = input().split()
    command = command_parts[0]
    direction = command_parts[1]

    if command == "move":
        steps = int(command_parts[2])
        next_row, next_col = get_next_pos(player_row, player_col, direction, steps)

        if is_inside(next_row, next_col, size) and matrix[next_row][next_col] == ".":
            player_row, player_col = next_row, next_col

    elif command == "shoot":
        bullet_row, bullet_col = get_next_pos(player_row, player_col, direction, 1)

        while is_inside(bullet_row, bullet_col, size):

            if matrix[bullet_row][bullet_col] == "x":
                targets -= 1
                matrix[bullet_row][bullet_col] = "."
                hit_targets.append([bullet_row, bullet_col])
                break

            bullet_row, bullet_col = get_next_pos(bullet_row, bullet_col, direction, 1)

        if targets == 0:
            break

if targets == 0:
    print(f"Training completed! All {len(hit_targets)} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")

print(*hit_targets, sep='\n')

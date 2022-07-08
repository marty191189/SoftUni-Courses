def get_next_pos(row_1, col_1, dir_1):

    r = 0
    c = 0

    if dir_1 == "up":
        r = row_1 - 1
        c = col_1

    elif dir_1 == "down":
        r = row_1 + 1
        c = col_1

    elif dir_1 == "left":
        r = row_1
        c = col_1 - 1

    elif dir_1 == "right":
        r = row_1
        c = col_1 + 1

    return r, c


def is_inside(new_row, new_col, matrix_size):

    condition = False

    if 0 <= new_row < matrix_size and 0 <= new_col < matrix_size:
        condition = True

    return condition


def find_nearby_children(row_1, col_1, matrix_1):

    result = []

    if is_inside(row_1, col_1 - 1, len(matrix_1)) and matrix_1[row_1][col_1 - 1] == "X" \
            or matrix_1[row_1][col_1 - 1] == "V":
        result.append([row_1, col_1 - 1])

    if is_inside(row_1, col_1 + 1, len(matrix_1)) and matrix_1[row_1][col_1 + 1] == "X" \
            or matrix_1[row_1][col_1 + 1] == "V":
        result.append([row_1, col_1 + 1])

    if is_inside(row_1 - 1, col_1, len(matrix_1)) and matrix_1[row_1 - 1][col_1] == "X" \
            or matrix_1[row_1 - 1][col_1] == "V":
        result.append([row_1 - 1, col_1])

    if is_inside(row_1 + 1, col_1, len(matrix_1)) and matrix_1[row_1 + 1][col_1] == "X" \
            or matrix_1[row_1 + 1][col_1] == "V":
        result.append([row_1 + 1, col_1])

    return result


gifts = int(input())
size = int(input())

matrix = []

santa_row = 0
santa_col = 0

nice_children = 0
nice_children_gifted = 0

for row in range(0, size):

    row_elements = input().split()

    for col in range(0, size):

        if row_elements[col] == "S":
            santa_row = row
            santa_col = col

        elif row_elements[col] == "V":
            nice_children += 1

    matrix.append(row_elements)

while gifts > 0:

    command = input()

    if command == "Christmas morning":
        break

    direction = command

    matrix[santa_row][santa_col] = "-"

    next_row, next_col = get_next_pos(santa_row, santa_col, direction)

    if is_inside(next_row, next_col, size):

        santa_row, santa_col = next_row, next_col

        if matrix[next_row][next_col] == "V":
            gifts -= 1
            nice_children_gifted += 1
            matrix[next_row][next_col] = "-"

        elif matrix[next_row][next_col] == "X":
            matrix[next_row][next_col] = "-"

        elif matrix[next_row][next_col] == "C":
            nearby_children = find_nearby_children(santa_row, santa_col, matrix)

            for child_row, child_col in nearby_children:

                if matrix[child_row][child_col] == "V":
                    nice_children_gifted += 1

                gifts -= 1
                matrix[child_row][child_col] = "-"

                if gifts == 0:
                    break

matrix[santa_row][santa_col] = "S"

if not nice_children_gifted == nice_children and gifts == 0:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row, sep=" ")

if nice_children_gifted == nice_children:
    print(f"Good job, Santa! {nice_children_gifted} happy nice kid/s.")
else:
    print(f"No presents for {nice_children - nice_children_gifted} nice kid/s.")

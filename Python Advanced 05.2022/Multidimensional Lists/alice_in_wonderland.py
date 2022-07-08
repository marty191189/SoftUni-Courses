def get_new_pos(row_1, col_1, dir_1):

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


size = int(input())

matrix = []

alice_row = 0
alice_col = 0

for row in range(0, size):

    matrix.append(input().split())

    for col in range(0, size):

        if matrix[row][col] == "A":
            alice_row = row
            alice_col = col

matrix[alice_row][alice_col] = "*"

tea_bags = 0

new_row = 0
new_col = 0

while tea_bags < 10:

    direction = input()

    new_row, new_col = get_new_pos(alice_row, alice_col, direction)

    if not 0 <= new_row < size and not 0 <= new_col < size:
        break

    elif not 0 <= new_row < size or not 0 <= new_col < size:
        break

    elif matrix[new_row][new_col] == "R":
        matrix[new_row][new_col] = "*"
        break

    elif matrix[new_row][new_col] == "*":
        alice_row = new_row
        alice_col = new_col

    elif matrix[new_row][new_col] == ".":
        matrix[new_row][new_col] = "*"

    elif matrix[new_row][new_col].isdigit():
        tea_bags += int(matrix[new_row][new_col])
        matrix[new_row][new_col] = "*"

    alice_row = new_row
    alice_col = new_col

if tea_bags >= 10:
    print(f"She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row, sep=' ')

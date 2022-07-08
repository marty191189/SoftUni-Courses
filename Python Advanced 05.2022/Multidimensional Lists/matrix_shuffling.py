def is_outside(row_index, col_index, original_rows, original_cols):

    condition = False

    if row_index < 0 or col_index < 0 or row_index >= original_rows or col_index >= original_cols:
        condition = True

    return condition


rows, cols = [int(el) for el in input().split()]

matrix = []

for row in range(0, rows):
    current_list = [el for el in input().split()]
    matrix.append(current_list)


while True:

    command = input()

    if command == "END":
        break

    data = command.split(" ")

    if not data[0] == "swap" or not len(data) == 5:
        print("Invalid input!")
        continue

    row_index_1 = int(data[1])
    col_index_1 = int(data[2])
    row_index_2 = int(data[3])
    col_index_2 = int(data[4])

    if is_outside(row_index_1, col_index_1, rows, cols) or is_outside(row_index_2, col_index_2, rows, cols):
        print("Invalid input!")
        continue

    matrix[row_index_1][col_index_1], matrix[row_index_2][col_index_2] = matrix[row_index_2][col_index_2], matrix[row_index_1][col_index_1]

    for row in matrix:
        print(*row, sep=" ")

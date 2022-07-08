def is_outside(row_index, col_index):

    condition = False

    if row_index < 0 or col_index < 0 or row_index >= len(matrix) or col_index >= len(matrix):
        condition = True

    return condition


rows = int(input())

matrix = []

for number in range(1, rows + 1):
    current_list = [int(el) for el in input().split()]
    matrix.append(current_list)

while True:

    command = input()

    if command == "END":
        break

    data = command.split()

    if data[0] == "Add":

        row = int(data[1])
        col = int(data[2])
        value = int(data[3])

        check = is_outside(row, col)

        if check:
            print("Invalid coordinates")
            continue

        matrix[row][col] += value

    elif data[0] == "Subtract":

        row = int(data[1])
        col = int(data[2])
        value = int(data[3])

        is_invalid = is_outside(row, col)

        if is_invalid:
            print("Invalid coordinates")
            continue

        matrix[row][col] -= value

for row in matrix:
    print(*row, sep=" ")

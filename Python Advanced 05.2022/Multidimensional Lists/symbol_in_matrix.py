rows = int(input())

matrix = []

position = None

for row in range(0, rows):
    current_list = [el for el in input()]
    matrix.append(current_list)

searched_symbol = input()

for row in range(0, rows):
    for col in range(0, rows):
        current_el = matrix[row][col]
        if current_el == searched_symbol:
            position = (row, col)
            print(position)
            break

    if position:
        break

if position is None:
    print(f"{searched_symbol} does not occur in the matrix")

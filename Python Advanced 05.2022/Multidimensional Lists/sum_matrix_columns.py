rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for row in range(0, rows):
    current_list = [int(el) for el in input().split()]
    matrix.append(current_list)

for col_index in range(0, cols):
    result = 0
    for row_index in range(0, rows):
        result += matrix[row_index][col_index]
    print(result)

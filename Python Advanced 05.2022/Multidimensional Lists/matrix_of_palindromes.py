rows, cols = [int(el) for el in input().split()]

matrix = []

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for row in range(0, rows):
    current_list = [int(el) for el in range(0, cols)]
    matrix.append(current_list)

for row in range(0, rows):
    for col in range(0, cols):
        matrix[row][col] = f"{alphabet_list[row]}{alphabet_list[row + col]}{alphabet_list[row]}"

for row in matrix:
    print(*row, sep=' ')

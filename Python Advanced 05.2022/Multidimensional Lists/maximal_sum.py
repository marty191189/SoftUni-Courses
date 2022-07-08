import sys

rows, cols = [int(el) for el in input().split()]

matrix = []

max_sub_matrix = []

max_sum = -sys.maxsize

for row in range(0, rows):
    current_list = [int(el) for el in input().split()]
    matrix.append(current_list)

for row in range(0, rows - 2):
    for col in range(0, cols - 2):
        sub_matrix = [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2],
                      matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2],
                      matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]

        current_sum = sum(sub_matrix)

        if current_sum > max_sum:
            max_sum = current_sum
            max_sub_matrix = sub_matrix.copy()

print(f"Sum = {max_sum}")

print(max_sub_matrix[0], max_sub_matrix[1], max_sub_matrix[2])
print(max_sub_matrix[3], max_sub_matrix[4], max_sub_matrix[5])
print(max_sub_matrix[6], max_sub_matrix[7], max_sub_matrix[8])

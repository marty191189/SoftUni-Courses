import sys

rows, cols = [int(el) for el in input().split(", ")]

matrix = []

max_sub_matrix = []

max_sum = -sys.maxsize

for row in range(0, rows):
    current_list = [int(el) for el in input().split(", ")]
    matrix.append(current_list)

for row in range(0, rows - 1):
    for col in range(0, cols - 1):
        sub_matrix = [matrix[row][col], matrix[row][col + 1],
                      matrix[row + 1][col], matrix[row + 1][col + 1]]

        current_sum = sum(sub_matrix)

        if current_sum > max_sum:
            max_sum = current_sum
            max_sub_matrix = sub_matrix.copy()

print(max_sub_matrix[0], max_sub_matrix[1])
print(max_sub_matrix[2], max_sub_matrix[3])

print(max_sum)

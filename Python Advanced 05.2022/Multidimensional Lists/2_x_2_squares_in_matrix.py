rows, cols = [int(el) for el in input().split()]

matrix = []

counter = 0

for row in range(0, rows):
    current_list = [el for el in input().split()]
    matrix.append(current_list)

for row in range(0, rows - 1):
    for col in range(0, cols - 1):

        # if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:

        if matrix[row][col] == matrix[row][col + 1] and matrix[row][col] == matrix[row + 1][col] and matrix[row][col] == matrix[row + 1][col + 1]:
            counter += 1

print(counter)

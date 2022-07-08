rows = int(input())

matrix = []

primary_diagonal_list = []
secondary_diagonal_list = []

for row in range(0, rows):
    current_list = [int(el) for el in input().split(" ")]
    matrix.append(current_list)

for row_index in range(0, rows):
    primary_diagonal_list.append(matrix[row_index][row_index])
    secondary_diagonal_list.append(matrix[row_index][(rows - 1) - row_index])

sum_primary_diagonal = sum(primary_diagonal_list)
sum_secondary_diagonal = sum(secondary_diagonal_list)

abs_sum = abs(sum_primary_diagonal - sum_secondary_diagonal)

print(abs_sum)

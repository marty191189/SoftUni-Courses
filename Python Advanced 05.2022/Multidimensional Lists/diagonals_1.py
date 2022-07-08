rows = int(input())

matrix = []

primary_diagonal_list = []
secondary_diagonal_list = []

for row in range(0, rows):
    current_list = [int(el) for el in input().split(", ")]
    matrix.append(current_list)

for row_index in range(0, rows):
    primary_diagonal_list.append(matrix[row_index][row_index])
    secondary_diagonal_list.append(matrix[row_index][(rows - 1) - row_index])

print(f"Primary diagonal: {', '.join([str(el) for el in primary_diagonal_list])}. Sum: {sum(primary_diagonal_list)}")
print(f"Secondary diagonal: {', '.join([str(el) for el in secondary_diagonal_list])}. Sum: {sum(secondary_diagonal_list)}")

# с матрица

number_of_rows = int(input())

matrix = []

result_list = []

for row in range(0, number_of_rows):
    current_list = [int(el) for el in input().split(", ")]
    matrix.append(current_list)

for row_index in range(0, len(matrix)):
    for col_index in range(0, len(matrix[row_index])):
        result_list.append(matrix[row_index][col_index])

print(result_list)


# без матрица
#
# number_of_rows = int(input())
#
# matrix = []
#
# for row in range(0, number_of_rows):
#     current_list = [int(el) for el in input().split(", ")]
#     matrix.extend(current_list)
#
# print(matrix)

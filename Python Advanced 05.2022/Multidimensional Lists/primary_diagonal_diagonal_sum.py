rows = int(input())

matrix = []

diagonal_sum = 0

for row in range(0, rows):
    current_list = [int(el) for el in input().split()]
    matrix.append(current_list)

for index in range(0, rows):
    diagonal_sum += matrix[index][index]

print(diagonal_sum)

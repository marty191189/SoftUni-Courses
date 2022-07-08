row, col = [int(el) for el in input().split(", ")]

matrix = []

result = 0

for number in range(0, row):
    data_list = [int(el) for el in input().split(", ")]
    matrix.append(data_list)
    result += sum(data_list)

print(result)
print(matrix)

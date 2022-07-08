rows = int(input())

matrix = []

for row in range(0, rows):
    nums_list = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(nums_list)

print(matrix)

rows, cols = [int(el) for el in input().split()]

word = input()

index = 0

for row in range(0, rows):

    matrix = [None] * cols

    if row % 2 == 0:
        for col in range(0, cols):
            matrix[col] = word[index % len(word)]
            index += 1

    else:
        for col in range(cols - 1, -1, -1):
            matrix[col] = word[index % len(word)]
            index += 1

    print("".join(matrix))

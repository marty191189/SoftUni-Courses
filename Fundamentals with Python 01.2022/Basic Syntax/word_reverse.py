word = input()

for index in range(len(word) - 1, 0 - 1, -1):
    print(word[index], end="")

# с разстояние между буквите
#   print(word[index], end=" ")

# същото, но по-кратко
#
# word = input()
#
# print(word[::-1])

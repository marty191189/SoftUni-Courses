word = input()

list_2 = []
counter = -1

for letter in word:

    counter += 1

    if 65 <= ord(letter) <= 90:
        list_2.append(counter)

print(list_2)

number = int(input())
search_word = input()

string = []
filtered = []

for i in range(1, number + 1):
    current_string = input()

    string.append(current_string)

    if search_word in current_string:
        filtered.append(current_string)

print(string)
print(filtered)

number = int(input())
search_word = input()

string = []

for i in range(1, number + 1):
    string.append(input())

print(string)

filtered = []

for current_string in string:
    if search_word in current_string:
        filtered.append(current_string)

print(filtered)

targets = input().split(" ")
targets = list(map(int, targets))

line = input()

while not line == "End":

    data = line.split(" ")
    command = data[0]
    index = int(data[1])
    value = int(data[2])

    if command == "Shoot" and 0 <= index < len(targets):
        current_target = targets[index]
        current_target -= value

        if current_target <= 0:
            targets.pop(index)
        else:
            targets[index] = current_target

    elif command == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        if (index - value) >= 0 and (index + value + 1) < len(targets):
            targets = targets[:index - value] + targets[index + value + 1:]
        else:
            print("Strike missed!")

    line = input()

targets = list(map(str, targets))

output = "|".join(targets)

print(output)

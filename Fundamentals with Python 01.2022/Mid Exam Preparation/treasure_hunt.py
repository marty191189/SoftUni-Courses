loot = input().split("|")

total_sum = 0
counter_steal = 0

steal_list = []

chest_is_empty = False

data = input()

while not data == "Yohoho!":
    data = data.split(" ")
    command = data[0]

    if command == "Loot":
        remove_item = data.pop(0)

        for item in data:
            if item not in loot:
                loot.insert(0, item)

    elif command == "Drop":
        index = int(data[1])

        if (0 <= index < len(loot)) or (-len(loot) <= index <= -1):
            item = loot[index]
            remove_item = loot.pop(index)
            add_item = loot.append(item)

    elif command == "Steal":
        number = int(data[1])

        if 1 <= number <= 100:

            if number < len(loot):
                counter_steal += 1
                loot = loot[::-1]

                for index in range(0, number):
                    current_el = loot[index]
                    steal_list.append(current_el)

                for index in range(0, number):
                    loot.remove(loot[0])

                if counter_steal >= 1:
                    steal_list = steal_list[::-1]

                print(", ".join(steal_list))

                steal_list = []

                loot = loot[::-1]

            elif number >= len(loot):

                loot = loot[::-1]

                for el in loot:
                    steal_list.append(el)

                steal_list = steal_list[::-1]

                print(", ".join(steal_list))

                loot.clear()

                chest_is_empty = True

    data = input()

if chest_is_empty:
    print("Failed treasure hunt.")

else:
    for el in loot:
        current_sum = len(el)
        total_sum += current_sum

    result = total_sum / len(loot)

    print(f"Average treasure gain: {result:.2f} pirate credits.")

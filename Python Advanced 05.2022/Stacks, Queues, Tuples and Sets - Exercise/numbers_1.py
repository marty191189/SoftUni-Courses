first_set = set(int(el) for el in input().split())
second_set = set(int(el) for el in input().split())

number_of_lines = int(input())

for line in range(1, number_of_lines + 1):

    data = input().split()

    command = f"{data[0]} {data[1]}"

    current_numbers_list = [int(data[index]) for index in range(2, len(data))]

    if command == "Add First":
        for el in current_numbers_list:
            first_set.add(el)

    elif command == "Add Second":
        for el in current_numbers_list:
            second_set.add(el)

    elif command == "Remove First":
        for el in current_numbers_list:
            if el in first_set:
                first_set.remove(el)

    elif command == "Remove Second":
        for el in current_numbers_list:
            if el in second_set:
                second_set.remove(el)

    elif command == "Check Subset":
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")

sorted_first_set = sorted(first_set)
print(*sorted_first_set, sep=', ')

sorted_second_set = sorted(second_set)
print(*sorted_second_set, sep=', ')

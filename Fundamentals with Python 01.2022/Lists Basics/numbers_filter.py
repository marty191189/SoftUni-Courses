number = int(input())

numbers_list = []

for i in range(1, number + 1):
    current_number = int(input())
    numbers_list.append(current_number)

filter_word = input()

filtered_list = []

for current_number in numbers_list:

    if filter_word == "even":
        if current_number % 2 == 0:
            filtered_list.append(current_number)

    elif filter_word == "odd":
        if not current_number % 2 == 0:
            filtered_list.append(current_number)

    elif filter_word == "positive":
        if current_number >= 0:
            filtered_list.append(current_number)

    elif filter_word == "negative":
        if current_number < 0:
            filtered_list.append(current_number)

print(filtered_list)

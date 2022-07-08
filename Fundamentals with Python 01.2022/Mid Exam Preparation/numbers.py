list_of_numbers = list(map(int, input().split(" ")))

positive_result = []
negative_result = []

result = []

average_number = sum(list_of_numbers) / len(list_of_numbers)

for el in list_of_numbers:
    if el > average_number:

        if el >= 0:
            positive_result.append(el)

        else:
            negative_result.append(el)

if len(positive_result) == 0 and len(negative_result) == 0:
    print("No")

if len(positive_result) > 0:
    positive_result.sort(reverse=True)
    result = positive_result[0:5]
    result = list(map(str, result))
    print(" ".join(result))

elif len(negative_result) > 0:
    result = negative_result[0:5]
    result = list(map(str, result))
    print(" ".join(result))

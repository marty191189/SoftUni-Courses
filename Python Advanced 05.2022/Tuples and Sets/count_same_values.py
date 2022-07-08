nums_tuple = (float(el) for el in input().split())
repeated_nums_dict = {}

for num in nums_tuple:
    if num not in repeated_nums_dict:
        repeated_nums_dict[num] = 0

    repeated_nums_dict[num] += 1

for key, value in repeated_nums_dict.items():
    print(f"{key} - {value} times")

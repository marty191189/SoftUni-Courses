text_list = input().lower().split(" ")

odd_dict = {}

for el in text_list:
    if el not in odd_dict:
        odd_dict[el] = 0
    odd_dict[el] += 1

for key, value in odd_dict.items():
    if value % 2 != 0:
        print(key, end=" ")






# първи начин
#
# numbers = input().split(", ")
# numbers = list(map(lambda x: int(x), numbers))
# group_number = 10
# old_number = 0
# while len(numbers) > 0:
#     group = [x for x in numbers if x in range(old_number, group_number+1)]
#     print(f"Group of {group_number}'s: {group}")
#     old_number = group_number
#     numbers = list(filter(lambda x: x not in group, numbers))
#     group_number += 10

# втори начин
#
# import math
# numbers = [int(x) for x in input().split(", ")]
# groups = (max(numbers)) / 10
# for group in range(1, math.ceil(groups) + 1):
#     print(
#         f"Group of {group}0's: {[numbers[x] for x in range(len(numbers)) if numbers[x] in range(group * 10 - 10 + 1, group * 10 + 1)]}")

import re

number_of_lines = int(input())

intersection_set = set()

max_len = None
winner_set = None

for line in range(1, number_of_lines + 1):

    text = input()

    pattern = r"\d+"

    valid_nums = re.finditer(pattern, text)
    valid_nums = [num.group() for num in valid_nums]

    first_start = int(valid_nums[0])
    first_end = int(valid_nums[1])
    second_start = int(valid_nums[2])
    second_end = int(valid_nums[3])

    first_range_set = set(num for num in range(first_start, first_end + 1))
    second_range_set = set(num for num in range(second_start, second_end + 1))

    sorted(first_range_set)
    sorted(second_range_set)

    if first_range_set.issubset(second_range_set):
        intersection_set = first_range_set.intersection(second_range_set)

    else:
        intersection_set = second_range_set.intersection(first_range_set)

    if line == 1:
        max_len = len(intersection_set)
        winner_set = intersection_set
    else:
        if max_len < len(intersection_set):
            max_len = len(intersection_set)
            winner_set = intersection_set

winner_list = [el for el in winner_set]

print(f"Longest intersection is {winner_list} with length {max_len}")

# втори начин
#
# number_of_lines = int(input())
#
# best_intersection_set = set()
#
# for line in range(1, number_of_lines + 1):
#     first_range, second_range = input().split("-")
#
#     first_start, first_end = [int(el) for el in first_range.split(",")]
#     second_start, second_end = [int(el) for el in second_range.split(",")]
#
#     first_range_set = set(range(first_start, first_end + 1))
#     second_range_set = set(range(second_start, second_end + 1))
#
#     current_intersection = first_range_set.intersection(second_range_set)
#
#     if len(current_intersection) > len(best_intersection_set):
#         best_intersection_set = current_intersection
#
# result = f"{', '.join([str(el) for el in best_intersection_set])}"
#
# print(f"Longest intersection is [{result}] with length {len(best_intersection_set)}")

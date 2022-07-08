words = input()

output_dict = {}

for letter in words:

    if not letter == " ":

        if letter not in output_dict:
            output_dict[letter] = 0
        output_dict[letter] += 1

    else:
        pass

for key, value in output_dict.items():
    print(f"{key} -> {value}")

# втори начин

# from collections import Counter
#
# word = input()
# result = Counter(word)
#
# for key, value in result.items():
#     if not key == " ":
#         print(f"{key} -> {value}")

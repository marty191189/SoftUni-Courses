def words_sorting(*args):

    unsorted_dict = {}

    for word in args:
        unsorted_dict[word] = sum(ord(letter) for letter in word)

    sum_of_dict_values = 0

    for value in unsorted_dict.values():
        sum_of_dict_values += value

    if sum_of_dict_values % 2 == 0:
        sorted_list = sorted(unsorted_dict.items(), key=lambda kvp_tuple: (kvp_tuple[0]))

    else:
        sorted_list = sorted(unsorted_dict.items(), key=lambda kvp_tuple: (kvp_tuple[1]), reverse=True)

    sorted_dict = {}

    for el in sorted_list:
        key = el[0]
        value = el[1]
        sorted_dict[key] = value

    result = ""

    for key, value in sorted_dict.items():
        result += f"{key} - {value}\n"

    return result


print(words_sorting('escape', 'charm', 'mythology'))

print(words_sorting('escape', 'charm', 'eye'))

print(words_sorting('cacophony', 'accolade'))

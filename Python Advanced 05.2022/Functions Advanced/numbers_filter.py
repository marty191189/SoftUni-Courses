def even_odd_filter(**kwargs):
    sorted_dict = {}

    for key, value in kwargs.items():

        if key == "even":
            my_list = [num for num in value if num % 2 == 0]
            kwargs[key] = my_list

        elif key == "odd":
            my_list = [num for num in value if not num % 2 == 0]
            kwargs[key] = my_list

    sorted_list = sorted(kwargs.items(), key=lambda kvp_tuple: -len(kvp_tuple[1]))

    for el in sorted_list:
        key = el[0]
        value = el[1]
        sorted_dict[key] = value

    return sorted_dict


print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2]))

print(even_odd_filter(odd=[2, 2, 30, 44, 10, 5]))

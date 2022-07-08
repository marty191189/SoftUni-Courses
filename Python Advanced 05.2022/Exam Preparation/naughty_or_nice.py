def naughty_or_nice_list(all_kids_list, *args, **kwargs):

    found_kids_dict = {}

    nice_list = []
    naughty_list = []
    not_found_list = []

    result = ""

    if args:

        for el in args:
            current_data = el.split("-")
            number = int(current_data[0])

            for kid_tuple in all_kids_list:

                if number == kid_tuple[0]:

                    if number not in found_kids_dict:
                        found_kids_dict[number] = []
                        found_kids_dict[number].append(kid_tuple[1])
                    else:
                        found_kids_dict[number].append(kid_tuple[1])

    if found_kids_dict:
        for key, value in found_kids_dict.items():
            if len(value) == 1 and (key, *value) in all_kids_list:
                all_kids_list.remove((key, *value))

    if found_kids_dict:

        for el in args:
            current_data = el.split("-")
            number = int(current_data[0])
            title = current_data[1]

            for key, value in found_kids_dict.items():

                if len(value) == 1 and number == key:

                    if title == "Nice":
                        nice_list.append(*value)

                    elif title == "Naughty":
                        naughty_list.append(*value)

    found_kids_dict.clear()

    if kwargs:

        for key, value in kwargs.items():

            name_kid = key

            for kid_tuple in all_kids_list:

                if name_kid == kid_tuple[1]:

                    if name_kid not in found_kids_dict:
                        found_kids_dict[name_kid] = 1
                    else:
                        found_kids_dict[name_kid] += 1

    if found_kids_dict:

        for key, value in kwargs.items():
            name_kid = key
            title = value

            for name, number in found_kids_dict.items():

                if number == 1 and name_kid == name:

                    if title == "Nice":
                        nice_list.append(name)

                    elif title == "Naughty":
                        naughty_list.append(name)

    if found_kids_dict:
        for key, value in found_kids_dict.items():
            if value == 1:
                for kid in all_kids_list:
                    if key == kid[1]:
                        all_kids_list.remove(kid)

    if all_kids_list:
        for el_tuple in all_kids_list:
            name = el_tuple[1]
            not_found_list.append(name)

    if nice_list:
        result += f"Nice: {', '.join(nice_list)}\n"
    if naughty_list:
        result += f"Naughty: {', '.join(naughty_list)}\n"
    if not_found_list:
        result += f"Not found: {', '.join(not_found_list)}"

    return result


print(naughty_or_nice_list([(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy")], "3-Nice", "1-Naughty", Amy="Nice", Katy="Naughty"))


print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon")
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice"
    ))


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank")
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty"
))

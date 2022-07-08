def start_spring(**kwargs):

    my_dict = {}

    my_dict_2 = {}

    for name_object, type_object in kwargs.items():

        if type_object not in my_dict:
            my_dict[type_object] = []
            my_dict[type_object].append(name_object)
        else:
            my_dict[type_object].append(name_object)

    for key, value in my_dict.items():
        my_dict_2[key] = sorted(value)

    sorted_list = sorted(my_dict_2.items(), key=lambda kvp_tuple: (-len(kvp_tuple[1]), kvp_tuple[0]))

    sorted_dict = {}

    for el in sorted_list:
        key = el[0]
        value = el[1]
        sorted_dict[key] = value

    result = ""

    for key, value in sorted_dict.items():

        result += f"{key}:\n"

        for el in value:
            result += f"-{''.join(el)}\n"

    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower"}

print(start_spring(**example_objects))


example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird"}

print(start_spring(**example_objects))


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}

print(start_spring(**example_objects))

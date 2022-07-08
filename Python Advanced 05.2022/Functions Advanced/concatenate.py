def concatenate(*args, **kwargs):

    final_string = "".join(args)

    # final_string = ""
    #
    # for string in args:
    #     final_string += string

    for key, value in kwargs.items():

        if key in final_string:
            final_string = final_string.replace(key, value)

    return final_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))

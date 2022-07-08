def age_assignment(*args, **kwargs):

    result_list = []

    for key, value in kwargs.items():

        for name in args:

            if key in name:
                result_list.append(f"{name} is {value} years old.")

    sorted_names_list = sorted(result_list, key=lambda x: x[0])

    return "\n".join(sorted_names_list)


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

data = input()

phone_dict = {}

while not len(data) == 1:
    data_list = data.split("-")

    person_name = data_list[0]
    person_phone = data_list[1]

    if person_name not in phone_dict.keys():
        phone_dict[person_name] = person_phone
    phone_dict[person_name] = person_phone

    data = input()

number_of_names = int(data)

for number in range(1, number_of_names + 1):
    name = input()

    a = phone_dict.get(name)

    if a is None:
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phone_dict.get(name)}")

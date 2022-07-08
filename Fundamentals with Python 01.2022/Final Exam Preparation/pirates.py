command_1 = input()

city_dict = {}

while not command_1 == "Sail":

    data = command_1.split("||")

    city = data[0]
    population = int(data[1])
    gold = int(data[2])

    if city not in city_dict:
        city_dict[city] = []
        city_dict[city].append(population)
        city_dict[city].append(gold)

    else:
        city_dict[city][0] += population
        city_dict[city][1] += gold

    command_1 = input()

command_2 = input()

while not command_2 == "End":

    action = command_2.split("=>")

    if action[0] == "Plunder":
        city = action[1]
        people = int(action[2])
        gold = int(action[3])

        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")

        city_dict[city][0] -= people
        city_dict[city][1] -= gold

        if city_dict[city][0] <= 0 or city_dict[city][1] <= 0:
            print(f"{city} has been wiped off the map!")
            del city_dict[city]

    elif action[0] == "Prosper":
        city = action[1]
        gold = int(action[2])

        if gold >= 0:
            city_dict[city][1] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {city_dict[city][1]} gold.")
        else:
            print("Gold added cannot be a negative number!")

    command_2 = input()

if city_dict:
    print(f"Ahoy, Captain! There are {len(city_dict)} wealthy settlements to go to:")

    for key, value in city_dict.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

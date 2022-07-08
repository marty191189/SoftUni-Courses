number_of_lines = int(input())

plant_dict = {}

for number in range(1, number_of_lines + 1):

    info = input().split("<->")
    plant = info[0]
    rarity = int(info[1])

    plant_dict[plant] = {}
    plant_dict[plant].update({"rarity": rarity})

command = input()

while not command == "Exhibition":

    data = command.split(": ")

    if " - " in data[1]:

        plant_and_number = data[1].split(" - ")

        plant = plant_and_number[0]

        if plant not in plant_dict:
            print("error")

        else:

            action = data[0]

            if action == "Rate":

                plant_and_rating = data[1].split(" - ")
                plant = plant_and_rating[0]
                rating = int(plant_and_rating[1])

                if "rating" not in plant_dict[plant]:
                    plant_dict[plant]["rating"] = []
                    plant_dict[plant]["rating"].append(rating)

                else:
                    plant_dict[plant]["rating"].append(rating)

            elif action == "Update":
                plant_and_new_rarity = data[1].split(" - ")
                plant = plant_and_new_rarity[0]
                new_rarity = int(plant_and_new_rarity[1])

                plant_dict[plant]["rarity"] = new_rarity

    elif " - " not in data[1]:
        plant = data[1]

        if plant not in plant_dict:
            print("error")

        else:
            action = data[0]

            if action == "Reset":
                plant = data[1]
                del plant_dict[plant]["rating"]

    command = input()

print("Plants for the exhibition:")

average_rating = 0

for key, value in plant_dict.items():

    if plant_dict[key].get("rating") is None:
        average_rating = 0
        print(f"- {key}; Rarity: {plant_dict[key].get('rarity')}; Rating: {average_rating:.2f}")

    else:
        average_rating = sum(plant_dict[key].get("rating")) / len(plant_dict[key].get("rating"))
        print(f"- {key}; Rarity: {plant_dict[key].get('rarity')}; Rating: {average_rating:.2f}")

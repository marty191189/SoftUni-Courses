prize_obtained = ""

prizes_dict = {"shards": 0, "fragments": 0, "motes": 0}

while prize_obtained == "":

    current_data = input().lower().split(" ")

    for index in range(0, len(current_data), 2):
        key = current_data[index + 1]
        value = int(current_data[index])

        if key not in prizes_dict:
            prizes_dict[key] = value

        else:

            prizes_dict[key] += value

            if prizes_dict["shards"] >= 250:
                prizes_dict["shards"] -= 250
                prize_obtained = "Shadowmourne obtained!"
                print("Shadowmourne obtained!")
                break

            elif prizes_dict["fragments"] >= 250:
                prizes_dict["fragments"] -= 250
                prize_obtained = "Valanyr obtained!"
                print("Valanyr obtained!")
                break

            elif prizes_dict["motes"] >= 250:
                prizes_dict["motes"] -= 250
                prize_obtained = "Dragonwrath obtained!"
                print("Dragonwrath obtained!")
                break

if not prize_obtained == "":

    print(f"shards: {prizes_dict.get('shards')}")
    print(f"fragments: {prizes_dict.get('fragments')}")
    print(f"motes: {prizes_dict.get('motes')}")

    del prizes_dict["shards"]
    del prizes_dict["fragments"]
    del prizes_dict["motes"]

    for key, value in prizes_dict.items():
        print(f"{key}: {value}")

else:
    for key, value in prizes_dict.items():
        print(f"{key}: {value}")

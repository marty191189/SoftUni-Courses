# решение Инес + Мартин

n = int(input())
heroes = {}

for i in range(n):
    hero_name, hp, mp = input().split()
    heroes[hero_name] = {"HP": int(hp), "MP": int(mp)}

data = input()

while not data == "End":
    split_data = data.split(" - ")
    if split_data[0] == "CastSpell":
        hero_name, mp_needed, spell_name = split_data[1:]
        mp_needed = int(mp_needed)
        if heroes[hero_name]["MP"] >= mp_needed:
            heroes[hero_name]["MP"] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif split_data[0] == "TakeDamage":
        hero_name, damage, attacker = split_data[1:]
        damage = int(damage)
        if heroes[hero_name]["HP"] - damage <= 0:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
        else:
            heroes[hero_name]["HP"] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
    elif split_data[0] == "Recharge":
        hero_name, amount = split_data[1:]
        amount = int(amount)
        if heroes[hero_name]["MP"] + amount > 200:
            print(f"{hero_name} recharged for {200 - heroes[hero_name]['MP']} MP!")
            heroes[hero_name]["MP"] = 200
        else:
            heroes[hero_name]["MP"] += amount
            print(f"{hero_name} recharged for {amount} MP!")

    elif split_data[0] == "Heal":
        hero_name, amount = split_data[1:]
        amount = int(amount)
        if heroes[hero_name]["HP"] + amount > 100:
            print(f"{hero_name} healed for {100 - heroes[hero_name]['HP']} HP!")
            heroes[hero_name]["HP"] = 100
        else:
            heroes[hero_name]["HP"] += amount
            print(f"{hero_name} healed for {amount} HP!")
    data = input()

for name, value in heroes.items():
    print(name)
    print(f"  HP: {heroes[name]['HP']}")
    print(f"  MP: {heroes[name]['MP']}")

# решение Ангел

count = int(input())
heroes = dict()

for i in range(count):
    current_hero = input().split(" ")
    hero_name = current_hero[0]
    hp = "HP"
    mp = "MP"
    hero_HP = int(current_hero[1])
    hero_MP = int(current_hero[2])

    current_hero_dict = dict()
    current_hero_dict[hp] = hero_HP
    current_hero_dict[mp] = hero_MP
    heroes[hero_name] = current_hero_dict

command = input()

while command != "End":
    command_params = command.split(" - ")
    command_name = command_params[0]
    hero_name = command_params[1]
    value = int(command_params[2])

    if command_name == "Heal":
        if heroes[hero_name]["HP"] + value > 100:
            value = 100 - heroes[hero_name]["HP"]
            heroes[hero_name]["HP"] = 100
        else:
            heroes[hero_name]["HP"] += value

        print(f"{hero_name} healed for {value} HP!")

    elif command_name == "Recharge":
        if heroes[hero_name]["MP"] + value > 200:
            value = 200 - heroes[hero_name]["MP"]
            heroes[hero_name]["MP"] = 200
        else:
            heroes[hero_name]["MP"] += value

        print(f"{hero_name} recharged for {value} MP!")

    elif command_name == "TakeDamage":
        attacker = command_params[3]
        heroes[hero_name]["HP"] -= value
        if heroes[hero_name]["HP"] > 0:
            print(f"{hero_name} was hit for {value} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
        else:
            heroes.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")

    elif command_name == "CastSpell":
        spell = command_params[3]
        if heroes[hero_name]["MP"] >= value:
            heroes[hero_name]["MP"] -= value
            print(f"{hero_name} has successfully cast {spell} and now has {heroes[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell}!")

    command = input()

for hero in heroes:
    print(f"{hero}")
    print(f"  HP: {heroes[hero]['HP']}")
    print(f"  MP: {heroes[hero]['MP']}")

energy = int(input())

counter_won_battles = 0

not_enough_energy = False

command = input()

while True:

    if command == "End of battle":
        print(f"Won battles: {counter_won_battles}. Energy left: {energy}")
        break

    distance = int(command)

    if energy >= distance:
        energy -= distance
        counter_won_battles += 1

    elif energy < distance:
        not_enough_energy = True
        break

    if counter_won_battles % 3 == 0:
        energy += counter_won_battles

    command = input()

if not_enough_energy:
    print(f"Not enough energy! Game ends with {counter_won_battles} won battles and {energy} energy")

budget_for_actors = float(input())

name_of_actor = input()

salary = None

while True:

    if name_of_actor == "ACTION":
        break

    if budget_for_actors <= 0:
        break

    if len(name_of_actor) <= 15:
        salary = float(input())

    if len(name_of_actor) > 15:
        salary = (20 / 100) * budget_for_actors

    budget_for_actors -= salary

    name_of_actor = input()

if budget_for_actors > 0:
    print(f"We are left with {budget_for_actors:.2f} leva.")

else:
    print(f"We need {abs(budget_for_actors):.2f} leva for our actors.")

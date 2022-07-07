cargo_volume = float(input())
suitcase_volume = input()
counter = 0
no_space = False

while suitcase_volume != "End":
    if (counter + 1) % 3 == 0:
        suitcase_volume = float(suitcase_volume) * 1.1
    if cargo_volume >= float(suitcase_volume):
        cargo_volume -= float(suitcase_volume)
        counter += 1
    else:
        no_space = True
        break
    suitcase_volume = input()

if no_space:
    print("No more space!")
else:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {counter} suitcases loaded.")

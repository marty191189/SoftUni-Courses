numbers = [int(el) for el in input().split()]
target = int(input())

counter_iterations = 0
pairs_set = set()

for main_index in range(len(numbers)):
    for secondary_index in range(main_index + 1, len(numbers)):
        counter_iterations += 1
        if numbers[main_index] + numbers[secondary_index] == target:
            current_pair = (numbers[main_index], numbers[secondary_index])
            print(f"{numbers[main_index]} + {numbers[secondary_index]} = {target}")
            pairs_set.add(current_pair)

print(f"Iterations done: {counter_iterations}")

for pair in pairs_set:
    print(pair)

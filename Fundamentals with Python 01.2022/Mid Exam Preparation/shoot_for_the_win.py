target_list = [int(number) for number in input().split()]

counter_shot_targets = 0

command = input()

while not command == "End":

    index = int(command)

    if 0 <= index < len(target_list):

        counter_shot_targets += 1

        current_target = target_list[index]

        for i in range(0, len(target_list)):

            if not i == index and not target_list[i] == -1:

                if target_list[i] > current_target:
                    target_list[i] -= int(current_target)

                elif target_list[i] <= current_target:
                    target_list[i] += int(current_target)

        target_list.pop(index)

        target_list.insert(index, -1)

    command = input()

target_list_str = [str(number) for number in target_list]

print(f"Shot targets: {counter_shot_targets} -> {' '.join(target_list_str)}")

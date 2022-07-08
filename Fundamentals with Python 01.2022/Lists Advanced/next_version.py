old_version = list(map(int, input().split(".")))

triple_9_version = False

if old_version[2] == 9:
    old_version[2] = 0

    if old_version[1] == 9:
        old_version[1] = 0

        if old_version[0] != 9:
            old_version[0] += 1

        else:
            triple_9_version = True

    else:
        old_version[1] += 1

else:
    old_version[2] += 1

if triple_9_version:
    print("9.9.9")

else:
    new_version = list(map(str, old_version))
    print(".".join(new_version))

# втори начин

# def new_version(version_number):
#     version_number = int("".join(version_number)) + 1
#     result = [str(num) for num in str(version_number)]
#     print(".".join(result))
#
#
# data = input().split(".")
# new_version(data)

password = input()

only_odds = ""

command = input()

while not command == "Done":

    data = command.split()

    if data[0] == "TakeOdd":

        for index in range(0, len(password)):

            if not index % 2 == 0:
                only_odds += password[index]

        password = only_odds

        print(password)

    elif data[0] == "Cut":
        index = int(data[1])
        length = int(data[2])

        beg = password[:index]

        chars_to_remove = index + (length - 1)

        end = password[chars_to_remove + 1:]

        password = beg + end

        print(password)

    elif data[0] == "Substitute":

        substring = data[1]
        substitute = data[2]

        if substring in password:
            password = password.replace(substring, substitute)
            print(password)

        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {password}")

text = input()

command = input()

while not command == "Travel":

    data = command.split(":")

    if data[0] == "Add Stop":
        index = int(data[1])
        string = data[2]

        if index < len(text):

            beg = text[:index]
            end = text[index:]

            text = beg + string + end

        print(text)

    elif data[0] == "Remove Stop":
        start_index = int(data[1])
        end_index = int(data[2])

        if start_index < len(text) and end_index < len(text):

            beg = text[:start_index]
            end = text[(end_index + 1):]

            text = beg + end

        print(text)

    elif data[0] == "Switch":
        old_string = data[1]
        new_string = data[2]

        text = text.replace(old_string, new_string)

        print(text)

    command = input()

print(f"Ready for world tour! Planned stops: {text}")

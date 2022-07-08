import os

command = input()

while not command == "End":

    data = command.split("-")

    action = data[0]
    file_name = data[1]

    if action == "Create":

        with open(file_name, "w") as file:
            file.write("")

    elif action == "Add":

        content = data[2]

        with open(file_name, "a") as file:
            file.write(f"{content}\n")

    elif action == "Replace":

        old_string = data[2]
        new_string = data[3]

        if os.path.exists(file_name):

            with open(file_name, "r+") as file:

                file_content = file.read().replace(old_string, new_string)
                file.seek(0)
                file.truncate()
                file.write(file_content)

        else:
            print("An error occurred")

    elif action == "Delete":

        if os.path.exists(file_name):
            os.remove(file_name)

        else:
            print("An error occurred")

    command = input()

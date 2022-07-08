chars_list = ["-", ",", ".", "!", "?"]

with open("text.txt", "w") as file:
    file.write("-I was quick to judge him, but it wasn't his fault.\n-Is this some kind of joke?! Is it?\n"
               "-Quick, hide here. It is safer.")

with open("text.txt", "r") as file:

    for index, line in enumerate(file):

        if index % 2 == 0:
            result = " ".join(line.strip().split()[::-1])

            for char in chars_list:
                result = result.replace(char, "@")

            print(result)

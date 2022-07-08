import re

with open("text.txt", "w") as file:
    file.write("-I was quick to judge him, but it wasn't his fault.\n-Is this some kind of joke?! Is it?\n"
               "-Quick, hide here. It is safer.")

with open("text.txt", "r") as input_file, open("output.txt", "a") as output_file:

    for index, line in enumerate(input_file):

        pattern_letters = r"\w"

        pattern_punctuation = r"[\-,\.,\!,\?,\',\,]"

        result_letters = re.findall(pattern_letters, line)
        result_punctuation = re.findall(pattern_punctuation, line)

        output_file.write(f"Line {index + 1}: {line.strip()} ({len(result_letters)})({len(result_punctuation)})\n")

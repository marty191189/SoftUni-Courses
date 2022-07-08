text = input().split()

current_number = ""

new_word = ""

letters = ""

mixed_letters_list = []

for el in text:
    for char in el:
        if 48 <= ord(char) <= 57:
            current_number += char

        else:
            letters += char

    new_word = chr(int(current_number)) + letters

    mixed_letters_list.append(new_word)

    current_number = ""
    new_word = ""
    letters = ""

result_list = []

for word in mixed_letters_list:

    if len(word) >= 3:
        sec_char = word[1]

        last_char = word[-1]

        repl_list = []

        repl_list.append(sec_char)
        repl_list.append(last_char)

        new_word = f"{word[0] + repl_list[-1] + word[2:-1] + repl_list[0]}"

        result_list.append(new_word)

    else:
        result_list.append(word)

print(" ".join(result_list))

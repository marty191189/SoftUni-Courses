key_number = int(input())
number_of_lines = int(input())

decrypted_word = ""

for line in range(1, number_of_lines + 1):

    current_letter = input()

    current_letter_as_ascii_number = ord(current_letter)

    new_letter_as_ascii_number = key_number + current_letter_as_ascii_number

    new_letter_as_chr = chr(new_letter_as_ascii_number)

    decrypted_word += new_letter_as_chr

print(decrypted_word)

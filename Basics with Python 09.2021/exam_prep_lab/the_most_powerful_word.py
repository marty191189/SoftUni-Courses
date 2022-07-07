most_powerful_word = ''
most_powerful_word_score = 0

while True:
    word = input()

    if word == "End of words":
        break

    current_counter_of_chars = 0

    for char in word:
        current_counter_of_chars += ord(char)

    if word[0].lower() in 'aeiouy':
        current_counter_of_chars = current_counter_of_chars * len(word)

    else:
        current_counter_of_chars = int(current_counter_of_chars / len(word))

    if current_counter_of_chars > most_powerful_word_score:
        most_powerful_word = word
        most_powerful_word_score = current_counter_of_chars

print(f"The most powerful word is {most_powerful_word} - {most_powerful_word_score}")

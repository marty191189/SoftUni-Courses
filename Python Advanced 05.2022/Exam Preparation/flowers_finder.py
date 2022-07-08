from collections import deque

vowel_deque = deque([letter for letter in input().split()])
consonant_stack = [letter for letter in input().split()]

searched_words_list = ["rose", "tulip", "lotus", "daffodil"]

found_letters_list = []

word_is_found = False

while True:

    if not vowel_deque:
        break

    if not consonant_stack:
        break

    current_vowel = vowel_deque.popleft()
    current_consonant = consonant_stack.pop()

    for word in searched_words_list:

        if current_consonant in word:
            found_letters_list.append(current_consonant)

        if current_vowel in word:
            found_letters_list.append(current_vowel)

    counter_found_letters = 0

    for word in searched_words_list:

        for letter in word:

            if letter in found_letters_list:
                counter_found_letters += 1

        if counter_found_letters == len(word):
            word_is_found = True
            print(f"Word found: {word}")
            break

        counter_found_letters = 0

    if word_is_found:
        break

if not word_is_found:
    print("Cannot find any word!")

if vowel_deque:
    print(f"Vowels left: {' '.join(vowel_deque)}")

if consonant_stack:
    print(f"Consonants left: {' '.join(consonant_stack)}")

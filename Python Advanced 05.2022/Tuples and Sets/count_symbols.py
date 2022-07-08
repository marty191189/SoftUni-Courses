text_list = [el for el in input()]

text_set = sorted(set(text_list))

for letter in text_set:
    counter = text_list.count(letter)
    print(f"{letter}: {counter} time/s")

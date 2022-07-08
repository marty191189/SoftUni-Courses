number_of_words = int(input())

synonym_dict = {}

for i in range(1, number_of_words + 1):
    word = input()
    synonym = input()

    if word not in synonym_dict:
        synonym_dict[word] = []
    synonym_dict[word].append(synonym)

for key, value in synonym_dict.items():
    print(f"{key} - {', '.join(value)}")

import re

with open("words.txt", "w") as file:
    file.write("quick is fault")

with open("input.txt", "w") as file:
    file.write("-I was quick to judge him, but it wasn't his fault.\n"
               "-Is this some kind of joke?! Is it?\n-Quick, hide here...It is safer.")

with open("words.txt") as file:
    searched_words_list = file.read().split()

word_count_dict = {}

with open("input.txt") as file:
    text = file.read()

    for word in searched_words_list:
        pattern = fr"\b{word}\b"
        current_count = len(re.findall(pattern, text, re.IGNORECASE))
        word_count_dict[word] = current_count

with open("output_file", "w") as file:
    sorted_result = sorted(word_count_dict.items(), key=lambda kvp: -kvp[1])

    for key, value in sorted_result:
        file.write(f"{key} - {value}\n")


# втори начин с функции
#
# import re
#
#
# def read_searched_words(file_path):
#     searched_words = []
#     with open(file_path) as file:
#         searched_words = file.read().split()
#     return searched_words
#
#
# def calculate_words_count(searched_words, file_path):
#     words_count = {}
#     with open(file_path) as file:
#         text = file.read()
#         for word in searched_words:
#             pattern = fr"\b{word}\b"
#             count = len(re.findall(pattern, text, re.IGNORECASE))
#             words_count[word] = count
#     return words_count
#
#
# def store_result(result, output_file_path):
#     with open(output_file_path, "w") as file:
#         sorted_result = sorted(result.items(), key=lambda kvpt: -kvpt[1])
#         for key, value in sorted_result:
#             file.writelines(f"{key} - {value}\n")
#
#
# words = read_searched_words("words.txt")
# result = calculate_words_count(words, "input.txt")
# store_result(result, "output.txt")

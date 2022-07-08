list_of_words_1 = input().split(", ")
list_of_words_2 = input()

my_list = []

for i in list_of_words_1:
    if i in list_of_words_2:
        my_list.append(i)

print(my_list)

# втори начин
#
# list_of_words_1 = input().split(", ")
# list_of_words_2 = input()
#
# print([i for i in list_of_words_1 if i in list_of_words_2])

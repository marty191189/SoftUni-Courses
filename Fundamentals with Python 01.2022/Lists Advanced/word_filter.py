text = input().split(" ")

for word in text:
    if len(word) % 2 == 0:
        print(word)

# втори начин

# text = input().split(" ")
#
# my_list = [word for word in text if len(word) % 2 == 0]
#
# print("\n".join(my_list))

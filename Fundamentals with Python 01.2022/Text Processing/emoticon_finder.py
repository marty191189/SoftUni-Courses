text = input()

emoji_list = []

while ":" in text:
    first_symbol = text[text.find(":")]
    second_symbol = text[text.find(":") + 1]

    emoji_list.append(first_symbol + second_symbol)

    text = text.replace(":", "", 1)

print("\n".join(emoji_list))

# втори начин

# text = input()
#
# emoji_list = []
#
# for index in range(0, len(text)):
#     if text[index] == ":":
#         emoji_list.append(f"{text[index]}{text[index + 1]}")
#
# print("\n".join(emoji_list))

# трети начин


# def emoji_finder(text):
#     result = [text[i] + text[i + 1] for i in range(len(text)) if text[i] == ":" and text[i + 1] != " "]
#
#     print("\n".join(result))
#
#
# text = input()
# emoji_finder(text)

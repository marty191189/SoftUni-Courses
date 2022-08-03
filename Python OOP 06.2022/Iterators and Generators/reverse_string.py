def reverse_text(text):

    i = len(text) - 1

    while 0 <= i:

        yield text[i]

        i -= 1


for char in reverse_text("step"):
    print(char, end='')

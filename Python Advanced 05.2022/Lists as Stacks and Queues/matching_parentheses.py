text = input()

parentheses_stack = []

for index in range(0, len(text)):

    if text[index] == "(":
        parentheses_stack.append(index)

    elif text[index] == ")":
        starting_index = parentheses_stack.pop()
        print(text[starting_index:index+1])

expression = input()

opening_brackets_stack = []

pairs_dict = {
    "(": ")",
    "[": "]",
    "{": "}"
}

pair_is_balanced = True

for char in expression:

    if char in "([{":
        opening_brackets_stack.append(char)

    elif not opening_brackets_stack:
        pair_is_balanced = False

    else:
        last_opening_bracket = opening_brackets_stack.pop()

        if not pairs_dict[last_opening_bracket] == char:
            pair_is_balanced = False

    if not pair_is_balanced:
        break

if not pair_is_balanced or opening_brackets_stack:
    print("NO")

else:
    print("YES")

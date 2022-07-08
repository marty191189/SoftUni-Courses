def palindrome(word, index):

    if index == len(word):

        if word == word[::-1]:
            return f"{word} is a palindrome"
        else:
            return f"{word} is not a palindrome"

    return palindrome(word, index + 1)


print(palindrome("abcba", 0))

print(palindrome("peter", 0))

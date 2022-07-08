text = input()
vowels = ['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O']
no_vowels_list = [x for x in text if x not in vowels]
print(''.join(no_vowels_list))

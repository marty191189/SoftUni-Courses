def vowel_filter(function):

    def wrapper():
        letters = function()
        filtered_list = [letter for letter in letters if letter.lower() in "aeiouy"]
        return filtered_list
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())

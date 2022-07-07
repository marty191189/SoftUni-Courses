counter_of_movies = 0
current_sum = 0
total_sum = 0
favourite_movie = None

name_of_movie = input()
counter_of_movies += 1

while True:

    for letter in name_of_movie:

        if 65 <= ord(letter) <= 90:
            current_sum += ord(letter) - len(name_of_movie)

        elif 97 <= ord(letter) <= 122:
            current_sum += ord(letter) - (2 * len(name_of_movie))

        elif ord(letter) == 32:
            current_sum += ord(letter)

        elif 48 <= ord(letter) <= 57:
            current_sum += ord(letter)

    if current_sum > total_sum:
        favourite_movie = name_of_movie
        total_sum = current_sum

    current_sum = 0

    name_of_movie = input()
    counter_of_movies += 1

    if name_of_movie == "STOP":
        break

    if counter_of_movies == 7:
        print("The limit is reached.")
        break

print(f"The best movie for you is {favourite_movie} with {total_sum} ASCII sum.")

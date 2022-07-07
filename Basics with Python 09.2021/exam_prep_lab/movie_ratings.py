import sys

number_of_movies = int(input())
max_rating_movie_name = ""
max_rating = -sys.maxsize
min_rating_movie_name = ""
min_rating = sys.maxsize

average_rating = 0

for movie in range(number_of_movies):
    name_of_movie = input()
    rating = float(input())

    average_rating += rating

    if rating > max_rating:
        max_rating = rating
        max_rating_movie_name = name_of_movie

    if rating < min_rating:
        min_rating = rating
        min_rating_movie_name = name_of_movie

average_rating = average_rating / number_of_movies

print(f"{max_rating_movie_name} is with highest rating: {max_rating:.1f}")
print(f"{min_rating_movie_name} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")

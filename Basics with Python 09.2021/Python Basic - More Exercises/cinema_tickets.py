counter_student_tickets_current_movie = 0
counter_student_tickets_all_movies = 0

counter_standard_tickets_current_movie = 0
counter_standard_tickets_all_movies = 0

counter_kid_tickets_current_movie = 0
counter_kid_tickets_all_movies = 0

total_tickets_current_movie = 0
total_tickets_all_movies = 0

free_seats_for_movie = 0

name_of_movie = input()

while name_of_movie != "Finish":

    free_seats_for_movie = int(input())

    type_of_ticket = input()

    while True:

        if type_of_ticket == "End":
            break

        if type_of_ticket == "student":
            counter_student_tickets_current_movie += 1
            counter_student_tickets_all_movies += 1
            total_tickets_current_movie += 1
            total_tickets_all_movies += 1

        elif type_of_ticket == "standard":
            counter_standard_tickets_current_movie += 1
            counter_standard_tickets_all_movies += 1
            total_tickets_current_movie += 1
            total_tickets_all_movies += 1

        elif type_of_ticket == "kid":
            counter_kid_tickets_current_movie += 1
            counter_kid_tickets_all_movies += 1
            total_tickets_current_movie += 1
            total_tickets_all_movies += 1

        if total_tickets_current_movie == free_seats_for_movie:
            break

        type_of_ticket = input()

    percent_room_full = (total_tickets_current_movie / free_seats_for_movie) * 100

    print(f"{name_of_movie} - {percent_room_full:.2f}% full.")

    counter_student_tickets_current_movie = 0
    counter_standard_tickets_current_movie = 0
    counter_kid_tickets_current_movie = 0
    total_tickets_current_movie = 0
    free_seats_for_movie = 0

    name_of_movie = input()

percent_student_tickets = (counter_student_tickets_all_movies / total_tickets_all_movies) * 100
percent_standard_tickets = (counter_standard_tickets_all_movies / total_tickets_all_movies) * 100
percent_kid_tickets = (counter_kid_tickets_all_movies / total_tickets_all_movies) * 100

print(f"Total tickets: {total_tickets_all_movies}")
print(f"{percent_student_tickets:.2f}% student tickets.")
print(f"{percent_standard_tickets:.2f}% standard tickets.")
print(f"{percent_kid_tickets:.2f}% kids tickets.")

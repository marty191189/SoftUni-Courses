student_ticket_counter = 0
standard_ticket_counter = 0
kid_ticket_counter = 0
total_ticket_counter = 0

command = input()

while command != "Finish":
    movie_name = command
    free_places = int(input())
    total_places = free_places
    sold_tickets = 0

    while free_places > 0:
        ticket_type = input()

        if ticket_type == "End":
            break

        elif ticket_type == "student":
            student_ticket_counter += 1

        elif ticket_type == "standard":
            standard_ticket_counter += 1

        elif ticket_type == "kid":
            kid_ticket_counter += 1

        free_places -= 1
        sold_tickets += 1
        total_ticket_counter += 1

    percent_places = (sold_tickets / total_places) * 100

    print(f"{movie_name} - {percent_places:.2f}% full.")

    command = input()

percent_student_ticket = (student_ticket_counter / total_ticket_counter) * 100
percent_standard_ticket = (standard_ticket_counter / total_ticket_counter) * 100
percent_kid_ticket = (kid_ticket_counter / total_ticket_counter) * 100

print(f"Total tickets: {total_ticket_counter}")
print(f"{percent_student_ticket:.2f}% student tickets.")
print(f"{percent_standard_ticket:.2f}% standard tickets.")
print(f"{percent_kid_ticket:.2f}% kids tickets.")

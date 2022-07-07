stage_of_tournament = input()
type_of_ticket = input()
number_of_tickets = int(input())
photo = input()

total_sum = 0

if stage_of_tournament == "Quarter final":

    if type_of_ticket == "Standard":
        total_sum = number_of_tickets * 55.50

    elif type_of_ticket == "Premium":
        total_sum = number_of_tickets * 105.20

    elif type_of_ticket == "VIP":
        total_sum = number_of_tickets * 118.90

elif stage_of_tournament == "Semi final":

    if type_of_ticket == "Standard":
        total_sum = number_of_tickets * 75.88

    elif type_of_ticket == "Premium":
        total_sum = number_of_tickets * 125.22

    elif type_of_ticket == "VIP":
        total_sum = number_of_tickets * 300.40

elif stage_of_tournament == "Final":

    if type_of_ticket == "Standard":
        total_sum = number_of_tickets * 110.10

    elif type_of_ticket == "Premium":
        total_sum = number_of_tickets * 160.66

    elif type_of_ticket == "VIP":
        total_sum = number_of_tickets * 400

if 0 < total_sum <= 2500:

    if photo == "Y":
        total_sum = total_sum + (number_of_tickets * 40)

    elif photo == "N":
        total_sum = total_sum

elif 2500 < total_sum <= 4000:
    total_sum = total_sum - ((10 / 100) * total_sum)

    if photo == "Y":
        total_sum = total_sum + (number_of_tickets * 40)

    elif photo == "N":
        total_sum = total_sum

if 4000 < total_sum:
    total_sum = total_sum - ((25 / 100) * total_sum)

    if photo == "Y":
        total_sum = total_sum

    elif photo == "N":
        total_sum = total_sum

print(f"{total_sum:.2f}")

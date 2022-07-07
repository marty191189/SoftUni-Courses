number_of_people = int(input())
number_of_nights = int(input())
number_of_cards = int(input())
number_of_tickets = int(input())

price_nights = number_of_nights * 20
price_cards = number_of_cards * 1.60
price_tickets = number_of_tickets * 6

price_for_one_person = price_nights + price_cards + price_tickets

total_sum = price_for_one_person * number_of_people

additional_costs = total_sum * (25 / 100)

total_sum = total_sum + additional_costs

print(f"{total_sum:.2f}")

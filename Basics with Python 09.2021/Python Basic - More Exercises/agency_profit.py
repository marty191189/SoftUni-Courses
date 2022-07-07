name_of_airline = input()
number_of_tickets_adults = int(input())
number_of_tickets_kids = int(input())
price_of_ticket_adults = float(input())
price_of_service = float(input())

price_of_ticket_kids = price_of_ticket_adults - ((70 / 100) * price_of_ticket_adults)

price_of_ticket_adults_plus_service = price_of_ticket_adults + price_of_service

price_of_ticket_kids_plus_service = price_of_ticket_kids + price_of_service

total_price = (number_of_tickets_adults * price_of_ticket_adults_plus_service) + (number_of_tickets_kids * price_of_ticket_kids_plus_service)

profit = (20 / 100) * total_price

print(f"The profit of your agency from {name_of_airline} tickets is {profit:.2f} lv.")

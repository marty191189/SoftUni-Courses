name_of_film = input()
type_of_hall = input()
number_sold_tickets = int(input())

price_of_ticket = 0
money_from_film = 0

if name_of_film == "A Star Is Born":

    if type_of_hall == "normal":
        price_of_ticket = 7.50
        money_from_film = price_of_ticket * number_sold_tickets

    elif type_of_hall == "luxury":
        price_of_ticket = 10.50
        money_from_film = price_of_ticket * number_sold_tickets

    elif type_of_hall == "ultra luxury":
        price_of_ticket = 13.50
        money_from_film = price_of_ticket * number_sold_tickets

elif name_of_film == "Bohemian Rhapsody":

    if type_of_hall == "normal":
        price_of_ticket = 7.35
        money_from_film = price_of_ticket * number_sold_tickets

    elif type_of_hall == "luxury":
        price_of_ticket = 9.45
        money_from_film = price_of_ticket * number_sold_tickets

    elif type_of_hall == "ultra luxury":
        price_of_ticket = 12.75
        money_from_film = price_of_ticket * number_sold_tickets

elif name_of_film == "Green Book":

    if type_of_hall == "normal":
        price_of_ticket = 8.15
        money_from_film = price_of_ticket * number_sold_tickets

    elif type_of_hall == "luxury":
        price_of_ticket = 10.25
        money_from_film = price_of_ticket * number_sold_tickets

    elif type_of_hall == "ultra luxury":
        price_of_ticket = 13.25
        money_from_film = price_of_ticket * number_sold_tickets

elif name_of_film == "The Favourite":

    if type_of_hall == "normal":
        price_of_ticket = 8.75
        money_from_film = price_of_ticket * number_sold_tickets

    elif type_of_hall == "luxury":
        price_of_ticket = 11.55
        money_from_film = price_of_ticket * number_sold_tickets

    elif type_of_hall == "ultra luxury":
        price_of_ticket = 13.95
        money_from_film = price_of_ticket * number_sold_tickets

print(f"{name_of_film} -> {money_from_film:.2f} lv.")

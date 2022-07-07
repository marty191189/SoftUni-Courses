type_of_movie = input()
rows = int(input())
columns = int(input())

total_places = rows * columns

price_of_ticket = 0

if type_of_movie == "Premiere":
    price_of_ticket = 12

elif type_of_movie == "Normal":
    price_of_ticket = 7.50

elif type_of_movie == "Discount":
    price_of_ticket = 5

total_profit = total_places * price_of_ticket

print(f"{total_profit:.2f} leva")

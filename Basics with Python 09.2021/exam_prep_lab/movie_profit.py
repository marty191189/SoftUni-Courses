movie_name = input()
number_of_days = int(input())
number_of_tickets = int(input())
price_of_ticket = float(input())
cinema_percent = int(input())

sum_from_tickets_per_day = number_of_tickets * price_of_ticket
profit_for_all_period = sum_from_tickets_per_day * number_of_days
percent_tax = profit_for_all_period * (cinema_percent / 100)
profit_for_movie = profit_for_all_period - percent_tax

print(f"The profit from the movie {movie_name} is {profit_for_movie:.2f} lv.")

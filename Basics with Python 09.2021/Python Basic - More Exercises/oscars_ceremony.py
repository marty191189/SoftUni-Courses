rent_hall = int(input())

price_statues = rent_hall - ((30 / 100) * rent_hall)
price_catering = price_statues - ((15 / 100) * price_statues)
price_audio = price_catering / 2

total_sum = rent_hall + price_statues + price_catering + price_audio

print(f"{total_sum:.2f}")

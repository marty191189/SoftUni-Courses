number_of_chrysanthemums = int(input())
number_of_roses = int(input())
number_of_tulips = int(input())
season = input()
celebration = input()

price_all_chrysanthemums = 0
price_all_roses = 0
price_all_tulips = 0

number_all_flowers = number_of_chrysanthemums + number_of_roses + number_of_tulips

price_all_flowers = 0
total_celeb_price = 0
price_b4_arrange = 0
final_price = 0

arranging_flowers = 2

if season == "Spring" or season == "Summer":
    if celebration == "Y":
        price_chrysanthemums = 2
        price_roses = 4.10
        price_tulips = 2.50

        price_all_chrysanthemums = price_chrysanthemums * number_of_chrysanthemums
        price_all_roses = price_roses * number_of_roses
        price_all_tulips = price_tulips * number_of_tulips

        price_all_flowers = price_all_chrysanthemums + price_all_roses + price_all_tulips

        total_celeb_price = price_all_flowers + ((15 / 100) * price_all_flowers)

        price_b4_arrange = total_celeb_price

        if season == "Spring" and number_of_tulips > 7:
            price_b4_arrange = price_b4_arrange - ((5 / 100) * price_b4_arrange)

        if number_all_flowers > 20:
            price_b4_arrange = price_b4_arrange - ((20 / 100) * price_b4_arrange)

    elif celebration == "N":
        price_chrysanthemums = 2
        price_roses = 4.10
        price_tulips = 2.50

        price_all_chrysanthemums = number_of_chrysanthemums * price_chrysanthemums
        price_all_roses = number_of_roses * price_roses
        price_all_tulips = number_of_tulips * price_tulips

        price_all_flowers = price_all_chrysanthemums + price_all_roses + price_all_tulips

        price_b4_arrange = price_all_flowers

        if number_all_flowers > 20:
            price_b4_arrange = price_b4_arrange - ((20 / 100) * price_b4_arrange)

elif season == "Autumn" or season == "Winter":
    if celebration == "Y":
        price_chrysanthemums = 3.75
        price_roses = 4.50
        price_tulips = 4.15

        price_all_chrysanthemums = price_chrysanthemums * number_of_chrysanthemums
        price_all_roses = price_roses * number_of_roses
        price_all_tulips = price_tulips * number_of_tulips

        price_all_flowers = price_all_chrysanthemums + price_all_roses + price_all_tulips

        total_celeb_price = price_all_flowers + ((15 / 100) * price_all_flowers)

        price_b4_arrange = total_celeb_price

        if season == "Winter" and number_of_roses >= 10:
            price_b4_arrange = price_b4_arrange - ((10 / 100) * price_b4_arrange)

        if number_all_flowers > 20:
            price_b4_arrange = price_b4_arrange - ((20 / 100) * price_b4_arrange)

    elif celebration == "N":
        price_chrysanthemums = 3.75
        price_roses = 4.50
        price_tulips = 4.15

        price_all_chrysanthemums = number_of_chrysanthemums * price_chrysanthemums
        price_all_roses = number_of_roses * price_roses
        price_all_tulips = number_of_tulips * price_tulips

        price_all_flowers = price_all_chrysanthemums + price_all_roses + price_all_tulips

        price_b4_arrange = price_all_flowers

        if season == "Winter" and number_of_roses >= 10:
            price_b4_arrange = price_b4_arrange - ((10 / 100) * price_b4_arrange)

        if number_all_flowers > 20:
            price_b4_arrange = price_b4_arrange - ((20 / 100) * price_b4_arrange)

final_price = price_b4_arrange + arranging_flowers

print(f"{final_price:.2f}")

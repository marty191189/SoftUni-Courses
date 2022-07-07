annual_fee = int(input())

sneakers = annual_fee - ((40 / 100) * annual_fee)
suit = sneakers - ((20 / 100) * sneakers)
basketball = suit * (1 / 4)
accessories = basketball * (1 / 5)

total_sum = annual_fee + sneakers + suit + basketball + accessories

print(total_sum)

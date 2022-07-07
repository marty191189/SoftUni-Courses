annual_tax = int(input())

sneakers = annual_tax - ((40 / 100) * annual_tax)
suit = sneakers - ((20 / 100) * sneakers)
ball = (1 / 4) * suit
accessories = (1 / 5) * ball

total_sum = annual_tax + sneakers + suit + ball + accessories

print(f"{total_sum:.2f}")

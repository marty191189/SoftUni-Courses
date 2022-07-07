price_strawberry = float(input())
kg_banana = float(input())
kg_orange = float(input())
kg_raspberry = float(input())
kg_strawberry = float(input())

price_raspberry = price_strawberry / 2
price_orange = price_raspberry - ((40 / 100) * price_raspberry)
price_banana = price_raspberry - ((80 / 100) * price_raspberry)

total_sum = (kg_strawberry * price_strawberry) + (kg_raspberry * price_raspberry) + (kg_orange * price_orange) + (kg_banana * price_banana)

print(total_sum)

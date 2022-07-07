kg_cargo = float(input())
type_of_shipment = input()
distance_in_km = int(input())
price_of_shipment = 0

special_price_for_kg = 0
special_price_for_km = 0

total_price = 0

if type_of_shipment == "standard" or type_of_shipment == "express":

    if kg_cargo < 1:
        total_price = distance_in_km * 0.03

    elif 1 < kg_cargo < 10:
        total_price = distance_in_km * 0.05

    elif 10 < kg_cargo <= 40:
        total_price = distance_in_km * 0.10

    elif 40 < kg_cargo <= 90:
        total_price = distance_in_km * 0.15

    elif 90 < kg_cargo <= 150:
        total_price = distance_in_km * 0.20

    if type_of_shipment == "express":

        if kg_cargo < 1:
            special_price_for_kg = (80 / 100) * 0.03
            special_price_for_km = kg_cargo * special_price_for_kg
            total_price += distance_in_km * special_price_for_km

        elif 1 < kg_cargo < 10:
            special_price_for_kg = (40 / 100) * 0.05
            special_price_for_km = kg_cargo * special_price_for_kg
            total_price += distance_in_km * special_price_for_km

        elif 10 < kg_cargo <= 40:
            special_price_for_kg = (5 / 100) * 0.10
            special_price_for_km = kg_cargo * special_price_for_kg
            total_price += distance_in_km * special_price_for_km

        elif 40 < kg_cargo <= 90:
            special_price_for_kg = (2 / 100) * 0.15
            special_price_for_km = kg_cargo * special_price_for_kg
            total_price += distance_in_km * special_price_for_km

        elif 90 < kg_cargo <= 150:
            special_price_for_kg = (1 / 100) * 0.20
            special_price_for_km = kg_cargo * special_price_for_kg
            total_price += distance_in_km * special_price_for_km

print(f"The delivery of your shipment with weight of {kg_cargo:.3f} kg. would cost {total_price:.2f} lv.")

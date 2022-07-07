budget = float(input())
season = input()

car_class = None
type_car = None
car_price = None

# •	Първи ред – "{Вид на класа}"
# o	"Economy class", "Compact class" или "Luxury class"

# •	Втори ред – "{Вид на колата} - {цена на колата}"
# o	Видът на колата – "Cabrio" или "Jeep"

if budget <= 100:
    car_class = "Economy class"

    if season == "Summer":
        type_car = "Cabrio"
        car_price = ((35 / 100) * budget)

    elif season == "Winter":
        type_car = "Jeep"
        car_price = ((65 / 100) * budget)

elif 100 < budget <= 500:
    car_class = "Compact class"

    if season == "Summer":
        type_car = "Cabrio"
        car_price = ((45 / 100) * budget)

    elif season == "Winter":
        type_car = "Jeep"
        car_price = ((80 / 100) * budget)

elif 500 < budget:
    car_class = "Luxury class"

    if season == "Summer":
        type_car = "Jeep"
        car_price = ((90 / 100) * budget)

    elif season == "Winter":
        type_car = "Jeep"
        car_price = ((90 / 100) * budget)

print(f"{car_class}")
print(f"{type_car} - {car_price:.2f}")

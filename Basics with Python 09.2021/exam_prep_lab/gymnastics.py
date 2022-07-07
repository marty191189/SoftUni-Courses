name_of_country = input()
category = input()
difficulty = 0
points = 0

if name_of_country == "Bulgaria":
    if category == "ribbon":
        difficulty = 9.6
        points = 9.4
    
    elif category == "hoop":
        difficulty = 9.55
        points = 9.75
    
    elif category == "rope":
        difficulty = 9.5
        points = 9.4

elif name_of_country == "Russia":
    if category == "ribbon":
        difficulty = 9.1
        points = 9.4

    elif category == "hoop":
        difficulty = 9.3
        points = 9.8

    elif category == "rope":
        difficulty = 9.6
        points = 9.0

if name_of_country == "Italy":
    if category == "ribbon":
        difficulty = 9.2
        points = 9.5

    elif category == "hoop":
        difficulty = 9.45
        points = 9.35

    elif category == "rope":
        difficulty = 9.7
        points = 9.15

total_score = difficulty + points

diff = 20 - total_score
needed_percent = (diff / 20) * 100

print(f"The team of {name_of_country} get {total_score:.3f} on {category}.")
print(f"{needed_percent:.2f}%")

# щастлива година е такава, на която цифрите са различни.
# 2018, 2019 - да; 2022 - не

year = int(input())

is_happy_year = False

while not is_happy_year:
    year += 1
    str_year = str(year)
    set_year = set()

    for i in range(len(str_year)):
        set_year.add(str_year[i])

    is_happy_year = len(str_year) == len(set_year)

print(year)

# същото, но по-кратко

year = int(input())

is_happy_year = False

while not is_happy_year:
    year += 1
    str_year = str(year)
    set_year = set(str_year)

    is_happy_year = len(str_year) == len(set_year)

print(year)

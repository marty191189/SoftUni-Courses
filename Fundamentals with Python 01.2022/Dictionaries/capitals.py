country_names_list = input().split(", ")
capital_cities_list = input().split(", ")

dict_zip = dict(zip(country_names_list, capital_cities_list))

for key, value in dict_zip.items():
    print(f"{key} -> {value}")

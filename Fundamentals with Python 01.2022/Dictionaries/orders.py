data = input()

orders_dict = {}

result_dict = {}

product_name = ""

while not data == "buy":
    current_data = data.split(" ")

    product_name = current_data[0]
    price = float(current_data[1])
    quantity = int(current_data[2])

    if product_name not in orders_dict:
        orders_dict[product_name] = []
        orders_dict[product_name].append(price)
        orders_dict[product_name].append(quantity)

    else:
        orders_dict[product_name][0] = price
        orders_dict[product_name][1] += quantity

    data = input()

for key in orders_dict.keys():

    a = orders_dict[key][0]
    b = orders_dict[key][1]

    c = a * b

    result_dict[key] = c

for key, value in result_dict.items():
    print(f"{key} -> {value:.2f}")

# втори начин

# data = input()
#
# orders_dict = {}
#
# product_name = ""
#
# while not data == "buy":
#     current_data = data.split(" ")
#
#     product_name = current_data[0]
#     price = float(current_data[1])
#     quantity = int(current_data[2])
#
#     if product_name not in orders_dict:
#         orders_dict[product_name] = []
#         orders_dict[product_name].append(price)
#         orders_dict[product_name].append(quantity)
#
#     else:
#         orders_dict[product_name][0] = price
#         orders_dict[product_name][1] += quantity
#
#     data = input()
#
# for key in orders_dict.keys():
#
#     total_sum = orders_dict[key][0] * orders_dict[key][1]
#
#     print(f"{key} -> {total_sum:.2f}")
